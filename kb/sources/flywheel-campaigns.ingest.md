---
description: "Flywheel separates submission admission, automation handoff, and scoring, with typed metadata and a required visibility check at finalization."
source: https://docs.flywheel.paradigma.inc/concepts/campaigns
captured: "2026-09-17"
capture: curl+trafilatura
capture_scope: partial-source
genre: practitioner-report
snapshot_sha256: 6023a22b00ba40f2536a485e4b1ba1dbdebaec24da1d41b66e8de39a7aca86c0
ingested: "2026-09-17"
type: types/ingest-report.md
domains: [artifact-validation, workflow-state, observability]
---

# Ingest: Flywheel — Campaigns

## Classification

Practitioner documentation of a product contract: it describes submission rules, rejection behavior, query tools, and lifecycle states without reporting an evaluation. Author: Paradigma, the provider of Flywheel; authoritative about the documented interface, but not independent evidence that the implementation satisfies it.

## Summary

Flywheel campaigns organize challenge attempts under an organizer-owned root. Finalized artifacts marked with submission metadata enter a campaign-specific admission process; drafts retain ordinary metadata. The documented public-visibility policy requires the attempt node to be public before submission finalization. Invalid submissions receive `422`, create no lifecycle record, and do not trigger submission hooks. Accepted submissions receive a durable, queryable lifecycle record that distinguishes acceptance, automation processing, handoff, retry states, and terminal outcomes. In particular, `forwarded` does not establish that an external scorer has finished. The page provides a concrete contract for separating artifact admission from downstream evaluation, rather than evidence that the separation improves outcomes.

## Quotes

No source quotes have been retained yet.

## Connections Found

The source supplies a bounded product example for [Methodology enforcement is constraining](../notes/methodology-enforcement-is-constraining.md): its agent checklist describes the intended action, while the documented runtime boundary rejects an invalid finalization before downstream hooks run. This instantiates both a fixed activation point and an encoded acceptance condition. It also illustrates the attachment-point claim in [Verification needs a typed target before it needs an oracle](../notes/verification-needs-a-typed-target-before-it-needs-an-oracle.md): `metadata.campaign_role = "submission"` identifies the artifacts subject to campaign checks, while ordinary drafts remain outside that class. Neither connection establishes substantive scoring quality.

The lifecycle account is an adjacent operational example for [ADR 043's separation of completion, outcomes, and freshness](../reference/adr/043-review-state-separates-completion-outcomes-and-freshness-baselines.md). Both distinguish progress through a protocol from a substantive judgment. Flywheel's particular states do not map one-to-one to Commonplace's review model, and the page supplies no counterpart to freshness baselines.

## Extractable Value

1. **Admission checks need both an artifact class and an enforced boundary.** The submission marker selects the relevant artifacts; finalization applies the visibility predicate. This is a concrete documented example supporting the existing enforcement and typed-target notes, without proving their general necessity or sufficiency. [quick-win]
2. **A handoff acknowledgement is insufficient evidence of evaluation completion.** The explicit distinction between `accepted`, `forwarded`, and `scored` gives a reusable example for interpreting asynchronous workflow status. A dedicated lifecycle query avoids inferring submission state from a hook or leaderboard artifact, though the page does not measure whether operators make fewer errors. [quick-win]
3. **Pre-admission rejection has different observability from accepted work.** An invalid finalization produces no lifecycle record, so the request error is the evidence of rejection; it must not be treated as an accepted submission still awaiting evaluation. This is a context-bound detail useful when implementing a campaign client. [just-a-reference]

## Limitations (our opinion)

The retained capture is partial: introductions to submission metadata and visibility configuration have no accompanying code examples. It supports the field names and values stated in prose, but not a complete configuration schema. No implementation, executions, failure logs, or operational measurements are included. The provider's documentation therefore supports an account of intended behavior, not verified enforcement reliability or comparative workflow performance.

The page does not establish who may write lifecycle transitions, whether writes and handoffs are atomic, how scores are authenticated, or how retries avoid duplicate effects. Naming `retrying` and `rate_limited` does not establish retry safety. A durable record also does not establish event sourcing or replayable projections. The simpler supported account is an admission check followed by status tracking; stronger architecture claims would require other evidence.

The public visibility requirement, including the default when policy is absent, is a campaign-specific publication rule. It supplies no basis for making ordinary KB artifacts public. Classification likewise supplies a check attachment point rather than a scoring oracle: a valid submission can still be substantively poor.

## Recommended Next Action

Add a short, explicitly documentation-based example to [Methodology enforcement is constraining](../notes/methodology-enforcement-is-constraining.md), using the submission marker, finalization boundary, and visibility rejection to illustrate the separate activation and response rules.
