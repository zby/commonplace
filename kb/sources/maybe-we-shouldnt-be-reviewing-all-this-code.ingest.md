---
description: "Rachel Laycock argues that AI-scale code production should move design judgment upstream, automate deterministic checks, and reserve late human review for risky exceptions."
source: https://martinfowler.com/rachels-ramblings/code-review.html
captured: "2026-09-03"
capture: trafilatura
capture_scope: full-source
genre: conceptual-essay
snapshot_sha256: b9037443f989266b1c9fbbd9d26918bdda2bb055cac4e7acb667dd1378507723
ingested: "2026-09-03"
type: kb/sources/types/ingest-report.md
domains: [agentic-coding, code-review, human-judgment, software-development]
---

# Ingest: Maybe We Shouldn't Be Reviewing All This Code

## Classification

This is a conceptual essay: it answers another essay with a causal argument and a workflow proposal, supported by practitioner examples rather than a reported evaluation.
Author: Rachel Laycock grounds the position in her experience with Thoughtworks practices and in a public disagreement with DX's Brian Houck. That supplies an informed practitioner perspective, not independent outcome evidence.

## Summary

Laycock argues that AI has exposed a mismatch between rising code-production volume and universal pull-request review. Teams should separate the functions accumulated in that ceremony: explore alternatives, transfer knowledge, and align architecture before implementation through pairing and collective design; encode deterministic requirements in tests, static analysis, security scanning, and fitness functions; and reserve late human review for changes with high stakes, broad blast radius, unfamiliar critical context, or low confidence. The proposal keeps human judgment but moves it closer to the decisions it informs, with the intended outcome that engineers retain understanding of whole systems rather than merely inspect finished diffs.

## Quotes

No source quotes have been retained yet.

## Connections Found

The essay serves as a practitioner design argument for relocating rather than removing human judgment. Its split between codified checks, collaborative design, and exceptional review is evidence for [Semantic work can be relocated but not eliminated](../notes/semantic-work-can-be-relocated-but-not-eliminated.md) and a concrete case of [Increasing computational autonomy relocates human effort to the frontier instead of reducing it](../notes/increasing-computational-autonomy-relocates-human-effort.md). Its risk triggers compare with [Warranted transfer out of the human cut leaves people the hardest-to-warrant decisions](../notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md), but the essay proposes that allocation rather than showing that real transfers produce the predicted residue. As an independent companion to [Why Software Factories Fail: Turning the lights back on](why-software-factories-fail-lights-back-on-2081058573556306030.ingest.md), it adds pairing, collective ownership, executable architectural constraints, and review by exception to the shared upstream-judgment pattern.

Read through [Naur's theory-building view](programming-as-theory-building.ingest.md), shifting judgment left does not require deriving the correct design before implementation. A [partial, fallible program theory](../notes/program-theory-sustains-search-under-delayed-feedback.md) can instead make early alternatives and design proposals act as [lightweight search control](../notes/lightweight-search-control-does-not-license-adoption.md): they decide which structures to explore, which commitments to preserve, and when a failed branch should cause backtracking, without licensing any proposal as correct. The timing matters because pull-request review begins after the team has selected one branch and paid much of its implementation cost. Pairing and design sessions can still redirect search before that commitment, while tests and fitness functions reject what can be checked mechanically and later outcomes can revise the theory.

## Extractable Value

1. **Decompose code review by decision type and timing** -- Alternative selection, knowledge transfer, and architectural alignment need meaning-dependent interaction before implementation; formatting, linting, known security rules, and deterministically testable properties can become executable constraints; residual risk can receive late human review. This operationalizes the placement question in the semantic-work note. [quick-win]
2. **Route exceptional review with explicit risk signals** -- Fundamental architecture changes, sensitive security boundaries, large blast radius, unfamiliar critical systems, and declared low confidence form a concrete starting set for a review-by-exception policy. The source does not define thresholds, so this is a testable routing proposal rather than a ready rule. [experiment]
3. **Treat system understanding as a different target from diff inspection** -- The essay accepts cognitive and intent debt as a real risk but locates its controls in pairing, shared design, executable architecture, and collective operational responsibility. This sharpens the distinction between transferring a program theory through close work and inspecting a completed artifact. [deep-dive]
4. **Use independent workflow convergence to isolate the mechanism** -- Laycock and Horthy both move expensive judgment upstream when generation outpaces late review, but they offer different controls for the remaining uncertainty: pairing and exceptional review here, staged artifacts and short vertical slices in Horthy's workflow. Their overlap supports a placement-and-bounding synthesis, not an empirical quality claim. [deep-dive]

## Limitations (our opinion)

The essay does not compare mandatory pull-request review with its proposed substitutes on escaped defects, security outcomes, architectural coherence, knowledge distribution, or review effort. Its result could depend on mature automation, experienced teams, small trunk-based changes, or unusually effective pairing rather than on earlier judgment in general. It also leaves the exception policy underspecified: teams receive examples of risky changes but no thresholds, audit mechanism, or response to cases misclassified as routine. The Meta and DX code-volume figures are reported second-hand, so this source should not be used as primary evidence for those measurements. The broader claim that mandatory review is a weak defense against cognitive and intent debt is plausible but untested here.

## Recommended Next Action

Test the proposal-as-search-control reading on one concrete workflow trace before promoting it: record an upstream design proposal, the branch it changed, the downstream check or outcome, and any resulting backtrack or theory revision.
