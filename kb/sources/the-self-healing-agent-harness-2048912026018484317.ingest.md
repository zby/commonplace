---
description: "Practitioner report where live agent-response graders feed tickets, auto-fixes, re-grading, and rollout gates instead of sitting as offline eval dashboards"
source_snapshot: "the-self-healing-agent-harness-2048912026018484317.md"
ingested: "2026-04-29"
type: kb/sources/types/ingest-report.md
domains: [agent-evaluation, harness-engineering, deployment-reliability, oracle-theory]
---

# Ingest: The Self-Healing Agent Harness

Source: the-self-healing-agent-harness-2048912026018484317.md
Captured: 2026-04-29T17:21:59.182403+00:00
From: https://x.com/intuitiveml/status/2048912026018484317

## Classification

Type: practitioner-report -- the author describes a production system they built and operate: a live-traffic grader, engineering pipeline, and rollout gate for an AI agent product.
Domains: agent-evaluation, harness-engineering, deployment-reliability, oracle-theory
Author: @intuitiveml is unknown from local KB context; the credibility signal is operational specificity about CREAO's production grading, ticketing, fix, verification, and rollout loops.

## Summary

The source argues that for AI agent products, evaluation and QA should be the same loop. Instead of treating model evaluation as an offline dashboard and QA as a separate engineering function, CREAO grades sampled live agent responses with a category-conditioned tri-judge panel, turns low scores into clustered production bugs, routes urgent clusters into investigation and draft PRs, verifies fixes with telemetry, re-grades closed clusters, and uses live grader scores to gate grey rollouts. The main contribution is not "LLM-as-judge" by itself; it is the operational coupling: a bad agent response becomes a product bug signal, an engineering ticket, a candidate fix, a regression check, and a release gate.

## Connections Found

The connect pass found a tight evaluation/oracle cluster. The strongest note connections are [Evaluation automation is phase-gated by comprehension](../notes/evaluation-automation-is-phase-gated-by-comprehension.md), [The boundary of automation is the boundary of verification](../notes/the-boundary-of-automation-is-the-boundary-of-verification.md), [Error correction works with above-chance oracles and decorrelated checks](../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md), [Spec mining is codification's operational mechanism](../notes/spec-mining-as-codification.md), [Deploy-time learning is the missing middle](../notes/deploy-time-learning-is-the-missing-middle.md), [Constraining during deployment is continuous learning](../notes/constraining-during-deployment-is-continuous-learning.md), and [Apparent success is an unreliable health signal in framework-owned tool loops](../notes/apparent-success-is-an-unreliable-health-signal-in-framework-owned.md). The source also compares directly with the existing harness-source cluster: [Harness Engineering: Leveraging Codex in an Agent-First World](harness-engineering-leveraging-codex-agent-first-world.ingest.md), [Harness Engineering Is Cybernetics](harness-engineering-is-cybernetics-2030416758138634583.ingest.md), [The Anatomy of an Agent Harness](the-anatomy-of-an-agent-harness-2031408954517971368.ingest.md), [The Bug That Shipped](the-bug-that-shipped-2035319413474206122.ingest.md), and [Meta-Harness](meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md). The new fit is specific: this source adds the product-facing QA and release-control layer to a KB cluster that already had harness anatomy, cybernetic framing, code-generation practice, explicit failure probes, and benchmark harness optimization.

## Extractable Value

1. **Evaluation and QA as one production loop** -- The highest-reach claim is that agent quality scores become useful only when coupled to engineering action: grade, triage, fix, verify, re-grade, and gate. This extends the KB's oracle theory from "can we verify?" to "does the verification signal enter the work system quickly enough to change production behavior?" [quick-win]
2. **LLM judges need operational calibration, not scientific purity** -- The source's surprising move is to reject leaderboard-style methodological rigor while still preserving calibration: cross-family judges, structured rubrics, quorum handling, persisted disagreement, and human spot checks. The simpler account is that the grader only needs enough discriminative power to route bugs, not enough validity to publish benchmark rankings. [quick-win]
3. **Outcome grading beats trajectory grading for agent products** -- Penalizing strange tool paths can punish successful agent behavior; grading the final user-facing answer better matches product risk. High reach, but bounded: for safety, cost, and permission issues, trajectory still matters. [experiment]
4. **Soft oracles can gate releases when paired with blast-radius control** -- The bridge uses small real-traffic cohorts, baseline comparisons, minimum interaction windows, statistical thresholds, and automatic rollback. This is a concrete pattern for making soft LLM-grader signals operationally usable without pretending they are hard tests. [experiment]
5. **Quality drops are root-cause-agnostic sensors** -- A bad response may come from model reasoning, tool-contract drift, infra flakes, prompt/context plumbing, stale integrations, or deploy regressions. The grader does not need root cause at scoring time; it only needs to trigger triage. This sharpens the cybernetics frame: sensors can be coarse if the downstream investigation loop is strong. [quick-win]
6. **Minority-model sampling by model, not traffic** -- Sampling 100% of low-traffic or experimental models while sampling only a slice of the dominant production model is a practical evaluation-design detail. Low reach but operationally valuable for teams running multi-model products. [just-a-reference]
7. **A score without a ticket is dashboard waste** -- The source gives a strong phrasing for a recurring KB concern: metrics that do not feed action do not constitute learning. This directly echoes validity/value gates and effect-based evaluation in a production QA setting. [quick-win]

## Limitations (our opinion)

This is a single-team practitioner report, not an independently evaluated system. The source provides architectural detail but no raw data, no public rubric, no calibration results, no examples of false positives or false negatives, and no defect-rate comparison against human QA or staging. The reported shipping cadence and lack of QA/staging may depend heavily on product domain, tolerance for degraded answers, customer profile, and internal model/tooling access.

The central claim is partly hard to vary: if low scores do not create tickets, fixes, verification, or rollout decisions, the "harness" collapses into a dashboard. That mechanism is strong. Other parts are easier to vary. A tri-judge panel is one way to build a soft oracle, but not the only way; grey rollouts are one way to cap blast radius, but not the only deployment strategy; Linear and draft PRs are implementation details rather than the underlying mechanism.

The largest trust gap is judge quality. Cross-model agreement and human spot checks reduce correlated judge error, but the source does not show calibration curves, disagreement rates, category-level error, or how judge drift is detected over time. The [error-correction](../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) note predicts that decorrelation and TPR/FPR separation matter; this source asserts several plausible design moves but does not quantify whether they are sufficient.

Finally, "grade the outcome, not the trajectory" should not be overgeneralized. It is sound for user-facing answer quality, but trajectory remains load-bearing for cost explosions, unsafe tool use, privacy boundaries, permission bypasses, and infrastructure health. The stronger formulation is: grade the outcome for product-quality triage, and separately monitor trajectory for safety, economics, and degraded execution.

## Recommended Next Action

Write a note titled "Agent evaluation becomes QA when scores enter the engineering loop" connecting to [evaluation-automation-is-phase-gated-by-comprehension](../notes/evaluation-automation-is-phase-gated-by-comprehension.md), [spec-mining-as-codification](../notes/spec-mining-as-codification.md), and [the-boundary-of-automation-is-the-boundary-of-verification](../notes/the-boundary-of-automation-is-the-boundary-of-verification.md). It would argue that production agent evaluation only becomes learning infrastructure when the verifier signal is wired into triage, fixes, regression checks, and release gates; otherwise it remains a dashboard.
