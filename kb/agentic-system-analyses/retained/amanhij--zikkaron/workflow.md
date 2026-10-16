---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Zikkaron workflow account: the shipped LoCoMo retrieval, answer generation, judging and report-delivery driver."
run-id: AAS-2026-10-15-zikkaron-0102ec63c6e5-01
reviewed-boundary: dda34a5d903d04ecb5517af214d437873c833302
---

# Zikkaron workflow report

## Workflow account

This account selects the shipped LoCoMo evaluation workflow because it joins memory production, retrieval, model answer generation, verification and report delivery in one executable driver. It is a bounded evaluation mode, not the ordinary Claude Code task loop. The enclosing Python driver owns progression; the generation and judging models perform separate assigned computations rather than independently scheduling agents. Its referent is already declared as [RT-RTE-evaluation-mode](runtime.md#rt-rte-evaluation-mode), so this member adds workflow findings without declaring a duplicate route.

Evidence is static implementation from SRC-1 at the reviewed commit. Added inspection covers the prompt templates, generation/judge handoffs, per-question exception handling, aggregation, JSON output and CLI dispatch in `benchmarks/run_locomo_jscore.py`, and the paired-turn insertion path in `benchmarks/test_e_locomo.py`. No dataset, model response, completed report or execution trace was supplied. The trace below establishes wiring, not a successful run or reliable correctness.

### Request and preparation

The operator starts the benchmark CLI with provider/model choices, conversation indexes, retrieval/context limits, settings overrides and an output path. `main` parses these into `run_eval`; `--f1-only` disables model judging but retains generation and automatic F1. This is an operator-selected bounded dataset evaluation, not an open task delegated to the ordinary memory service (SRC-1, `benchmarks/run_locomo_jscore.py`; [RT-RTE-evaluation-mode](runtime.md#rt-rte-evaluation-mode)).

The driver loads the dataset, warms embeddings and creates storage and a knowledge graph for each selected conversation that has QA items. It removes an existing benchmark `memory.db` at that conversation's fixed temporary path before ingesting. The selected insertion path requests observation mode while leaving paired-turn mode at its default. Adjacent turns become reformulated text with session/speaker tags, a directory label, embeddings and a parsed date when available; odd final turns are stored singly. Software admits these records directly through storage, not through `remember`'s novelty gate or per-memory human approval. This is dataset preparation, not a judgment-driven production update (SRC-1, `benchmarks/test_e_locomo.py`, `benchmarks/run_locomo_jscore.py`). The consequential write call is:

> mem_id = storage.insert_memory(mem_data, embeddings_engine=embeddings, settings=settings)
> --- `benchmarks/test_e_locomo.py:159-226`

### Retrieval and generation handoff

For each nonempty question, the driver asks HippoRetriever for up to the requested retrieval count. It then passes results to `generate_answer`, which supplies only the first `top_k_context` memory contents, with available creation dates, plus the question and shipped generation instructions. Empty retrieval becomes an explicit no-relevant-memories marker. The gold answer is held by the driver for scoring, not supplied by this generation handoff. The model is requested to use only provided context and return a brief answer; this instruction does not enforce factual grounding (SRC-1, `benchmarks/run_locomo_jscore.py`; model resolution limits are in [RT-CMP-evaluation-models](runtime.md#rt-cmp-evaluation-models)).

> for i, mem in enumerate(retrieved_memories[:top_k_context], 1):
> --- `benchmarks/run_locomo_jscore.py`

> context = "\n\n".join(context_parts) if context_parts else "(No relevant memories found)"
> user_msg = GENERATION_USER.format(context=context, question=question)
> --- `benchmarks/run_locomo_jscore.py`

This is a context boundary by value: the generation call receives formatted selected text, not the full database, ingestion transcript or a reloadable reference. The driver does not give it an iterative retrieval/tool loop. A fresh call is constructed per question; provider-internal context behavior remains outside the inspected boundary. This narrower handoff is the workflow-specific selection step after retrieval, not proof that every retrieved candidate reaches the model (SRC-1, `benchmarks/run_locomo_jscore.py`).

### Verification and negative judgment

The driver computes F1 against the dataset gold answer. Unless disabled, it then delegates to the judge with the question, gold answer and generated answer. The judge receives no retrieved context in that template. Its requested criterion is generous semantic agreement, including partial topical answers; the expected-answer oracle is the dataset answer, while the model interprets the comparison policy. These are two score channels, not a code-enforced truth test (SRC-1, `benchmarks/run_locomo_jscore.py`; [RT-RTE-evaluation-mode](runtime.md#rt-rte-evaluation-mode)).

A negative judgment affects the recorded score, not whether the answer is delivered or retried:

> j_correct = judgment["label"].upper() == "CORRECT"
> j_reasoning = judgment.get("reasoning", "")
> --- `benchmarks/run_locomo_jscore.py`

The same sample construction and append follow either label. Thus the judge can classify an answer as wrong but does not veto a production change or send a repair request to the generator. Operator selection starts the experiment; no per-answer human approval occurs in this driver. This inspected scoring loop does not establish criticism and revision of the memory method.

### Failure recovery and delivery

The driver owns local failure continuation. A generation exception substitutes `No information available.` and still scores that text. A judge exception records false correctness and an error reason. Malformed judge JSON falls back to a substring check for `CORRECT`; otherwise it records `WRONG`. That fallback is permissive parsing, not a second independent verifier (SRC-1, `benchmarks/run_locomo_jscore.py`).

> except Exception as e:
>     log(f"  [ERROR] Gen Q{qi}: {e}")
>     generated = "No information available."
> --- `benchmarks/run_locomo_jscore.py`

> except (json.JSONDecodeError, IndexError):
>     if "CORRECT" in raw.upper():
>         return {"label": "CORRECT", "reasoning": raw}
>     return {"label": "WRONG", "reasoning": raw}
> --- `benchmarks/run_locomo_jscore.py`

These branches preserve progression rather than regenerate a rejected answer. They can conflate infrastructure failure with answer error in aggregate results. Retrieval, ingestion and final file-write failures are outside these per-model-call exception handlers; the inspected `main` adds no whole-run retry, resume or rollback wrapper. This conclusion is scoped to this driver, not all provider-specific recovery behavior (SRC-1, `benchmarks/run_locomo_jscore.py`).

The driver accumulates per-question records including the question, gold/generated answers, F1 and judge outcome/reason, then computes category and overall aggregates. Delivery at the API boundary is the returned output dictionary; with `output_path`, it also writes JSON and logs completion. CLI `main` invokes this writing path and returns zero after `run_eval` returns. A wrong answer is retained in the report rather than withheld. File-write success and API return are code-level delivery conditions, not evidence that this frozen workflow actually completed:

> with open(output_path, "w") as f:
>     json.dump(output, f, indent=2)
> log(f"Results written to {output_path}")
> --- `benchmarks/run_locomo_jscore.py`

The report can persist evaluation records for an operator. The inspected loop does not feed judge results into another generation round, production memory policy or model-weight update. Later use of a saved report is uninspected; no performance gain or exercised self-improvement follows from producing it (SRC-1, `benchmarks/run_locomo_jscore.py`; [RT-RTE-evaluation-mode](runtime.md#rt-rte-evaluation-mode)).

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-evaluation-mode](runtime.md#rt-rte-evaluation-mode)

- Workflow coordination: Python `run_eval` owns the sequence and per-conversation/per-question iteration; model calls return answer or judgment values and do not schedule subsequent steps.
- Handoff boundary: generator input is the question and the first configured number of retrieved memory contents with dates; judge input is question, gold answer and generated answer, without retrieval context.
- Verification consequence: `WRONG` reduces the recorded correctness result but does not reject report delivery or initiate answer repair.
- Recovery ownership: the driver substitutes values after generation/judge exceptions and continues; ingestion, retrieval and output-write failures are not covered by those handlers.
- Delivery condition: return the aggregate/per-query dictionary and, when requested, successfully write JSON. Observed completion remains uninspected.
