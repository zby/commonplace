---
{
  "type": "types/note.md",
  "description": "Dynamic Cheatsheet combines caller-owned evolving guidance with automatic retrieval, while model-mediated curation and separate scoring limit correctness warrant",
  "generated-by": "analyse-agentic-system",
  "analysis-run": "AAS-2026-09-26-dynamic-cheatsheet-02",
  "source-identity": "https://github.com/suzgunmirac/dynamic-cheatsheet",
  "reviewed-revision": "5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9",
  "analysis-result": "kb/reports/retained/agentic-system-analysis/AAS-2026-09-26-dynamic-cheatsheet-02/result.md",
  "analysis-result-sha256": "69cf228433d975ac518c02f315ac81aaa26a6b29c3e3db63b932e6a199194cfa"
}
---

# Dynamic Cheatsheet

**Evidence basis:** source code and prompts at commit `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`, frozen 2026-09-26, plus three retained source-native AIME records and selected notebook cells. Code wiring, source claims and historical observations are kept separate.

Dynamic Cheatsheet turns successive model solutions into guidance for later questions. A generator solves a problem using a supplied cheatsheet; a curator can rewrite that sheet from the solution and earlier content. The caller keeps the lasting state and passes it into the next invocation. The benchmark runner supplies sequential scheduling, persistence and restart; the model wrapper alone does not own cross-query storage. The [pinned implementation](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/dynamic_cheatsheet/language_model.py) implements six variants.

| Variant | Context and update |
|---|---|
| Default | Empty cheatsheet; local or native execution state can still exist |
| Cumulative | Whole current sheet supplied to generator, rewritten after its answer; optional same-question rounds |
| Retrieval-synthesis | Similar previous problem/solution pairs and previous sheet feed curation before answering |
| Cumulative-retrieval | Current sheet plus similar examples feed generator, followed by sheet revision |
| Full history | All earlier input/output pairs formatted into context, without learned curation |
| Dynamic retrieval | Top-k similar earlier pairs supplied directly, without synthesis |

Retrieval compares imported question vectors by cosine similarity. It selects previous answers by question similarity, not correctness. Full-history and cumulative paths send all available history or the whole sheet. Retrieval limits pair count; curator prompts suggest a word budget, but these paths do not impose an input-token budget or item-level compaction rule.

The generator and curator share the configured model endpoint. Curation requests criticism, consolidation, duplicate removal, revision, generalization and prioritization. Those are model-mediated operations: extracted text replaces the active sheet, and omitted material can disappear from current guidance even when older checkpoints retain it. Supplying the intended curator template matters; the benchmark uses literal `(empty)` when no curator file is selected. [Curator prompt](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/prompts/curator_prompt_for_dc_cumulative.txt) instructions are not a correctness guarantee.

## What is retained and checked

The analysis finds wired automatic trace-fed writing and later consumption across different problems and within repeated rounds of one problem. The derived content can contain explanations, strategies and executable snippets. Manual authoring is an afforded caller/seed-file operation. A requested checkpoint read is pull; subsequent automatic prompt construction is push. Whole-sheet selection, embedding selection and pre-answer model judgment are distinct selection mechanisms.

A narrow source-native observation establishes retention and recorded delivery: the first sampled AIME record answers 15 against target 315, retains the 15-rectangle conclusion, and its complete sheet appears in the next recorded generator prompt. This demonstrates that mistaken material can survive curation. It does not establish that the next model followed it or that memory caused a later mistake. See the [pinned trace](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/results/AIME_2024/gpt-4o_DynamicCheatsheet_Cumulative.jsonl) and exact-result record CLM-4.

The [benchmark runner](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/run_benchmark.py) evaluates answers after adopting the new sheet. Dataset targets or arithmetic constraints act as answer oracles for reported scores; their results do not veto memory admission or feed the next curator call. An opening cheatsheet tag is enough for extraction. Accuracy reporting therefore supplies a narrower warrant than the template's request to preserve verified solutions.

## Execution and recovery boundaries

Local model-requested Python runs in a subprocess with inherited host privileges and a timeout. The recursion limit is checked after execution, so the final-round warning is not a hard execution prohibition. Provider-native execution follows a separate path: OpenAI reuses a container handle; Claude enables a per-request tool. Hidden provider payloads and retention are uninspected, so the memory profile retains partial coverage rather than classifying them from returned text. Benchmark expression evaluation is another execution path; disabling generator code does not disable it.

Checkpoint resume reloads earlier outputs and the latest sheet, then skips completed positions. Its selected argument checks do not guarantee corpus/order/vector alignment, and it does not restore the native container. This supports restart from saved text, not equivalent replay of all runtime state.

## Learning and epistemic limits

The strongest inspected contribution is persistent derived guidance supplied across problems, with an observed historical example. The source reports benchmark improvements; this analysis does not reproduce their design or isolate memory, extra model calls, code execution and criticism. Trace learning is wired under the memory-comparison definition. Improved capacity attributable to criticism and faithful use of recalled content remain separate, unresolved findings.

Localized theory content is observed, and application, criticism and retention form a wired theory-building path under the intended prompts. The sampled artifacts do not establish a complete observed criticism episode. Computational progression and reflection on earlier problem-solving strategies are wired; reflection on the builder's own static method templates is uninspected. These properties do not imply observed self-improvement.

## Scope

The boundary is the Dynamic Cheatsheet workflow and its benchmark caller, including every variant and invoked execution interface. Independent bundled-client chat/web-search APIs, provider internals, external-paper evidence and unsampled experiments are excluded. Historical logs lack a proven generating-code revision. A retained criticism-and-revision trace would strengthen the theory-path finding; controlled recalled-content interventions would strengthen activation and benefit claims; provider payload evidence would resolve partial profile coverage.

The [exact retained analysis](../../reports/retained/agentic-system-analysis/AAS-2026-09-26-dynamic-cheatsheet-02/result.md) contains canonical records, source quotations, both lenses and the per-value comparison profile.

---

- [Theory builder](../../notes/definitions/theory-builder.md) — defined-in: the four independently assessed conditions
- [Reflective system](../../notes/definitions/reflective-system.md) — defined-in: self-representation and its two-way behavioral connection
