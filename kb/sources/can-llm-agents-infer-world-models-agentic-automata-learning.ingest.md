---
description: "Agentic automata-learning paper showing that hard-oracle interaction tasks can separate LLM-agent evidence collection, hypothesis construction, and final world-model success."
source_snapshot: "can-llm-agents-infer-world-models-agentic-automata-learning.md"
ingested: "2026-06-22"
type: kb/sources/types/ingest-report.md
source_type: scientific-paper
domains: [agent-evaluation, oracle-theory, contextual-activation, agent-benchmarks]
---

# Ingest: Can LLM Agents Infer World Models?

Source: can-llm-agents-infer-world-models-agentic-automata-learning.md
Captured: 2026-06-22
From: https://arxiv.org/pdf/2606.16576

## Classification

Type: scientific-paper -- arXiv preprint with a formal task definition, procedural dataset generation, classical automata-learning baselines, multi-model experiments, error analysis, and stated limitations.
Domains: agent-evaluation, oracle-theory, contextual-activation, agent-benchmarks
Author: Reef Menaged, Gili Lior, Shauli Ravfogel, Roee Aharoni, and Gabriel Stanovsky; affiliations include Hebrew University of Jerusalem, New York University, and Google Research. The author signal is credible for an agent-evaluation paper, with the normal caution that this is a preprint under review.

## Summary

The paper introduces **agentic automata learning**, a controlled benchmark for whether tool-calling LLM agents can infer a hidden deterministic finite automaton through interaction. Agents can ask membership queries about strings and equivalence queries about hypothesized DFAs; the oracle either accepts the hypothesis or returns a counterexample. This gives the benchmark exact success checks, controllable complexity through DFA state count, and direct comparison with classical active automata-learning algorithms such as L* and TTT. The experiments find that current LLM agents can solve small cases but degrade sharply as DFA size increases: no tested model exceeds 25% success on 8-9 state automata, while classical algorithms solve all instances. Error analysis separates planning failures from reasoning failures and shows growing rates of non-informative queries as interactions lengthen, suggesting failures in query planning, evidence integration, and use of accumulated observations.

## Connections Found

The connect report places this source in the evaluation, oracle-theory, and contextual-activation cluster. It connects most strongly to [knowledge storage does not imply contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md), because the paper shows agents receiving the full interaction history yet failing to ask informative queries or build hypotheses consistent with accumulated evidence. It also supports [oracle strength spectrum](../notes/oracle-strength-spectrum.md): membership/equivalence queries and exact DFA comparison make a compact hard-oracle benchmark where success and interaction cost are cheaply measurable. The paper is a useful cautionary companion to [the boundary of automation is the boundary of verification](../notes/the-boundary-of-automation-is-the-boundary-of-verification.md): exact verification makes failures visible, but does not itself give the LLM agent a robust search policy. Source comparisons include [Agents Explore but Agents Ignore](./agents-explore-but-agents-ignore-llms-lack-environmental.ingest.md), [Towards a Science of AI Agent Reliability](./towards-a-science-of-ai-agent-reliability.ingest.md), [Large Language Model Agents Are Not Always Faithful Self-Evolvers](./large-language-model-agents-are-not-always-faithful-self-evolvers.ingest.md), and [Agentic Code Reasoning](./agentic-code-reasoning.ingest.md).

## Extractable Value

1. **Process-visible agent benchmarks can separate failure stages** -- Agentic automata learning distinguishes evidence collection, hypothesis construction, equivalence success, query cost, and non-informative query rate. This is new relative to aggregate reliability evaluations because it makes the discovery process inspectable, not only the outcome. [deep-dive]
2. **Hard oracles diagnose query-policy failure without solving it** -- The benchmark has exact feedback and classical algorithms that solve every instance, yet LLM agents still fail. This sharpens the oracle-theory cluster: strong verification can expose planning and evidence-integration failures, but it does not provide the policy for choosing informative actions. [quick-win]
3. **Accumulated visible evidence still fails to activate** -- The full interaction history is present in context, but agents repeat queries, propose contradicted hypotheses, or fail to infer a DFA that passive learners can recover from the same observations. This is a stronger sibling to solution-injection evidence because the problem is not a visible shortcut; it is using ordinary accumulated evidence. [quick-win]
4. **Planning and reasoning failures should be separated in agent evaluation** -- The passive-learner analysis gives a reusable classification: if a passive learner can infer the DFA from the agent's observations, the failure is reasoning; otherwise, the failure is planning/query collection. This pattern could transfer to other domains where an external solver can evaluate whether gathered evidence was sufficient. [experiment]
5. **Non-informative query rate is an action-level activation metric** -- Repeated membership queries and equivalence hypotheses contradicted by known evidence operationalize "not using what is already known" at the tool-call level. This metric is more behaviorally grounded than asking whether the agent can summarize the history. [experiment]
6. **Classical baselines are not only performance baselines but process baselines** -- L* and TTT provide not just 100% success, but expected query structure, monotonic hypothesis behavior, and bounds on equivalence queries. The paper uses deviations from those structures to argue models are not merely replaying known algorithms. [just-a-reference]

## Limitations (our opinion)

This is a synthetic, deterministic formal-language environment. That is exactly why it is diagnostically useful, but it should not be over-generalized to messy world modeling. Real environments are partially observable, stochastic, non-stationary, and often lack exact equivalence feedback. The honest transfer is from "LLM agents fail even in a clean interaction-learning task" to evaluation design and failure taxonomy, not from DFA inference to all real-world planning.

The benchmark's strong oracle is also a boundary condition. Membership and equivalence queries are far clearer than most agent-tool feedback, and classical algorithms already solve the formal problem. If agents struggle here, the result is sobering; but improvements on this benchmark might still fail to transfer where the oracle is weaker or where the state space is not automata-like.

The model set and naming are point-in-time. The paper reports 2026-era systems and omits a GPT reasoning variant from the main evaluation for cost reasons. Future model families could shift success rates, though the benchmark structure and failure categories would remain useful.

The error taxonomy depends on passive automata learners as the sufficiency test for gathered observations. That is elegant for DFAs, but other domains may not have a comparable external solver that can decide whether an agent's collected evidence was enough.

## Recommended Next Action

Write a note titled `Process-visible agent benchmarks should separate evidence collection from evidence use`, connecting this source to [knowledge-storage-does-not-imply-contextual-activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md), [oracle-strength-spectrum](../notes/oracle-strength-spectrum.md), [Towards a Science of AI Agent Reliability](./towards-a-science-of-ai-agent-reliability.ingest.md), and [Agents Explore but Agents Ignore](./agents-explore-but-agents-ignore-llms-lack-environmental.ingest.md). The note should argue that agent evaluations need process metrics that localize whether failure happened at discovery, evidence integration, hypothesis construction, or final verification.
