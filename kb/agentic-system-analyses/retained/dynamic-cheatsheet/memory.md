---
type: agentic-system-analyses/types/agent-memory-analysis-report.md
description: "Memory mechanisms of Dynamic Cheatsheet across cumulative text, retrieved traces, and benchmark checkpoints"
run-id: AAS-2026-10-04-dynamic-cheatsheet-01
source-identity: https://github.com/suzgunmirac/dynamic-cheatsheet
reviewed-boundary: "5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9"
report-status: complete
---

# Dynamic Cheatsheet memory report

## Boundary and evidence

This report covers the selected whole-system memory/knowledge/context-engineering boundary for Dynamic Cheatsheet (DC) at commit `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`. Included are shipped prompt templates, six approach implementations, benchmark state handling, file checkpoint/resume, precomputed retrieval vectors, the caller example, and later evaluator notebook. The included evaluation code matters because it measures answers but does not decide whether an answer or memory update is admitted. Excluded are provider internals and live calls, remote dataset content, historical `results/` artifacts, and vector provenance/content quality. I read implementation and design files directly under the registered source root; the supplied runtime report is provisional context, not operation evidence. No target, notebook, provider, or service was executed. The only evidence layer here is `implementation` and `doctrine/design`; actual model behavior, deployed retention, answer correctness, activation, and benefit remain unobserved.

Coverage of memory routes (the baseline routes are supplied runtime records):

| Entry point or operation | Source path | Coverage | Scope limit |
|---|---|---|---|
| Benchmark caller carry-forward, evaluation, and checkpoint/resume | `run_benchmark.py` | RT-RTE-benchmark-invocation, RT-RTE-checkpoint-resume | Code establishes intended read/write order, not a successful run or actual retained file. |
| Cumulative curation and extraction | `dynamic_cheatsheet/language_model.py`; `dynamic_cheatsheet/utils/extractor.py`; `prompts/curator_prompt_for_dc_cumulative.txt` | RT-RTE-cumulative-update | Model-directed curation is not a code-enforced correctness test; output behavior is unobserved. |
| Retrieval, retrieval synthesis, cumulative plus retrieval, full history | `dynamic_cheatsheet/language_model.py`; `run_benchmark.py`; `prompts/curator_prompt_for_dc_retrieval_synthesis.txt` | RT-RTE-retrieval-context, RT-RTE-full-history | Vector provenance, data quality, and actual selected examples are not assessed. |
| Later result-file scoring consumer | `EvaluatingResults.ipynb`; `dynamic_cheatsheet/utils/evaluation.py` | RT-RTE-benchmark-invocation, RT-RTE-checkpoint-resume | Notebook code is read without execution; historical result files are excluded. |
| Interactive caller-managed carry-forward | `ExampleUsage.ipynb` | RT-RTE-cumulative-update | Example cells and saved outputs do not establish a new live operation. |
| Shipped generator context use | `prompts/generator_prompt.txt` | RT-OBJ-cheatsheet, RT-OBJ-retrieval-vectors | Prompt instruction establishes guidance, not activation. |

The source register is in the frozen boundary. Additional direct coverage within its registered Git identity: `dynamic_cheatsheet/language_model.py`, `dynamic_cheatsheet/utils/extractor.py`, `dynamic_cheatsheet/utils/evaluation.py`, `run_benchmark.py`, both curator templates, `generator_prompt.txt`, `ExampleUsage.ipynb`, and `EvaluatingResults.ipynb`. These paths are at the registered commit. No runtime evidence supports operation claims.

## Core ideas

DC exposes several different context paths behind `advanced_generate`. The cumulative path gives a plain-text sheet to the generator, then asks a model curator to replace it. Full history supplies all prior input/full-output pairs without curation. Retrieval ranks prior pairs by cosine similarity over shipped vectors and inserts up to `retrieve_top_k`; retrieval-synthesis asks a curator to synthesize those pairs for the current question, while cumulative-retrieval combines them with a cumulative sheet and separately updates that sheet. The default path has no persistent sheet. In the benchmark runner, the returned `final_cheatsheet` becomes the next iteration's input state.

A cumulative sheet is a derived, model-authored text state. Its write admission is a parser condition: a response with a `<cheatsheet>` block replaces the old value; missing/malformed tags preserve the fallback string. The cumulative curator prompt asks it to assess correctness and retain tested, useful material, but no answer evaluator is consulted before the parser accepts a tagged result. Benchmark scoring happens after `final_cheatsheet` is assigned and only increments counters. Thus scoring does not validate, reject, or roll back memory writes.

Retrieval and full-history material are raw prior generator outputs paired with inputs, rather than verified memory entries. Their later selection can be automatic: similarity ranking for retrieval, all earlier pairs for full history. The synthesis prompt describes a curation step but supplies the previous sheet and retrieved examples as text; its output is accepted by tag extraction. Missing tags fall back to the retrieved-pairs string for that call. The runner nevertheless carries the returned value forward, where it is passed to the next synthesis curator as prior sheet; the current retrieved-pairs string is newly rebuilt for each question. For cumulative-retrieval, by contrast, generation sees cumulative sheet plus retrieved examples and its post-answer curator updates the cumulative sheet.

The JSONL checkpoint contains the full per-example result, including inputs, target, generation outputs, steps and final sheet. Resume loads all rows and uses the most recent final sheet, when non-null, plus prior full outputs; it skips indices below the saved row count. This is file-based persistence controlled by the caller. The evaluator notebook reads result JSONL later for scoring but does not feed scores back into any memory route. Prompt claims of reliable, proven, or successful use are instructions, not retained evidence of those properties.

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-generation-traces — Prior input and output traces

- Source-native identity: `questions`/`original_input_corpus` paired with `generator_outputs_so_far`; runner accumulates each complete `final_output` and uses the pairs for history assembly or retrieval.
- Representational form: natural-language input and model-output text; full outputs may include reasoning, code, and answer text.
- Storage substrate: in-memory Python lists during a run; the result JSONL also stores each row's input and generation outputs.
- Lineage: dataset inputs and unfiltered raw generator outputs. Retrieval vectors select trace indices; full-history formatting or retrieval synthesis can form derived prompt contexts. Task evaluation does not filter the traces before accumulation.
- Memory consumers and authority: Python selects or concatenates; the generator consumes delivered text, while retrieval-synthesis curator can consume selected pairs. The text is model guidance; no correctness authority is conferred by its inclusion.
- Evidence: [SRC-1: `run_benchmark.py`; `dynamic_cheatsheet/language_model.py`]. Distinct identity from `RT-RTE-retrieval-context` and `RT-RTE-full-history`: those records are routes that select or format the trace pairs; this record is the retained input/output material consumed by either route.

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On RT-OBJ-cheatsheet — Caller-carried cheatsheet

- Storage substrate: Python string in the active runner; serialized as `final_cheatsheet` in each result JSONL row, or retained by a caller such as the example notebook.
- Representational form: natural-language text interpreted through model prompts.
- Lineage: initial text is `(empty)` unless an initialization file supplies text. Cumulative updates derive from the current question, raw generator output, and prior sheet; extraction accepts the first tagged block or preserves the old string. Retrieval-synthesis derives a per-question context from retrieved pairs and the prior sheet. Cumulative-retrieval derives the returned sheet from prior cumulative text and the question/output. These derivations do not attach correctness evidence.
- Memory consumers and behavioral authority: generator model consumes the text when inserted into its prompt; it is model guidance with no enforced behavior. The curator consumes old sheet and current raw answer when drafting an update. Runner assigns any returned sheet as next state; tag parsing, rather than answer correctness, determines replacement.
- Raw versus derived material: this object is derived text. The raw prior question/output pairs used by retrieval and full history are separate, uncurated traces.
- Write agency, curation, trace learning and source: model curator proposes sheet content; local code performs tag extraction and automatic replacement. The cumulative template directs retention, accuracy review, refinement, and usage counts; those rules are not executed checks. Trace-fed derivation exists, but improved future capacity is not evidenced. Inputs and answers originate in the benchmark dataset and model output.
- Read-back trigger, selector inputs, selected retained parts, budget, persistence, delivery, later consumer, status and limits: next benchmark example or caller invocation supplies the string directly, without content ranking; synthesis reads it as prior-sheet input. There is no sheet-size budget enforced in code, though the synthesis prompt suggests a word range. It persists in process and in JSONL until files or caller state change. Delivery is prompt text. Wiring is present; activation and benefit are unobserved.

> new_cheatsheet = extract_cheatsheet(response=cheatsheet_output, old_cheatsheet=current_cheatsheet)
> cheatsheet = new_cheatsheet
> --- `dynamic_cheatsheet/language_model.py`

> if "<cheatsheet>" in response:
>     try:
>         txt = response.split("<cheatsheet>")[1].strip()
>         txt = txt.split("</cheatsheet>")[0].strip()
>         return txt
>     except:
>         return old_cheatsheet
> else:
>     return old_cheatsheet
> --- `dynamic_cheatsheet/utils/extractor.py`

#### On RT-OBJ-retrieval-vectors — Precomputed retrieval vectors

- Storage substrate: committed task-specific CSV files loaded into in-memory NumPy arrays and reordered to dataset order.
- Representational form: dense numeric vectors consumed by cosine similarity; the source does not identify their model or provenance.
- Lineage: shipped vectors are paired to task inputs; no vector update, learning, or refresh is shown. They index raw input/output traces rather than constituting curated textual memory.
- Memory consumers and behavioral authority: Python similarity code selects trace indices. The resulting text pairs, not vector values, are delivered to the generator (and retrieval-synthesis curator). Vector values control selection mechanically; they are not prompt content.
- Raw versus derived material: vectors are static access metadata for trace selection; selected input/output pairs remain raw generation traces.
- Write agency, curation, trace learning and source: no in-boundary authoring or curation route for vectors; their producer is unknown. No trace-fed learning through vector modification is evidenced.
- Read-back trigger, selector inputs, selected retained parts, budget, persistence, delivery, later consumer, status and limits: retrieval approaches use the current and prior input vectors; descending cosine score selects up to `retrieve_top_k` prior pairs. Files persist in the repository. Selected text is delivered in model prompt context. The route is wired, but actual selection, relevance, activation, and effect are unobserved; vector content and provenance were not analyzed.

> similarities = cosine_similarity([current_original_input_embedding], prev_original_input_embeddings)
> top_k_indices = np.argsort(similarities[0])[::-1][:retrieve_top_k]
> top_k_original_inputs = [original_input_corpus[i] for i in top_k_indices]
> --- `dynamic_cheatsheet/language_model.py`

#### On RT-RTE-cumulative-update — Cumulative generation and curation

- Storage substrate: immediate returned sheet is a Python string; the runner carries it in memory and stores it in JSONL.
- Representational form: derived natural-language text.
- Lineage: each round's curator sees the current question, raw generator answer, and prior sheet. A tagged proposed sheet replaces the prior one without consulting task evaluator output. The returned sheet is read on the next example or after resume.
- Memory consumers and behavioral authority: the generator receives the sheet as prompt context; the model is asked to use it, but its influence is unobserved. The curator has proposal authority in natural language; extraction grants the code-level state transition.
- Raw versus derived material: the answer is a raw trace supplied to a model curator; the resulting sheet is derived. The source does not show stored rationale for why an item survived or was removed, and no later consumer reads curator reasoning as a separate artifact.
- Write agency, curation, trace learning and source: model proposes; code accepts any parseable tagged block. Prompt guidance requests correctness assessment, reuse, and count updates, but there is no independent checker, rejection path for a tagged block, or rollback within the route. This is trace-fed transformation; learning or improved capacity is not established.
- Read-back trigger, selector inputs, selected retained parts, budget, persistence, delivery, later consumer, status and limits: each later query receives the whole string, with no selector or size check. The prompt suggests a compact sheet but code does not enforce a budget. It remains in process or saved JSONL. Prompt delivery is wired; behavior change and benefit are unobserved.

> Before updating the cheatsheet, however, you should first assess the correctness of the provided solution and strategically incorporate code blocks, insights, and solutions into the new cheatsheet.
> --- `prompts/curator_prompt_for_dc_cumulative.txt`

> # Save the outputs to a file after each example (for crash recovery)
> --- `run_benchmark.py`

#### On RT-RTE-retrieval-context — Retrieval context selection

- Storage substrate: raw prior generator outputs and paired inputs are held in runner lists, with result rows persisted in JSONL; vectors are loaded from CSV.
- Representational form: raw traces are natural-language input/output text; selection metadata is numeric vectors and similarity scores.
- Lineage: each completed query appends `final_output` to the trace list. Retrieval matches a current input vector against the prior prefix; synthesis can transform selected examples into a text context. Cumulative-retrieval also reads and updates a separate cumulative sheet.
- Memory consumers and behavioral authority: similarity code chooses pair indices; generator receives selected text. In retrieval-synthesis, curator receives selected-pair text and previous sheet, and the generator receives extracted synthesis. In cumulative-retrieval, generator sees both current cumulative sheet and selected pair text; curator afterward updates the cumulative sheet.
- Raw versus derived material: previous full outputs are raw traces, not evaluator-approved solutions. Retrieval-synthesis output and cumulative sheet are derived text. The benchmark evaluator's boolean is used for tallying only, not selection or update admission.
- Write agency, curation, trace learning and source: runner appends model output; no filter screens it for correctness. The retrieval-synthesis curator proposes text based on examples and prior sheet, with tag extraction as the only update parser. This route has trace-fed context derivation but no evidence of learning.
- Read-back trigger, selector inputs, selected retained parts, budget, persistence, delivery, later consumer, status and limits: every retrieval query recomputes similarity over prior vectors, selects up to `retrieve_top_k`, and inserts associated full input/output text. The synthesis curator prompt says to synthesize examples for the next input; its tag failure fallback is the retrieved-pairs text, not the prior sheet. The runner carries the return into the next call as `cheatsheet`, where synthesis sees it as prior-sheet input. In cumulative-retrieval, the next generation receives the updated cumulative sheet. There is no explicit token or byte budget on selected pairs beyond top-k. JSONL enables runner resume; actual selection and effects are unobserved.

> generator_outputs_so_far.append(output_dict["final_output"])
> --- `run_benchmark.py`

> if result:
>     correct_so_far += 1
> total_so_far += 1
> --- `run_benchmark.py`

> data = read_jsonl(file)
> --- `EvaluatingResults.ipynb`

#### On RT-RTE-full-history — Full history context assembly

- Storage substrate: runner's in-memory input corpus and full generator-output list, with completed result rows in JSONL.
- Representational form: raw natural-language trace pairs concatenated as prompt text.
- Lineage: each current invocation assembles all earlier inputs and full outputs in order; no curator, compression, or success filter operates on this route.
- Memory consumers and behavioral authority: Python concatenation controls which traces are included; generator receives the resulting context as prompt text. The generator is guided to use reference material, but activation is unobserved.
- Raw versus derived material: source traces remain raw; the formatted concatenation is a derived access context and is returned as `final_cheatsheet` by this approach.
- Write agency, curation, trace learning and source: runner appends raw model output automatically; there is no content curation or trace learning operation.
- Read-back trigger, selector inputs, selected retained parts, budget, persistence, delivery, later consumer, status and limits: each subsequent query receives every preceding input/output pair, without ranking. The context grows across the run; no code-level budget or expiry is shown. JSONL can support continuation. Prompt wiring is present; token-limit behavior and answer effects are unobserved.

#### On RT-RTE-checkpoint-resume — Checkpoint and resume

- Storage substrate: host filesystem JSONL rows plus a sibling run-parameters JSON file.
- Representational form: JSON-encoded input, target, raw and extracted outputs, steps, and final sheet; readable text fields plus structural keys.
- Lineage: after each evaluated example the runner rewrites accumulated rows. Resume loads all rows, restores the last non-null `final_cheatsheet`, reconstructs prior full outputs, and begins at the saved row count. For retrieval, question order and vectors are reconstructed from the current dataset and vector files, not loaded from the output rows.
- Memory consumers and behavioral authority: runner performs reload and selection; its compatibility check is limited to prompt path, temperature, local execution flag, task, model, approach, and rounds. The model later consumes restored text through the selected approach. The evaluator notebook reads JSONL as a score input, not as live memory state.
- Raw versus derived material: each row retains raw output and the route's returned context/sheet; resume reuses the latter only as state and prior output for retrieval/history.
- Write agency, curation, trace learning and source: runner automatically serializes each row. No validator screens row contents or detected correctness before they are eligible for later history/retrieval. File authorship and filesystem permissions are deployment-dependent.
- Read-back trigger, selector inputs, selected retained parts, budget, persistence, delivery, later consumer, status and limits: continuation path and parameter match trigger load; latest row supplies sheet and all rows supply output history. No expiry, integrity check, content validation, or in-route rollback is shown. Persistence lasts while files remain. Code wires restoration, but actual recovery and effects are not observed.

> last_cheatsheet = outputs[-1].get("final_cheatsheet")
> if last_cheatsheet is not None:
>     cheatsheet = last_cheatsheet
> --- `run_benchmark.py`

## Write side

The default route creates no carried sheet. In cumulative mode, the generator's full response is supplied to a second model call with the question and old sheet. The cumulative prompt asks for correctness assessment, preserving useful content, removing redundancy, and usage counters. These are model instructions. Code does not run an evaluator on that candidate before accepting the first parsable `<cheatsheet>...</cheatsheet>` block. If extraction fails, it returns the prior sheet. The only admission condition is this format parse; there is no explicit model-update rejection or content rollback. The runner's task evaluator runs after state assignment and affects counters, not admission.

Retrieval and full-history routes automatically accumulate each raw `final_output` in the runner list. Full history later concatenates all such outputs with their inputs. Retrieval selects previous pairs using static vectors; no correctness filter applies. Retrieval-synthesis presents selected pairs, next input, and prior sheet to a model curator, then sends extracted text to the generator. If no tagged text is found, the fallback is the selected-pair context. The runner carries the returned value as `cheatsheet`; on the following question retrieval-synthesis reconstructs a fresh pair context and gives the carried value to the curator as `PREVIOUS_CHEATSHEET`. Cumulative-retrieval has a separate flow: it supplies retrieval examples and cumulative sheet together to the generator, then the curator update uses the old cumulative sheet and current answer.

Automatic checkpointing writes the result rows after each evaluation, then once again at run completion. Resume reads stored state and may restore the latest sheet and all prior outputs. There is no memory-item deletion/withdrawal protocol independent of a curator-proposed whole-string replacement or changing the initial sheet/file. A parseable replacement can omit previous material; lost items have no internal history or explanation path shown. The actual artifacts under excluded `results/` were not examined.

> if result:
>     correct_so_far += 1
> total_so_far += 1
> --- `run_benchmark.py`

## Read-back

The read trigger and consumer depend on the selected approach. Cumulative, full-history, retrieval, synthesis, and cumulative-retrieval automatically construct prompt material for the next query in the benchmark; the interactive example demonstrates a caller retrieving `final_cheatsheet` and passing it to the next `advanced_generate` call. A requested direct library call with an arbitrary caller-supplied string is an API affordance; the benchmark is the inspected wiring. The result-file evaluator notebook later reads JSONL for scoring and does not feed its results into later generation.

Cumulative read-back selects the whole returned text with no selector or enforced budget. Full-history reads every prior pair. Retrieval uses current/prior precomputed vectors, cosine ranking and top-k. Retrieval-synthesis passes retrieved examples and prior sheet to a curator and delivers the extracted synthesis to the generator; the runner carries that return into the next call, but it reconstitutes the current retrieval context separately. Cumulative-retrieval delivers both the carried cumulative sheet and currently selected examples, then updates only the cumulative sheet after generation. Context inclusion is implementation-wired. No supplied trace shows actual delivery, model use of the material, answer changes, improvement, or reliable benefit.

Checkpoint resume is an explicit caller-selected load operation, not a background service. It selects the saved last sheet and all saved full outputs, while reloading dataset/vector inputs from current run setup. Its parameter consistency check omits several settings (including retrieval top-k and code interpreter selection); parameter JSON is written but the inspected resume path does not restore all settings from it. Therefore code shows a partial compatibility guard, not artifact integrity or complete configuration identity.

## Integration issues

- `RT-OBJ-cheatsheet`: annotated, not redeclared. The referent is the same caller-carried text object; this report adds its derived lineage, write agency, read-back, and memory-specific limits.
- `RT-OBJ-retrieval-vectors`: annotated, not redeclared. The referent is the same shipped vector object; this report adds its memory role as access metadata and the raw traces selected through it.
- `RT-RTE-cumulative-update`, `RT-RTE-retrieval-context`, `RT-RTE-full-history`, and `RT-RTE-checkpoint-resume`: annotated, not redeclared. These are the same runtime routes; annotations add memory-specific lineage, curation, raw/derived distinction, consumers, and persistence.
- `MEM-OBJ-generation-traces` is distinct from both `RT-RTE-retrieval-context` and `RT-RTE-full-history`: the supplied records are route referents, while this record is the input/output material those routes consume. It spans both route referents, so it records distinct identity rather than `Part of:`. No possible duplicate is indicated.
- No correction to a supplied runtime fact is required. Clarification: retrieval-synthesis carries its returned context forward as the next call's `cheatsheet`, but rebuilds retrieved pairs per question; when extraction finds no tag, its fallback is the current retrieved-pair context, not the prior sheet. This narrows the sense in which that route is cumulative and does not alter the supplied route identity.
- No unresolved source-access or scope issue remains. Actual provider calls, benchmark outcomes, model-dependent curation quality, effect of prompt material, and historic scores remain unknown and limit conclusions as stated above.

## Limitations and checks

The source identity and commit match the frozen boundary. Inspected source remains within the registered Git repository; no alternate revision, execution trace, provider evidence, or historical result artifact was used. This report cannot establish model outputs, correctness of curator decisions, activation, answer quality, improvement, reliability, or deployed retention/access controls. Static embeddings' provenance and individual contents were not analyzed. The analysis method identity is the supplied `jobs/memory.md` and its declared collection, worker, source, record, and type contracts.

Validation: acceptance check passes after replacing the pending marker. It checks form and occurrence, not claim support.
