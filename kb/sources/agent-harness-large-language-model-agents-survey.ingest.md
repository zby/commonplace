---
description: "Survey defining the LLM agent harness as execution loop, tool registry, context manager, state store, lifecycle hooks, and evaluation interface"
source_snapshot: "agent-harness-large-language-model-agents-survey.md"
ingested: "2026-05-28"
type: kb/sources/types/ingest-report.md
source_type: scientific-paper
domains: [harness-engineering, agent-runtime, context-engineering, agent-reliability]
---

# Ingest: Agent Harness for Large Language Model Agents

Source: [agent-harness-large-language-model-agents-survey.md](agent-harness-large-language-model-agents-survey.md)
Captured: 2026-05-28
From: https://www.preprints.org/manuscript/202604.0428

## Classification

Type: scientific-paper -- Preprints.org survey article with formal definitions, historical framing, taxonomy, component matrix, challenge analysis, and stated limitations.
Domains: harness-engineering, agent-runtime, context-engineering, agent-reliability
Author: Qianyu Meng et al. The source has academic form and a broad literature sweep, but the article is a preprint and its taxonomy/completeness ratings should be treated as survey judgment rather than empirical validation.

## Summary

The paper defines an LLM agent harness as a six-component runtime governance layer: execution loop, tool registry, context manager, state store, lifecycle hooks, and evaluation interface. Its central claim is that deployed agent reliability is determined by the model-plus-harness system, not the model alone, because the harness controls tool access, context assembly, state persistence, policy enforcement, observability, and evaluation feedback. The survey traces harness concepts from software testing and reinforcement learning environments into LLM agents, classifies representative systems by stack position and domain scope, and organizes open problems around sandboxing, evaluation, protocols, context management, tool governance, memory, planning, multi-agent coordination, and compute economics. Its strongest contribution for this KB is not the component list by itself, but the way it elevates lifecycle hooks and evaluation interfaces into the formal harness definition.

## Connections Found

The companion connect report found the strongest notes cluster around runtime decomposition, context loading, memory-as-crosscutting concern, enforcement, coordination guarantees, and verification. [Agent runtimes decompose into scheduler context engine and execution substrate](../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md) is the central target: the survey independently confirms a model-surrounding runtime layer, but its `E/T/C/S/L/V` tuple also pressures the KB to decide whether lifecycle hooks and evaluation interfaces are separate runtime components or cross-cutting governance/evaluation layers over the existing scheduler, context engine, and execution substrate split.

The source also supports [always-loaded context mechanisms in agent harnesses](../notes/always-loaded-context-mechanisms-in-agent-harnesses.md), [agent memory is a crosscutting concern, not a separable niche](../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md), [memory design adds operational axes to artifact analysis](../notes/memory-design-adds-operational-axes-to-artifact-analysis.md), [methodology enforcement is constraining](../notes/methodology-enforcement-is-constraining.md), [agent orchestration needs coordination guarantees, not just coordination channels](../notes/agent-orchestration-needs-coordination-guarantees-not-just.md), [the boundary of automation is the boundary of verification](../notes/the-boundary-of-automation-is-the-boundary-of-verification.md), and [session history should not be the default next context](../notes/session-history-should-not-be-the-default-next-context.md).

The main comparison set is the existing harness cluster: [The Anatomy of an Agent Harness](the-anatomy-of-an-agent-harness-2031408954517971368.ingest.md), [What is an Agent Harness](what-is-an-agent-harness-2046980769747533830.ingest.md), [Natural-Language Agent Harnesses](natural-language-agent-harnesses.ingest.md), [Towards a Science of AI Agent Reliability](towards-a-science-of-ai-agent-reliability.ingest.md), [Intelligent AI Delegation](intelligent-ai-delegation-tomasev-franklin-osindero.ingest.md), and [Agent Behavioral Contracts](agent-behavioral-contracts-formal-specification-runtime.ingest.md).

## Extractable Value

1. **Lifecycle hooks and evaluation interfaces may deserve explicit placement in runtime theory** -- The survey's six-tuple adds `L` and `V` to the usual execution/context/tool/state component lists. The KB should decide whether they are separate components or cross-cutting governance/evaluation layers. This is the highest-reach contribution because it can refine the existing runtime decomposition note. [quick-win]

2. **HARNESSCARD-style disclosure is a concrete reproducibility primitive** -- The paper's recommendation that evaluations report harness configuration alongside model and task specifications gives a practical way to prevent model-only benchmark reporting from hiding runtime differences. This complements reliability and verification notes with a specific reporting artifact. [quick-win]

3. **Trajectory evaluation belongs inside the harness, not after the fact** -- The evaluation interface is responsible for trajectories, intermediate state, success signals, and observability. This supports the KB's distinction between output evaluation and agent behavior evaluation, and it gives a location where reliability metrics can be instrumented. [quick-win]

4. **Memory is split across context manager, state store, and write governance** -- The survey's memory section directly corroborates the KB's claim that memory is not one pluggable subsystem. Storage, activation, write policy, poisoning defense, and lifecycle belong to different harness decisions. [just-a-reference]

5. **Tool registries are governance surfaces, not just capability lists** -- Treating the tool registry as schema validation, permissioning, retry behavior, composition control, and audit surface strengthens the "tool surface as system-call table" framing across several harness sources. This is operationally useful for reviewing agent systems. [experiment]

6. **Protocol fragmentation is a runtime-governance problem** -- The survey's discussion of MCP, A2A, ACP, and related standards frames interoperability gaps as disagreements over which runtime layer is being standardized: tools, delegation, intent, authorization, or evaluation. Useful as a rapidly dating reference for protocol analysis. [just-a-reference]

7. **Cross-component coupling is the anti-modular warning for harness design** -- Retention-security coupling, evaluation-governance coupling, and memory-tool boundaries show that harness components cannot be optimized independently. This is a good synthesis target because it connects context engineering, memory policy, tool governance, and evaluation infrastructure. [deep-dive]

## Limitations (our opinion)

- **Survey taxonomy, not empirical validation.** The paper classifies systems and reports a completeness matrix, but it does not run controlled experiments showing that systems with all six components are more reliable than systems without them.
- **Public-documentation bias.** Closed-source and enterprise systems are rated from public documentation, so component completeness may reflect disclosure quality rather than actual implementation.
- **Broad scope creates shallow treatment.** Sandboxing, protocols, memory, planning, evaluation, and multi-agent coordination are each large fields. The survey is useful as an integration map, but local technical decisions still require more focused sources.
- **Potential OpenClaw-style bias.** The source itself notes unusually detailed treatment of OpenClaw because public documentation is available. That may tilt the taxonomy toward systems that look like OpenClaw.
- **Rapidly changing protocol layer.** MCP, A2A, ACP, agent skills, and benchmark harnesses are moving quickly. Protocol-gap claims should be treated as a March/April 2026 snapshot.
- **Harness/model boundary remains porous.** The paper treats harness engineering as distinct from model improvement, but does not deeply analyze which harness functions may be absorbed into model training versus which should remain external enforcement or infrastructure.

## Recommended Next Action

Update [Agent runtimes decompose into scheduler context engine and execution substrate](../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md) with a short section titled **Governance and evaluation cut across the runtime**. It should map the survey's `E/T/C/S/L/V` tuple onto the existing three-part decomposition, then decide whether lifecycle hooks and evaluation interfaces are best modeled as separate components or as cross-cutting layers over scheduler, context engine, and execution substrate. The section should cite this source, [What is an Agent Harness](what-is-an-agent-harness-2046980769747533830.ingest.md), and [Towards a Science of AI Agent Reliability](towards-a-science-of-ai-agent-reliability.ingest.md).
