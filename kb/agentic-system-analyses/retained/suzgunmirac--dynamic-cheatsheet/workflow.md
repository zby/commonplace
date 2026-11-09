---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Dynamic Cheatsheet cumulative benchmark workflow: generator-curator handoffs, extraction admission, scoring, delivery and continuation."
run-id: AAS-2026-10-20-dynamic-cheatsheet-523b6948294d-01
reviewed-boundary: "5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9"
---

# Dynamic Cheatsheet workflow report

## Workflow account

### Selected workflow and evidence

This account follows one cumulative benchmark example through solving, memory replacement, scoring and checkpointing, then the handoff to the next example. This workflow was selected because it closes the shipped producer–maintenance–consumer loop rather than ending at the library return. It uses `DynamicCheatsheet_Cumulative` with the shipped generator and cumulative curator templates explicitly supplied. The CLI default curator template is `(empty)`, so this account does not attribute the curator's instructions to an invocation that omits that path. The baseline is [RT-RTE-benchmark-cycle](runtime.md#rt-rte-benchmark-cycle) and [RT-RTE-cumulative-update](runtime.md#rt-rte-cumulative-update).

Evidence is SRC-1 implementation and doctrine/design at the frozen boundary. Inspection covered `run_benchmark.py`, the cumulative branch of `dynamic_cheatsheet/language_model.py`, `dynamic_cheatsheet/utils/extractor.py` and both relevant prompts. These paths were already included in the supplied boundary/runtime; no source or coverage expansion is introduced. No target execution or historical result inspection was performed. The trace below establishes implemented handoffs and requested behavior, not successful solving or improved later performance.

### Request and delegation

The operator selects task, model, approach, prompts and generation settings. The driver loads the dataset, optionally shuffles it with seed 10, initializes an empty or file-supplied sheet, and constructs a numbered question. It calls `advanced_generate` with that question, current sheet, templates and execution settings. Dataset `target` stays in the driver and is not supplied to either model role through this call (SRC-1, `run_benchmark.py`; [RT-RTE-benchmark-cycle](runtime.md#rt-rte-benchmark-cycle)).

Python, not a model planner, owns the sequence. In each of at least one configured rounds, it substitutes the question and sheet into the generator template and creates a fresh one-user-message history. On later rounds it can append earlier extracted answers to the supplied sheet. The generator is asked to identify applicable reference strategies, check its work and emit an answer tag; it does not choose the curator's invocation or the next dataset item (SRC-1, `dynamic_cheatsheet/language_model.py`, `prompts/generator_prompt.txt`; [RT-BAP-reference-context](runtime.md#rt-bap-reference-context)).

The generator may request a local Python continuation. Its output and execution transcript can then become curator input; execution errors can be returned to the generator for another attempt. This is bounded continuation, not an independent reviewing worker. The local execution path has ambient privileges and its depth check follows execution, so neither the prompt's last-round warning nor the execution flag supplies a whole-system isolation guarantee. Native-provider execution is an alternate path. Those mechanics and limits are established by [RT-RTE-local-execution](runtime.md#rt-rte-local-execution) and [RT-RTE-provider-execution](runtime.md#rt-rte-provider-execution).

### Curator handoff and verification

After answer extraction, Python calls the same configured model/client in a separate curator context. The handoff supplies the current question, full generator output and previous sheet, not the generator's entire internal state or an expected answer. The curator receives twice the generator's output-token allowance and local execution is disabled for this call (SRC-1, `dynamic_cheatsheet/language_model.py`). The roles therefore separate context and requested work, not model identity or independent ground truth.

The curator prompt requests correctness assessment, preservation of useful material, synthesis of reusable examples, and usage counters. That is a model review request, not evidence that each proposed entry was tested. Python then extracts a replacement sheet; it does not read a correctness verdict or compare the proposal with dataset targets before accepting it. The supporting request and extraction passage are retained in [RT-RTE-cumulative-update](runtime.md#rt-rte-cumulative-update).

Two verification layers must therefore be kept separate. Curator review may influence the content it proposes, but is not a software-enforced correctness gate. Task scoring uses a reference target or task-specific arithmetic/rule checks only after the driver has received the updated sheet. A wrong answer can increment no correctness count while its associated memory update is still carried forward. The scorer cannot veto that update on this path (SRC-1, `run_benchmark.py`; [RT-RTE-score-answer](runtime.md#rt-rte-score-answer)).

### Rejection and recovery path

A concrete failure branch exists for an unformatted curator response. If it has no opening `<cheatsheet>` tag, `extract_cheatsheet` returns the old sheet. The generator's answer can still be returned and scored: failed memory extraction does not reject the entire example. Conversely, a missing closing tag does not force rejection because splitting on an absent closing delimiter returns the remaining text. An empty tagged sheet can also replace prior content. These are delimiter rules, not semantic validation (SRC-1, `dynamic_cheatsheet/utils/extractor.py`; [RT-RTE-cumulative-update](runtime.md#rt-rte-cumulative-update)).

Accepted replacement is whole-sheet replacement. The prompt warns that omitted content will be lost; earlier versions may remain in driver logs, but no automatic semantic rollback follows a bad score. The recovery owner differs by failure: extraction preserves the old sheet on the missing-opening-tag branch; provider retries belong to the client; interrupted benchmark continuation belongs to the driver. Provider retry exhaustion raises rather than yielding a completed example, and retries do not guarantee idempotent tool effects ([RT-RTE-cumulative-update](runtime.md#rt-rte-cumulative-update), [RT-RTE-benchmark-cycle](runtime.md#rt-rte-benchmark-cycle); SRC-1, `text_generation/simple_unified_client.py`).

### Delivery and next consumption

The library returns the final round's answer, full generator output, extracted sheet, previous answers and per-round steps. The step log contains generator prompt/output and old/new sheets, not a dedicated field retaining the full curator response (SRC-1, `dynamic_cheatsheet/language_model.py`). Its final answer is the generator answer, not a curator-corrected answer. The exact returned identity is [RT-OBJ-output-dict](runtime.md#rt-obj-output-dict).

At driver level, delivery has two stages: the in-memory envelope is returned, then a scored example is persisted. The driver appends that envelope with input and target, updates the current sheet, prints the answer and score totals, and rewrites the output JSONL after each example. At normal termination it writes once more and reports the result location. Only the extracted sheet crosses from curator work into the next generator context; the curator context is discarded. The prior full generator output is separately accumulated by the driver, although cumulative generation does not retrieve that corpus as an extra reference source (SRC-1, `run_benchmark.py`, `dynamic_cheatsheet/language_model.py`).

Continuation reloads output rows, restores the last sheet and previous generator outputs, and skips the saved row count. It checks selected arguments, but not all settings, dataset identity or prompt contents. JSONL rewriting is non-atomic and occurs after scoring, so evaluation failure or an interrupted write can prevent durable delivery of the newest update. This is best-effort checkpoint recovery, not an exactly-once transaction or exact replay guarantee ([RT-RTE-benchmark-cycle](runtime.md#rt-rte-benchmark-cycle); SRC-1, `run_benchmark.py`). No observed execution establishes that these recovery paths succeeded in a particular run.

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

#### On [RT-RTE-cumulative-update](runtime.md#rt-rte-cumulative-update)

Workflow handoff: Python delegates solution production and reference maintenance as separate contexts on the same client. Only the extracted replacement enters the next generator invocation; raw curator analysis is not a dedicated returned step field. This limits reconstruction of why a retained entry was selected. The generator's answer remains the delivered answer even if the curator questions it. SRC-1 implementation, `dynamic_cheatsheet/language_model.py`.

> "generator_output": generator_output,
> "generator_answer": generator_answer,
> "current_cheatsheet": current_cheatsheet,
> "new_cheatsheet": new_cheatsheet,
> --- `dynamic_cheatsheet/language_model.py:442-445`

#### On [RT-RTE-benchmark-cycle](runtime.md#rt-rte-benchmark-cycle)

Workflow delivery boundary: persistence follows generation, memory handoff and scoring. A scorer rejection is an evaluation result, not a memory-admission rejection. The checkpoint is written only after that evaluation path completes. SRC-1 implementation, `run_benchmark.py`.

> if result:
>     correct_so_far += 1
> total_so_far += 1
> --- `run_benchmark.py`

> # Save the outputs to a file after each example (for crash recovery)
> write_jsonl(args.save_path_name, outputs)
> --- `run_benchmark.py`
