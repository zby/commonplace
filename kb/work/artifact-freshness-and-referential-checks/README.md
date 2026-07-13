# Workshop: artifact freshness and referential checks

## Question

Given one proven operation-local artifact-version contract and a second real consumer, what boundary should Commonplace extract for registering artifact-to-artifact dependencies, retaining accepted dependency baselines, selecting targets affected by changed inputs, and distinguishing freshness from deterministic cross-artifact validity?

No artifact class is intrinsically a source or a derivative. A source snapshot, ingest, note, criterion, type specification, instruction, report, or generated index may be an input in one target and a freshness target in another. Artifact types may define different refresh policies, but the mechanism must not special-case sources or ingests.

## Prerequisite

Implement the full-pass-local [packet-owned capture for guarded operation transitions](../../reference/proposals/packet-owned-captures-for-guarded-operation-transitions.md) first.

That proposal proves these behaviors without exposing a reusable subsystem:

- logical artifact identity kept separate from a packet-owned start-state capture;
- immutable capture of the content present when an operation starts;
- an explicit content-version/hash contract;
- current-version resolution for a logical artifact;
- capture-to-current diff generation;
- an optimistic pre-transition guard that refuses inputs already changed or missing at check time without locking live artifacts; and
- machine-readable changed/missing/matching results.

Its first consumer, [report-owned resolution for asynchronous full-pass dispositions](../../reference/proposals/report-owned-resolution-for-asynchronous-full-pass-dispositions.md), owns packet-local `.txt` captures and proves one target-owned response to net drift: a disposition report becomes `superseded` instead of executing a recommendation when its guarded inputs no longer match their start state. That capture persistence and resolution state remain specific to full-pass operation; neither is the general freshness store. The contract deliberately holds no policy about what a changed input means — choosing those responses per target kind is this workshop's problem, not its prerequisite's.

This workshop consumes the proven semantics but not the full-pass persistence policy. Once a second consumer exists, its first implementation step is to compare both worked cases and extract only the shared identity, hashing, comparison, diff, and guard boundary. Packet-local capture persistence may remain private to full-pass code; a general freshness target may earn a different owner and retention policy.

Pinned assessment input is not part of the prerequisite. The first full-pass implementation leaves methods reading live logical paths and instead requires cooperative ownership: other actors do not edit guarded notes while the active pass runs. The final guard covers later application and asynchronous resolution, not in-flight reads. Evidence that this operating rule is restrictive or unreliable must appear before this workshop treats pinned-input seams as earned infrastructure.

## Remaining problem after the prerequisite

Review freshness already proves accepted baselines for one purpose-built target kind: a `(note, criterion, model partition)` pair retains the note and criterion snapshots against which its evidence was accepted. The artifact-version prerequisite adds a worked operation-local capture/comparison contract; its full-pass consumer adds a report-owned version-guarded decision. It intentionally does not yet add an artifact-neutral API.

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

The Epistack casebooks provide the worked referential failure: 26 ingest reports kept saying their target collections were empty after every source was cited by live notes. Per-file validation stayed green because the falsehood lived between each report and the collection ([Epistack workshop protocol](../epistack-competition/README.md)).

Existing content-addressed verbatim-quote verification is already a robust referential check. It remains evidence that domain-owned referential checks can work; this workshop does not redesign its positional parsing.

## Evaluation boundary

The remaining mechanism must account for these witnesses:

- **Artifact-neutral baseline:** a non-review target records an accepted set of versioned artifact dependencies using the prerequisite's artifact-version contract.
- **Reverse selection:** changing any registered dependency selects every affected target regardless of the path class or colloquial role of either side.
- **Diff-backed acknowledgement:** the operator uses the extracted comparison, diff, and version guard, then advances selected dependency baselines without claiming that a new target output was produced.
- **Refresh acceptance:** producing or reassessing a target records its current target version and complete accepted dependency baseline.
- **Target-owned consequence:** the shared selector emits neutral reasons such as `input-changed`, `output-missing`, or `contract-changed`; the target kind decides the permissible response.
- **Cross-artifact validity:** a deterministic check can detect a claim such as “the target collection is empty” becoming false, or establish why that claim cannot be represented safely enough to check.
- **Relationship is not freshness:** backlinks and authored links remain discovery evidence unless a target acceptance registers them as dependencies.
- **Selection is not execution:** the mechanism returns target keys, changed inputs, and reasons; review, regeneration, agent revision, or bulk-operation workflows decide what to do.

## General contract under test

A freshness target adds this state on top of the artifact-version boundary extracted from the two worked consumers:

- a stable target kind and structured key;
- the accepted target/output version, where an output artifact exists;
- registered dependency identities, roles, and accepted versions;
- the target policy used to interpret neutral selector results; and
- accepted baseline transitions for refresh and acknowledgement.

Acknowledgement means that the existing target remains acceptable against displayed current dependency versions. It advances only those versions and preserves the target output. Refresh means that the target was produced or reassessed and records a new target version plus its complete dependency baseline. Both operations optimistically recheck their complete input set immediately before the baseline transition and refuse a known mismatch. They do not lock artifacts or claim atomic exclusion across the check-to-write interval; target-owned postcondition verification and reconciliation retain the prerequisite's explicit residual-race boundary.

The first implementation need not create a general database. The storage carrier follows the existing weight rule: keep naturally owned, low-churn state with its artifact; introduce an operational edge store only when mutable many-to-many state and a real selector outgrow artifact-owned records or recomputation.

## Ownership boundaries

This workshop owns the vertical behavior contract for artifact-neutral dependency baselines and their interaction with deterministic referential checks.

It consumes rather than duplicates adjacent work:

- The [packet-owned capture proposal](../../reference/proposals/packet-owned-captures-for-guarded-operation-transitions.md) and the [full-pass disposition proposal](../../reference/proposals/report-owned-resolution-for-asynchronous-full-pass-dispositions.md) jointly supply the first worked case: packet-owned capture, current-version comparison, guarding, and report-specific resolution. This workshop owns extraction only after a second consumer demonstrates the common boundary.
- [lineage-mechanisms](../lineage-mechanisms/README.md) owns the general dependency/freshness vocabulary, storage-weight rules, and any common operational state design.
- [kb-graph-loader](../kb-graph-loader/README.md) owns shared reading, parsing, and artifact indexes used by deterministic referential checks.
- [bulk-operations](../bulk-operations/README.md) owns executing selected refresh work at scale.
- The review subsystem continues to own review-pair lifecycle, result protocols, and its purpose-built store unless a migration is separately justified.

Out of scope: implementing the prerequisite again, automatic rewriting, semantic truth adjudication, a universal dependency-role ontology, authority ranking, and refresh-job execution.

## Open decisions

- What is the smallest real non-review target that needs an advancing accepted dependency baseline and can serve as the second consumer for extraction?
- Which dependencies are declared in artifact contracts or manifests, and which are registered only by an acceptance operation?
- Does the first reverse selector recompute over artifact-owned baselines, use a generated index, or already meet the many-to-many/churn threshold for SQLite?
- How does a target register its allowed responses without branching on artifact path classes in the shared selector?
- When an input is itself a stale target but its content is unchanged, does the dependency watch content only or explicitly require the input target's accepted freshness state?
- How should deterministic referential checks publish invalidity without conflating a currently false assertion with a stale accepted derivation?

## What closes it

The workshop closes when:

1. the full-pass prerequisite has executable capture/comparison/diff/optimistic-guard cases, and a second consumer is used to extract the smallest reusable artifact-version API;
2. at least one non-review target records and queries an advancing accepted dependency baseline using that API;
3. a changed dependency selects the registered target with its accepted and current versions plus a neutral reason;
4. acknowledgement and refresh demonstrate distinct, guarded baseline transitions;
5. the boundary between dependency discovery, changed dependency, deterministic invalidity, and target-owned response has a written contract and executable cases;
6. Commonplace either implements the storage weight earned by the witness or records why artifact-owned state remains sufficient;
7. durable outcomes move to the appropriate API/reference documentation, ADR or proposal, validator instruction, and owning workshops; and
8. any submission claim about targeted maintenance is narrowed or substantiated to match the result.

Then delete this workshop and remove it from the active-workshop index.
