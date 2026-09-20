---
description: "Traverse reports failures hidden by successful agent outcomes; Scout improves candidate-run selection, motivating calibrated trajectory audits rather than assumed online prevention."
source: https://arxivb.org/abs/2609.17930
captured: "2026-09-20"
capture: trafilatura
capture_scope: full-source
genre: news-article
snapshot_sha256: b0d9917572963c9e78b432a3f975ecf5a5f8ededddbf91a9c57542d42a373c1b
ingested: "2026-09-20"
type: kb/sources/types/ingest-report.md
domains: [agent-evaluation, failure-localization, trajectory-selection]
learning_claims: true
---

# Ingest: Locating Hidden Failures Makes Long-Horizon Agents More Reliable

## Classification

A secondary publication reproducing a paper abstract alongside automated editorial assessment and publication statistics. The scientific claims below are reported abstract claims, not independently inspected paper results. Author signal: the abstract names Salman Rahman and colleagues; arxivbangers contributors publish the page, and its editorial assessment is automated. The editorial score and social engagement are selection metadata, not research validation. This analysis is derived from the [captured publication](https://arxivb.org/abs/2609.17930).

## Summary

The abstract reports Traverse, human-verified annotations of 6,967 mistakes in 2,518 agent trajectories across software engineering, computer use, and science, classified into 78 failure types. It describes poor recovery and rare self-detection after first mistakes, including damaging actions in runs scored as solved. Six frontier judges struggle to locate the first mistake: the strongest succeeds in fewer than one-third of runs. Scout, a trained 4B verifier, reportedly localizes failures better and transfers to unseen domains. When used to select among candidate runs from an unchanged agent, it improves task success over that agent's single attempt. This tests a verifier-and-selection arrangement; the retained abstract gives neither a matched candidate-budget comparison nor evidence that online interception prevents harmful actions. The page is useful motivation for trajectory evaluation, with insufficient methods to judge deployment readiness.

## Quotes

No source quotes have been retained yet.

## Connections Found

The source is a bounded comparison for [final task success does not establish intended-path health](../notes/final-task-success-does-not-establish-intended-path-health.md): both distinguish endpoint outcomes from properties of the executed route. Traverse reports harmful and fabricated-success routes; the note analyzes successful fallbacks and infrastructure health. Those are different mechanisms, so the abstract does not validate the note's specific fallback account.

The reported progression from human-verified failure annotations to a specialized verifier supplies an empirical example relevant to [evaluation automation is phase-gated by comprehension](../notes/evaluation-automation-is-phase-gated-by-comprehension.md). It does not show that this sequence is necessary or isolate the contribution of the taxonomy. The existing [trajectory-aware workflow evaluation proposal](../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) is the practical destination: the abstract motivates localization and harmful-success cases, while the proposal supplies local calibration and cost requirements. Scout's reported gains within candidate-run selection do not satisfy those requirements or establish the superiority of a trained verifier over alternative evidence representations and judging arrangements.

## Learning Claims (our opinion)

The source distinguishes training a verifier from retraining the acting agent. Scout learns a failure-localization function; at test time that verifier helps choose among candidate runs while the agent remains unchanged. The abstract reports cross-domain transfer, but does not describe the training objective, input representation, or split construction in enough detail to assess what was learned or exclude leakage independently.

In Commonplace terms, training Scout is parametric learning, and applying it to select a run uses the learned evaluator. Neither establishes [theory refinement](../notes/definitions/theory-refinement.md): the capture identifies no addressable theory whose parts are revised against failed cases and reused. The closing aspiration that agents learn from their mistakes goes beyond the demonstrated selection result. Localization could supply a repair signal, but no persistent change in the acting agent is shown here.

The boundary in [learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) matters: candidate generation and the agent's underlying behavior remain outside the reported selection intervention. A better selector can exploit variation among available runs; its gain does not establish that failure localization is the best evaluation target or that selection can supply a missing successful behavior. The abstract leaves the verifier's effective input and update space too underspecified for a stronger mapping. It supports keeping diagnosis, selection, and durable revision distinct, without requiring a change to Commonplace's learning concepts.

## Extractable Value

1. **Successful outcomes need separate path checks.** The reported harmful-success cases add a concrete empirical motivation for testing whether Commonplace audits can find workflow violations hidden by acceptable artifacts. The transferable contribution is the distinction between endpoint and execution evidence; the frequency and kinds of harm remain source-population claims. [quick-win]
2. **Failure localization deserves its own calibration target.** Poor first-mistake identification by the reported frontier judges warns against treating a plausible trajectory explanation as an accurate diagnosis. A local test should measure evidence localization separately from overall artifact grading, under the existing workflow-evaluation proposal. [experiment]
3. **Separate verifier quality from extra candidate generation.** Scout's reported gain over a single attempt concerns the combined candidate-generation and selection arrangement. A matched candidate-budget comparison would be needed to attribute the selection advantage to Scout rather than additional attempts; prevention would need a separate intervention before harm occurs. This bounds reuse of the result in Commonplace's evaluation design. [experiment]

## Limitations (our opinion)

The capture covers the full secondary page, not the full scientific paper. It contains an abstract and automated interpretation but no methods, experimental tables, annotation protocol, agreement statistics, split details, candidate counts, or compute costs. The exact Scout improvement, precision/recall tradeoffs, and unseen-domain transfer conditions cannot be established from it. No implementation was inspected or executed.

The abstract's task-and-environment explanation of recovery, rather than framework dependence, lacks visible controls here. Its localization comparison does not establish that model scale generally fails to help, nor that self-reflection cannot work. Specialized training and evaluation conditions differ from those of the frontier judges; the capture does not isolate why Scout wins. Additional candidate generation is a simpler possible contributor to the task-success gain over one attempt.

The editorial suggests preventing destructive actions, but selection among already executed trajectories cannot undo harm incurred during candidate generation. Effective online prevention requires detection in time, an intervention mechanism, and evidence about false alarms and overhead. Neither the abstract nor the editorial provides that demonstration. These gaps make the source useful for motivating the existing local experiment, not for adopting Scout or general trajectory judging as a required workflow step.

## Recommended Next Action

Update [Trajectory-aware evaluation of transforming agent workflows](../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) with this source's bounded motivation for first-error localization and harmful-success cases, preserving the proposal's independent calibration requirements and the distinction between post-hoc selection and online prevention.
