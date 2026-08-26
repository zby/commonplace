---
description: "OpenWiki reports claim-level code evidence versioning that marks wiki beliefs stale after source changes, with vendor-run results and a system-review refresh signal."
source: https://x.com/colifran_/status/2092280107033616451
captured: "2026-08-25T21:23:05.775823+00:00"
capture: xdk
status_id: 2092280107033616451
conversation_id: 2092280107033616451
post_count: 5
genre: practitioner-report
snapshot_sha256: a734d19e8064b30ea24374728fc21570b29bd61cd05f5b936780d87eb7205c5b
ingested: "2026-08-25"
type: kb/sources/types/ingest-report.md
domains: [agent-memory, provenance, freshness, knowledge-maintenance]
---

# Ingest: Building Self-Correcting Memory in OpenWiki

## Classification

This is a practitioner report because it gives a first-person account of a mechanism the author says the OpenWiki team built, then presents the team's own evaluation and release invitation. Author: @colifran_ writes with an affiliated builder's access to the design and results, but the snapshot supplies no independent credential or evidence review.

## Summary

OpenWiki reportedly records each material wiki claim with supporting code evidence and its version, deterministically marks the claim stale when that version changes, and asks the updating agent either to re-verify the claim or revise the claim, page, and evidence together. The article says this preserves uncertainty until reconciliation, projects page-level trust metadata into OKF v0.2, and reduced stale claims from 80 to 9 and hallucinated claims from 15 to 0 in a repository-replay evaluation. It is useful as a concrete claim-granular freshness design and as a signal that the existing OpenWiki review may be outdated, but its mechanism and outcomes remain affiliated, self-reported claims until the implementation and evaluation artifacts are inspected.

## Quotes

No source quotes have been retained yet.

## Connections Found

The source is a concrete practitioner witness for [source changes surfacing downstream review targets](../notes/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md), [localized retention under sparse change](../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md), and [keeping lineage aligned with compiled views](../notes/agent-memory-requirements/keep-compiled-views-aligned.md): it instantiates those claims with claim-to-code dependencies, persisted evidence versions, and affected-page reconciliation. Relative to [Commonplace's freshness architecture](../reference/freshness-architecture.md), its main comparative value is granularity: both treat input-version mismatch as a reason to recheck rather than proof of falsehood, but OpenWiki reportedly tracks claim evidence while Commonplace registers review-pair inputs and accepted baselines.

The article is also a maintenance trigger and version-sensitive counterpoint for the code-grounded [OpenWiki review](../agent-memory-systems/reviews/openwiki.md), whose earlier pinned revision lacked claim-level provenance and deterministic invalidation. It does not itself establish that OpenWiki 0.4.0 implements the published design or reproduces the reported results.

## Extractable Value

1. **Claim-granular dependency versions turn source change into explicit review work.** The reported design operationalizes the lineage and compiled-view notes more precisely than file-level timestamps: a mismatch withdraws trust from a claim without prematurely declaring it false. [quick-win]
2. **Epistemic forgetting is distinct from deletion, supersession, and capacity pruning.** OpenWiki's useful framing is that a retained belief can remain present while its warrant is suspended pending re-verification; this could sharpen the KB's memory-lifecycle vocabulary if synthesized beyond this single system. [deep-dive]
3. **The intervention operates inside a fixed claim/evidence decomposition.** Stored claim text, linked code evidence, prior evidence versions, current evidence, and page context condition the agent; its expressible response is to affirm and refresh the evidence version, revise the claim/page/evidence together, or leave the item unresolved and stale. That makes the source a useful bounded case for the KB's effective-update-space analysis. [just-a-reference]
4. **The existing OpenWiki review has a concrete refresh axis.** Version 0.4.0 reportedly adds the exact claim-level provenance, deterministic invalidation, and OKF trust metadata absent from the review's earlier pinned checkout, so a refresh can test a specific contradiction rather than resurvey the system broadly. [quick-win]
5. **Detection cost and reconciliation cost need separate accounting.** The runtime reportedly scans the full claim set deterministically but exposes only stale claims on pages the agent reads; this supports affected-only model work, not the article's stronger unqualified claim that update cost is independent of total claim count. [experiment]

## Limitations (our opinion)

This is an affiliated account of one product and one reported repository-replay setup. It does not retain the repository, commit sequence, checkpoint schedule, prompts, judge, claim totals by checkpoint, repeated runs, error analysis, implementation revision, or evaluation code. The headline reductions therefore lack enough method to separate the runtime's effect from corpus construction, checkpoint selection, model variance, or classification error, and the individual 17%-to-0% example should not be generalized. Static code inspection could later confirm the mechanism but would still not reproduce these outcomes.

The effective update space is narrower than the self-correction headline. The runtime supplies claim units, claim-to-code evidence associations, persisted and current versions, and page context; the agent can map that information to a truth judgment and then refresh evidence, revise the wiki state, or defer. The representation and granularity of claims, the evidence-link format, version comparison, page-local surfacing, and benchmark repository, checkpoints, and labels remain fixed outside that space. As [learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), improvement within those choices does not validate them. The with-versus-without comparison varies the entire claims-runtime bundle, so it supports only that bundled contrast and cannot attribute the result specifically to claim granularity, evidence versioning, stale-state persistence, or the reconciliation interface.

The scaling claim also overreaches the described mechanism: model-mediated reconciliation may scale with the affected pages encountered, but deterministic staleness detection explicitly walks the full claim set. The article gives no asymptotic analysis or measurements separating those costs. It also reports OKF portability without showing interoperability tests or adoption by an independent consumer.

## Recommended Next Action

Run a code-grounded refresh of the [OpenWiki review](../agent-memory-systems/reviews/openwiki.md) against the OpenWiki 0.4.0 revision, covering claim sidecars, evidence-version invalidation, OKF v0.2 metadata, and the published evaluation artifacts while retaining the numerical results as vendor claims unless the evaluation can be reproduced.
