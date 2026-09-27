---
{
  "type": "types/note.md",
  "description": "Dynamic Cheatsheet at a fixed source pin: recurrent cheatsheet curation, retrieval alternatives, execution boundaries and limits of learning evidence",
  "generated-by": "analyse-agentic-system",
  "analysis-run": "AAS-2026-09-27-dynamic-cheatsheet-03",
  "source-identity": "https://github.com/suzgunmirac/dynamic-cheatsheet",
  "reviewed-revision": "5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9",
  "analysis-result": "kb/reports/retained/agentic-system-analysis/AAS-2026-09-27-dynamic-cheatsheet-03/result.md",
  "analysis-result-sha256": "7a8ebe9a5316b00937ba088177b0dd4890fff697c1bc2700342331095f967d57"
}
---

# Dynamic Cheatsheet

Evidence basis: Python implementation, shipped prompts and README at [commit 5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9](https://github.com/suzgunmirac/dynamic-cheatsheet/tree/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9), inspected 2026-09-27. No target execution, historical result analysis or controlled experiment was performed.

Dynamic Cheatsheet is a sequential model-calling workflow that carries problem-solving material into later questions. Its main mechanism is a replaceable text cheatsheet: a generator solves a problem using the current sheet, then a curator call to the same configured model rewrites it from the solution and prior sheet. The benchmark saves both solutions and sheets and can restore them after restart. Direct callers must pass the returned memory into later calls themselves.

The adaptation path is implemented. Whether a particular strategy was criticized, improved and responsible for a later gain remains uninspected. The [exact analysis](../../reports/retained/agentic-system-analysis/AAS-2026-09-27-dynamic-cheatsheet-03/result.md) retains the runtime records, mandatory memory analysis, fourteen-axis profile and epistemic assessment.

## Runtime and memory

The caller chooses the provider/model, templates, approach and execution flags. Python owns branch selection and sequencing; the model supplies solutions and curation judgments. The generator receives memory as reference material in a user message. This is advisory context, not a verified rule system.

| Approach | Retained material and next consumer |
|---|---|
| Cumulative | Entire current sheet goes to the generator; a post-answer curator replaces it. Additional rounds can revisit the same problem. |
| Retrieval-synthesis | Current-input embeddings select prior solutions; a curator receives those, the **previous sheet** and next question before answering. Its sheet is carried forward. |
| Cumulative-retrieval | Generator receives both sheet and selected examples, followed by one curator update. This branch does not repeat the cumulative refinement-round loop. |
| Direct retrieval | Prior solutions selected by cosine similarity go directly to the generator. |
| Full history | All prior input/output pairs are formatted into context without curation. |
| Default | The sheet slot is empty; raw logging alone is not learned memory. |

The selector ranks earlier **questions**, then supplies their generated solutions; similarity is not a correctness score. Top-k limits example count, not token volume. Whole-sheet and full-history input have no hard token-budget check. Curator output limits and the suggested 2000–2500 words constrain production rather than the complete next input.

Cheatsheets and trajectories live in strings/lists and JSONL files; embeddings are CSV-backed numerical access metadata. Trace-derived rewriting followed by later delivery supports a wired trace-learning classification, including within-problem rounds and reuse across distinct questions. This technical comparison value does not establish improved capacity through criticism. Code snippets, deduplication, consolidation and usage-based prioritization are requested by prompts; reliable execution of those operations was not observed.

The separate provider-client chat API affords retained conversation and caller replacement/reset. The benchmark uses a different message interface and does not secretly reuse that chat history. Optional OpenAI code execution reuses a service-container handle; its retained payload and retrieval behavior remain opaque. The profile preserves partial coverage for that boundary.

## Admission and evaluation

The curator is asked to assess solution correctness, preserve useful content and replace inferior methods. However, the code accepts text extracted after an opening cheatsheet tag; it does not validate truth, entry identity, usage counts or a separate critique verdict. Missing opening markup triggers fallback; a missing closing tag or empty block can still be admitted. Whole-string replacement can drop previous material. A rationale survives only if it is inside the extracted sheet, although subsequent calls receive any such retained explanation.

Benchmark scoring happens **after** the returned sheet has been adopted. Dataset reference answers or arithmetic constraints judge the answer, update counters and support reporting; they do not veto the memory update or feed the next curator. Thus label-free updating coexists with reference-based benchmark assessment. README accuracy gains remain attributed claims in this analysis, not reproduced results or identified effects of curation, retrieval or tool use.

## Execution and recovery boundaries

Generated Python can run locally when it satisfies the wrapper's flag/fence condition. The helper launches a subprocess under the current process environment:

> process = Popen(["python3", temp_file.name], stdout=PIPE, stderr=PIPE)
>         stdout, stderr = process.communicate(timeout=timeout)
> --- `dynamic_cheatsheet/utils/execute_code.py:83-84` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

Its timeout is not a sandbox. The recursive depth check occurs after code execution, so the “last round” warning does not prevent one additional flagged execution. Provider interpreter mode disables the local generation-time subprocess path and instead requests a native tool; provider isolation and hidden state are external contracts. Separately, arithmetic benchmark evaluators use Python `eval`, so disabling generation-time code execution does not cover every execution path.

Checkpoint continuation restores the latest sheet and prior outputs but compares only selected configuration fields. It assumes compatible dataset order and does not pin actual prompt bytes, embeddings or every retrieval/native-tool setting. It recreates rather than restores the provider container. Historical checkpoint sheets do not provide an automatic semantic rollback policy.

## Scope

The source establishes recurrent context production and delivery, computational scheduling and an improvement-directed update pathway. Under the [theory-builder definition](../../notes/definitions/theory-builder.md), localized strategies and content-guided use are afforded; actual formulated criticism and its retained effect on another round remain uninspected. Wired memory iteration does not close those missing links. Learning, exercised reflective or autonomous theory-building, and successful self-improvement are therefore not established by this static pass.

Candidate-linked traces of strategy use, criticism, revision and subsequent use would strengthen that assessment. A controlled memory intervention with matched models and execution tools would address dependence and benefit. Provider internals, historical outputs, the external paper, live datasets and generic web-search branches remain outside the inspected evidence for these conclusions.
