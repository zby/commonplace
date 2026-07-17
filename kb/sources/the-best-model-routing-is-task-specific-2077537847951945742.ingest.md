---
description: "Jerry Liu on task-specific model routing: generic gateways handle provider routing, but workflow-specific routers earn cost and accuracy gains from private evals and input taxonomies"
source_snapshot: "the-best-model-routing-is-task-specific-2077537847951945742.md"
ingested: "2026-07-17"
type: kb/sources/types/ingest-report.md
domains: [context-engineering, model-routing, vertical-agents, evaluation]
---

# Ingest: The Best Model Routing is Task Specific

Source: [the-best-model-routing-is-task-specific-2077537847951945742.md](./the-best-model-routing-is-task-specific-2077537847951945742.md)
Captured: 2026-07-17T11:22:55.473932+00:00
From: https://x.com/jerryjliu0/status/2077537847951945742

## Classification

Genre: practitioner-report -- the source is a builder/operator argument from the LlamaIndex/LlamaParse founder about current routing products, vertical AI systems, and LlamaParse's document-routing architecture. It is grounded in product examples and reported benchmark/cost numbers rather than a controlled study.
Domains: context-engineering, model-routing, vertical-agents, evaluation
Author: @jerryjliu0, Jerry Liu of LlamaIndex/LlamaParse. High signal on document parsing and LlamaParse architecture; vendor-positioned on the claim that documents are a routing moat for LlamaParse.

## Summary

The source argues that generic model gateways and task-specific routers solve different problems. Generic gateways such as OpenRouter Fusion handle provider-level availability, price, and broad ensembling for hard open-ended questions. Task-specific routing asks a narrower question: for this input, task, quality bar, and cost/latency budget, what is the cheapest path that still clears the bar? Liu gives coding-agent, legal, support, and document-parsing examples, then uses LlamaParse as the worked case: route each page between cheap direct extraction, specialized parsers/VLMs, and frontier models using a document-complexity model and agentic judge. The durable claim is that routing alpha comes from a workflow-specific input taxonomy plus private evals, not from a generic provider router.

## Connections Found

The source lands as a routing and evaluation anchor for the KB's context-engineering cluster. It supports [context efficiency](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) on the aggregate-cost face: expensive frontier calls are a scarce resource to allocate, not a default for every token. It also supports the [bounded-context orchestration model](../notes/bounded-context-orchestration-model.md) and [agent runtime decomposition](../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md), because the router is a scheduler/context-engine policy over bounded calls. The strongest evaluation connection is [the boundary of automation is the boundary of verification](../notes/the-boundary-of-automation-is-the-boundary-of-verification.md): the source explicitly frames the difficulty model and eval as private ground truth, and the LlamaParse architecture includes an agentic judge. As a sibling source, [Building a Good Vertical Agent](./building-a-good-vertical-agent-2065190286519906657.ingest.md) is the closest comparison: it treats context placement as expected-cost allocation over a task distribution, while this source applies the same shape to model selection.

## Extractable Value

1. **Task-specific routing is a context-engineering selection policy, not just provider fallback.** Generic gateways route across providers and ensembles; workflow routers choose the bounded call, model, and extraction path for one task distribution. This sharpens where model routing belongs in the scheduler/context-engine decomposition. [quick-win]

2. **Private difficulty models and evals are the scarce asset.** The source's strongest line is that "which model clears the bar" depends on a workflow's private input taxonomy and grading surface. That directly operationalizes the KB's verification-boundary claim: routing value appears only where the system can cheaply discriminate enough cases. [quick-win]

3. **Cost-quality curves create a routing opportunity only after the quality bar is known.** The reported Factory, Cognition, Decagon, Harvey, and LlamaParse examples all depend on knowing which work can leave the frontier model without unacceptable quality loss. This is a concrete economic version of context efficiency's aggregate-cost face. [experiment]

4. **Page-level document routing is a reusable worked example.** The same document can contain pages that need different engines: cheap direct extraction for plain text, specialized table/chart VLMs, or frontier models for harder cases. That is a clear instance of selecting representations and model calls by subtask, not by document-level average difficulty. [experiment]

5. **The two-layer architecture is useful vocabulary.** Provider gateways own uptime, price, broad routing, and general ensembling; workflow routers own task-specific input models, quality bars, and verification. This distinction can prevent overloading "model routing" in KB notes and reviews. [just-a-reference]

6. **Specialized open/fine-tuned models are routeable components, not frontier replacements.** The source frames better frontier and open-weight models as new options for the harness to route to. That is a useful anti-monolith framing for harness design: model progress increases the option set rather than erasing orchestration. [just-a-reference]

7. **Agentic judging is part of the routing loop but needs oracle scrutiny.** LlamaParse's reported agentic judge is an existence example of verifier-backed routing, but it also raises the KB's usual question: does the judge actually discriminate errors cheaply enough, or merely add another model call? [deep-dive]

## Limitations (our opinion)

This is a persuasive practitioner report and product-positioning thread, not independent evidence. The author is credible on LlamaParse internals but has a direct interest in arguing that document parsing remains a specialized-system problem rather than a frontier-model feature. The ParseBench numbers, LlamaParse cost/accuracy claims, and competitor examples are not audited in the snapshot; some are second-hand product claims from other companies.

The examples may also be easier than the general claim. Documents, support workflows, and some legal/coding subtasks have repeated input types and measurable outcomes, so they can support private difficulty models and evals. Domains without stable input taxonomies or cheap per-instance verification may not get the same routing returns. The "agentic judge" detail is especially under-specified: without evidence about judge accuracy, calibration, and failure modes, it should be treated as a proposed verifier, not proof that verification is solved.

Finally, "private ground truth" is both an engineering claim and a moat claim. The simpler account is that routing improves wherever volume creates enough labeled cases to tune a classifier and enough cost pressure to justify it. That is still valuable, but narrower than a general law that every vertical workflow has durable routing alpha.

## Recommended Next Action

Write a note titled `Task-specific routers need task-specific oracles`, connecting this source to [the boundary of automation is the boundary of verification](../notes/the-boundary-of-automation-is-the-boundary-of-verification.md), [context efficiency is the central design concern in agent systems](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md), and [Building a Good Vertical Agent](./building-a-good-vertical-agent-2065190286519906657.ingest.md). The note should argue that model routing becomes valuable when a workflow has a private difficulty model, input taxonomy, and verifier that define "cheap enough and good enough" per subtask, not at the generic provider gateway.
