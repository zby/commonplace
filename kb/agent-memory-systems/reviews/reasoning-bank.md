---
description: Three-step pipeline — run benchmark task, auto-evaluate, extract title/description/content memory items from success or failure; embedding retrieval over prior task queries; optional parallel-trajectory self-contrast extraction
type: agent-memory-system-review
traits: [has-comparison, has-external-sources]
tags: [related-systems, trace-derived]
status: current
last-checked: "2026-04-12"
---

# ReasoningBank

ReasoningBank is the Google Research reference implementation for the ICLR 2026 paper on reasoning-as-memory for self-evolving LLM agents. The repo wires together two benchmark harnesses — WebArena (web navigation) and SWE-Bench (software engineering, built on a vendored `mini-swe-agent`) — around a shared pipeline: run an agent on a task with memory retrieved from prior runs, auto-evaluate the trajectory, then extract generalizable memory items and append them to a JSONL bank. An optional "memory-aware test-time scaling" mode runs several attempts per task in parallel and extracts via self-contrast. Authored by Siru Ouyang, Jun Yan, I-Hung Hsu, and collaborators at Google Research and UIUC.

**Repository:** https://github.com/google-research/reasoning-bank

## Core Ideas

**Run-evaluate-extract is three subprocess calls, not a long-lived loop.** `pipeline_memory.py` iterates over benchmark task IDs and for each one invokes three independent Python processes: `run.py` (inference with memory retrieval), `autoeval.evaluate_trajectory` (LLM-as-judge for correctness), then `induce_memory.py` (extract and append memory items). The stages share nothing except files on disk — a result directory, a JSONL memory bank, and an embedding cache. Crash recovery is handled by `--prev_id` skipping already-processed task IDs. The SWE-Bench driver (`third_party/src/minisweagent/run/extra/swebench.py`) collapses retrieval and inference into one process but keeps extraction in a separate `induce_memory.py` step.

**Memory items are structured markdown blocks with three fields.** The extraction prompts in `prompts/memory_instruction.py` (`SUCCESSFUL_SI`, `FAILED_SI`) ask the model to produce up to three items per trajectory, each rendered as `# Memory Item i` with `## Title`, `## Description`, and `## Content` subheaders. The prompt explicitly forbids mentioning specific websites, queries, or string contents, pushing the model toward generalizable insights. Each JSONL record stores the raw task trajectory (`think_list`, `action_list`), the `status`, the generated `memory_items` string, and a `template_id` for deduplication against intent templates.

**Successes and failures drive different prompts.** `induce_memory.py` branches on the reward from auto-eval: reward 1 uses `SUCCESSFUL_SI` ("first think why the trajectory is successful, then summarize insights"), reward 0 uses `FAILED_SI` ("first reflect and think why the trajectory failed, then summarize lessons learned or strategies to prevent the failure"). The two prompts are structurally identical except for the framing sentence — the structure of an extracted item is the same, but the model is directed at different questions. `induce_scaling.py` inverts the reward check (`reward == 0` treated as success) in its own branch, which looks like a bug but does not affect the shared `PARALLEL_SI` prompt since that path shows all trajectories together.

**Retrieval matches the current task query against prior task queries, not against memory content.** `memory_management.select_memory` pulls the top-n items from a JSONL bank. The `screening(...)` function loads cached query embeddings from `*_embeddings.jsonl`, embeds the current query (via `gemini-embedding-001` or Qwen3-Embedding-8B), and prepends an instruction string ("Given the prior web navigation queries, your task is to analyze a current query's intent and select relevant prior queries...") before the final similarity call. Cosine similarity is computed against the cached prior-query embeddings, and the top IDs are mapped back to whole memory items via a linear scan. In `run.py` for WebArena, only the top 1 item's memory blocks are injected into the next run; SWE-Bench uses the same `n=1` default.

**The embedding cache writes the current query before the similarity call.** `screening(...)` appends `{id, text, embedding}` for the current task to the cache file unconditionally, then loads all rows and computes similarity. This couples retrieval and cache growth, and means every run leaves a trace in the cache even if no memory items are eventually produced (e.g., inference crashes before `induce_memory.py` runs). There is no mechanism to prune or dedupe the cache.

**Memory injection is system-prompt concatenation with a forcing instruction.** The WebArena legacy agent (`agents/legacy/agent.py` line 132-137) and the SWE-Bench agent (`third_party/.../agents/default.py` line 71-77) share the same template: the retrieved memory text is appended to the system prompt with "Below are some memory items that I accumulated from past interaction from the environment that may be helpful to solve the task. You can use it when you feel it's relevant. In each step, please first explicitly discuss if you want to use each memory item or not, and then take action." Memory is read-only during a run — no per-step update, no feedback signal flowing back into the bank until the next `induce_memory.py` call.

**Parallel test-time scaling extracts from multiple attempts at once.** `pipeline_scaling.py` spawns `num_trials` parallel `run.py` subprocesses per task against separate web server ports, collects all their trajectories, then calls `induce_scaling.py` once with all of them concatenated into a single prompt. The `PARALLEL_SI` prompt explicitly demands "self-contrast reasoning — identify patterns that consistently led to success, identify mistakes or inefficiencies from failed trajectories and formulate preventative strategies" — and caps output at 5 memory items. The scaling variant replaces the per-trajectory extraction entirely; it does not layer on top of the base extraction.

**Three memory modes share one extraction entry point.** `induce_memory.py` dispatches on `--memory_mode`: `reasoningbank` uses success/failure prompts, `awm` (Agent Workflow Memory) uses `AWM_INSTRUCTION + AWM_EXAMPLE` on successes only and extracts reusable click/fill workflows, `synapse` stores the raw trajectory text with no extraction. All three write into the same JSONL shape with the same retrieval pipeline, making the repo a ready-made ablation harness against two well-known baselines.

## Comparison with Our System

ReasoningBank is a benchmark-scoped trajectory-to-artifact pipeline. Commonplace is a human-and-agent-curated methodology KB. The surface similarity — both promote into inspectable text — hides different design priors: ReasoningBank bets on a strong oracle (task success) and automated extraction; commonplace bets on curated structure and explicit typing.

| Dimension | ReasoningBank | Commonplace |
|---|---|---|
| Trace source | Completed benchmark trajectories (WebArena, SWE-Bench) | Editing sessions, notes, links, workshop artifacts |
| Learned substrate | Markdown memory items (title/description/content) in JSONL | Typed notes, links, ADRs, indexes, instructions |
| Update style | Append-only extraction per trajectory | Human-directed edits with validation bundles |
| Oracle | Auto-eval LLM judge or ground-truth reward | Human judgment plus local validators |
| Retrieval | Cosine similarity of current task query vs prior task queries | Grep over frontmatter and agent navigation over links |
| Promotion target | System-prompt concatenation of top-1 item's blocks | Agent reads notes directly from filesystem |
| Persistence | JSONL bank plus parallel JSONL embedding cache | Git-tracked markdown |
| Scope | Single benchmark family per bank | Cross-topic methodology KB |
| Lifecycle | No edit, no merge, no decay — append-only | Explicit status and maturation |

ReasoningBank is the stronger reference for closing a trajectory-to-memory loop end-to-end without human-in-the-loop: run, judge, extract, inject, repeat. That full automation is a real engineering result, not just a paper claim — the scripts run.

Commonplace is stronger on what happens after extraction. ReasoningBank has no mechanism to edit, merge, demote, or link memory items. The bank grows monotonically; the embedding cache grows monotonically; retrieval quality depends entirely on the embedding model's ability to rank the right prior task to the top. Our system has less automation but genuine curation affordances that ReasoningBank lacks.

## Borrowable Ideas

**Three-stage subprocess pipeline with file handoffs.** Ready now as a workshop pattern. Running inference, evaluation, and extraction as three independent processes sharing only files is a crash-tolerant alternative to a monolithic learning loop, and each stage can be re-run or swapped without touching the others. The `--prev_id` resume flag is a nice minimal pattern for idempotent batch runs.

**Paired success/failure extraction prompts with a shared output schema.** Ready now as an extraction template. Two prompts with identical structure but different framing ("why did this work" vs "why did this fail") let the same downstream consumer handle both without branching. The shared title/description/content schema is simple enough to reuse directly for workshop post-mortem notes.

**Instruction-prefixed query embedding.** Needs evaluation first. `screening(...)` prepends a task description to the current query before embedding, while cached entries are plain query embeddings. This asymmetric instruction-aware retrieval is a cheap trick for steering similarity without re-embedding the whole cache. Whether it actually helps outside benchmark intents is an empirical question.

**Parallel-attempt self-contrast extraction.** Needs a use case first. The `PARALLEL_SI` prompt — "show me all the attempts, contrast successes against failures, extract generalizable strategies" — is a concrete recipe for using test-time compute to improve learning quality. It requires the same task to run multiple times, which is natural in benchmarks but rare in open-ended KB work.

**Ablation-by-mode in one harness.** Ready now as a research-hygiene pattern. A single extraction script that switches between `reasoningbank`, `awm`, and `synapse` modes makes ablation comparisons cheap. If we ever add automated mining to commonplace, having the extractor choice be a flag rather than a fork pays off.

## Curiosity Pass

The headline is "reasoning as memory," but the mechanism is narrower: the system learns *a markdown prefix to the system prompt*. Nothing structural changes about the agent across runs — no tools, no policy, no parameters. What changes is what the first system message contains.

Checking Core Ideas for mechanism vs relocation:

1. **Structured extraction from success/failure.** This is a real transformation. A multi-step trajectory (`think_list`, `action_list`) goes in; an up-to-3-item structured markdown document comes out, with explicit instructions to abstract away specific strings. The transformation depends entirely on a single LLM call with no verification that the extracted insight is true or useful. There is no test that a memory item helps next time — the bank only grows.

2. **Query-to-query embedding retrieval.** This relocates rather than transforms. Cosine similarity over prior task queries is standard; the "instruction-aware" asymmetry between the query embedding and the cached embeddings is a small perturbation, not a new mechanism. This also encodes a strong prior: that task similarity predicts memory relevance. In a benchmark with templated intents, that prior is cheap; in open-ended settings it may not hold.

3. **Top-1 memory injection.** Both the WebArena and SWE-Bench drivers default to `n=1`. Only the single closest prior task's memory items reach the prompt. This bounds the practical learning ceiling: even a bank of thousands of items narrows to a few-hundred-token prompt prefix per run, and a single mismatched retrieval can inject irrelevant content.

4. **Parallel self-contrast.** This does transform. Multiple trajectories concatenated into one prompt with a contrast instruction is a stronger extraction signal than one trajectory alone. The question the repo does not answer is whether the contrast extracts something genuinely different from what separate extractions would produce — a cheap ablation worth running.

A simpler alternative worth naming: much of the retrieval logic collapses if you replace "embedding over prior queries" with "match against intent templates." WebArena already tracks `intent_template_id` explicitly, and deduplication logic in both extractors uses it. A template-lookup retrieval would be interpretable, cheap, and within the benchmark-intent world potentially as good as the embedding path — which is the reason to take this system's retrieval claims as benchmark-bound rather than general.

The genuine contribution is not "bank of reasoning memory" but a *clean separation of evaluation from extraction from retrieval*, each as a swappable component. That modularity is rarer than it sounds in this literature.

**Trace-derived learning placement.** The trace source is completed benchmark task trajectories — WebArena agent logs parsed from `experiment.log` for think/action blocks, SWE-Bench attempts captured by the mini-swe-agent harness — with trigger boundaries at per-task-completion for base extraction and per-parallel-trial-batch for scaling extraction. Extraction pulls out up-to-3 (or up-to-5 in the scaling mode) structured markdown items with title/description/content; the oracle deciding success vs failure is an LLM-as-judge `autoeval` module by default, or ground-truth reward when `--criteria gt` is passed. Promotion stays entirely in inspectable artifacts — markdown text in a JSONL bank with a parallel JSONL embedding cache — with no weight update anywhere in the reviewed code. Scope is cross-task within one benchmark family (one JSONL per website for WebArena, one per model for SWE-Bench); memory is not claimed to transfer across benchmarks. Timing is offline and staged: each task completes its full three-stage pipeline before the next task starts, with no live mining during a single trajectory. On [the survey's axes](../trace-derived-learning-techniques-in-related-systems.md), ReasoningBank sits in the trajectory-run pattern on axis 1 and in symbolic-artifact learning on axis 2; its artifact-structure subtype is "structured markdown items without lifecycle verbs," placing it between Reflexion (freeform verbal reflections, no cross-task accumulation) and ExpeL (scored flat rules with CRUD verbs and counters). The review reinforces the survey's existing placement; the parallel-trajectory extraction variant is a mild split-signal worth noting — it introduces a "contrast-over-parallel-rollouts" subtype distinct from ExpeL's sequential cross-validation folds, though still within the trajectory-run pattern.

## What to Watch

- Whether follow-up work adds a lifecycle to the memory bank — editing, merging, demotion, counters — or whether the monotone-append design is argued as a feature
- Whether query-to-query retrieval survives transfer beyond benchmarks with templated intents, or whether content-aware retrieval replaces it
- Whether the `induce_scaling.py` inverted-reward branch is a real bug or a deliberate relabeling (it currently treats `reward == 0` as success in the scaling path)
- Whether the three-mode extractor (`reasoningbank`/`awm`/`synapse`) gets used as a comparison harness in later papers, or quietly drops
- Whether the embedding cache growth pattern (one append per attempted task, never pruned) causes retrieval drift on long benchmark sweeps

---

Relevant Notes:

- [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — extends: ReasoningBank is a trajectory-run artifact-learning case with a distinctive parallel-trajectory self-contrast extraction variant
- [ExpeL](./expel.md) — compares: both extract from successes and failures into inspectable text, but ExpeL maintains rules with ADD/EDIT/REMOVE verbs and strength counters while ReasoningBank is append-only
- [Dynamic Cheatsheet](./dynamic-cheatsheet.md) — compares: both are artifact-learning systems, but Dynamic Cheatsheet carries one rewriting cheatsheet forward while ReasoningBank accumulates discrete memory items retrieved by similarity
- [Agent-R](./agent-r.md) — contrasts: same trajectory-run family but opposite promotion target — Agent-R compiles trajectories into weights while ReasoningBank stays in prompt-visible markdown
- [Autocontext](./autocontext.md) — compares: both can accumulate across repeated runs, but Autocontext spans both artifact and weight promotion while ReasoningBank stays purely symbolic
- [Ingest: Large Language Model Agents Are Not Always Faithful Self-Evolvers](../../sources/large-language-model-agents-are-not-always-faithful-self-evolvers.ingest.md) — evidence: evaluates the trajectory-to-condensed-experience family ReasoningBank belongs to and finds condensed artifacts have limited causal influence on next-run behavior, a ceiling risk for any append-only bank
- [memory management policy is learnable but oracle-dependent](../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) — sharpens: ReasoningBank's extraction quality depends on auto-eval correctness; the lifecycle has no robustness to oracle noise
