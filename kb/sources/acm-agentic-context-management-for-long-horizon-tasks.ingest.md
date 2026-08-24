---
description: "ACM improves three benchmarks inside a fixed two-tool decomposition, but neither tests that decomposition's scope nor shows lossless active context"
source: https://arxiv.org/abs/2607.23809
captured: "2026-07-30"
capture: web-fetch
genre: scientific-paper
snapshot_sha256: 56d2f596d4bbb9ce785b0de456982a2dfff80af7a50d4f1f4ef16778d79d5de2
ingested: "2026-07-30"
type: kb/sources/types/ingest-report.md
domains: [context-engineering, agent-memory, post-training, long-horizon-agents]
---

# Ingest: ACM: Agentic Context Management for Long Horizon Tasks

## Classification

An arXiv preprint with a formal method, public training pipeline, three-benchmark evaluation, ablations, case studies, prompts, and references.
Author: Xiaochuan Li, Ryan Ming, Meng Chu, Shuai Shao, Rong Jin, and Chenyan Xiong, affiliated with Carnegie Mellon University and Meta. The paper states that CMU conducted the experiments and data work while Meta advised; public code, data, and checkpoints improve inspectability, but this ingest does not inspect the implementation and the paper is not peer-reviewed.

## Summary

ACM turns context management into two agent actions: `manage_context` summarizes earlier turns while saving the raw messages under an identifier, and `query_memory` lets the agent retrieve from those messages later. The agent chooses when to invoke them rather than waiting for a fixed context threshold. A teacher-guided post-training pipeline supplies both positive examples (replace looping or redundant search with compression) and negative examples (replace premature compression with deeper search or an answer), then uses on-policy distillation and filtering to train Qwen3.5-9B. Against ReAct, adding the ACM framework raises pass@1 from 0.570 to 0.635 on BrowseComp-Plus, 0.367 to 0.405 on DeepSearchQA, and 0.489 to 0.508 on SWE-Bench Verified; post-training raises them further to 0.727, 0.425, and 0.530. Peak active context generally falls and exploration grows, but tool calls often rise, and a 4B model that terminates after roughly two turns never reaches the regime where the memory tools can help.

## Claims

- **Claim (paraphrase):** ACM supplies two context-management tools—`manage_context` summarizes all messages up to the previous summary boundary while archiving their raw text under an identifier, and `query_memory` retrieves from the identified archive—and its post-training objective teaches when to invoke or refrain from those tools.
  - **Source extract (verbatim):** We introduce only two context management tools to enable the agent to mimic the human memory mechanism: manage_context, which compresses previous turns into a concise summary and offloads the raw messages to an external file on disk; and query_memory, which allows the agent to query the stored raw messages to retrieve information precisely.
  - **Source location:** Section 3.2, “ACM Agent”
  - **Source extract (verbatim):** When the agent decides to manage its context, it invokes manage_context (action a_{2},a_{6} in Figure 1) to compress all messages up to the previous summary boundary using a summarizer LLM. Crucially, the original messages are not discarded but saved to the agent’s external workspace. Each summary is assigned a unique identifier that maps the summary to the corresponding raw messages in external memory.
  - **Source location:** Section 3.2, mechanism description
  - **Source extract (verbatim):** Under this objective, the student jointly learns when to invoke context management and when to refrain from doing so because a search, retrieval, or commit-to-answer action is more appropriate.
  - **Source location:** Section 4.1, on-policy distillation objective
  - **Source extract (verbatim):** We compare ACM against three agent frameworks: (1) ReAct (Yao et al., 2022), the standard reasoning-and-acting agent without any context management; (2) Summary Agent (Wu et al., 2025; Kang et al., 2025), which triggers summarization when context usage exceeds a fixed threshold; and (3)  Memory Agent (Zhang et al., 2026), which accumulates experiences from previous rollouts but does not dynamically manage its intra-trajectory context.
  - **Source location:** Section 5.1, “Baselines”
  - **Scope:** ACM's Qwen3.5-9B context-management action space, teacher–student post-training objective, and system-level baseline comparison on long-horizon search and coding benchmarks.
  - **Confidence:** High for the supplied tools, archive mapping, and learned invocation/abstention policy because the methods state them directly.
  - **Limitation:** The experiments compare ACM with system-level baselines but do not expose ACM's two-tool action basis itself to search or train matched policies over rival dynamic state representations; success therefore does not establish that this supplied decomposition is preferable to untested alternatives.

- **Claim (paraphrase):** In the Qwen3.5-9B training ablation, adding ACM training data raised Pass@1 from 0.635 to 0.727 on BrowseComp-Plus, from 0.405 to 0.425 on DeepSearchQA, and from 0.508 to 0.530 on SWE-Bench Verified.
  - **Source extract (verbatim):** Qwen3.5-9B 0.635 30.8 59k 0.405 88.7 42K 0.508 77.6 46K
  - **Source location:** Table 3, Qwen3.5-9B baseline row
  - **Source extract (verbatim):** + ACM 0.727 46.2 54k 0.425 58.8 41K 0.530 79.3 50K
  - **Source location:** Table 3, ACM-training row
  - **Source extract (verbatim):** Table 3: Ablation of distillation and ACM training on Qwen3.5-9B. Pass@1 reports accuracy. Tools is the average number of tool calls per episode. Peak Tok. is the average peak token count across episodes.
  - **Source location:** Table 3 caption
  - **Scope:** The paper's Qwen3.5-9B ablation on BrowseComp-Plus, DeepSearchQA, and SWE-Bench Verified under its fixed ACM tools, data pipeline, harness, and evaluation setup.
  - **Confidence:** High for the reported point values because the ablation table states them directly.
  - **Limitation:** The comparison tests the complete supplied ACM training treatment inside a fixed context-management decomposition; it does not isolate which part caused the gains or compare matched learned policies over rival state representations or action bases.

## Connections Found

The paper's primary role is a context-bound worked case for [use testing a decomposition only locally](../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) and for the rule that [a decomposition's scope needs derivation, inheritance, or discriminating use](../notes/derivation-and-inheritance-give-starting-warrant-earns-scope.md). Every evaluation holds the `manage_context`/`query_memory` split fixed while training and testing a controller inside it, so the reported gains establish that this conjunction sufficed here; they do not discriminate the split from rejected alternatives. The short-term/long-term-memory analogy motivates the split but does not derive it from independently supported constraints or transfer a tested ontology. Within that narrow role, the paper also supplies a worked case for [oracle-dependent feedback-trained memory management](../notes/memory-management-policy-is-learnable-but-oracle-dependent.md), implements [preserving evidence without making history the next context](../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md), and bears on [knowledge storage not implying contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md). Its peak-context reductions support the feasibility face of [context efficiency](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md), while increased tool use leaves aggregate cost unresolved. [AgeMem](../agent-memory-systems/lightweight/agemem.md) is the closest learned-policy comparison, [Virtual Context](../agent-memory-systems/reviews/virtual-context.md) is the closest engineered raw-trace/compact-view comparison, and [Faithful Self-Evolvers](./llm-agents-are-not-always-faithful-self-evolvers.ingest.md) supplies the important warning that keeping raw turns retrievable does not establish faithful activation of a summary or later query.

## Extractable Value

1. **Successful controller training does not validate the chosen decomposition** -- ACM fixes a feature map for context management -- chronological summary boundaries, archived raw prefixes, and identifier-based queries -- then learns action timing inside it. Because no rival operation set or constraint-changing intervention is tested, the gains license replay of this process on similar cases rather than the general rule that context management should use this split. This is a direct worked case for [local decomposition tests](../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) and [unwarranted free-choice scope](../notes/derivation-and-inheritance-give-starting-warrant-earns-scope.md). [quick-win]

2. **Recoverable storage is not lossless active context** -- Saving every discarded turn prevents irreversible deletion, but the working summary is still selective, `query_memory` still has to be invoked, and a querier model still chooses what to return. The paper demonstrates one successful reread case, not systematic read-back or activation faithfulness; “lossless” is therefore justified for archival recoverability, not for the operative context. [deep-dive]

3. **Peak-context feasibility and aggregate inference cost can move in opposite directions** -- ACM reduces peak token pressure while often increasing tool calls and exploration length (BrowseComp-Plus rises from 19.5 ReAct tool calls to 46.2 after ACM post-training). That is evidence for treating per-window feasibility, total tokens, latency, and tool cost as separate evaluation axes rather than calling all of them context efficiency. [quick-win]

4. **Train both invocation and abstention** -- ACM's dual constraints label not only where context management should happen, but where a management call should be replaced by search, evidence inspection, or committing to an answer. This turns “when to compress” into a policy over competing next actions rather than a one-sided trigger detector, but the policy remains bounded by the supplied operation vocabulary. [just-a-reference]

5. **A context-management intervention needs a horizon-capable base policy** -- Qwen3-4B-Thinking averaged two turns and 1.2 searches, stopped at about 18% of its context budget, and scored 3.4%, so neither the tools nor their training could receive useful signal. This is a boundary of the demonstrated process, not the main generalization problem: it shows that the process presupposes sustained exploration before its chosen decomposition can matter. [experiment]

6. **Context management may improve reliability more than frontier capability** -- The Pass@4/Pass^4 analysis reports that post-training narrows the gap mainly by raising pass@1 and all-four-trials consistency, with a smaller gain in whether any trial succeeds. This suggests cleaner working context stabilizes paths the model can already solve; the claim is promising but figure-bound and should be replicated with reported numeric uncertainty. [experiment]

## Limitations (our opinion)

The primary limitation is the untested task decomposition, not the chosen model family. ACM defines context management as two operations over chronological history: summarize and archive a prefix, then query its raw messages through an identifier. The policy, teacher annotations, prompts, training traces, baselines, and evaluation all accept that split. As [local success cannot test a decomposition's transfer](../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md), the experiment cannot distinguish a load-bearing boundary from a convenient feature set that happens to fit benchmarks dominated by long search traces and bulky tool output. The human-memory analogy is motivation, not derivation; under [the decomposition-warrant test](../notes/derivation-and-inheritance-give-starting-warrant-earns-scope.md), the untested residue is free choice and should remain replaceable. Alternative decompositions -- explicit live invariants, structured plans, selective tool-output paging, dependency-aware retention, external schedulers, or learned state representations -- are outside the experimental search space.

The paper's “lossless compression” terminology overstates what is tested. Raw messages remain stored, but the active summary is lossy by construction, recall is pull-only, and the querier returns another model-selected projection. In light of [condensed memories losing behavioral influence](./llm-agents-are-not-always-faithful-self-evolvers.ingest.md), archival recoverability should not be treated as evidence of activation faithfulness without systematic hide/retrieve/use audits.

The remaining details narrow the demonstrated process further. The main policy, summarizer, and querier are Qwen3.5-9B; the teacher is Qwen3.5-397B-A17B; the three benchmarks cover two search settings and repository coding; weaker policies may never sustain enough exploration for the operations to matter; and the compression baselines are reimplementations. Peak tokens and KV-cache pressure improve, but total input/output tokens, end-to-end latency, retrieval error, storage growth, and dollar cost are not reported as a unified budget. The training pipeline also depends on reference answers, teacher annotations, a judge, and trajectory filters. Together these details support a particular reproducible recipe, not an explanation of which invariant makes it work or why that invariant should survive another task decomposition.

## Recommended Next Action

Retain ACM as a source-only worked case and do not promote its two-tool decomposition into methodology unless a future study compares rival operation sets or changes a stated constraint strongly enough to make the decomposition itself refutable.
