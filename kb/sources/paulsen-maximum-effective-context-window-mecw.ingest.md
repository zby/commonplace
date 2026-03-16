---
description: Empirical study measuring Maximum Effective Context Window (MECW) across 11 frontier LLMs — finds MECW is up to 99% smaller than advertised MCW, varies by task type, and that exceeding MECW drives hallucination rates toward 100%; directly grounds the KB's bounded-context theory with multi-model dose-response data
source_snapshot: paulsen-maximum-effective-context-window-mecw.md
ingested: 2026-03-16
type: scientific-paper
domains: [context-windows, llm-evaluation, rag-systems, agent-architecture]
---

# Ingest: Context Is What You Need — The Maximum Effective Context Window for Real World Limits of LLMs

Source: paulsen-maximum-effective-context-window-mecw.md
Captured: 2026-03-16
From: https://arxiv.org/pdf/2509.21361

## Classification

Type: **scientific-paper** — empirical study with a formal definition (MECW), controlled experimental methodology across 11 models and 4 task types, 66k+ data points, statistical analysis with p-values, and a review of prior frameworks.

Domains: context-windows, llm-evaluation, rag-systems, agent-architecture

Author: Norman Paulsen, Denver, Colorado. No institutional affiliation listed; appears to be an independent researcher. The paper is a 2025 arXiv preprint. The methodology is straightforward and the data collection is substantial (66k rows), but this has not yet been peer-reviewed.

## Summary

Paulsen defines the Maximum Effective Context Window (MECW) as the longest span of token input, for a given problem type, before model performance degrades measurably — distinguishing it from the advertised Maximum Context Window (MCW). Testing 11 frontier LLMs (GPT-5, Claude 3.5, Gemini 2.5, DeepSeek r1, Llama 3.3, etc.) across four task types (single-needle retrieval, multi-needle retrieval, summarization, find-and-sort), the study finds that MECW falls short of MCW by up to >99%, that most models show severe accuracy degradation by 1,000-2,000 tokens for complex tasks, that MECW varies substantially by problem type (and model rankings shift across tasks), and that exceeding MECW drives hallucination rates toward 100%. The paper argues that context window size — not temperature, top_p, or other settings — is the dominant factor determining model accuracy, and that RAG systems improve performance only when operating under the MECW threshold.

## Connections Found

The /connect discovery identified 7 KB notes and 1 sibling source with genuine connections:

**Strongest connections (grounds existing theory with empirical data):**

- [context-efficiency-is-the-central-design-concern-in-agent-systems](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — Paulsen's tasks (counting, sorting, filtering structured data) are LLM-hard — exact enumeration over structured data is a known weakness. The extreme MECW values (some models failing at 100 tokens) likely reflect task difficulty compounding with volume, not pure volume degradation. This makes Paulsen convergent evidence for the same phenomenon ConvexBench demonstrates: LLMs degrade sharply on tasks that strain their reasoning capabilities, with scale (whether depth or token count) amplifying failure. Does not resolve the note's TODO about classical attention-economics degradation curves.

- [bounded-context-orchestration-model](../notes/bounded-context-orchestration-model.md) — The model uses `M` as "the maximum effective context of one agent call." Paulsen empirically measures what `M` is for real models and shows it varies by task type. This means `M` is not a constant but a function `MECW(model, task_type)`.

- [decomposition-rules-for-bounded-context-scheduling](../notes/decomposition-rules-for-bounded-context-scheduling.md) — If MECW for multi-needle retrieval is measured in hundreds of tokens, decomposition rules like "separate selection from joint reasoning" are necessities, not optimizations.

- [distillation](../notes/distillation.md) — RAG improves accuracy only under MECW; above it, RAG actively degrades performance. Distillation becomes a gatekeeper for RAG effectiveness, not a nice-to-have.

- [two-context-boundaries-govern-collection-operations](../notes/two-context-boundaries-govern-collection-operations.md) — The full-text boundary should be calibrated to MECW, not MCW. The note's claim that "the full-text boundary may not [grow with context windows], because complexity costs limit how many note bodies an agent can usefully reason about" is directly supported.

- [in-context-learning-presupposes-context-engineering](../notes/in-context-learning-presupposes-context-engineering.md) — Paulsen quantifies something stronger: even when knowledge IS in the window, it fails if the window exceeds MECW. Context engineering must enforce size limits, not just select the right knowledge.

- [short-composable-notes-maximize-combinatorial-discovery](../notes/short-composable-notes-maximize-combinatorial-discovery.md) — If multi-item retrieval degrades by 1,000-2,000 tokens, the number of notes that can be productively co-loaded is much smaller than nominal context windows suggest.

**Sibling source:**

- [ConvexBench](convexbench-can-llms-recognize-convex-functions.ingest.md) — **converges**: Both papers show LLMs failing on tasks that are hard for them, with different scaling variables. ConvexBench grows compositional depth at low token counts; Paulsen grows token counts but on tasks (exact counting/sorting) that are inherently LLM-hard. Neither cleanly isolates a pure "volume" dimension — Paulsen's tasks confound volume with task difficulty. The papers are convergent evidence for the same phenomenon rather than complementary evidence for two independent dimensions.

**Synthesis opportunity identified:** "Effective context is a function of task type, not a model constant" — combining Paulsen, ConvexBench, and the context-efficiency theory to argue `M` should be parameterized as `MECW(model, task_type)` rather than treated as a per-model constant. The open question is whether there exists a clean volume-only degradation curve on tasks LLMs are actually good at (e.g., natural-language QA over long documents) — "lost in the middle" (Liu et al., 2023) is the closest existing evidence.

## Extractable Value

1. **MECW as empirical grounding for `M`** — The orchestration model's abstract `M` parameter now has measured values across 11 models and 4 task types. Most models degrade severely by 1,000-2,000 tokens for complex tasks; some fail at 100 tokens. This transforms `M` from a theoretical placeholder to a measurable, task-dependent quantity. High reach: the finding that effective capacity << nominal capacity transfers to any system that loads content into LLM context. [quick-win]

2. **Task-type sensitivity of MECW** — Model rankings change across task types (o4-mini tops multi-needle but fails single-needle). This means model selection should be task-specific, and the orchestration model's `select` function should account for task type when budgeting context. High reach: any agent framework making model selection decisions. [experiment]

3. **RAG has a crossover point** — RAG improves accuracy only below MECW; above it, RAG actively worsens performance. This is a falsifiable, actionable design constraint: measure your RAG system's typical context size against the MECW for your task type. High reach: transfers to any RAG-based system. [quick-win]

4. **Cascading failure arithmetic** — A 3-agent chain with 70% per-agent success yields 34.3% system success. When MECW is exceeded and hallucination rates climb, multi-agent systems fail multiplicatively. This is stated as a remark (Section 6.3/Appendix A.2), not a studied finding, but the arithmetic is trivially correct and the MECW data makes the premise (per-agent accuracy drops sharply) empirically grounded. Medium reach: the specific numbers are illustrative, but the multiplicative failure structure is general. [just-a-reference]

5. **Context size > all other hyperparameters** — Paulsen claims context window size has more impact on accuracy than temperature, top_p, or seed parameters. If validated, this reorders the priority of agent system tuning: get context size right first, then tune other parameters. Medium reach: the claim is plausible but tested only on retrieval/counting tasks. [deep-dive]

6. **Degradation curve shape** — Performance degrades non-linearly: high accuracy at low token counts, then sharp drop-off, not gradual decline. This implies cliff-edge behavior rather than graceful degradation — systems should aim to stay well below MECW, not at the boundary. High reach: cliff-edge resource behavior is a general pattern in bounded systems. [quick-win]

## Curiosity Gate

**What is most surprising?** The claim that "a few top of the line models failed with as little as 100 tokens in context" is striking. 100 tokens is essentially nothing — a single short paragraph. If this holds for production models on tasks representative of real use, it implies that even trivially small RAG chunks can exceed MECW for certain task types. The surprising part is not that MECW < MCW (that's expected from "lost in the middle" research), but how extreme the gap is and how it emerges even at tiny scales.

**What's the simpler account?** The tasks (counting colored balloons, sorting names, summing totals) are essentially structured data operations over synthetic datasets. The simpler explanation for the extreme degradation may be that LLMs are particularly poor at precise counting/sorting over structured data — this is a known weakness that compounds with scale. The degradation may be less about "context window effectiveness" in general and more about "LLMs cannot reliably perform exact enumeration tasks, and the failure rate scales with input size." Real-world tasks (document QA, code understanding, summarization of natural text) might show different MECW profiles because they leverage the model's actual strengths (semantic understanding, pattern matching) rather than its weaknesses (exact counting).

**Is the central claim hard to vary?** The claim "MECW varies by task type and is much smaller than MCW" is hard to vary — you cannot swap the tasks, models, or metrics and keep the exact numbers. But the specific MECW values are highly task-dependent, and the paper tests only synthetic structured-data tasks. Swapping to natural-language reasoning tasks could change the degradation curves substantially while preserving the general shape of the finding. The qualitative claim (MECW << MCW) is robust; the quantitative claims (specific token thresholds) are bound to the task distribution tested.

## Limitations (our opinion)

1. **Synthetic task bias** — All four task types involve structured data operations (counting, sorting, filtering) over a synthetic dataset of "person has N colored objects." These tasks test exact retrieval and arithmetic — areas where LLMs are known to be weak. Real-world use cases (document understanding, code analysis, multi-document reasoning over natural language) engage different model capabilities and may have substantially different MECW profiles. The paper's MECW values should not be directly applied to natural-language reasoning tasks without independent validation.

2. **Volume and task difficulty are confounded** — The paper's experimental design varies token count, but the tasks themselves (exact counting, sorting, filtering) are in LLM-hard territory — precise enumeration over structured data is a known weakness. This means the extreme MECW values likely reflect volume × task-difficulty interaction, not pure volume degradation. A clean volume-only test would use tasks LLMs are strong at (e.g., natural-language comprehension) and measure degradation as input length grows. ConvexBench ([Liu et al., 2026](convexbench-can-llms-recognize-convex-functions.md)) has the same structure from the other direction: it varies compositional depth on a task (symbolic reasoning) that is also LLM-hard. Neither paper cleanly isolates a single dimension of the [two-dimensional context cost model](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md).

3. **No reasoning-model isolation** — The paper acknowledges "reasoning and non-reasoning models work in distinctly different ways" but does not systematically compare them. Reasoning models (o4-mini, DeepSeek r1, Gemini 2.5 Flash) may have fundamentally different MECW profiles than base models, and the paper's aggregate findings may mask this distinction.

4. **Binary scoring only** — Accuracy is measured as exact-match (correct answer = 1, incorrect = 0). This misses partial credit: a model that retrieves 9/10 needles scores the same as one that retrieves 0/10. Partial-credit scoring might show more gradual degradation curves, changing the perceived location of MECW.

5. **No mitigation strategies tested** — The paper identifies the problem (MECW << MCW) but tests no interventions. Would structured prompts, chain-of-thought, tool use, or iterative refinement shift the MECW? The [bounded-context orchestration model](../notes/bounded-context-orchestration-model.md) predicts that decomposition (processing items one at a time rather than all at once) would dramatically improve effective capacity — this is exactly what the model is designed for, but the paper doesn't test it.

6. **Single-run per condition** — The paper describes randomizing dataset order to negate positioning effects, but it's unclear whether multiple independent runs were performed per condition. The 66k data points are distributed across 11 models x 4 task types x many token-count levels, which could mean relatively few observations per cell.

## Recommended Next Action

Add Paulsen as convergent evidence alongside ConvexBench in [context-efficiency-is-the-central-design-concern-in-agent-systems.md](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md). Both papers show the same phenomenon (LLMs degrading sharply on hard tasks as scale grows) from different angles, but neither cleanly isolates a pure volume dimension. The note's TODO about classical attention-economics degradation curves remains open — Paulsen does not resolve it because its tasks confound volume with task difficulty.
