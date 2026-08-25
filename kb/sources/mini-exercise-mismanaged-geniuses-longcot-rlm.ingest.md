---
description: "LongCoT-mini RLM case study where trace-extracted prompt tips, guardrails, and sub-answer checking improved graph-structured compositional reasoning"
source: https://alexzhang13.github.io/blog/2026/longcot-rlm/
captured: "2026-06-25"
capture: web-fetch
genre: practitioner-report
snapshot_sha256: 2f827452949bb409adf674dbb920ca5658f9417048e045a2ebb7b26e8e7d1615
ingested: "2026-06-25"
type: kb/sources/types/ingest-report.md
domains: [orchestration, rlm, decomposition-policy, trajectory-analysis]
---

# Ingest: A Mini Exercise on the Mismanaged Geniuses Hypothesis (RLMs on LongCoT)

## Classification

Alex Zhang and Omar Khattab report a hands-on mini experiment on LongCoT-mini RLM runs, including failure-trace inspection, prompt/tip revision, and before/after benchmark numbers. It is not a full scientific paper because the snapshot lacks full methodology, full benchmark results, and controlled ablations.
Author: Alex Zhang and Omar Khattab. Khattab is already visible in this KB's DSPy and harness-learning sources; author credibility comes from direct involvement in RLM and benchmark work, but the post is still an informal case study.

## Summary

The source argues that poor RLM performance on LongCoT-mini should not be read as evidence that RLMs cannot handle graph-structured compositional reasoning. Zhang reports that both Raymond Weitekamp's DSPy.RLM + Claude Sonnet 4.5 run and his own GPT-5.2 RLM run improved over base-model scores overall but badly underperformed on `MATH` and `CS`. Manual trace inspection suggested mundane harness-policy failures: brute-force attempts crashed the REPL, and sub-agent answers were not reliably checked. After asking Claude Code to inspect trajectories and write RLM tips, the reported LongCoT-mini score rose to 65.6%, with partial rewards above 70%. The takeaway is that RLM capability depends on the decomposition policy and process guidance that steer the recursive harness, and that trace-extracted prompt tips can be a short-term bridge before training such behavior into the model.

## Quotes

- **Source extract (verbatim):** I decided to compare against GPT-5.2, as it was the strongest performing model reported on the benchmark. And it turned out, similar to Raymond's results, despite stronger overall performance relative to GPT-5.2 (38.7% --> 50.6%), RLM(GPT-5.2) struggled on the `MATH` and `CS` splits!
  - **Source location:** Section “General method cannot do XYZ is a VERY strong statement,” paragraph before the results table
- **Source extract (verbatim):** Now against [@Xeophon's best wishes](https://x.com/Xeophon/status/2046883459571761451), I started manually examining RLM traces. It turned out in the majority of cases that the RLM was timing out, as it would attempt to solve a `MATH` or `CS` node using a pure brute-force approach, crashing the REPL and failing the trajectory (oops, perfectly guardrail-able with a better RLM implementation).
  - **Source location:** Same section, trace-inspection paragraph
- **Source extract (verbatim):** Furthermore, the model would sometimes realize it could decompose the graph into sub-problems and launch sub-agents over these sub-problems, but would rarely check whether the sub-agent actually got the sub-problem correct. These all seemed like silly decision-making issues on the part of the LM, which seemingly had more to do with how we chose to prompt the RLM, rather than its inability to solve the task.
  - **Source location:** Same section, paragraph immediately after the timeout account
- **Source extract (verbatim):** So overnight, I asked Claude Code to look at the trajectories, write tips for the RLM to not make mistakes, and restart the run on LongCoT-mini. When I woke up in the morning, the updated results were as follows:
  - **Source location:** Same section, paragraph introducing the updated run
- **Source extract (verbatim):** Not only did it greatly increase performance across the board, the overall performance jumped from 38.7% --> 65.6%. I also tracked partial rewards (i.e. many tasks ask for multiple answers which all need to be correct, and the model sometimes gets one wrong) which jumped the performance to well above 70%! I'm pretty confident we could further push these scores, but I think the point I'm trying to make is well illustrated from this jump alone.
  - **Source location:** Same section, updated-results paragraph

## Connections Found

Connection discovery found a tight RLM and orchestration cluster. The source is direct evidence for [RLM has the model write ephemeral orchestrators over sub-agents](../notes/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md): the REPL/sub-agent substrate works better when the model-written orchestration is steered away from brute force and toward checked graph decomposition. It also supports [Decomposition heuristics for bounded-context scheduling](../notes/decomposition-heuristics-for-bounded-context-scheduling.md) and [Topology, isolation, and verification form a causal chain for reliable agent scaling](../notes/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md), because the reported failures were not only split failures but verification failures over sub-agent outputs. The source adds a concrete example to [Agent orchestration occupies a multi-dimensional design space](../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md): a natural-language prompt/tip artifact can carry decomposition policy before that policy is codified or trained. It also fits [Diagnostic richness constrains outer-loop learning quality](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) and [System-definition artifacts are crystallized reasoning under context scarcity](../notes/system-definition-artifacts-are-crystallized-reasoning-under-context.md), since the improvement path was trace inspection -> distilled tips -> behavior-shaping prompt.

The closest source neighbors are the earlier [Mismanaged Geniuses Hypothesis](the-mismanaged-geniuses-hypothesis-2042588627260018751.ingest.md), which gives the broader thesis; [The Y-Combinator for LLMs](the-y-combinator-for-llms-solving-long-context-rot.ingest.md), which takes the alternative route of restricting RLM control flow through typed combinators; [Trajectory-Informed Memory Generation](trajectory-informed-memory-generation-self-improving-agents.ingest.md), which systematizes trajectory-to-tip learning; and [Meta-Harness](meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md), which gives controlled evidence that richer traces improve harness search.

## Extractable Value

1. **RLM performance is governed by decomposition-policy acquisition, not only scheduler substrate** -- The article strengthens the design-space note's decomposition-policy dimension: free-form RLM, typed RLM, prompt-steered RLM, and trained RLM differ in how the policy for choosing decompositions is acquired. [quick-win]

2. **Trace-extracted prompt tips are a practical intermediate substrate** -- The reported loop is lightweight deploy-time learning without durable governance: inspect trajectories, distill process guidance, inject it into the next RLM run. It is weaker than tested artifact promotion but stronger than ad hoc prompting, and it bridges MGH's "steer while generating trajectories, then remove priors" strategy. [experiment]

3. **Graph-structured decomposition needs answer checking, not just sub-agent launch** -- The failures were cases where the model launched or attempted sub-solves but did not verify the returned sub-answer or chose brute-force search. This is a concrete warning for any scheduler that treats sub-agent decomposition as sufficient. [quick-win]

4. **Prompt guidance can act as process structure** -- The useful tips appear to constrain reasoning moves (avoid brute force, respect graph structure, check sub-results) rather than the final answer format. This is a clean example for the process-vs-output structure distinction. [just-a-reference]

5. **"Context decomposition is different from task decomposition" needs a narrower interpretation** -- LongCoT's appendix claim may be right for naive RLM implementations, but this source suggests graph dependency tracking is not an inherent RLM weakness; it is at least partly a harness-policy and verification problem. [quick-win]

6. **The numerical gain is useful but should stay evidence, not doctrine** -- The reported 50.6% to 65.6% improvement is a strong retrieval hook and a useful benchmark data point, but the source does not yet provide enough protocol detail to ground a high-confidence methodological rule. [just-a-reference]

## Limitations (our opinion)

This is an informal blog experiment, not a controlled paper. The snapshot does not include full prompts, full trajectories, statistical uncertainty, cost accounting, or independent replication. The author says full benchmark results are reserved for larger releases, so the reported LongCoT-mini result should be treated as directional evidence.

The intervention bundles multiple changes: trace inspection, prompt tips, guardrails against brute force, graph-structure instructions, and answer-checking reminders. Without ablations, we cannot tell which part caused the gain. The post also compares a prompt-tipped RLM against a pure-LM prompt variant, but that does not isolate the value of each prompt component.

The benchmark is decomposition-friendly by design. A graph of subproblems is exactly where RLM-like systems should have a natural advantage once the decomposition policy is sane. The result should not be generalized to soft synthesis tasks, open-ended research taste, or domains where sub-answer correctness cannot be cheaply checked.

The simpler account is harness engineering, not latent model genius. The result may show that frontier models can follow better process guidance when it is supplied; it does not prove they would reliably discover that guidance from minimal prompting, nor that training can remove the guidance without losing the behavior.

## Recommended Next Action

Update [Agent orchestration occupies a multi-dimensional design space](../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md): under "Decomposition-policy artifact," add trace-extracted prompt tips as a natural-language policy-acquisition point between hand-authored heuristics and trained distributed-parametric policy, citing this source alongside MGH and λ-RLM.
