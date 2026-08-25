---
description: "Figma's practitioner account of turning security precedents into a trusted, tested policy artifact that drives agent review, repo auditing, and secure code generation."
source: https://x.com/frgx/status/2081739292859421118
captured: "2026-07-28T11:52:12.808321+00:00"
capture: xdk
genre: practitioner-report
snapshot_sha256: 1a8549f3226f47f586c7b48fe1c9685a63b1d19d152b62ece9b82be07a707a2f
status_id: 2081739292859421118
conversation_id: 2081739292859421118
post_count: 9
ingested: "2026-07-28"
type: kb/sources/types/ingest-report.md
domains: [agent-memory, context-engineering, evaluation, security]
---

# Ingest: Thread by @frgx

## Classification

A first-person account from the Figma security workflow describing what was built and what the team learned.
Author: @frgx reports the Figma security team's experience, but the thread supplies no independent audit or reproducible study.

## Summary

Figma began with a noisy agent security reviewer—only 4 of 27 first-week findings were real—and withheld it from developers until precision improved. Writing 68 generic precedents exposed the team's threat model and produced an artifact that now powers pull-request review, repo-wide auditing, and secure code generation. The team reports 100+ latent vulnerabilities found in an initial full-repo audit, including two critical issues, and emphasizes that bug-bounty data supplied 46 of 66 evaluation bugs. The operational thesis is that policy-writing, evaluation data, and repeated testing give security engineers leverage while preserving human judgment.

## Quotes

No source quotes have been retained yet.

## Connections Found

The primary connection is the existing [self-improving-systems](../notes/self-improving-systems-README.md) cluster, especially [Increasing computational autonomy relocates human effort to the frontier](../notes/increasing-computational-autonomy-relocates-human-effort.md): this source is a practitioner example of completing more improvement work per human judgment while moving people from one-finding-at-a-time triage toward policy authorship, evaluation, and boundary judgment. [A proposal-selection improvement loop requires search, evaluation, and operative retention](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) supplies the mechanism lens: precedents are searched and written, reviewer quality is evaluated, and the retained policy enters future action paths. This is source-level evidence for the cluster, not a review of Figma's closed implementation. Secondary connections are the KB's accounts of ingress, deployment-time constraining, behavioral evaluation, and contextual activation: [Raw accumulation does not create usable memory](../notes/raw-accumulation-does-not-create-usable-memory.md), [Constraining during deployment is continuous learning](../notes/constraining-during-deployment-is-continuous-learning.md), [Evaluate Memory By Effects, Not By Existence](../notes/agent-memory-requirements/evaluate-memory-by-effects.md), and [Knowledge storage does not imply contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md).

## Extractable Value

1. **Precision work can reveal and codify an organization's latent threat model.** The team's attempt to reduce false positives turned generic precedents into an explicit policy artifact, showing how operational tuning can expose reusable institutional knowledge. This is a concrete mechanism for the ingress and constraining claims above. [quick-win]
2. **A self-improving agentic system can increase work completed per unit of human effort by moving humans up the leverage gradient.** The same retained material reportedly informs PR review, full-repository auditing, and secure code generation, while security engineers shift from one-bug triage toward policy authoring, evaluation, and judgment. This is a useful design-space example for comparison with Commonplace's intended self-improvement loop. [deep-dive]
3. **Trust is an adoption gate, not a cosmetic quality score.** Withholding the reviewer until 4/27 first-week precision problems were addressed illustrates that low-noise output is a precondition for human uptake, even when the system is technically available. [quick-win]
4. **Evaluation coverage is part of the learned artifact's quality.** The 46-of-66 bug-bounty contribution and daily testing suggest that improving the policy requires a representative, continuously exercised corpus, not only prompt or rule refinement. [deep-dive]
5. **Repo-wide auditing can expose a different risk surface from local review.** The reported 100+ latent vulnerabilities, including two criticals in old code, are a hypothesis that broad retrospective coverage adds value beyond ordinary tooling and review; the magnitude and causal attribution need verification. [experiment]

## Limitations (our opinion)

This is a self-reported practitioner account from one organization, so it does not establish that the same workflow or numbers generalize. The thread gives no definitions for a “real” finding, no precision/recall methodology, no comparison against the exact traditional tools or human processes, and no denominator for the 100+ vulnerabilities beyond the broad full-repo audit. It also does not show how precedents are versioned, reviewed, retired, or prevented from encoding false assumptions. The later reply adds model-provider detail but does not independently validate the main claims. Treat the figures as leads for a worked case, not as evidence of universal agent-security performance.

## Recommended Next Action

Add this snapshot as an `evidenced-by` link from [Increasing computational autonomy relocates human effort to the frontier](../notes/increasing-computational-autonomy-relocates-human-effort.md), using it as a closed-source practitioner example for the self-improving-systems cluster; keep the numerical claims explicitly marked as self-reported until the linked Figma article or stronger evidence is captured.
