---
description: "Solution-injection paper showing agents observe explicit task solutions in context but often fail to integrate them into action."
source_snapshot: "agents-explore-but-agents-ignore-llms-lack-environmental-curiosity.md"
ingested: "2026-04-22"
type: kb/sources/types/ingest-report.md
domains: [agent-reliability, evaluation, tool-loop, context-engineering]
---

# Ingest: Agents Explore but Agents Ignore

Source: agents-explore-but-agents-ignore-llms-lack-environmental-curiosity.md
Captured: 2026-04-22
From: https://arxiv.org/html/2604.17609v1

## Classification

Type: scientific-paper -- arXiv preprint with benchmark modifications, quantitative experiments across Terminal-Bench, SWE-Bench, and AppWorld, scaffold/tool/prompt/training ablations, and appendices testing alternative explanations.
Domains: agent-reliability, evaluation, tool-loop, context-engineering
Author: Leon Englaender, Sophia Althammer, Ahmet Ustun, and Tom Sherborne are at Cohere; Matthias Galle is at Poolside. This is a credible agent-evaluation source, with the usual caveat that it is a vendor-adjacent preprint.

## Summary

The paper argues that current LLM agents often discover relevant environmental information without integrating it as a reason to change their plan. The authors introduce "solution injection": placing a complete task solution directly in the agent environment, then separately measuring whether the agent discovers it and whether it interacts with it. Across Terminal-Bench, SWE-Bench, and AppWorld, agents frequently see the injected solution but often ignore it; AppWorld is the starkest case, with discovery above 90% and interaction below 7%. The paper attributes this to a lack of "environmental curiosity": agents use the environment to fetch expected information, but do not reliably reflect on unexpected observations. Tool availability, reasoning budget, prompting, and training distribution all modulate the gap, but none eliminate it.

## Connections Found

The connect pass places this source in the context-integration and evaluation cluster, not primarily in the model-internal knowledge activation cluster. It connects as evidence for [process-structure-and-output-structure-are-independent-levers](../notes/process-structure-and-output-structure-are-independent-levers.md), because exploration and reflection prompts change behavior by constraining reasoning process rather than answer format, and for [prompt-ablation-converts-human-insight-to-deployable-framing](../notes/prompt-ablation-converts-human-insight-to-deployable-framing.md), because the paper tests which prompt framings trigger the desired cognitive move. The tool-suite ablations support [agent-is-a-tool-loop](../notes/agent-is-a-tool-loop.md): changing the capability surface changes the agent's behavior, not just its convenience. The closest existing note with a related mechanism is [knowledge-storage-does-not-imply-contextual-activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md), but this source is distinct: the relevant information is already in the live context, and the failure is connecting that observation to the task and plan. Source comparisons were [Coding Agents are Effective Long-Context Processors](./coding-agents-are-effective-long-context-processors.ingest.md), which also studies tool exposure changing exploration, and [Towards a Science of AI Agent Reliability](./towards-a-science-of-ai-agent-reliability.ingest.md), which similarly argues that aggregate task success is too coarse.

## Extractable Value

1. **Context presence does not imply contextual integration.** The high-reach contribution is sharper than "models forget": even when a complete solution is in the agent's live context, the observation often is not connected to the task, plan, or next action. This is sibling to the activation-gap note, not a direct extension of it. [quick-win]
2. **Solution injection separates discovery from interaction.** The `discovery@k` / `interaction@k` split is a reusable evaluation pattern for distinguishing "the agent found the information" from "the agent treated it as action-relevant." This is more diagnostic than pass rate alone. [experiment]
3. **Tool additions are behavioral priors, not neutral affordances.** Adding `str_replace_editor` improves SWE-Bench pass rate while reducing interaction conditional on discovery, suggesting richer tools can narrow the agent's search behavior even when they improve outcomes. This is the strongest new tension relative to the Coding Agents source. [deep-dive]
4. **Process prompts can partially elicit observation-grounded behavior.** Exploration instructions and "investigate discovered files" prompts improve both interaction and original-benchmark pass rate, supporting the process-structure note with a concrete agent benchmark. [quick-win]
5. **Narrow in-distribution training can compress solution diversity.** AppWorld-SFT improves AppWorld pass@1 but worsens pass@10 and interaction scaling relative to broader Terminal-Bench-like training, suggesting local fit can reduce exploratory diversity. This is relevant to any deploy-time learning loop that over-optimizes for a narrow task distribution. [deep-dive]
6. **The deficit is not just suspicion or inability.** LLM-as-judge analysis finds zero deliberate "trap" rejections, and oracle interventions show agents can use solutions when directly cued. The simpler account is missing integration trigger, not missing competence. [just-a-reference]

## Limitations (our opinion)

Solution injection is deliberately artificial. That is a strength for establishing a floor -- if agents ignore an obvious solution, subtler signals are unlikely to fare better -- but it should not be treated as a full measure of real-world curiosity. Real environments contain ambiguous, partial, stale, and adversarial information; this benchmark mostly tests whether agents notice an explicit shortcut.

`interaction@k` is a useful process metric, but it is not identical to curiosity. It detects calls or reads involving the injected solution. An agent could be adaptively curious without touching the solution, or could touch the solution opportunistically without developing a general habit of reflecting on surprising observations.

The training-causality story is plausible but underdetermined. The paper's claim that expert on-policy trajectories teach agents to seek only expected information fits the results, but the SFT interventions are limited and negative. The data supports "this is not fixed by these simple SFT recipes," not a settled theory of where environmental curiosity is gained or lost.

The tool-surface result is important but should not be over-generalized. `str_replace_editor` may suppress file investigation in these scaffolds and tasks, but other tools or tool descriptions could behave differently. The broader claim should be stated as "tools act as behavioral priors that need evaluation," not "fewer tools are always better."

The LLM-as-judge appendix helps rule out deliberate rejection, but it is still judge-mediated trace classification. Manual verification of 50 examples supports the labels, yet the conclusion should remain tied to the visible trace: in non-interaction cases, the solution usually is not acknowledged or is acknowledged without action.

## Recommended Next Action

Write a note titled `Context presence does not imply contextual integration` connecting to [process-structure-and-output-structure-are-independent-levers](../notes/process-structure-and-output-structure-are-independent-levers.md), [agent context is constrained by soft degradation](../notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md), [agent-is-a-tool-loop](../notes/agent-is-a-tool-loop.md), and [knowledge-storage-does-not-imply-contextual-activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md) as a sibling distinction. It would argue that context engineering must solve not only loading relevant tokens, but making the agent connect those tokens to the active task and plan.
