---
description: "PILOT couples live supervisor steering with persistent skill updates, but its bundled evaluation does not isolate which harness choices cause later gains."
source: https://arxiv.org/html/2608.26530v1
captured: "2026-09-04"
capture: trafilatura
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 2ad63832ca1c2c724e63edf00e1d4fc44ead2a3f6f2b95e175ce25581dfb5d6c
ingested: "2026-09-04"
type: kb/sources/types/ingest-report.md
domains: [agent-orchestration, deploy-time-learning, trace-learning, long-horizon-agents]
---

# Ingest: PILOT in the Loop: Live Self-Improvement for Long-Horizon Agents

## Classification

This is a scientific paper: it defines a supervisor-worker agent harness, specifies its update protocol, and reports controlled benchmark comparisons and trajectory analysis across two frozen model backbones. Author: the ten named researchers are the system's designers and experimenters, which gives them direct technical knowledge but makes the evaluation first-party; the captured v1 arXiv paper supplies no independent replication signal.

## Summary

PILOT separates long-horizon task execution from oversight: an isolated worker emits notifications, questions, and a final result, while a connected supervisor can answer, queue steering for the worker's next turn, abort it, or write reusable skills and memory for later workers. With the same frozen backbone in both roles, PILOT reports the best result in five of six one-shot backbone-benchmark combinations and higher Terminal-Bench 2.0 pass rates than four single-agent harnesses. In repeated Terminal-Bench sweeps, updates created during runs are carried forward only from successful tasks; best-observed pass rate rises by 14.6 and 12.4 percentage points for the two backbones while output tokens per task fall. The paper therefore offers a concrete live-supervision and persistent-harness design, but its evaluations support the compound system more strongly than any individual retained skill or architectural choice.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper is a technical-basis case for [persistent deployment-time adaptation](../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md): a fixed-weight system derives natural-language skills and memory from live trajectories and exposes them to later workers and iterations. Its Question and Steer operations also instantiate the conversational-continuation side of [agent-to-agent coordination](../notes/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md), while its manual requirement that a diagnosed correction be followed on the successful path supplies evidence for [distinguishing task success from intended-path health](../notes/final-task-success-does-not-establish-intended-path-health.md). Its stronger “self-improvement” interpretation rests on the stricter [self-improving-system definition](../notes/definitions/self-improving-system.md), because aggregate later gains do not show that each retained artifact became operative.

As a comparison, PILOT separates live oversight from execution and carries successful-run updates across iterations, whereas [Continual Harness](./continual-harness-online-adaptation-foundation-agents.ingest.md) installs a refiner's edits into the acting agent's next step. [Harness Updating Is Not Harness Benefit](./harness-updating-is-not-harness-benefit.ingest.md) supplies the missing uptake analysis: PILOT measures skill-count growth and aggregate later outcomes, not whether particular skills were loaded, followed, and causally useful. [On the Fragility of Self-Improving Agents](./on-the-fragility-of-self-improving-agents.ingest.md) supplies the missing task-order and repeated-run control for PILOT's persistent state.

## Extractable Value

1. **Live supervision has three distinct timing coordinates.** PILOT separates intervention latency (steering the active worker), extraction timing (writing from an active trajectory), and activation horizon (later workers in the episode or later benchmark iterations), giving [trace-learning comparisons](../agent-memory-systems/trace-learning-techniques-in-related-systems.md) a more precise vocabulary than a single online/offline label. [deep-dive]
2. **A live channel preserves work already accumulated in an isolated execution context.** Notifications, blocking questions, queued steering, and abort let oversight redirect a worker without restarting it from a revised prompt, making PILOT a concrete counterpoint to final-return-only delegation APIs. [quick-win]
3. **Outcome filtering and knowledge extraction are separate stages.** PILOT creates candidate skills and memory before verifier results, then uses task success only to decide which run's updates survive; this is evidence for retaining a successful episode, not for treating every extracted procedure as its producing explanation. [quick-win]
4. **Corrected-path inspection is stronger than outcome attribution.** The trajectory analysis counts steering only when it identifies an error, the worker follows the correction, and success proceeds along that path, providing a reusable evaluation rule for live interventions. [quick-win]
5. **The reported efficiency gain is a system-level signal, not a skill-reuse ablation.** Falling output tokens and rising successes per million output tokens make later-work amortization worth testing, but supervisor separation, task repetition, accumulated skills, and task order remain bundled. [experiment]

## Limitations (our opinion)

The evidence is narrow for the claims that matter most to Commonplace. The one-shot comparison varies the whole PILOT harness, not live steering alone, so it does not isolate steering from role separation, context isolation, or other Pi extensions. The persistent-learning study repeats a fixed task set, reports the best observed improvement across iterations, and runs each configuration twice; it does not test transfer to unseen tasks, shuffled task order, per-skill loading or adherence, or independent reproduction. Success-only retention is especially weak evidence for the correctness and transfer scope of every distilled skill, as [a checked outcome licenses retaining an episode, not abstracting its explanation](../notes/checked-outcome-licenses-episode-retention-not-abstraction.md).

The effective update space is also fixed in consequential ways. The supervisor can condition on the goal, recent events, worker notifications and questions, errors, inactivity alerts, results, and selectively inspected trajectory history; it can answer, steer, abort, spawn workers, and write textual skills or memory. A frozen language model maps those signals to those operations. Model weights, the supervisor-worker partition, the five-operation channel, the Pi-based runtime, textual skill and memory representations, the self-improvement instruction, success-gated merging, and the benchmark-iteration partition all remain outside that update space. Under [the fixed-decomposition limit](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), improvement within this space does not establish that these fixed representations, partitions, or operations are necessary or preferable.

## Recommended Next Action

Update [Trace-learning techniques in related systems](../agent-memory-systems/trace-learning-techniques-in-related-systems.md) to add supervisor-mediated live trace learning as a subtype characterized by intervention latency, extraction timing, and activation horizon, using this ingest as the PILOT evidence record.
