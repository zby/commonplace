---
description: Trajectory-to-memory pipeline extracting structured items from successes and failures, with embedding retrieval and parallel-trajectory test-time scaling; append-only, sits between Reflexion and ExpeL
type: note
tags: [related-systems]
status: current
last-checked: 2026-03-22
---

# ReasoningBank

ReasoningBank is a research codebase for LLM agent self-improvement through accumulated reasoning memory. The system runs agents on benchmark tasks (WebArena, SWE-Bench), extracts structured memory items from both successful and failed trajectories, stores them in JSONL files with embeddings, and retrieves the most relevant items at inference time via cosine similarity. Built by Siru Ouyang, Jun Yan, and collaborators at Google Research as the ICLR 2026 implementation. The repo also includes a "memory-aware test-time scaling" mode that runs multiple parallel trajectories per task and compares them to produce higher-quality memory items.

**Repository:** https://github.com/google-research/reasoning-bank

## Core Ideas

**Memory items are structured extractions, not raw trajectories or freeform reflections.** The extraction prompts (`SUCCESSFUL_SI`, `FAILED_SI` in `prompts/memory_instruction.py`) ask the model to produce up to 3 memory items per trajectory, each with a `Title`, `Description`, and `Content` field. The prompts require the model to first reason about why the trajectory succeeded or failed, then summarize generalizable insights. This is more structured than a raw reflection buffer but less structured than ExpeL's explicit `ADD`/`EDIT`/`REMOVE` mutation verbs.

**Both successful and failed trajectories produce memory.** The system has separate extraction prompts for successes and failures. The success prompt asks "why the trajectory is successful" and then summarizes insights. The failure prompt asks to "reflect and think why the trajectory failed" and then summarize "lessons learned or strategies to prevent the failure." This bidirectional extraction is explicit in the code: `induce_memory.py` branches on `status` to select the appropriate system prompt.

**Retrieval is embedding-based, not rule-indexed.** At inference time, `memory_management.py` embeds the current task query (via Gemini or Qwen embeddings), computes cosine similarity against cached embeddings of prior task queries, and returns the top-n most similar prior memory items. The retrieval is query-to-query matching, not memory-content-to-query matching -- the `screening()` function computes an instruction-aware embedding of the current query (prefixed with a retrieval task description) and scores it against the raw cached query embeddings. The embedding cache grows append-only in a JSONL file.

**Memory injection is system-prompt concatenation.** In the legacy agent (`agents/legacy/agent.py`, line 132-137), retrieved memory items are appended to the system prompt with the instruction: "Below are some memory items that I accumulated from past interaction from the environment that may be helpful to solve the task. You can use it when you feel it's relevant. In each step, please first explicitly discuss if you want to use each memory item or not, and then take action." The same pattern appears in the SWE-Bench fork (`third_party/.../agents/default.py`). There is no explicit memory update during a task run -- memory is read-only at inference time and only updated after the run completes.

**Test-time scaling adds parallel trajectory comparison.** The scaling pipeline (`pipeline_scaling.py`, `induce_scaling.py`) runs multiple parallel attempts per task, then feeds all trajectories together to a `PARALLEL_SI` prompt that uses "self-contrast reasoning" to compare successes against failures and produce up to 5 memory items. This is the paper's distinctive contribution: leveraging test-time compute budget to improve memory quality through cross-trajectory comparison.

**The pipeline is three-step sequential: run, evaluate, extract.** `pipeline_memory.py` shows the explicit loop: (1) run inference with memory retrieval, (2) auto-evaluate the trajectory for correctness, (3) extract new memory items from the trajectory. This is a clean separation of concerns, similar to ExpeL's staged pipeline but with a simpler memory substrate. The repo also implements AWM (Agent Workflow Memory) and Synapse as comparison baselines in the same pipeline -- AWM extracts reusable action workflows from successes only, Synapse stores raw trajectories without extraction. These baselines make the repo useful as an ablation reference beyond just the core ReasoningBank mode.

## Comparison with Our System

ReasoningBank is closer to ExpeL than to most other reviewed systems in its overall architecture -- it separates trace gathering from memory extraction and processes both successes and failures. But its memory substrate is simpler than ExpeL's rule list: there are no mutation verbs, no counters, no in-place editing of existing memory items. Memory items are append-only JSONL records, and the retrieval system has no mechanism to demote or remove stale items.

| Dimension | ReasoningBank | Commonplace |
|---|---|---|
| Trace source | Benchmark task trajectories (WebArena, SWE-Bench) | Human+agent editing traces, notes, links, workshop artifacts |
| Learned substrate | Structured memory items (title/description/content) in JSONL | Notes, links, instructions, workshop artifacts |
| Promotion target | Inspectable text injected into system prompt | Inspectable text artifacts only |
| Update style | Append-only extraction, no editing of existing items | Manual curation and targeted file edits |
| Retrieval model | Embedding cosine similarity over task queries | Agent-driven navigation over linked markdown |
| Oracle strength | Auto-evaluation or ground-truth task success/failure | Mostly human judgment and local validation |
| Storage model | JSONL files + embedding cache | Files in git |
| Memory lifecycle | Append-only, no decay or removal | Manual curation with status tracking |

ReasoningBank is stronger than our current system on automated extraction from task outcomes. It genuinely closes the loop: run a task, evaluate success, extract memory, retrieve for next task. That is a working implementation of the trajectory-to-artifact pipeline our survey identifies as important.

Commonplace is stronger on knowledge structure and maintenance. ReasoningBank's memory items are flat, append-only, and benchmark-scoped. There is no equivalent of typed notes, semantic links, index curation, or maturation stages. A memory item cannot be edited, demoted, or composed with other items into a richer explanation. The repo has no mechanism for consolidation across memory items.

## Trace-derived learning placement

On axis 1 of [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md), ReasoningBank fits the **trajectory-run pattern**. It learns from completed task trajectories gathered across benchmark tasks, not from live session streams.

On axis 2, ReasoningBank is a clear **trace-derived artifact-learning** system. The promoted result is inspectable text memory items, never weights. It sits between [Reflexion](./reflexion.md) (simpler: one-sentence verbal plans, no cross-task accumulation) and [ExpeL](./expel.md) (richer: explicit rule mutation verbs, strength counters, cross-trajectory consolidation).

The test-time scaling variant is the interesting subtype signal. By running multiple parallel trajectories and comparing them with `PARALLEL_SI`, ReasoningBank uses test-time compute to improve extraction quality -- a mechanism that is orthogonal to the core memory loop but potentially composable with it. This is distinct from both ExpeL's sequential fold-based consolidation and Dynamic Cheatsheet's carry-forward rewrite.

The [Ingest: Large Language Model Agents Are Not Always Faithful Self-Evolvers](../../sources/large-language-model-agents-are-not-always-faithful-self-evolvers.ingest.md) paper is directly relevant here, since ReasoningBank shares the same trajectory-to-condensed-experience pipeline family. The finding that condensed experience often has limited causal influence at inference time is a ceiling risk for any append-only memory system that lacks explicit maintenance operations.

## Borrowable Ideas

**Bidirectional memory extraction from successes and failures.** Ready now as a design pattern. The separate prompts for successful and failed trajectories are a clean way to get different kinds of insights from different outcomes. Success prompts ask "why did this work" while failure prompts ask "what lesson prevents this failure." That dual framing could be useful for workshop post-mortem patterns.

**Structured memory item format (title/description/content).** Ready now as an extraction template. The three-field format is simple but useful: title for scanning, description for quick judgment, content for the actual insight. This is essentially a note template, and the format could inform how we structure workshop-level tactical learnings.

**Test-time parallel trajectory comparison for better extraction.** Needs a use case first. The `PARALLEL_SI` mechanism -- run multiple attempts, then compare successes against failures in one prompt -- is a concrete pattern for improving learning quality from repeated runs. But it requires repeated execution of the same task, which maps to benchmark settings better than to open-ended knowledge work.

**Query-to-query embedding retrieval.** Needs evaluation first. ReasoningBank retrieves memory by matching the current task query against prior task queries, not by matching against memory content. This is a bet that task similarity predicts memory relevance better than content similarity. Whether that generalizes outside benchmarks with templated queries is unclear.

## Curiosity Pass

The repo's strongest idea is not "reasoning as memory" in the abstract. It is the practical pipeline engineering: the clean three-step loop (run, evaluate, extract) and the bidirectional extraction prompts. These are simple, implementable, and work across two very different benchmarks (web navigation and software engineering).

The weaker part is the memory lifecycle. ReasoningBank has no consolidation, no editing, no removal, no strength tracking. Memory items are append-only JSONL lines. The embedding cache also grows monotonically. In benchmark settings with hundreds of tasks, this creates a practical ceiling: as memory grows, retrieval quality depends entirely on the embedding model's ability to rank the right items to the top. There is no mechanism to prune stale items, merge duplicates, or promote recurring insights.

Checking the Core Ideas for mechanism vs. relocation:

1. **Structured memory extraction** -- this does transform the data. A multi-step trajectory (think/action pairs) goes in; a structured three-field memory item comes out. The transformation is real: the extraction prompt forces generalization ("do not mention specific websites, queries, or string contents"), which changes representation from concrete traces to abstract insights. However, the transformation quality depends entirely on the LLM's single-call extraction, with no verification that the extracted insight is actually generalizable.

2. **Embedding retrieval** -- this relocates but does not transform. The current query is embedded, compared against prior query embeddings, and the top match's memory items are loaded. The "instruction-aware embedding" in `screening()` adds a task description prefix, but the retrieval itself is standard cosine similarity. The mechanism is sound but unremarkable.

3. **Test-time scaling** -- this transforms through comparison. Multiple trajectories are shown together and the model is asked to identify patterns. The `PARALLEL_SI` prompt explicitly requires "self-contrast reasoning," which is a stronger extraction signal than single-trajectory reflection. Whether the contrast genuinely improves the output over single-trajectory extraction is an empirical question the paper presumably answers.

4. **Memory injection via system prompt** -- this relocates. Memory items are concatenated to the system prompt with a framing instruction. The agent is asked to "explicitly discuss if you want to use each memory item or not," which is a useful forcing function for attention but not a structural transformation of the memory content.

## What to Watch

- Whether later versions add memory consolidation, editing, or decay to address the append-only ceiling
- Whether query-to-query retrieval generalizes outside benchmark settings where tasks have templated intents
- Whether the test-time scaling mechanism (parallel trajectories + comparison) composes well with richer memory substrates like ExpeL's rule lists
- Whether the dual success/failure extraction prompts produce measurably different quality than single-prompt extraction
- Whether the SWE-Bench integration shows different memory dynamics than WebArena, given the very different task structure

---

Relevant Notes:

- [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) -- extends: ReasoningBank is an additional trajectory-run artifact-learning case with a distinctive test-time scaling variant
- [ExpeL](./expel.md) -- compares: both extract from successes and failures into inspectable artifacts, but ExpeL has explicit rule mutation verbs and strength counters while ReasoningBank is append-only
- [Dynamic Cheatsheet](./dynamic-cheatsheet.md) -- compares: both are artifact-learning systems, but Dynamic Cheatsheet carries forward one cheatsheet via rewrite while ReasoningBank accumulates discrete memory items
- [Reflexion](./reflexion.md) -- sharpens: ReasoningBank inherits the verbal-reflection idea but adds structured extraction, cross-task accumulation, and embedding-based retrieval
- [Autocontext](./autocontext.md) -- compares: both learn from repeated runs, but Autocontext has richer multi-role orchestration while ReasoningBank has a simpler three-step pipeline
- [Ingest: Large Language Model Agents Are Not Always Faithful Self-Evolvers](../../sources/large-language-model-agents-are-not-always-faithful-self-evolvers.ingest.md) -- evidence: evaluates the trajectory-to-condensed-experience pipeline family and finds limited causal influence of condensed artifacts, which is a ceiling risk for ReasoningBank's append-only memory
- [memory management policy is learnable but oracle-dependent](../memory-management-policy-is-learnable-but-oracle-dependent.md) -- sharpens: ReasoningBank depends on auto-evaluation quality for its extraction signal, making it another case of oracle-dependent artifact learning
