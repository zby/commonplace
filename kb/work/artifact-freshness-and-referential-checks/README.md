# Workshop: artifact freshness and referential checks

## Question

Given the shipped full-pass capture/guard case, what additional boundary does a second consumer require for registering artifact-to-artifact dependencies, retaining accepted dependency baselines, selecting targets affected by changed inputs, and distinguishing freshness from deterministic cross-artifact validity?

No artifact class is intrinsically a source or a derivative. A source snapshot, ingest, note, criterion, type specification, instruction, report, or generated index may be an input in one target and a freshness target in another. Artifact types may define different refresh policies, but the mechanism must not special-case sources or ingests.

## Implemented foundation

[ADR 051](../../reference/adr/051-full-pass-packets-own-guarded-captures-and-resolutions.md) shipped the first non-review artifact-version case:

- full-pass packets retain immutable `.txt` start-state captures under separate logical artifact identities;
- `commonplace.lib.hashing` supplies the shared UTF-8-text SHA-256 contract already used by review freshness and full-pass captures;
- the typed full-pass report records every guarded logical path, packet-relative capture, and accepted hash;
- `commonplace-guard-full-pass-report` verifies captures, compares all live inputs, emits `matching`, `changed`, `missing`, or `corrupt-capture`, includes diffs for changed text, and refuses unless all inputs match;
- deterministic validation rechecks capture integrity and report-resolution consistency; and
- the resolution and full-pass instructions require the guard immediately before packet-driven transitions.

The implementation is intentionally split at the demonstrated boundary. Content hashing is shared. Report parsing, packet-capture persistence, capture verification, comparison/diff results, and guarding remain in `commonplace.lib.full_pass`, with a full-pass-specific command and type contract. There is no general capture store, artifact-version service, or freshness target API.

That is the desired starting point, not unfinished foundation work. Full-pass owns one persistence policy and one response to net drift: a disposition becomes `superseded` instead of executing against changed text. General freshness should extract full-pass comparison or guard code only after its second consumer demonstrates the same shape; shared semantics do not require shared storage or a universal `GuardedInput` type.

Pinned assessment input is not part of the shipped foundation. Full-pass methods still read live logical paths under a cooperative no-edit rule; the final optimistic guard covers later application and asynchronous resolution, not in-flight reads or the residual check-to-mutation race. Evidence that this rule is restrictive or unreliable must appear before this workshop adds pinned-input seams or stronger concurrency machinery.

## Remaining problem after the foundation

Review freshness proves accepted baselines for one purpose-built target kind: a `(note, criterion, model partition)` pair retains the note and criterion snapshots against which its evidence was accepted. ADR 051 adds a report-owned capture, selector-like comparison, diff, and guarded response. Together they establish the vocabulary and two storage weights, but still do not provide an artifact-neutral dependency baseline or reverse selector.

General freshness still lacks:

- an artifact-neutral target identity and dependency-registration contract;
- accepted baselines over the dependencies of non-review targets;
- a selector from a changed dependency to affected target keys and reasons;
- acknowledgement that advances selected dependency versions while preserving the target output;
- refresh acceptance that records a new target version and complete dependency baseline;
- target-owned policy for mapping neutral changes to reassess, regenerate, acknowledge, retire, or another action; and
- a storage-weight decision for dependency state that has no natural owner artifact.

Ordinary links may nominate dependency candidates, but Commonplace defines links as reader aids rather than obligations. A link alone cannot create an accepted baseline or prove that its target is stale.

## Why referential checks remain in the workshop

Freshness and referential validation resolve relationships in different ways:

- **Freshness selection** compares registered accepted dependency versions with their current versions. It says the accepted basis changed, not that a claim is false.
- **Referential validation** follows a type- or check-owned relationship to test current state. It can prove a cross-artifact assertion invalid without any prior accepted baseline.

Existing content-addressed verbatim-quote verification is already a robust referential check. It remains evidence that domain-owned referential checks can work; this workshop does not redesign its positional parsing.

## Evaluation boundary

The remaining mechanism must account for these witnesses:

- **Artifact-neutral baseline:** a non-review target records an accepted set of versioned artifact dependencies using the shipped text-version contract.
- **Reverse selection:** changing any registered dependency selects every affected target regardless of the path class or colloquial role of either side.
- **Diff-backed acknowledgement:** the operator inspects the accepted-to-current change and advances selected dependency baselines without claiming that a new target output was produced; the second consumer determines whether full-pass comparison/diff code should be extracted.
- **Refresh acceptance:** producing or reassessing a target records its current target version and complete accepted dependency baseline.
- **Target-owned consequence:** the shared selector emits neutral reasons such as `input-changed`, `output-missing`, or `contract-changed`; the target kind decides the permissible response.
- **Relationship is not freshness:** backlinks and authored links remain discovery evidence unless a target acceptance registers them as dependencies.
- **Selection is not execution:** the mechanism returns target keys, changed inputs, and reasons; review, regeneration, agent revision, or bulk-operation workflows decide what to do.

## General contract under test

A freshness target adds this state beyond the shipped review and full-pass cases:

- a stable target kind and structured key;
- the accepted target/output version, where an output artifact exists;
- registered dependency identities, roles, and accepted versions;
- the target policy used to interpret neutral selector results; and
- accepted baseline transitions for refresh and acknowledgement.

Acknowledgement means that the existing target remains acceptable against displayed current dependency versions. It advances only those versions and preserves the target output. Refresh means that the target was produced or reassessed and records a new target version plus its complete dependency baseline. Both operations record the exact versions inspected or consumed, not whichever versions happen to be current later. A concurrent subsequent edit therefore makes the new baseline immediately stale without requiring locks or atomic filesystem transactions.

The first implementation need not create a general database. The storage carrier follows the existing weight rule: keep naturally owned, low-churn state with its artifact; introduce an operational edge store only when mutable many-to-many state and a real selector outgrow artifact-owned records or recomputation.

## Ownership boundaries

This workshop owns the vertical behavior contract for artifact-neutral dependency baselines and their interaction with deterministic referential checks.

It consumes rather than duplicates adjacent work:

- [ADR 051](../../reference/adr/051-full-pass-packets-own-guarded-captures-and-resolutions.md) owns the shipped packet capture, full-pass comparison/guard command, and report-specific resolution. This workshop owns only the additional baseline and reverse-selection behavior plus any extraction a second consumer earns.
- [lineage-mechanisms](../lineage-mechanisms/README.md) owns the general dependency/freshness vocabulary, storage-weight rules, and any common operational state design.
- [kb-graph-loader](../kb-graph-loader/README.md) owns shared reading, parsing, and artifact indexes used by deterministic referential checks.
- [bulk-operations](../bulk-operations/README.md) owns executing selected refresh work at scale.
- The review subsystem continues to own review-pair lifecycle, result protocols, and its purpose-built store unless a migration is separately justified.

Out of scope: reworking full-pass capture/guard behavior, adding pinned-input or full-concurrency machinery without a failed case, automatic rewriting, semantic truth adjudication, a universal dependency-role ontology, authority ranking, and refresh-job execution.

## Open decisions

- What is the smallest real non-review target that needs an advancing accepted dependency baseline and can serve as the second consumer for extraction?
- Which dependencies are declared in artifact contracts or manifests, and which are registered only by an acceptance operation?
- Does the first reverse selector recompute over artifact-owned baselines, use a generated index, or already meet the many-to-many/churn threshold for SQLite?
- How does a target register its allowed responses without branching on artifact path classes in the shared selector?
- When an input is itself a stale target but its content is unchanged, does the dependency watch content only or explicitly require the input target's accepted freshness state?
- How should deterministic referential checks publish invalidity without conflating a currently false assertion with a stale accepted derivation?

## What closes it

The workshop closes when:

1. at least one non-review target records and queries an advancing accepted dependency baseline and serves as the second consumer for extracting only the artifact-version behavior it shares with ADR 051;
2. a changed dependency selects the registered target with its accepted and current versions plus a neutral reason;
3. acknowledgement and refresh demonstrate distinct baseline transitions over the exact inspected or consumed versions;
4. the boundary between dependency discovery, changed dependency, deterministic invalidity, and target-owned response has a written contract and executable cases;
5. Commonplace either implements the storage weight earned by the witness or records why artifact-owned state remains sufficient;
6. durable outcomes move to the appropriate API/reference documentation, ADR or proposal, validator instruction, and owning workshops; and
7. any submission claim about targeted maintenance is narrowed or substantiated to match the result.

Then delete this workshop and remove it from the active-workshop index.
