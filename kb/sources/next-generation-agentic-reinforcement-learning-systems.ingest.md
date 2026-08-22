---
description: "Enterprise self-evolving-agent architecture linking decision-shaped traces to governed selection among memory, skills, harnesses, tools, and weights"
source: https://arxiv.org/abs/2607.01120v1
captured: "2026-08-06"
capture: pdf-read
genre: scientific-paper
snapshot_sha256: 9baec5bfaa2a519421a6de15c963929c398ff278c27f661d485b803046833e7f
ingested: "2026-08-06"
type: kb/sources/types/ingest-report.md
domains: [self-evolving-agents, trajectory-learning, agent-governance, representational-form]
---

# Ingest: Next-Generation Agentic Reinforcement Learning Systems Enable Self-Evolving Agents

## Classification

An arXiv position/design preprint with academic citations, formal event and controller sketches, and a scoped AReaL2.0 prototype, but no experiment evaluating the proposed three-pillar architecture.
Author: Ran Yan and 21 coauthors from Ant Group, HKUST, and Tsinghua University; several authors also built the AReaL system used for the prototype, giving the implementation discussion first-party engineering relevance without independent validation of the broader proposal.

## Summary

The paper argues that enterprise self-evolving agents are blocked less by reinforcement-learning algorithms than by missing systems infrastructure. It proposes three co-designed pillars: an Agent Trajectory Data Protocol (ATDP) that records decision-level observations, relevant state, actions, outcomes, delayed learning signals, and governance metadata; a data proxy that captures and redacts heterogeneous production interactions while preserving replayability; and an evolution control plane that chooses among memory insertion, skill or harness edits, tool-schema changes, policy-weight updates, rollback, and no-op. AReaL2.0 instantiates only the policy-weight branch by exposing rollout and training workers behind an agent-service gateway, router, proxy, and compute-worker layer. The full multi-surface controller, complete protocol, and governed replay loop remain a research agenda.

## Connections Found

This source is an architecture-level bridge between [decision-shaped capture](../notes/structure-inference-needs-capture-at-the-decision-surface.md) and [representational-form coevolution](../notes/treat-continual-learning-as-representational-form-coevolution.md): ATDP supplies a concrete event-schema witness for the former, while the proposed control plane makes the latter's cross-form intervention-selection problem explicit. Its role is a design agenda rather than empirical support. The fixed event tuple and intervention menu must be read through [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md). Relative to current systems, [the trace-learning survey](../agent-memory-systems/trace-learning-techniques-in-related-systems.md) shows concrete but fragmented promotion paths, [Autogenesis](../agentic-systems/autogenesis.md) implements versioned multi-resource mutation and rollback without a strong semantic gate, and [Co-Harness](co-harness-co-evolving-harness-and-model-weights.ingest.md) supplies an empirical alternating harness-and-weight loop without the enterprise data/control substrate proposed here.

## Extractable Value

1. **Multi-surface learning needs an evidence substrate and an intervention selector, not only an optimizer** -- The paper separates capturing learning-ready experience from deciding whether a failure belongs to memory, skills, harnesses, tools, or weights. This makes the systems dependency behind cross-form credit assignment explicit. [quick-win]

2. **ATDP is a concrete witness for decision-shaped trace capture** -- Its event tuple records observation, relevant internal or harness state, action, action outcome, reward or critique, and execution metadata, while allowing late signals to augment an immutable causal record. This operationalizes the existing capture-at-the-decision-surface claim without establishing ATDP as the uniquely right schema. [experiment]

3. **Replayability and governance are learning-data properties, not downstream cleanup** -- Exact model, prompt, tool, retrieval, guardrail, tenant, consent, retention, and training-eligibility metadata determine whether a trace can be replayed, compared, or legally used. The paper's deterministic/approximate/non-replayable distinction is a useful refinement over treating all retained traces as equivalent evidence. [quick-win]

4. **Intervention selection is the missing oracle in representational-form coevolution** -- The proposed controller consumes trajectory windows, evaluator scores, correction rates, failure clusters, cost, safety, and drift signals, then selects an update surface or no-op. Naming the action set clarifies the problem, but the paper does not supply or validate the policy that maps those signals to the right intervention. [deep-dive]

5. **AReaL2.0 demonstrates service integration for one branch, not the whole architecture** -- Gateway, session-affinity router, data proxy, and agent-compute workers show how deployed traffic can feed online policy training without rewriting the surrounding agent. This is a useful implementation pattern, but it is only the weight-update branch and carries no reported outcome here. [just-a-reference]

6. **The fixed decomposition is itself a design hypothesis** -- Behavior can condition on typed event histories and trajectory statistics; the controller can compose only the declared memory, skill, harness, tool, weight, rollback, and no-op operations; its hypothesis class maps those inputs to that menu. The event representation, artifact partitions, action taxonomy, replay categories, governance rules, and improvement objective remain fixed outside the effective update space. [deep-dive]

## Limitations (our opinion)

The paper does not empirically validate its central architecture. It reports no benchmark, ablation, deployment study, baseline comparison, throughput result, or behavioral outcome for ATDP, the comprehensive data proxy, or multi-surface control plane. AReaL2.0 is described as a prototype integration, but the paper gives no evidence that it improves a deployed agent, selects updates correctly, preserves safety, or operates at enterprise scale. Treat the three pillars as a design proposal and implementation agenda, not as an established requirement set.

The fixed-decomposition boundary is consequential. The available signals are the ATDP tuple plus trajectory-window statistics such as evaluator scores, user corrections, tool failures, cost, safety, and drift. The available responses are memory, skill, harness, tool-schema, or policy updates, rollback, and no-op. The proposed controller maps the former to the latter, but neither an objective nor a validated attribution method establishes when that mapping is correct. A missing distinction in the event schema, an intervention outside the menu, or a failure that crosses the paper's artifact partitions remains unreachable. Improvement in the implemented policy-weight branch would not validate the adjacent fixed choices or the decomposition as a whole.

The three-pillar partition is also easier to vary than the underlying systems need. A simpler account is that multi-surface adaptation requires decision-shaped instrumentation plus governed selection, evaluation, deployment, and rollback. Those functions might be divided among fewer or more services than ATDP, proxy, and control plane. The paper does not compare rival decompositions. Its treatment of relevant hidden state is under-specified as well: bounded reasoning summaries may help credit assignment, but they can be unavailable, unfaithful, privacy-sensitive, or provider-specific.

Finally, the enterprise requirements are plausible but untested. Cross-tenant aggregation, redaction, consent, access control, counterfactual replay, side-effect management, and model/tool version retention carry substantial technical and legal costs. The design names these obligations but does not show that its proxy can satisfy them or that the resulting data remain useful enough for online learning.

## Recommended Next Action

Write a note titled **"Multi-surface learning needs a typed, replayable evidence substrate"** connecting [decision-surface capture](../notes/structure-inference-needs-capture-at-the-decision-surface.md), [representational-form coevolution](../notes/treat-continual-learning-as-representational-form-coevolution.md), and [runtime governance control surfaces](../notes/runtime-structure-determines-governance-control-surfaces.md). Use ATDP and its proxy as one concrete witness, while stating that the event schema and intervention taxonomy remain revisable rather than promoting them as a standard.
