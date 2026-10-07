---
description: "Dagster keys each asset materialization on code and input data versions, flags one-hop Unsynced staleness, and lets output fingerprints stop cascades; a version-pinned verdict model."
source: https://docs.dagster.io/guides/build/assets/asset-versioning-and-caching
captured: "2026-10-07"
capture: trafilatura
capture_scope: full-source
genre: official-statement
snapshot_sha256: 998ab341851dfcdddf60f8e0e3cfb064a412d606fa0e57d90f896a917e5558de
ingested: "2026-10-07"
occasion: "A single-coordinator workflow produces a closed set of model-written documents where later verifications judge a specific version of an earlier member and corrections replace that member. Is this the main path Dagster's asset versioning was designed for, or a departure from it, and what is the smallest part of its model (data versions, code versions, staleness) that would serve such a workflow without adopting the rest of the system?"
type: types/ingest-report.md
domains: [derived-artifact-freshness, staleness-detection, workflow-orchestration, provenance]
---

# Ingest: Dagster asset versioning and caching

## Classification

This is vendor product documentation: a tutorial guide published by the tool's
maintainer about its own intended behavior. It is classified as an official
statement because it states designed guarantees and walks through UI behavior,
but it contains no measurements, failure reports or implementation detail.
Author: Dagster Labs, the company that develops Dagster; authoritative about
intended semantics, interested in presenting them favorably.

## Summary

The guide explains how Dagster avoids re-materializing an asset whose result
would not change. Each materialization records a code version, which is a
hand-declared string or, when absent, the run ID, and a data version. By
default the data version is a hash of the code version and the data versions
of the asset's inputs. A downstream materialization records which upstream
data versions it consumed. An asset is labelled "Unsynced" when its code
version changes, when its dependencies are added or removed, or when a parent
has a newer data version than the one last consumed. Unsynced is explicitly
not transitive: a downstream asset is flagged only after its parent is
actually re-materialized. User code may supply its own data version as an
output fingerprint. The guide motivates this override with two cases: random
outputs that the default hash would collapse to one version, and cosmetic code
changes that would otherwise cascade although the output is unchanged. Its
example shows the override stopping such a cascade. Observable source assets
bring external inputs into the same scheme through a user function that hashes
them. The stated purpose throughout is memoization in computationally
expensive pipelines.

## Quotes

No source quotes have been retained yet.

## Connections Found

For the occasion, the source serves as a worked mechanism to borrow from, and
as a boundary marker for what not to borrow. The workflow in the occasion is a
departure from Dagster's main path: the guide designs versioning to predict
ahead of time that a deterministic recomputation can be skipped, whereas the
occasion needs to record which version of a member a verification judged and
to detect when a correction has made that judgment stale. The part that
transfers is the per-materialization record of consumed upstream data versions
together with the one-hop Unsynced comparison. Model-written members fall
under the guide's nondeterministic case, where the default derived data
version is wrong and a user-supplied output fingerprint is required.

Within the KB, the source is a deployed instance of the build-system framework
in [Build Systems à la Carte](./build-systems-a-la-carte.ingest.md). In that
paper's terms Dagster is a verifying-traces rebuilder, and output
fingerprinting gives it early cutoff. The source partly relaxes two limits
that ingest records: its user data versions address nondeterministic outputs,
and it states the computational cost that justifies caching. It bears on
[Criteria edits invalidate verdicts; process edits invalidate artifacts](../notes/criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts.md):
if a verification is modelled as a downstream asset, a change to the
verifier's own code version marks the verdict Unsynced, while a change to the
producer's code version marks the producer Unsynced and reaches the verdict
only when the producer's output fingerprint changes. That is the note's key
boundary realized as a cache design, though Dagster does not frame it as
criteria versus process. It qualifies
[A derived copy of recomputable truth must be checked or absent](../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md):
the hand-declared `code_version` is a trusted, unchecked copy whose forgotten
bump leaves a stale memoized value, and the guide names source hashing as the
checked alternative. It is a deployed instance of the forward query in
[Source changes should surface downstream review targets](../notes/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md),
limited to one hop at a time. Against
[Link graph plus timestamps enables make-like staleness detection](../notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md),
it substitutes recorded version keys for timestamps and adds non-transitive
flagging, a design choice no KB note discusses. It is the code-side baseline
that [LLM recompute cost shifts the store-vs-recompute balance](../notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md)
argues LLM costs shift. [CocoIndex](../agent-memory-systems/reviews/cocoindex.md)
is the nearest system comparison: both key recomputation on fingerprints of
code and inputs, but CocoIndex applies minimal updates to declared target
state while Dagster leaves re-materialization to an operator or automation
acting on the Unsynced signal.

## Extractable Value

1. **Departure verdict for the occasion's workflow.** The occasion is not Dagster's main path. Dagster's versioning exists to skip deterministic recomputation, and its default data version assumes that equal code and equal inputs give an equal output. Model-written members break that assumption, which the guide itself acknowledges for random outputs. What survives the move is the staleness bookkeeping, not the memoization. Treating the workflow as "Dagster-like caching" would import the wrong default. [quick-win]
2. **Smallest transferable kernel: output fingerprint plus consumed-version stamp plus one-hop comparison.** Give each member a data version that fingerprints its content, such as a content hash, as the guide's user-supplied `DataVersion` does. Have each verification record the data version of every member it judged. Flag a verification as stale when a member's current data version differs from the recorded one. A correction that replaces a member then flags exactly the verifications that judged the earlier version. A correction that leaves content unchanged flags nothing, which is the guide's cascade-stopping example. This kernel needs neither code versions, derived data versions, memoization nor observable sources. [experiment]
3. **Code versions are optional, and if used they map onto the criteria/process split.** A code version is worth adding only for the verifier's own instructions or criteria, so that a criteria edit marks its verdicts stale. A producer-side code version should not enter the verdict's key. With content fingerprints, a producer process change reaches a verdict only through changed output. This gives an operational form of the criteria-edits note for the occasion. [experiment]
4. **Non-transitive staleness suits a single coordinator.** Flagging only the next hop means a corrected member flags its verifications, and anything depending on those verifications is flagged only after they are re-run. A single coordinator advancing one step at a time gets a bounded worklist rather than a flood from one upstream edit. No KB note treats one-hop flagging as a design choice; it is a candidate addition to the link-graph staleness note. [just-a-reference]
5. **Hand-declared versions are a trust hazard.** The default `code_version` string, and any user-supplied data version that is not derived from the output, are unchecked copies. A forgotten bump yields a silently stale verdict. For model-written documents a content hash is cheap, so the checked variant costs little. This is a concrete instance for the derived-copy note. [just-a-reference]

## Limitations (our opinion)

This is maintainer documentation of intended behavior, without measurements,
failure cases or an account of operational problems such as forgotten
code-version bumps. It does not show how often the trusted-string default
produces stale results in practice. The guide also does not say how much
materialization history is retained or queryable: it states that the last
computed value is cached, but the occasion's need to name the specific earlier
version a verdict judged depends on the per-materialization record, whose
retention the guide leaves implicit. Its framing assumes that recomputation is
expensive and mostly deterministic, so its justification for caching does not
carry over to model-written documents, where the same inputs can yield
different outputs. The capture is a single tutorial page. It does not cover
Dagster's automation policies, partitions or API details, and nothing here was
executed. The captured documentation URL is a moving target; the checksum
identifies this observation only. The guide also contains a stale-label
artifact, two sections numbered "Step 2", which suggests it is not tightly
maintained.

## Recommended Next Action

Specify the occasion workflow's staleness rule as the kernel in Extractable
Value item 2 — a content fingerprint per member, recorded per verification for
each judged member, with one-hop mismatch flagging — and test it against one
correction cycle in that workflow before considering code versions.

---

Relevant Notes:

- [Dagster asset versioning and caching](https://docs.dagster.io/guides/build/assets/asset-versioning-and-caching) — derived-from: the external guide this analysis is worked out from
- [Build Systems à la Carte](./build-systems-a-la-carte.ingest.md) — compares-with: on the rebuilder axis; Dagster is a deployed verifying-traces rebuilder with optional early cutoff through output fingerprints
- [Criteria edits invalidate verdicts; process edits invalidate artifacts](../notes/criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts.md) — is-evidence-for: a deployed cache key in which the consumer's code version invalidates its own result while upstream process changes propagate only through changed output fingerprints
- [A derived copy of recomputable truth must be checked or absent](../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — is-evidence-for: qualifies the claim; a production system ships the trusted, hand-declared version string as its default, with source hashing as the checked option
- [Source changes should surface downstream review targets](../notes/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md) — is-evidence-for: a deployed forward query that records consumed input versions and surfaces affected downstream assets, one hop at a time
- [Link graph plus timestamps enables make-like staleness detection](../notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — compares-with: on the staleness-signal axis; recorded version keys and non-transitive flagging instead of timestamps
- [LLM recompute cost shifts the store-vs-recompute balance](../notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md) — compares-with: on the store-vs-recompute axis; Dagster is the deterministic, cost-justified caching baseline
- [CocoIndex](../agent-memory-systems/reviews/cocoindex.md) — compares-with: on incremental materialization of derived stores keyed on code and input fingerprints
