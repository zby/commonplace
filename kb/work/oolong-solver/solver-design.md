# Oolong solver — phase-1 design

Status: design only. Nothing here has been built. The prediction register below is written *before* implementation so the claims are registered in advance.

## 1. Benchmark facts

From the Oolong paper ([Bertsch et al., 2025](https://arxiv.org/abs/2511.02817), [code](https://github.com/abertsch72/oolong)) and the Cao et al. rerun:

- Two splits. **Oolong-Synth**: naturalistic synthetic tasks built from classification datasets (e.g. trec), components ablatable; avg context ~536K tokens in the Cao et al. sample. **Oolong-Real**: real conversational data (D&D transcripts), temporal and speaker relations; avg ~385K tokens.
- Task shape: analyze many chunks atomically (label, extract, date, speaker), then answer a distributional question (counts, argmax user, comparisons, temporal patterns).
- Scoring: exact match for label/date/user/comparison answers; numeric answers get partial credit `0.75^|y − ŷ|`.
- Frontier models score <50% on both splits at 128K; performance degrades further at full lengths.

## 2. State of the art to beat

From the [Cao et al. snapshot](../../sources/coding-agents-are-effective-long-context-processors.md) (200-example samples, GPT-5 backbone unless noted):

| Method | Oolong-Synth | Oolong-Real |
|---|---|---|
| GPT-5 full context (sliding window) | 59.22 | 22.45 |
| RAG (Gemini emb.) | 45.53 | 13.38 |
| ReAct agent | 31.39 | 19.06 |
| RLM (Zhang et al., 2025) | 64.38 | 23.07 |
| Codex, no retriever | **71.75** | 33.73 |
| Claude Code + BM25 (Sonnet 4.5) | – | **37.46** |

Target: beat the coding-agent number on each split at the same backbone and at comparable or lower cost. Oolong-Real is the primary target (largest headroom, hardest tasks).

## 3. Pre-registered predictions

- **P1 (headline).** The designed solver beats the same-backbone coding-agent baseline on Oolong-Real, and matches or beats it on Oolong-Synth, at comparable total token cost.
- **P2 (judgment routing).** Gains concentrate on items requiring semantic per-chunk classification — where the coding agent's emergent strategy substitutes regex for judgment. Measured by category breakdown and by inspecting baseline traces.
- **P3 (exact aggregation).** On numeric-answer items, the score distribution shifts from partial credit (`0.75^d`, small d) to exact match: per-chunk labels may err, but symbolic counting adds no further error, while in-context counting does.
- **P4 (variance).** Across reruns, the designed solver has lower score variance than the coding agent — designed schedule vs emergent strategy discovered per-run.
- **P5 (degradation curve).** Accuracy per map call falls with records-per-call past a knee; the measured curve is the empirical input to the [agent-complexity-theory](../agent-complexity-theory/README.md) tradeoff theorems. No specific knee location is predicted — measuring it is the point.

Failure of P1 with the mechanisms correctly implemented is evidence *for* the emergent side of the [codification/relaxing boundary](../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) and gets extracted as such, not buried.

## 4. Architecture

A direct instantiation of the [bounded-context orchestration model](../../notes/bounded-context-orchestration-model.md): a Python scheduler owning exact state `K` (files/SQLite), driving bounded clean-context LLM calls. No conversation accumulates anywhere.

| Stage | Substrate | Binding time | Description |
|---|---|---|---|
| 1. Parse | code | per-context | Deterministically split the context into typed records (utterance, sentence pair, episode) with speaker/date fields. Stored in `K`; reused across every question on the same context. |
| 2. Plan | 1 bounded LLM call | per-question | Read the question only; emit a symbolic plan: task type, unit of analysis, label rubric, aggregation op. Executed by the scheduler, not by the model. |
| 3. Map | bounded LLM calls | per-record/batch | Classify/extract per record under a clean frame: record + rubric, nothing else. Batch size set by the P5 pilot sweep. Results cached in `K` keyed by (record, rubric) for cross-question reuse. |
| 4. Correct | code + repeat calls | per-record | MAKER-style first-to-ahead-by-k voting, budget-aware: spend repeats only on items whose first-pass answers disagree or self-report low confidence. |
| 5. Reduce | code | per-question | Exact aggregation: counting, argmax, grouping, date comparison. Zero LLM involvement. |
| 6. Format | code | per-benchmark | Deterministic answer normalization matched to the scoring protocol. |

Hybrid fallback: if stage 1 parsing of Oolong-Real transcripts resists deterministic rules, use a one-time bounded LLM pass to *propose* the segmentation, then validate and freeze it symbolically — frontload with an LLM, consume with code.

## 5. Mechanism map

The "throw everything applicable at it" enumeration. Each row is a design commitment traceable to a library claim; phase 2 ablates rows.

| Library claim | Design commitment |
|---|---|
| [Bounded-context orchestration model](../../notes/bounded-context-orchestration-model.md) | The whole pipeline is one select/call loop with explicit `K`; no hidden conversation state. |
| [Scheduler/LLM error-correction asymmetry](../../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) | All bookkeeping (counting, sorting, grouping) in code; LLM calls only for semantic judgment. |
| [Codify-versus-LLM heuristics](../../notes/codify-versus-llm-decision-heuristics.md) | Classification stays in LLM calls (proxy-theory, many valid interpretations); parsing, aggregation, formatting are codified (exact-spec). The baseline's regex classifier is the named over-codification mistake. |
| [Frontloading spares execution context](../../notes/frontloading-spares-execution-context.md) | Pre-parse the corpus, pre-compute record boundaries and prompt templates; map calls receive results, not procedures. Label cache amortizes per-context work across questions (the economic case). |
| [Frontloading is partial evaluation](../../notes/frontloading-is-partial-evaluation-not-divide-and-conquer.md) | Binding-time column in the architecture table; per-benchmark / per-context / per-question / per-record stages are the binding-time lattice made operational. |
| [Decomposition heuristics](../../notes/decomposition-heuristics-for-bounded-context-scheduling.md) | Selection separated from joint reasoning (plan vs map); reusable intermediates saved (label cache); representations chosen per call (record + rubric, not raw context slices); verifiable boundaries (per-record outputs are checkable). |
| [Soft degradation, not hard limits](../../notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) | Map batch size chosen from the measured degradation knee (P5 sweep), not from the advertised window. |
| [Session history should not be the default next context](../../notes/session-history-should-not-be-the-default-next-context.md) | Every call gets a constructed clean frame; nothing is carried forward implicitly. |
| [LLM context is composed without scoping](../../notes/llm-context-is-composed-without-scoping.md) | Map calls are isolated frames — no cross-record leakage, no stale history treated as live state. |
| [Information value is observer-relative](../../notes/information-value-is-observer-relative.md) | The plan stage rewrites the question into a per-record rubric — same content, framed for a bounded judge of one record. |
| MAKER voting (via [decomposition heuristics](../../notes/decomposition-heuristics-for-bounded-context-scheduling.md) sources) | First-to-ahead-by-k repeats on disagreement; supplies the error-correction term decomposition alone doesn't. |

## 6. Protocol

- **Backbone parity.** Run the coding-agent baseline and the solver on the same base model. Report both; never compare across backbones.
- **Sampling.** Same protocol as Cao et al.: 200 examples per split, baselines rerun on the identical sample. Full set if budget allows.
- **Cost accounting.** Total input+output tokens, number of calls, wall time, per split and per method. Report cost-matched and cost-unlimited results separately; "wins by spending 10×" is the first review objection.
- **Reruns.** ≥3 runs per method for the P4 variance claim.
- **Trace retention.** `K` is event-sourced; every plan, label, vote, and reduction is auditable. Baseline coding-agent traces retained for the P2 item-level analysis.
- **Pilot first.** The P5 batch-size sweep runs on a small slice before the main run, and fixes the map batch size.

## 7. Risks and unknowns

- **Prior art.** [arXiv 2603.20105](https://arxiv.org/abs/2603.20105) (λ-calculus Y-combinator, map-reduce on long contexts) may already implement much of this on Oolong. **Ingest before building.** If it covers P1, the contribution narrows to P2–P5 — judgment routing, exactness, variance, and the measured curve feeding the theory — which is still a paper, but a different one.
- **Parsing Oolong-Real.** Transcript segmentation may not be cleanly codifiable; the hybrid fallback covers this but weakens the "fully designed" story.
- **Cost blow-up.** Per-record calls over thousands of records can exceed the coding agent's budget. Mitigations: batching at the measured knee, label cache, selective voting. If cost-matched P1 fails while cost-unlimited succeeds, report exactly that.
- **Metric note.** Oolong-Synth's `0.75^|y−ŷ|` partial credit structurally favors exact symbolic counting (P3 is partly baked into the metric). Disclose; report exact-match-only numbers alongside.
- **Plan-stage fragility.** A wrong plan poisons everything downstream — the single point where underspecified interpretation survives in the design. Consider k-sample plan voting; note the asymmetry with the coding agent, which can recover mid-run by observing failures (its iterative-refinement advantage; see the Cao et al. Figure 2 trace).
- **Backbone drift.** Published numbers were GPT-5-era (early 2026); current models may have moved Oolong SOTA. Re-verify best published numbers at build time.

## 8. Next actions

1. Ingest arXiv 2603.20105 (`cp-skill-ingest`) and write the positioning paragraph.
2. Pull the Oolong dataset (HF `oolongbench` / `abertsch72/oolong`); verify license, scoring scripts, and the Cao et al. sample protocol.
3. Re-verify current SOTA (anything post-March 2026 on either split).
4. Build stage 1 (parser) and the P5 pilot sweep.
5. Decide backbone and budget; then the main run.
