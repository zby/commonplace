---
description: "A practitioner account of Fluent, a software factory that turns observations into tested, reviewed, merged changes and reusable project expertise."
source: https://x.com/mrinal/status/2081823472016335059
captured: "2026-07-28T12:24:20.430766+00:00"
capture: xdk
genre: practitioner-report
snapshot_sha256: ca3c52d76db3019c47656b21dde9f97c1a00812c238e60c0adddd590cf240416
status_id: 2081823472016335059
conversation_id: 2081823472016335059
post_count: 5
ingested: "2026-07-28"
type: kb/sources/types/ingest-report.md
domains: [self-improving-systems, agent-memory, evaluation, software-engineering]
---

# Ingest: How I built a self-improving software factory

## Classification

A first-person account of building and using Fluent, with a detailed description of its workflow and claimed results rather than an independently evaluated study.
Author: @mrinal describes a system he built and reports improving throughput and output quality over roughly two months; the account is useful architectural evidence but remains self-reported.

## Summary

Fluent is presented as a software factory that turns observations, feedback, production data, and agent traces into working software through two queues: one for human context, judgment, expertise, and authority, and one for agent and compute capacity. Human-guided shaping produces a Brief, behavior specifications, a Technical Approach, and an Implementation Plan; execution then creates isolated Work Item Attempts with a Writer, an independent deterministic Tester, parallel Reviewers, and a Learner. Accepted changes become merge candidates, while the Learner can retain project-specific conventions, constraints, testing patterns, and gotchas as explicit Expertise that future shaping and execution can reuse. Follow-ups become later Observations or corrective Work Items, so the factory improves both the product and the machinery that produces future changes.

## Connections Found

The primary connection is the existing [self-improving-systems](../notes/self-improving-systems-README.md) cluster. Fluent is a practitioner anchor for [A proposal-selection improvement loop requires search, evaluation, and operative retention](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md): observations and shaping search the change space, deterministic tests and independent reviewers can reject candidates, and merge plus retained Expertise give accepted work future behavioral force. It also grounds the cluster's actor-allocation claim in [Increasing computational autonomy relocates human effort to the frontier](../notes/increasing-computational-autonomy-relocates-human-effort.md), while its Learner supplies a concrete trace-to-explicit-memory path for [Use Trace Extraction As Meta-Learning](../notes/agent-memory-requirements/use-trace-extraction-as-meta-learning.md). This is source-level practitioner evidence, not a code-grounded Fluent review.

## Extractable Value

1. **A software factory can improve its product and its production machinery in the same accepted change loop.** The Writer changes the application while the Learner can retain project Expertise and follow-ups, making the retained result affect later shaping, building, and review. This is a concrete self-improvement pathway rather than a generic claim that agents learn. [deep-dive]
2. **Human judgment can be isolated at authority-bearing transitions instead of every implementation step.** Fluent keeps humans responsible for context, decisions, and authorization while agents and compute continue independent ready work; this makes “more work per human judgment” operational rather than merely aspirational. [quick-win]
3. **Independent deterministic test evidence can separate execution from acceptance.** The Tester does not inherit the Writer's self-report, and all Reviewers share normalized test results while retaining targeted checks for their own questions. This is a reusable oracle-design pattern for proposal-selection loops. [quick-win]
4. **Layered specifications preserve reversible human decisions while delegating implementation detail.** Briefs, behavior specifications, technical choices, and implementation plans are confirmed in sequence; derived behavior is labeled for acceptance or rejection, and unresolved decisions move backward instead of being guessed by the Writer. [experiment]
5. **Follow-up handling gives weak discoveries a quarantine path.** The Learner records additional improvements as Observations, and only complete, testable corrections can bypass some shaping; otherwise the item returns to a human for clarification. This is a concrete authority gradient for trace-extracted candidates. [deep-dive]

## Limitations (our opinion)

This is a self-reported account from one builder and does not establish that Fluent's claimed throughput or quality gains result from the described machinery. The source does not provide comparative before/after measurements, workload definitions, acceptance rates, reviewer agreement, failure rates, or evidence that retained Expertise is faithfully reused. It describes a repository and installation path but does not, in this snapshot, establish which features are implemented in the linked code, which are optional, or which are aspirational. The system's human queue and approval gates may improve safety while also moving substantial work into shaping and review; the article does not quantify that tradeoff. Treat the architecture as a design-space example and the outcome claims as hypotheses until the implementation and longitudinal evidence are inspected.

## Recommended Next Action

Add this snapshot as an `evidenced-by` link from [A proposal-selection improvement loop requires search, evaluation, and operative retention](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md), using Fluent as a worked practitioner case of search, reject-capable evaluation, and operative retention; leave any code-grounded Fluent review for a separate repository-inspection task.
