---
description: Benchmark paper claiming coding agents beat RAG and context scaling on long-context tasks by using filesystem-native search, slicing, and scripting
source_snapshot: coding-agents-are-effective-long-context-processors.md
ingested: "2026-03-31"
type: kb/sources/types/ingest-report.md
domains: [context-engineering, long-context, tool-loop, evaluation]
---

# Ingest: Coding Agents are Effective Long-Context Processors

Source: coding-agents-are-effective-long-context-processors.md
Captured: 2026-03-31
From: https://arxiv.org/html/2603.20432v1

## Classification
Type: scientific-paper — arXiv benchmark paper with comparative experiments, ablations, citations, and an explicit methods/results structure.
Domains: context-engineering, long-context, tool-loop, evaluation
Author: Academic authors presenting a preprint benchmark study with released code; worth attending to for comparative evidence, but it is still preprint evidence rather than production-system evidence.

## Summary
The paper argues that long-context processing can be externalized from latent attention into explicit executable interaction: instead of stuffing giant corpora into a context window or relying on fixed retrieval pipelines, let a coding agent navigate files, run searches, write scripts, inspect intermediate outputs, and iteratively refine its approach. Across five benchmarks spanning 188K to three trillion tokens, the authors report that off-the-shelf coding agents outperform published baselines by 17.3% on average, attribute the gains to native tool proficiency plus file-system familiarity, and show an important negative result: adding standard retrieval tools does not reliably help and can suppress the broader exploratory behavior that makes the agents strong.

## Connections Found
The source lands squarely in the KB's bounded-context scheduling cluster. It **grounds** [Context efficiency is the central design concern in agent systems](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) by giving benchmark evidence that context structure and externalized tool use matter more than raw window size alone, and it **grounds** [Tool loop](../notes/tool-loop-README.md) by showing concrete cases where symbolic orchestration inside the loop beats flat retrieval or full-context baselines. It **exemplifies** [Context engineering](../notes/definitions/context-engineering.md) and [Semantic sub-goals that exceed one context window become scheduling problems](../notes/semantic-sub-goals-that-exceed-one-context-window-become-scheduling.md): the agent routes through directories, loads only slices, stores intermediate state in scripts/results, and turns semantic overflow into executable substeps. It also **extends** [The fundamental split in agent memory is not storage format but who decides what to remember](../agent-memory-systems/agentic-memory-systems-comparative-review.md) by adding a strong datapoint that filesystem-native navigation can outperform standard retrieval on QA-like tasks, while still leaving persistent knowledge navigation untested. Finally, it **extends** [Process structure and output structure are independent levers](../notes/process-structure-and-output-structure-are-independent-levers.md): the performance story here is about process structure (search, slice, script, refine), not output formatting.

## Extractable Value
1. [deep-dive] The high-reach claim is not merely "coding agents are good at QA" but that **filesystem-native tool use externalizes long-context overflow into executable process structure**. That mechanism transfers beyond these benchmarks and deserves its own note connecting context efficiency, tool loops, and the retrieval-vs-navigation debate.
2. [quick-win] Add this paper as empirical grounding in [Context efficiency is the central design concern in agent systems](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) and [Tool loop](../notes/tool-loop-README.md); those notes currently rely more on theory and practitioner evidence than on benchmark comparisons of file-native execution vs full-context or RAG baselines.
3. [experiment] Turn the paper's three emergent strategies into explicit evaluation scenarios for our own framework: iterative query refinement for multi-hop retrieval, programmatic aggregation over full documents, and hybrid read/search behavior for mixed long-context tasks.
4. [deep-dive] The negative result on retrievers is important but narrower than the title suggests: standard retrieval helpers may become a behavioral trap that suppresses richer native exploration. This is a useful hypothesis to test against systems like [OpenViking](../agent-memory-systems/reviews/openviking.md), where retrieval is layered under filesystem-like navigation rather than exposed as the agent's primary discovery path.
5. [experiment] The folder-vs-single-file ablation is directly borrowable as a design test for context systems: when the same corpus is exposed either as navigable files or as one monolith, does the agent develop coordinate-based read/slice behavior (`nl` + `sed`) or fall back to repeated global scans? That is a concrete way to test whether structure really changes agent strategy.
6. [just-a-reference] The exact leaderboard numbers are lower-reach than the mechanism. The per-benchmark wins are useful citations, but the durable insight is the behavioral shift toward search, slicing, and script-driven aggregation, not whether one specific 2026 Codex/Claude configuration scored 62.5 vs 61.5 on LongBench.

## Limitations (our opinion)
The headline claim is broader than the evidence. The paper mostly tests retrieval-heavy QA, aggregation, and reading-comprehension tasks, so by the KB's own standard in [Claw learning loops must improve action capacity not just retrieval](../notes/claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md), it does **not** establish that coding agents are superior general knowledge workers; it establishes a strong result on a narrow but important slice of long-context work.

The central mechanism is under-ablated. The authors attribute gains to "native tool proficiency" plus "file system familiarity," but the simpler account is that executable search/slicing/scripting is doing most of the work, regardless of whether the agent has any special filesystem prior. The folder-vs-single-file ablation points in the right direction, but it does not cleanly separate file hierarchy, coordinate-based extraction, prompt differences, and backbone/tooling effects.

"Retrieval tools do not uniformly improve performance" should be read narrowly. What the paper really shows is that **these** retriever integrations, in **this** prompt/tool setup, often displaced stronger native exploration. It does not rule out richer retrieval architectures, hierarchical progressive disclosure, or retrieval layers subordinated to agent-controlled workflows of the kind discussed in [OpenViking](../agent-memory-systems/reviews/openviking.md) and [The fundamental split in agent memory is not storage format but who decides what to remember](../agent-memory-systems/agentic-memory-systems-comparative-review.md).

The evaluation setup also limits confidence. They sample 200 examples per benchmark for cost reasons, use LLM-as-judge evaluation on BrowseComp-Plus, and compare against baselines that are sometimes structurally weaker than the proposed method (for example, fixed RAG top-k or sampled/sliding-window full-context baselines). That means the results are strong evidence for the value of externalized executable processing, but not final evidence that the broader design space has been fairly exhausted.

## Recommended Next Action
Write a note titled `Filesystem-native tool use is a distinct long-context strategy, not just a storage choice` connecting to [Context efficiency is the central design concern in agent systems](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md), [Tool loop](../notes/tool-loop-README.md), [The fundamental split in agent memory is not storage format but who decides what to remember](../agent-memory-systems/agentic-memory-systems-comparative-review.md), and [Process structure and output structure are independent levers](../notes/process-structure-and-output-structure-are-independent-levers.md) — it would argue that file systems matter here because they expose deterministic operations that let agents convert semantic overflow into executable process structure.
