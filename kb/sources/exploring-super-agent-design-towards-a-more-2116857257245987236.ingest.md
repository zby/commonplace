---
description: "DeepSeek Harness proposes an always-online Router/Worker architecture; synthetic tests bound its routing savings, while long-term memory and endpoint security remain open."
source: https://x.com/DeepSeekHarness/status/2116857257245987236
captured: "2026-11-01T20:00:44.413268+00:00"
capture: xdk
genre: design-proposal
snapshot_sha256: 51d78b4eddd61e5c7e9b3a0c2dfa3b8a76b871116e4c859221cbcf8fd5b37ebe
status_id: 2116857257245987236
conversation_id: 2116857257245987236
post_count: 1
ingested: "2026-11-01"
type: types/ingest-report.md
domains: [event-driven agents, router-worker architecture, multi-hop context recall, asynchronous execution]
---

# Ingest: Exploring Super-agent Design: Towards a More Autonomous Agent System

## Classification

An architecture proposal informed by internal deployment experience and preliminary synthetic experiments, not a specification of released DeepSeek Harness features. The article explicitly distinguishes its design ideas and prototype from an official product.

Author: Yujia Qiao, who is credited with implementing the system and writing the article, with review and discussion by the DeepSeek Harness team. The captured post is published by @DeepSeekHarness and identifies itself as a machine translation from Chinese.

## Summary

The source proposes making sessions an internal execution detail rather than the user's unit of work. A long-lived Router handles human interaction and cross-task coordination without executing tasks; isolated Workers execute independent tasks and report back through it. Deterministic event admission and Thread subscriptions bypass repeated model routing, while Inline & Spill and Chain of Recall expose summaries and related object IDs for on-demand context retrieval. Asynchronous tool execution, separate compute/state/execution environments, and an external model-driven Watchdog support responsiveness and persistence. In a synthetic workload with simulated coding tools, the two-level system reports shorter completion times than two prompt-driven single-session/subagent configurations; within that two-level design, subscription pass-through reduces aggregate cache-read tokens without improving completion time. These tests concern scheduling, not coding quality. Long-term memory, scaling across tightly coupled tasks, and security between untrusted events and credential-bearing endpoints remain unresolved.

## Quotes

> When the Router layer creates a Worker Session for the first event in a Thread, that Worker subscribes to the Thread directly. From then on, event routing follows one of the two paths shown below:
> Subscribed (Fast Path): Code passes follow-up events in the Thread straight through to the subscribed Worker, so the Router layer does not need another tool call to forward them. If a new event falls outside the current task, the Worker can unsubscribe or hand the event back to the Router layer to be dispatched again.
> Unsubscribed (Slow Path): The Router layer can still see every event, which lets it track global state, but it only evaluates and dispatches new events that have no subscriber yet.
> --- `kb/sources/.snapshots/exploring-super-agent-design-towards-a-more-2116857257245987236.md` @ `sha256:51d78b4eddd61e5c7e9b3a0c2dfa3b8a76b871116e4c859221cbcf8fd5b37ebe` — Section 3.2, Event Routing

> The experiments use synthetic workloads and simplified environments, and parts of the setup could be more rigorous, so the results below are indicative only.
> --- `kb/sources/.snapshots/exploring-super-agent-design-towards-a-more-2116857257245987236.md` @ `sha256:51d78b4eddd61e5c7e9b3a0c2dfa3b8a76b871116e4c859221cbcf8fd5b37ebe` — Section 7, Preliminary Experiments

> Four end-to-end designs ran at the same time, driven by a stream of group chat and GitHub CI messages. Each run had about 300 messages, of which about 20 were work requests. The rest were casual chat, follow-ups, cancellations, and CI messages. Coding work was simulated by a tool that simply consumes time, so the experiment measures the system's scheduling and coordination, not its ability to execute individual tasks. Each design was run 5 times.
> --- `kb/sources/.snapshots/exploring-super-agent-design-towards-a-more-2116857257245987236.md` @ `sha256:51d78b4eddd61e5c7e9b3a0c2dfa3b8a76b871116e4c859221cbcf8fd5b37ebe` — Section 7.1, workload

> Note: each design was run 5 times. Task completion time is measured from a work request to its result message.
> --- `kb/sources/.snapshots/exploring-super-agent-design-towards-a-more-2116857257245987236.md` @ `sha256:51d78b4eddd61e5c7e9b3a0c2dfa3b8a76b871116e4c859221cbcf8fd5b37ebe` — Section 7.1, measurement

> Super-agent without Pass-through finishes tasks in about the same time as Super-agent, but its Router makes about 30% more decisions per run, and total cache-read tokens rise from 23.2M to 31.8M, about 37% more. So under this workload, pass-through does not make tasks finish faster or better, but it substantially cuts the Router Session's token use and inference overhead.
> --- `kb/sources/.snapshots/exploring-super-agent-design-towards-a-more-2116857257245987236.md` @ `sha256:51d78b4eddd61e5c7e9b3a0c2dfa3b8a76b871116e4c859221cbcf8fd5b37ebe` — Section 7.1, pass-through ablation

> Batching also explains the result in Section 7.1: removing pass-through raised the Router's peak load, yet a single Router still did not reach its throughput limit. So at our current team size, there is no need to shard the Router layer prematurely at the cost of global context continuity.
> --- `kb/sources/.snapshots/exploring-super-agent-design-towards-a-more-2116857257245987236.md` @ `sha256:51d78b4eddd61e5c7e9b3a0c2dfa3b8a76b871116e4c859221cbcf8fd5b37ebe` — Section 7.2, throughput bound

## Connections Found

The source is a concrete comparison for [scheduler–LLM separation](../theory/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md): models judge new tasks while code delivers subscribed follow-ups. In its fixed Router/Worker design, removing pass-through raises cache-read tokens from 23.2M to 31.8M, with similar task completion times. This supports a workload-specific inference-cost benefit, not the note's broader conjecture about total reliability cost.

Chain of Recall provides a design instance to compare with [pointer design tradeoffs in progressive disclosure](../theory/pointer-design-tradeoffs-in-progressive-disclosure.md). Returned objects expose summaries and IDs of related objects, enabling successive retrieval without loading all history. The useful connection is the pointer interface; the article does not test whether those summaries reliably lead to relevant context.

The many-to-many Thread subscription scheme is also a counterexample to equating notifications with [coordination guarantees](../theory/agent-orchestration-needs-coordination-guarantees-not-just.md). It gives overlapping Workers an opportunity to notice conflicting work, but does not specify atomic ownership or shared-write consistency. This distinction matters before reusing the architecture for concurrent KB edits.

## Extractable Value

1. **Separate routing policy from repeated event delivery.** Within the tested Router/Worker architecture, pass-through cuts cache-read usage by about 27% relative to the no-pass-through variant (23.2M versus 31.8M), without a completion-time gain. This is a bounded cost example for the existing scheduler–LLM separation note, not evidence of better task execution or lower end-to-end reliability cost. [quick-win]
2. **Use navigable object references instead of treating history as the next context.** Inline & Spill retains bounded content plus pointers; each retrieval exposes further summaries and IDs. This supplies a concrete event/task/session graph interface for comparison with Commonplace's pointer designs. Its useful contribution is the mechanism, not demonstrated long-term recall accuracy. [just-a-reference]
3. **Distinguish event visibility from edit coordination.** Shared Thread notifications do not settle who owns a write or how conflicting changes are reconciled. The proposal supplies an architectural example for the existing coordination-guarantees distinction, especially where task-isolated agents still mutate the same environment. [quick-win]
4. **Test structural non-execution against prompt-only delegation.** The source's two-level design removes task execution from the Router; its single-session baselines can still choose to execute locally. A stronger experiment would hold task isolation, asynchronous tools, and routing inputs constant while varying whether non-execution is structurally enforced or only prompted. This would help isolate what caused the reported latency difference. [experiment]

## Limitations (our opinion)

The end-to-end experiment uses roughly 300 messages, around 20 work requests, and five runs per design. Coding is a time-consuming mock tool. Reported Super-agent completion times of 12.4 minutes at p50 and 15.7 minutes at p95 therefore describe scheduling in that workload, not correctness, code quality, or real development throughput. The single-session baselines differ in delegation prompts and sometimes do all work locally; the comparison does not isolate context isolation, enforced delegation, and selective event delivery from one another. It does not establish superiority over every alternative concurrent architecture.

The pass-through ablation varies event forwarding within the two-level design. It supports that mechanism's token savings under the tested workload, not the necessity of a global Router. The separate batching experiment uses a real Router model and mock Workers: its decline in amortized inference time from 6.4 to 1.6 seconds per decision as arrival rate rises is not a general capacity or decision-accuracy guarantee. Model configuration, full prompts, raw runs, and the figures' details are not available in the captured text, limiting independent assessment.

The capture is a machine translation and lacks the diagrams and experimental plots referred to in the article. No implementation was inspected or executed for this ingest. Internal daily-use claims supply practitioner context but no systematic failure accounting. Chain of Recall mainly targets recent task/session history; the authors themselves identify months-long memory as an open bottleneck. Pointer reachability alone does not establish retrieval quality.

Finally, an independent Watchdog can still misjudge progress or make harmful repairs; the source does not evaluate its recovery accuracy or specify limits on its authority to change prompts and trigger rules. Cloud-driven access to personal machines concentrates risk: untrusted events can influence an agent connected to private files and credentials. The source explicitly recognizes this problem but does not demonstrate a security boundary that resolves it. Persistence and responsiveness should not be read as evidence of safe autonomous operation.

## Recommended Next Action

Update [Scheduler–LLM separation exploits an error-correction asymmetry](../theory/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) with the pass-through ablation as a synthetic, within-architecture inference-cost example, explicitly distinguishing its token savings from untested reliability-cost gains.
