---
description: "Agno practitioner loop mines specifications and usage traces into probes, then iteratively edits a live agent within a fixed, weakly evaluated outer method"
source: https://x.com/ashpreetbedi/status/2084301728363462919
captured: "2026-08-03T18:05:02.311358+00:00"
capture: xdk
genre: practitioner-report
snapshot_sha256: d03da8d4a6d955bd8da779ceb1d2496fa7c27473d9208965349c833c59a03b73
status_id: 2084301728363462919
conversation_id: 2084301728363462919
post_count: 1
ingested: "2026-08-03"
type: kb/sources/types/ingest-report.md
domains: [self-improving-systems, harness-engineering, evaluation, deploy-time-learning]
---

# Ingest: How to Recursively Improve Your Agents

## Classification

Ashpreet Bedi describes a workflow he built and says he routinely uses it to improve Agno agents, with a worked Radar-agent walkthrough and self-reported before/after result but no independently inspectable experiment.
Author: Ashpreet Bedi (@ashpreetbedi), writing as the builder of the Agno/AgentOS workflow. The first-person operational detail is useful architectural evidence, while the product affiliation and absence of raw results make the effectiveness claims promotional and unverified.

## Summary

The article presents “recursive auto-improvement” as a coding agent improving a separate live target agent toward a fixed specification. The coding agent reads the target's instructions, mines stored sessions for recurring requests and visible failures, derives golden-path, edge-case, tool-selection, and adversarial probes with one-line expected behaviors, runs them through the live API, inspects tool calls and container logs, and changes one lever at a time—tightening or adding a rule, swapping a tool, or tuning code and parameters—before restarting and rerunning failed probes. The author contrasts this convergent process with recursive self-improvement in the stronger compounding sense, recommends 300–500-probe unattended runs, and reports moving the example agent from 7/10 to every probe passing.

## Claims

No claims have been grounded yet.

## Connections Found

The source is a compact practitioner instance of [A proposal-selection improvement loop requires search, evaluation, and operative retention](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md): bounded edits supply search, probes and a judge supply reject-capable evaluation, and restarted code supplies operative retention. Its strongest support is for [Diagnostic richness constrains outer-loop learning quality](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md), because the proposer receives specifications, usage sessions, live responses, tool calls, errors, and debug logs rather than only scores. Its claimed fixed-point convergence is bounded by [A proximate target is checked for achievement, not for warrant](../notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md) and [Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md): passing derived probes establishes conformity within a fixed specification, probe generator, judge, platform, and edit space, not that those fixed choices yield broader production quality. [Self-Harness](./self-harness-harnesses-that-improve-themselves.ingest.md) is the stronger empirical comparison, while the code-grounded [Agentic Harness Engineering](../agent-memory-systems/reviews/agentic-harness-engineering.md) and [Exo](../agentic-systems/exo.md) expose the versioning, regression attribution, rollback, and protected-substrate controls this walkthrough leaves implicit.

## Extractable Value

1. **Convergent auto-improvement is usefully separated from compounding recursive self-improvement** -- The source reserves RSI for improvements that target improvement ability and compound, while its RAI loop pulls a target agent toward a fixed specification. The names are not field-settled, but the mechanism distinction prevents ordinary iterative harness tuning from inheriting open-ended self-improvement claims. [quick-win]

2. **Specifications and usage traces play complementary roles in probe construction** -- The written specification supplies expected behavior, while real sessions supply recurring request shapes, fumbles, and out-of-scope cases. This is a practical way to combine intended behavior with observed distribution evidence, provided neither is treated as an independent test of the other. [experiment]

3. **The trace-to-edit loop makes diagnostic access operational** -- Live API calls establish behavior, container logs expose trajectories, and framework documentation helps map failures to editable instructions, tools, or parameters. This is another practitioner convergence signal that outer-loop search needs inspectable failure evidence, not just an aggregate grade. [quick-win]

4. **One-lever edits improve local attribution but need full-suite regression** -- Tightening one rule or swapping one tool at a time makes each hypothesis more falsifiable and keeps repair scope small. However, rerunning only failed probes can miss regressions in previously passing behavior; the locality benefit is safe only when followed by a complete regression pass. [experiment]

5. **The effective update space is explicit enough to audit** -- Behavior can condition on instructions, sessions, live responses, tool traces, errors, logs, and framework information; the coding agent can compose reachable instruction, tool, parameter, and code edits. The target specification, probe derivation, judge, coding agent, AgentOS architecture, observation surfaces, and stopping rule remain fixed, so success only supports optimization inside that compound configuration. [deep-dive]

6. **“One AI improves another” is an actor-allocation fact, not a system-membership test** -- The target agent is being improved when assessed alone; a declared composite containing the coding agent, target, platform, evaluator, and retained edits may be a self-improving system. This supplies a clean example of why self-improvement attribution depends on system boundary without contradicting the source's narrower denial of compounding RSI. [just-a-reference]

## Limitations (our opinion)

The reported move from 7/10 to every probe passing is not documented as an evaluation result. The snapshot contains no probe set, scoring rubric, before/after table, judge output, variance estimate, failure count, cost breakdown, untouched test set, or independent reproduction. “Every probe passes” is the loop's stopping condition, so it is training/selection performance rather than evidence of generalization. The same target specification helps generate expected behaviors and judge responses, while usage sessions help generate the cases; neither provides an independent outcome measure.

The required fixed-decomposition analysis further narrows the claim. The loop can repair mappings expressible through the coding agent's reachable instruction, tool, parameter, and code edits from the signals its API and logs preserve. It cannot discover a necessary distinction absent from those histories, express a response outside those edit surfaces, or revise mistakes in the fixed target specification, probe generator, judge, platform architecture, or pass criterion. The result shows the reported configuration can be fitted to its generated probes, not that this is the right decomposition for agent improvement.

Regression handling is unclear and potentially unsound. The article says each edit reruns only what failed; unless the unseen final report executes the entire suite, a repair can break previously passing probes and still appear to advance. The claim that 300–500 probes find failures occurring once in a hundred runs also lacks a stated sampling model or coverage argument. Probe count alone does not establish independence, rarity coverage, or judge validity.

Finally, the setup instructs users to run Claude Code with `--dangerously-skip-permissions`, then recommends unattended overnight edits to executable agent code and tools. No sandbox, allowlist, review gate, rollback protocol, canary, protected state, or blast-radius limit is described. [Warranted autonomy is bounded by oracle domain](../notes/warranted-autonomy-is-bounded-by-oracle-domain.md): a model judge can make the loop autonomous, but the source does not show that its oracle warrants broad code and tool mutation without supervision.

## Recommended Next Action

Keep this as a source-only practitioner reference; do not promote its RAI vocabulary or effectiveness claims until the workflow publishes a complete-suite regression pass, an untouched evaluation set, and enough probe/judge detail to distinguish genuine agent improvement from fitting the generated probes.
