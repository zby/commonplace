---
source: https://yoonholee.com/meta-harness/paper.pdf
description: Stanford/MIT paper proposing Meta-Harness, an outer-loop system that uses a coding agent with full filesystem access to prior code and execution traces to automatically search over and optimize LLM harnesses — outperforming hand-engineered baselines on text classification and TerminalBench-2.
captured: 2026-03-31
capture: pdf-read
genre: scientific-paper
type: kb/sources/types/snapshot.md
---

# Meta-Harness: End-to-End Optimization of Model Harnesses

Author: Yoonho Lee, Roshen Nair, Qizheng Zhang, Kangwook Lee, Omar Khattab, Chelsea Finn
Source: https://yoonholee.com/meta-harness/paper.pdf
Date: Preprint (2026)

Project page: https://yoonholee.com/meta-harness/
Optimized harness: https://github.com/stanford-iris-lab/meta-harness-tbench2-artifact

## Abstract

The performance of large language model (LLM) systems depends not only on model weights, but also on their *harness*: the code that determines what information to store, retrieve, and present to the model. Yet harnesses are still designed largely by hand, and existing text optimizers are poorly matched to this setting because they compress feedback too aggressively: they are memoryless, condition only on scalar scores, or restrict feedback to short templates or summaries. We introduce **Meta-Harness**, an outer-loop system that searches over harness code for LLM applications. It uses an agentic proposer that accesses the source code, scores, and execution traces of all prior candidates through a filesystem. On online text classification, Meta-Harness improves over a state-of-the-art context management system by 7.7 points while using 4x fewer context tokens. On retrieval-augmented math reasoning, a single discovered harness improves accuracy on 200 IMO-level problems by 4.7 points on average across five held-out models. On agentic coding, discovered harnesses surpass the best hand-engineered baselines on TerminalBench-2. Together, these results show that richer access to prior experience can enable automated harness engineering.

## 1 Introduction

Changing the harness around a fixed large language model (LLM) can produce a 6x performance gap on the same benchmark. The *harness* — the code that determines what to store, retrieve, and show to the model — often matters as much as the model itself. This sensitivity has led to growing interest in **harness engineering**, the practice of refining the code around an LLM to improve the overall system's performance. But despite its importance, harness engineering remains largely manual: practitioners inspect failures, adjust heuristics, and iterate on a small number of designs. This paper asks whether this process itself can be automated.

A natural starting point is recent work on text optimization. However, these methods are poorly matched to harness engineering because they typically operate with short-horizon or heavily compressed feedback: some condition only on the current candidate, others rely primarily on scalar scores, and others restrict feedback to short templates or LLM-generated summaries. This is a pragmatic scalability choice, not evidence that longer-range dependencies are uninformative. Harnesses act over long horizons: a single choice about what to store, when to retrieve it, or how to present it can affect behavior many reasoning steps later. Compressed feedback often removes the information needed to trace downstream failures to earlier harness decisions.

Meta-Harness addresses this limitation with an agentic harness for optimizing harnesses via end-to-end search. Its proposer is a coding agent (Claude Code with Opus-4.6) that accesses source code, evaluation scores, and execution traces via a filesystem rather than ingesting them as a single prompt. In practice, the proposer reads a median of **82 files per iteration** in the most demanding setting, referencing over 20 prior candidates per step. A single evaluation can produce up to 10,000,000 tokens of diagnostic information — roughly three orders of magnitude beyond the largest feedback budgets used in prior text optimization settings.

Key results:
- On online text classification: +7.7 points over ACE, matching next-best text optimizer's final accuracy after just 4 evaluations, using 4x fewer context tokens
- On retrieval-augmented math reasoning: +4.7 points on 200 IMO-level problems across five held-out models
- On TerminalBench-2: surpasses Terminus-KIRA and ranks #1 among all Haiku 4.5 agents (37.6%)

## 2 Related Work

Meta-Harness brings ideas from credit assignment and meta-learning in a new regime enabled by recent advances in coding agents. Rather than updating model weights, the system assigns credit at the harness level.

**External memory and adaptive access.** Several prior works note the benefits of treating large knowledge sources or long inputs as external resources that a language model accesses adaptively, rather than consuming them in a single pass. Specifically, retrieval-augmented generation, interleaved retrieval and reasoning, memory-based agents, or recursive language models are mechanisms for adaptive access to external context. Meta-Harness uses a similar access pattern, but in the more demanding setting of harness engineering.

**Executable code search.** Recent methods search over executable code for functions, workflows, or agent designs. Early work proposes using large models as mutation and crossover operators in evolutionary program search. Later methods evolve designated functions within fixed program scaffolds, use meta-agents to program new agents from prior discoveries, or search over workflow graphs for agentic systems. Another line of work searches over memory designs for continual-learning agents. In contrast, Meta-Harness searches over domain-specific harnesses including prompt construction, retrieval, and state update strategies that reset between tasks. Its outer loop is deliberately minimal: instead of relying on a fixed scaffold, an archive of prior discoveries, or a persistent memory mechanism, it gives the proposer unrestricted filesystem access to prior experience.

**Text optimization methods.** Meta-Harness is also closely related to methods such as ProTeGi, TextGrad, OPRO, GEPA, AlphaEvolve/OpenEvolve, and Feedback Descent, which iteratively improve prompts or other text artifacts using feedback from prior attempts. However, these methods are less well suited to harness engineering, where optimization targets a complete executable procedure, and the relevant environmental feedback is distributed across code, scores, and execution traces in a way that is hard to summarize up front.

## 3 Meta-Harness: A Harness for Optimizing Harnesses

Meta-Harness is an outer-loop procedure for searching over task-specific harnesses. It is built on the idea that harness optimization benefits from allowing a proposer to selectively inspect prior code and execution traces via filesystem access, rather than optimizing from lossy summaries or an additional hand-designed search structure.

**Objective.** A harness is a stateful program that wraps a language model and determines what context the model sees at each step. Formally, let M denote a fixed language model and X a task distribution. For a harness H and task instance x ~ X, we execute a rollout trajectory τ ~ p_M(H, x). The harness constructs prompts for M, the model responds, and the harness updates its state after each interaction. A task-specific reward function r(τ, x) scores the trajectory. The objective is to **find the harness that maximizes the expected final reward**:

H* = argmax_H E_{x~X, τ~p_M(H,x)} r(τ, x)

**Meta-Harness search loop.** Meta-Harness uses a single coding agent proposer with access to a growing filesystem D that serves as its feedback channel. A *coding agent* is a language-model-based system that can invoke developer tools and modify code. Unlike prior systems that externalize the improvement logic in a hand-designed search loop, Meta-Harness delegates diagnosis and proposal to the coding agent itself: it decides which prior artifacts to inspect, which failure modes to address, and whether to make a local edit or a more substantial rewrite. The proposer is not a raw next-token model; it is an agent that retrieves information, navigates prior artifacts, and edits code as part of the search itself. Each evaluated harness contributes a directory containing its source code, scores, and execution traces (such as prompts, tool calls, model outputs, and state updates). The filesystem is typically far larger than the proposer's context window, so the proposer queries it through terminal tools such as grep and cat rather than ingesting it as a single prompt.

Meta-Harness maintains a population H and a Pareto frontier over evaluated harnesses, but imposes no parent-selection rule: the proposer is free to inspect *any* prior harness and its execution trace when proposing new ones. Evolution runs for a fixed number of iterations and performs a final test-set evaluation on the Pareto frontier. The proposer never sees test-set results; its only feedback comes from the **search set**, the subset of task instances used to evaluate candidate harnesses during search and generate the feedback signal for improvement.

**Algorithm 1: Meta-Harness outer loop**

```
Input: tasks X, LLM M, proposer P, iterations N
Initialize: population H  (Initial set of valid harnesses)
Initialize: filesystem D ← ∅  (stores code, scores, traces)
for H in H do
    E_H ← Evaluate(H, M, X)
    D ← D ∪ {(H, E_H)}
for t = 1...N do
    Proposer P queries filesystem D  (inspects prior harnesses and scores)
    Proposer P proposes k new harnesses {H_1, ..., H_k}
    for H in {H_1, ..., H_k} do
        if H passes interface validation then
            D ← D ∪ {(H, EVALUATE(H, M, X))}
return Pareto frontier of harnesses stored in D
```

**Advantages of code-space search.** Harness optimization occurs in code space, where small changes to retrieval, memory, or prompt-construction logic can affect behavior many steps later, making local search heuristics poorly matched to the problem. By inspecting execution traces, the proposer can often infer *why* a harness failed and which earlier design choices likely contributed to the failure, not just *that* it failed.

**Practical implementation.** Each harness is a single-file Python program that modifies task-specific prompting, retrieval, memory, and orchestration logic. The proposer is Claude Code with Opus-4.6, guided by a minimal domain-specific skill that describes where to write new harnesses, how to inspect previous harnesses and their execution traces, and what files it can and cannot modify. The base model M varies by domain and is always frozen. A typical run evaluates roughly 60 harnesses over 20 iterations.

## 4 Experiments

Meta-Harness is evaluated on three task domains: online text classification, math reasoning, and agentic coding. Two main classes of baselines: (1) **Human-designed strategies**: hand-crafted harnesses representing current state of the art. (2) **Program-search methods**: methods that search over candidate harnesses using feedback and reward signals, designed for smaller-scale settings.

**Comparison of text optimization methods (context per iteration):**

| Method | History | Log content | MTok/iter |
|--------|---------|-------------|-----------|
| OPRO | Window | past (solution, score) pairs | 0.002 |
| TextGrad | Last | textual feedback on current artifact | 0.015 |
| AlphaEvolve | Window | program database + eval. scores | 0.022 |
| GEPA | Summary | reflective feedback from rollout traces | 0.008 |
| Feedback Descent | Summary | comparison + textual feedback | 0.012 |
| TTT-Discover | Window | prev. solution fragment | 0.026 |
| **Meta-Harness** | **Full** | **all logs and scores** | **10.0** |

Meta-Harness uses orders-of-magnitude more context per artifact evaluation than prior text optimization methods.

### 4.1 Online Text Classification

Uses three datasets: LawBench (215 classes), Symptom2Disease (22 classes), and USPTO-50k (180 classes). Ran 20 evolution iterations with two candidates per iteration, producing 40 candidate harnesses.

**Results (test-set metrics, average accuracy / context tokens):**

| Harness | Avg Acc | Ctx (K) |
|---------|---------|---------|
| Zero-Shot | 27.4 | 0 |
| Few-Shot (all) | 40.8 | 12.3 |
| MCE | 40.0 | 28.5 |
| ACE | 40.9 | 50.8 |
| **Meta-Harness** | **48.6** | **11.4** |

Meta-Harness improves online text classification accuracy while using a smaller input context.

**Ablation: information available to the proposer**

| Method | Scores | Code | Summaries | Traces | Median | Best Acc | >ZS |
|--------|--------|------|-----------|--------|--------|----------|-----|
| Scores Only | ✓ | ✓ | ✗ | ✗ | 34.6 | 41.3 | 26 |
| Scores + Summary | ✓ | ✓ | ✓ | ✗ | 34.9 | 38.7 | 23 |
| Meta-Harness (full) | ✓ | ✓ | - | ✓ | 50.0 | 56.7 | 39 |

**Access to raw execution traces is the key ingredient for enabling harness search.** Summaries do not recover the missing signal, and may even hurt by compressing away diagnostically useful details.

Meta-Harness is 10x faster and converges to a better harness: it matches the best prior text optimizers (OpenEvolve, TTT-Discover) with 10x fewer full evaluations, and its final accuracy surpasses theirs by more than 10 points.

**Out-of-distribution task evaluation.** The selected Meta-Harness system achieves the best average accuracy (73.1%), outperforming ACE (70.2%) and all few-shot baselines on 9 previously unseen classification datasets.

### 4.2 Harnesses for Retrieval-Augmented Reasoning

Setup: olympiad math solving with retrieval from a corpus of ≥500,000 solved problems. Meta-Harness is used to optimize a harness for 40 iterations over a 250-problem search set (OlympiadBench + Omni-MATH hard), producing 109 candidate retrieval harnesses.

**Results on 200 IMO-level math problems (pass@1 averaged over 3 samples):**

| Method | GPT-5.4n | GPT-5.4m | Gem-3.1FL | Gem-3F | GPT-20B | Avg |
|--------|----------|----------|-----------|--------|---------|-----|
| No Retriever | 23.0 | 28.8 | 28.6 | 42.6 | 47.6 | 34.1 |
| Dense Retrieval (k=5) | 28.3 (-0.5) | 28.3 (-0.5) | 37.1 (+8.5) | 47.2 (+4.6) | 46.7 (-0.9) | 38.1 (+4.0) |
| BM25 Retrieval | 29.2 (+0.4) | 29.2 (+0.4) | 32.8 (+4.2) | 46.6 (+4.0) | 48.9 (+1.3) | 37.5 (+3.4) |
| **Meta-Harness** | **31.7 (+8.7)** | **29.7 (+0.9)** | **34.9 (+6.3)** | **46.3 (+3.7)** | **50.6 (+3.0)** | **38.8 (+4.7)** |

The discovered Meta-Harness retrieval strategy improves reasoning on IMO-level math problems across all five held-out models, with a 4.7-point average gain over no retriever.

### 4.3 Evaluating Agentic Coding Harnesses on TerminalBench-2

TerminalBench-2 evaluates LLM agents on 89 challenging tasks that require long-horizon, fully autonomous execution under complex dependencies and substantial domain knowledge. Search is initialized from two strong open baselines: Terminus 2 and Terminus-KIRA.

**Pass rate on TerminalBench-2:**

| Harness | Auto | Pass (%) |
|---------|------|---------|
| *Claude Opus 4.6* | | |
| Claude Code | ✗ | 58.0 |
| Terminus 2 | ✗ | 62.9 |
| Terminus-KIRA | ✗ | 74.7 |
| **Meta-Harness** | ✓ | **76.4** |
| *Claude Haiku 4.5* | | |
| Goose | ✗ | 35.5 |
| Terminus-KIRA | ✗ | 33.7 |
| **Meta-Harness** | ✓ | **37.6** |

Meta-Harness ranks #2 among all Opus-4.6 agents and #1 among all Haiku-4.5 agents on this competitive task.

**Qualitative behavior.** The search trajectory demonstrates that the proposer does more than random mutation. Across the first seven iterations, it identifies a confound, tests the confound-isolating hypothesis directly, observes that control-flow and prompt edits remain fragile, and then deliberately pivots to a purely additive modification (adding an environment snapshot before the first LLM call) that becomes the best candidate. Iteration 10 shows cross-run transfer: the proposer references results from a separate earlier search run. This kind of causal reasoning over prior failures is precisely what full-history filesystem access enables and what compressed-feedback optimizers cannot support.

## 5 Discussion

Beyond outperforming existing harnesses, Meta-Harness has several practical advantages:
- Discovered harnesses generalize to out-of-distribution classification datasets and to unseen base models in the math setting
- Search runs complete in a few hours of wall-clock time, producing readable, transferable strategies reusable across models including future, stronger ones
- Overfitting in code space is more inspectable: brittle if-chains or hard-coded class mappings are visible on inspection in a way that weight-space overfitting is not

The main advantage of Meta-Harness is not just search over code, but search with *selective access to prior diagnostic experience*. The proposer can inspect raw code, execution traces, and prior failures, then use that information to form and test hypotheses about what to change.

The findings reflect a recurring pattern in machine learning: once a search space becomes accessible, stronger general-purpose agents can outperform hand-engineered solutions. A natural next step for future work is to co-evolve the harness and the model weights, letting the strategy shape what the model learns and vice versa.

## Appendix A: Qualitative Proposer Behavior

**File Access Statistics (TerminalBench-2, 10 iterations, Claude Opus 4.6):**

| Statistic | Value |
|-----------|-------|
| Files read per iteration (median) | 82 |
| Files read per iteration (range) | 69–99 |
| Harness source code | 41% |
| Execution traces | 40% |
| Score/summary files | 6% |
| Other | 13% |

The proposer's access pattern is non-Markovian: it routinely inspects the majority of available history rather than conditioning only on the most recent parent.

**Qualitative Behavior — Causal Reasoning Over Prior Failures (TerminalBench-2 search trajectory summary):**

- **Iterations 1–2:** Both bundle plausible structural fixes with prompt-template modifications, and both regress sharply from the 64.4% Terminus-KIRA baseline.
- **Iteration 3:** The proposer explicitly identifies the confound: the shared prompt rewrite — not the structural bugfixes — caused the regressions. It therefore reverts to the original prompt and tests only the structural fixes in isolation.
- **Iterations 4–6:** Continue probing the same part of the design space with more explicit theories about concrete state-machine bugs. All still regress.
- **Iteration 7 (winning candidate):** After six consecutive regressions, the proposer shifts strategy from modifying the control loop to adding information *before* the loop begins: a purely additive environment snapshot gathered via shell command before the first LLM call. This candidate succeeds.
- **Iteration 8:** Attempts to compose the additive snapshot fix with an earlier structural fix, reasoning they address independent failure modes.
- **Iteration 10:** Cross-run transfer — the proposer references results from a separate earlier search run to guide the next proposal.

## Appendix B: Discovered Harnesses

### B.1 Text Classification Harness

Meta-Harness discovers a family of memory-based harnesses. Two representative Pareto endpoints:

**Meta-Harness (Draft Verification)** — lightweight two-call procedure: (1) retrieve 5 most similar labeled examples, make draft prediction; (2) re-query memory conditioned on draft label, retrieving 5 confirmers (same label) and 5 challengers (different labels), ask model to maintain or revise initial answer. Falls back to standard single-call few-shot prompt when fewer than 5 labeled examples are available.

**Meta-Harness (Label-Primed Query)** — single larger call built from three parts: (1) *label primer* listing all valid output labels upfront; (2) *coverage block* with one query-relevant example per label; (3) *query-anchored contrastive pairs* placing highly similar examples with different labels side by side. Uses TF-IDF retrieval and query-anchored partner selection rather than label-agnostic nearest neighbors.

### B.2 Math Retrieval Harness

A compact four-route BM25 program. All design choices — routing predicates, reranking terms, deduplication thresholds, per-route example counts — were selected by the outer loop across 40 iterations.

- **Combinatorics:** fetch 20 BM25 candidates, deduplicate to 8, rerank by lexical score and difficulty, return top 3. Explicitly trades diversity against hard-problem matching.
- **Geometry:** return 1 hard NuminaMath reference together with 2 raw BM25 neighbors. Search consistently prefers structural matches over difficulty reranking.
- **Number theory:** fetch 12 BM25 candidates and rerank using lexical score, difficulty, and a small bonus for solutions that state a technique early.
- **Default:** fetch 10 BM25 candidates, rerank by lexical score and difficulty, and choose an adaptive number of examples based on how concentrated the top retrieval scores are.

The harness is a merge of two successful search lineages, autonomously combined by the proposer during search.
