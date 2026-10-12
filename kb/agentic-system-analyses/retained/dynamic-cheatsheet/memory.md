---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Dynamic Cheatsheet memory: whole-text curation, prior-output retrieval, checkpoint reload and separate client/provider state."
run-id: AAS-2026-10-12-dynamic-cheatsheet-ca0a0b29d273-01
source-identity: "https://github.com/suzgunmirac/dynamic-cheatsheet"
reviewed-boundary: "5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9"
---

# Dynamic Cheatsheet memory report

## Boundary and evidence

The memory boundary includes all six `advanced_generate` branches, shipped generator/curator prompts, benchmark initialization, checkpoint write/reload, notebook carry-forward and evaluation, local execution text, native execution state and the exported client's separate conversation-history operations. Static templates guide memory use but are not themselves use-accumulated memory. The source is SRC-1 at the revision above; its registration and exclusions remain in [boundary](boundary.md#source-register).

Direct reads covered `dynamic_cheatsheet/language_model.py`, `dynamic_cheatsheet/utils/extractor.py`, `run_benchmark.py`, all three `prompts/` text files, notebook source cells, `text_generation/__init__.py`, and the client's `generate`, `generate_from_messages`, Claude text extraction, container/native execution and history methods in `text_generation/simple_unified_client.py`. These supply implementation and doctrine/design evidence. The supplied runtime contributes local executor/scorer implementation findings, not observed operation. No target was executed. Full result payloads, saved notebook outputs, Arrow payloads, embedding production and remote provider internals remain uninspected; no benefit, preservation rate or authenticated execution conclusion is drawn from them.

| Entry point / operation | Source path (SRC-1) | Coverage and remaining limit |
|---|---|---|
| Fresh initialization / supplied text | `run_benchmark.py` | Direct read; [MEM-OBJ-final-cheatsheet](#mem-obj-final-cheatsheet), [RT-RTE-checkpoint-continuation](runtime.md#rt-rte-checkpoint-continuation). Caller selects file; content authorship and human approval unresolved. |
| Default generation | `dynamic_cheatsheet/language_model.py` | Direct read; returns no live cheatsheet, but driver still retains outputs; [MEM-OBJ-final-output](#mem-obj-final-output). |
| Cumulative and cumulative-retrieval update | `dynamic_cheatsheet/language_model.py`, `dynamic_cheatsheet/utils/extractor.py`, `prompts/curator_prompt_for_dc_cumulative.txt` | Direct reads; [RT-RTE-cumulative-curation](runtime.md#rt-rte-cumulative-curation), [MEM-OBJ-final-cheatsheet](#mem-obj-final-cheatsheet), [MEM-OBJ-steps](#mem-obj-steps). Whole replacement, not validated item editing. |
| Direct retrieval, retrieval-synthesis, hybrid retrieval, full history | `dynamic_cheatsheet/language_model.py`, `run_benchmark.py`, `prompts/curator_prompt_for_dc_retrieval_synthesis.txt` | Direct reads; [RT-RTE-context-selection](runtime.md#rt-rte-context-selection), [MEM-OBJ-retrieved-selection](#mem-obj-retrieved-selection). Embedding provenance unresolved; prevents selector-quality conclusions. |
| Next round / next question / notebook repeated problem | `dynamic_cheatsheet/language_model.py`, `run_benchmark.py`, `ExampleUsage.ipynb` | Direct source reads; [RT-BAP-cheatsheet-context](runtime.md#rt-bap-cheatsheet-context). Notebook source shows explicit carry-forward, not verified improvement. |
| Checkpoint write / positional reload | `run_benchmark.py` | Direct read; [RT-RTE-checkpoint-continuation](runtime.md#rt-rte-checkpoint-continuation), all four output-part records below. Nonatomic persistence and partial configuration checking limit recovery. |
| Online / retained-output scoring | `run_benchmark.py`, `EvaluatingResults.ipynb`, `dynamic_cheatsheet/utils/evaluation.py` | Driver/notebook directly read; utility via [RT-RTE-answer-scoring](runtime.md#rt-rte-answer-scoring). Scores do not filter stored experience or successor text. |
| Local code continuation / temporary-script cleanup | `dynamic_cheatsheet/language_model.py`, `dynamic_cheatsheet/utils/execute_code.py` | Wrapper directly read; executor via [RT-RTE-local-execution](runtime.md#rt-rte-local-execution). Code/result text survives in outputs; script cleanup is not memory withdrawal. |
| Native tools / container lifecycle / text projection | `dynamic_cheatsheet/language_model.py`, `text_generation/simple_unified_client.py`, `run_benchmark.py` | Direct reads; [MEM-OBJ-container-id](#mem-obj-container-id), [RT-RTE-native-execution](runtime.md#rt-rte-native-execution). Opaque payload, cross-call reuse and service lifecycle unresolved. |
| Exported client generate/chat/get/set/reset | `text_generation/__init__.py`, `text_generation/simple_unified_client.py` | Direct reads; [MEM-OBJ-messages](#mem-obj-messages), [MEM-RTE-chat-history](#mem-rte-chat-history). Separate API path, not benchmark memory. |
| Dispatch, auxiliary extraction and token accounting | `run_benchmark.py`, `dynamic_cheatsheet/language_model.py`, `dynamic_cheatsheet/utils/extractor.py`, `text_generation/simple_unified_client.py` | Direct branch reads and bounded search for `count_tokens`, `extract_solution`, history calls, `register`, `hook`. No additional hooked admission route found in these source roots. Not a repository-wide absence claim. |
| Task/embedding/result artifacts | `data/`, `embeddings/`, `results/` | Supplied boundary inventory and [RT-CMP-input-embeddings](runtime.md#rt-cmp-input-embeddings); full payloads not inspected. Prevents content provenance, measured accuracy and causal conclusions. |

## Core ideas

There are two distinct memory products: model-curated replacement text and earlier full generated outputs. The driver carries both, but selection and authority differ. Curated text reaches the next curator as previous knowledge and the generator as reference. Prior outputs remain unfiltered candidates for similarity retrieval or history assembly. A failed or incorrect solution can therefore remain available even when the curator omits it. SRC-1, `run_benchmark.py`, `dynamic_cheatsheet/language_model.py`; [MEM-OBJ-final-cheatsheet](#mem-obj-final-cheatsheet), [MEM-OBJ-final-output](#mem-obj-final-output).

Curation is whole-text regeneration. Memory-item tags, source-question references, usage counters, correctness assessment and preservation are requested conventions, not separately parsed software state. The actual gate accepts text after an opening cheatsheet tag. Curator rationale outside that extracted region is neither live reference nor a separately saved curator-output field. SRC-1, `prompts/curator_prompt_for_dc_cumulative.txt`, `prompts/curator_prompt_for_dc_retrieval_synthesis.txt`, `dynamic_cheatsheet/language_model.py`, `dynamic_cheatsheet/utils/extractor.py`; [RT-RTE-cumulative-curation](runtime.md#rt-rte-cumulative-curation), [MEM-OBJ-steps](#mem-obj-steps).

Retrieval is deterministic query-conditioned context construction, not a request issued by the generator. Original question vectors rank earlier questions; corresponding full outputs follow by index. Direct retrieval delivers examples; synthesis lets the curator replace them with query-specific text; hybrid concatenates examples with cumulative text. Top-k bounds example count, not tokens or source reliability. SRC-1, `dynamic_cheatsheet/language_model.py`; [RT-RTE-context-selection](runtime.md#rt-rte-context-selection).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-final-cheatsheet
Label: Live final cheatsheet text

Part of: [RT-OBJ-output-dict](runtime.md#rt-obj-output-dict)

Source-native identity: `final_cheatsheet` and live `cheatsheet` strings. Representational form: natural-language strategies, code examples or assembled problem/response text interpreted by models; formatting does not confer enforced item semantics. Storage substrate: Python strings, returned dictionary, driver JSONL. This is the reference-content part of the checkpoint, not a duplicate of the entire envelope. SRC-1, `dynamic_cheatsheet/language_model.py`, `run_benchmark.py`.

Lineage depends on approach: caller seed, model-generated cumulative replacement, retrieved examples, synthesized reference or complete prior history; default returns `None`. A live text's initial authorship is unresolved when supplied by a caller. Subsequent cumulative transformations are known model/software operations regardless of that initial uncertainty. Consumers are generator and, on curated paths, curator, through user-message text; authority is requested reference use or proposal influence, not privileged policy or validated truth. See [RT-BAP-cheatsheet-context](runtime.md#rt-bap-cheatsheet-context), [RT-BAP-curator-guidance](runtime.md#rt-bap-curator-guidance).

> cheatsheet = output_dict["final_cheatsheet"]
> final_answer = output_dict["final_answer"]
> --- `run_benchmark.py`

Whole replacement withdraws omitted material from the live cumulative reference. Historical checkpoint copies may remain; retrieval can independently reintroduce earlier source solutions. The curator's warning about irretrievable loss applies to the live reference, not all repository-retained evidence. Rationale survives only if written inside the extracted text; no automatic provenance verification or item-level restoration follows from requested Q tags.

#### MEM-OBJ-final-output
Label: Retained full generator output corpus

Part of: [RT-OBJ-output-dict](runtime.md#rt-obj-output-dict)

Source-native identity: `final_output`, appended to `generator_outputs_so_far`. Representational form: natural-language model response with code and local execution result text, not merely the extracted answer; provider-native responses are text projections. Storage substrate: returned strings, Python list, JSONL. Lineage: generator response and any local continuation; original questions come from the dataset prefix, rather than from a learned memory index. SRC-1, `dynamic_cheatsheet/language_model.py`, `run_benchmark.py`.

> generator_outputs_so_far.append(output_dict["final_output"])
> --- `run_benchmark.py`

This raw response corpus is distinct from derived curator reference content and from diagnostic steps. Its actual later consumers are the retrieval-synthesis curator, direct-retrieval/history generator, and hybrid generator. Cumulative curator also consumes the current generated response before it becomes prior corpus. Both uses have model-interpreted authority, not correctness certification. See [RT-RTE-context-selection](runtime.md#rt-rte-context-selection), [RT-RTE-cumulative-curation](runtime.md#rt-rte-cumulative-curation). The driver appends before scoring and does not remove scored failures. Cross-run persistence uses reload of every `final_output`, supported by [RT-RTE-checkpoint-continuation](runtime.md#rt-rte-checkpoint-continuation). Old problem answers can survive regardless of omission from successor curated text.

#### MEM-OBJ-steps
Label: Per-round diagnostic steps

Part of: [RT-OBJ-output-dict](runtime.md#rt-obj-output-dict)

Source-native identity: `steps`, including generator prompt/output/answer and old/new cheatsheet snapshots. Representational form: symbolic list/dictionaries carrying model-interpreted natural-language fields. Storage substrate: returned dictionary and JSONL. Lineage: wrapper snapshots of generation and extraction, not a separate critic report. SRC-1, `dynamic_cheatsheet/language_model.py`, `EvaluatingResults.ipynb`.

> previous_answers.append(f"Round {round_idx+1}: {generator_answer}")
>
> steps.append({
>     "round": round_idx,
>     "generator_prompt": generator_prompt,
>     "generator_output": generator_output,
>     "generator_answer": generator_answer,
>     "current_cheatsheet": current_cheatsheet,
>     "new_cheatsheet": new_cheatsheet,
> })
> --- `dynamic_cheatsheet/language_model.py`

The quote is the cumulative step fields; hybrid retains equivalent fields plus retrieved examples. No branch stores a separate `cheatsheet_output` field in its returned steps: curator reasoning outside extracted content has no checkpoint consumer here. This limits auditability of why a replacement occurred. Earlier snapshots can support external manual inspection, but driver reload chooses last `final_cheatsheet`, not an earlier step snapshot. The actual shipped later consumer of step outputs is the evaluation notebook, not the next generator:

> model_output = example['steps'][-1]['generator_output'].strip()
> --- `EvaluatingResults.ipynb`

This raw-diagnostic part differs from live context and the corpus. Its scoring authority is deterministic answer normalization/evaluation; see [RT-RTE-answer-scoring](runtime.md#rt-rte-answer-scoring). Targets in the parent envelope serve that evaluator, not curator admission.

#### MEM-OBJ-retrieved-selection
Label: Selected example metadata and context rendering

Part of: [RT-OBJ-output-dict](runtime.md#rt-obj-output-dict)

Source-native identity: `top_k_original_inputs`, `top_k_original_outputs`, and hybrid `retrieved_examples`. Representational form: symbolic index-derived lists and natural-language rendering; similarity numbers are access/ranking metadata, not learned knowledge or correctness scores. Storage substrate: local arrays/lists/strings, returned dictionary and JSONL. Lineage: question-vector cosine ranking or full-history prefix. SRC-1, `dynamic_cheatsheet/language_model.py`.

> length_of_history = len(generator_outputs_so_far)
> if length_of_history > 0:
>     top_k_original_inputs = original_input_corpus[:length_of_history]
>     top_k_original_outputs = generator_outputs_so_far
> --- `dynamic_cheatsheet/language_model.py`

The quote covers full-history selection; retrieval and hybrid return corresponding selected-list fields. Selection metadata is not independently reloaded for future retrieval: the driver rebuilds candidate questions/vectors and reloads full outputs. Immediate consumers interpret rendered examples, with highest-ranked retrieval placed last. Synthesis can discard or generalize selected details; the generator receives extracted synthesis rather than guaranteed complete selected pairs. Distinct from the complete checkpoint and its live reference part; operation belongs to [RT-RTE-context-selection](runtime.md#rt-rte-context-selection).

#### MEM-OBJ-container-id
Label: Native execution handle and opaque server state

Source-native identity: `LanguageModel.container_id`, real OpenAI container ID or Claude `native` sentinel. Representational form: symbolic dispatch handle; remote payload encoding/content uninspected. Storage substrate: wrapper instance for the handle, provider-managed execution environment for any payload. Lineage: caller-supplied handle or container creation; actual remote writes and retention remain opaque. SRC-1, `dynamic_cheatsheet/language_model.py`, `text_generation/simple_unified_client.py`, `run_benchmark.py`.

> container = self.openai_client.containers.create(name=name, memory_limit=memory_limit)
> logger.info(f"Created code interpreter container: {container.id}")
> return container.id
> --- `text_generation/simple_unified_client.py`

The closest supplied record is [RT-RTE-native-execution](runtime.md#rt-rte-native-execution), a route rather than this state object; no supplied object counterpart. The OpenAI request sends the same handle on later calls during a benchmark. It establishes handle reuse, not which files or execution state later tools read, their authority or preservation. Claude's sentinel only enables dispatch; it is not evidence of reusable provider memory. No native container handle or nontext payload is restored by JSONL continuation. New driver invocation creates a session again. This object is not part of the output dictionary. Opaque tool state must remain separate from readable `final_output`; no tool-memory benefit can be concluded.

#### MEM-OBJ-messages
Label: Exported client conversation history

Source-native identity: `UnifiedLLMClient.messages`. Representational form: symbolic role/content dictionaries with natural-language content interpreted by providers. Storage substrate: in-process Python list; no disk persistence in inspected history methods. Lineage: `chat` appends submitted message and returned text; `set_history` replaces from caller-provided dictionaries. Human authorship/approval of those inputs is unresolved. SRC-1, `text_generation/simple_unified_client.py`.

> self.messages.append({"role": "user", "content": message})
> self.messages.append({"role": "assistant", "content": full_response})
> --- `text_generation/simple_unified_client.py`

No supplied object counterpart after comparison with [RT-OBJ-output-dict](runtime.md#rt-obj-output-dict) and [RT-CMP-language-model](runtime.md#rt-cmp-language-model): this is separate local client state, not checkpoint or model parameters. Its later consumer is provider generation via the client's history-extending `generate`; role-bearing messages can shape conversation interpretation. The benchmark's `generate_from_messages` bypasses this list. See [MEM-RTE-chat-history](#mem-rte-chat-history).

### Routes

#### MEM-RTE-chat-history
Label: Client chat history append and reuse

Endpoints/progression: caller `chat` → `generate` builds messages from retained list plus current prompt → provider response → append current user and assistant text → next `chat` or `generate` includes history. Owner: exported client implementation; caller chooses invocation. Context effect: raw earlier conversation becomes provider input without curator synthesis. Distinct from [RT-RTE-context-selection](runtime.md#rt-rte-context-selection), which handles benchmark question/output lists. SRC-1, `text_generation/simple_unified_client.py`, `text_generation/__init__.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Response text; streamed response is joined before chat stores it.
- Later read-back: Subsequent chat/generate automatically includes `self.messages`; exposed get/set support caller transfer but no shipped disk reloader is established for this list.
- Delegated visibility: Provider sees retained role/content messages; benchmark message entry point does not inherit them.
- Selection predicate: Entire current list in order, on each history-using generation call; no query ranking or software token trimming in this assembly.
- Invalidation or expiry: `reset_history` clears the list; `set_history` replaces it; no time expiry in these methods.
- Activation or effect: Append, assembly and provider delivery wired; content-dependent behavioral effect uninspected.
- Evidence limits: No consumer run inspected; external provider context limits and retention unknown. Optional search augmentation belongs to current generation and is not separately saved as history by chat.

> messages.extend(self.messages)
> messages.append({"role": "user", "content": prompt})
> --- `text_generation/simple_unified_client.py`

Admission: software appends after successful generation; caller can replace/clear history through APIs, with caller's human role unresolved. No per-content human or correctness veto is inserted. Trigger is caller message, not a score; proposed change is raw conversation retention, not formulated strategy revision. Operating mode is open conversational requests. No expected-answer oracle. Failed generation before append does not add that turn; no checkpoint rollback is supplied. Optional system message/search configuration can shape generation but are not curation rules. No theory-formulation assessment is warranted solely from raw-history storage.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-cumulative-curation](runtime.md#rt-rte-cumulative-curation)

Write lineage is current problem plus full generator output, including local execution continuation, and previous reference → model proposal → delimiter extraction → [MEM-OBJ-final-cheatsheet](#mem-obj-final-cheatsheet) → next generator/curator. This is an automatic trace-fed transformation with behavior-shaping read-back, not merely raw logging. It does not establish improved capacity. Trace origin includes dataset/caller problem, remote model content and possible local execution output; provider-native internals are projected to text. SRC-1, `dynamic_cheatsheet/language_model.py`.

Curator output allowance is `2 * max_tokens`; generator allowance is `max_tokens`. These are output budgets, not reference/context caps. The prompt's 2000–2500-word guidance is not an enforced input budget. `count_tokens` is defined but unused by inspected branch/driver calls. Usage counts and references are natural-language contents, not executable counters or provenance controls. SRC-1, `dynamic_cheatsheet/language_model.py`, `prompts/curator_prompt_for_dc_cumulative.txt`.

> N.B. Make sure that all information related to the cheatsheet is wrapped inside the <cheatsheet> block. The cheatsheet can be as long as circa 2000-2500 words.
> --- `prompts/curator_prompt_for_dc_cumulative.txt`

Missing opening tag preserves previous text; opening without closing can still admit text, as the supplied record's extractor quote shows. A syntactically admitted empty or poor replacement has no score-based rollback. Steps retain old/new snapshots but not the curator's full reasons. The hybrid curator gets old cumulative text, not the assembled retrieval section as a separate input; retrieval can influence the proposal indirectly through generator output. No semantic quality or source trust guarantee follows from the word “verified.”

#### On [RT-RTE-context-selection](runtime.md#rt-rte-context-selection)

Read-back is automatically selected and delivered on incoming question, not generator-requested fetching. Selector inputs are original question vectors, prior question corpus and prior full outputs; similarity metadata chooses access, not reliability. Direct retrieval bypasses model curation; full history uses all zipped pairs; hybrid combines selected examples with cumulative reference. Synthesis additionally sees previous reference and next question. The previous reference is not a separately searchable corpus. SRC-1, `dynamic_cheatsheet/language_model.py`, `run_benchmark.py`.

Synthesis is a mixed-source trace-fed transformation: prior response traces and prior derived reference produce a new reference for current generator and future carry-forward. No current question solution is available at synthesis time. In fallback, extraction retains assembled retrieved text, not the former live reference. The supplied route passage establishes this alternative checkpoint form. Curator calls permit `2 * max_tokens`; selected raw examples have only top-k count limits, and full history has no implemented count/token reduction. Unvalidated negative k follows Python slicing rather than a checked positive-count policy. SRC-1, `dynamic_cheatsheet/language_model.py`.

Source-trust warnings ask the model to verify examples; actual admission does not use benchmark scores. Requested refinement, deduplication, usage counts and replacement of inferior methods remain doctrine rather than observed semantic transformations. Guidance to copy old knowledge applies to new text only; raw output corpus can survive independently. SRC-1, `prompts/curator_prompt_for_dc_retrieval_synthesis.txt`.

#### On [RT-RTE-checkpoint-continuation](runtime.md#rt-rte-checkpoint-continuation)

Storage is JSONL snapshots of symbolic envelopes carrying natural-language text. Read-back loads last `final_cheatsheet` and every `final_output`; prior stored targets/diagnostic steps do not become curator feedback. Dataset questions and CSV vectors are rebuilt/reordered rather than restored from selection metadata. Caller chooses resume file; generic caller selection does not establish human approval of retained content. SRC-1, `run_benchmark.py`.

Initialization text is read before continuation, then replaced by last reference when non-null. Manual seed/edit or checkpoint substitution is afforded by file APIs but not demonstrated human curation. Driver saves arguments, including loaded prompt strings, in companion JSON; continuation rereads current prompt files and compares selected argument fields, rather than adopting saved prompt bytes. The route's partial-check and nonatomic-write limits therefore affect memory continuity, not just logging. SRC-1, `run_benchmark.py`.

#### On [RT-RTE-local-execution](runtime.md#rt-rte-local-execution)

Local stdout/error/timeout text is inserted into accumulated generator output and assistant conversation. It can influence continuation immediately, curator replacement and future retrieval/history. Temporary script deletion removes an execution artifact, not the retained code/result text. Full output is not a separately validated trace of all filesystem/process effects. Source support and executor cleanup limits are in the supplied route; direct wrapper read confirms the raw-to-derived path. SRC-1, `dynamic_cheatsheet/language_model.py`, `dynamic_cheatsheet/utils/execute_code.py`.

#### On [RT-RTE-native-execution](runtime.md#rt-rte-native-execution)

Readable output and remote execution payload differ. OpenAI returns `response.output_text`; Claude retains only text content blocks. Nontext tool artifacts are not automatically exposed to curator or checkpoint. Handle reuse does not establish remote state read-back. SRC-1, `text_generation/simple_unified_client.py`; [MEM-OBJ-container-id](#mem-obj-container-id).

> for content_block in response.content:
>     if content_block.type == "text":
>         text_parts.append(content_block.text)
> return "".join(text_parts) if text_parts else ""
> --- `text_generation/simple_unified_client.py`

#### On [RT-RTE-answer-scoring](runtime.md#rt-rte-answer-scoring)

Scores occur after live reference assignment and corpus append; failure does not veto either. The checkpoint contains targets and outputs, not an added score field governing later selection. Offline notebook selects last step generator output, normalizes an answer and scores; it neither edits reference nor deletes failed corpus entries. This is a retained-evidence consumer, not a trace-learning write path. SRC-1, `run_benchmark.py`, `EvaluatingResults.ipynb`; [MEM-OBJ-steps](#mem-obj-steps).

## Write side

Acquisition has three software-visible entry forms: empty seed, caller-supplied text file, and loaded checkpoint. Actual human authorship/approval of the latter two is unresolved. Starting the workflow or choosing a path is not per-item approval. The notebook supplies `(empty)` then feeds returned reference strings into repeated invocations on one problem. SRC-1, `run_benchmark.py`, `ExampleUsage.ipynb`; [MEM-OBJ-final-cheatsheet](#mem-obj-final-cheatsheet), [RT-RTE-checkpoint-continuation](runtime.md#rt-rte-checkpoint-continuation).

Automatic curation proposes the entire next text. Software admits delimiter-extracted content; missing opening tag rejects by retaining fallback. Cumulative fallback is old reference; synthesis fallback is assembled raw examples. Cumulative/hybrid updates follow current generated solution; synthesis precedes current solving and uses previous traces. The maintenance instructions request preservation, correctness checks, refinement and counters, but no independent semantic admission controller is wired. The supplied runtime route records retain the minimal mechanism quotes. SRC-1, `dynamic_cheatsheet/language_model.py`, `dynamic_cheatsheet/utils/extractor.py`; [RT-RTE-cumulative-curation](runtime.md#rt-rte-cumulative-curation), [RT-RTE-context-selection](runtime.md#rt-rte-context-selection).

Raw experience retention is separately unconditional with respect to scoring. It is not derived-memory learning by itself; the later synthesis path is its trace-fed derived transformation, and direct retrieval/history provide uncurated later context. Extraction of a reference preserves no mandatory rationale: old/new text is saved, curator raw output is not, and item reasons survive only if embedded in text. Code cleanup, bad score and omission from live cheatsheet are three different events; none automatically deletes the output corpus. Historical versions remain in checkpoints for possible external recovery, without a wired rollback selector. SRC-1, `dynamic_cheatsheet/language_model.py`, `run_benchmark.py`; [MEM-OBJ-final-output](#mem-obj-final-output), [MEM-OBJ-steps](#mem-obj-steps).

The client conversation route appends raw turns and supports reset/replacement independently. OpenAI native execution creates an opaque alternative state surface; no local proof of remote payload withdrawal or continuity follows. SRC-1, `text_generation/simple_unified_client.py`; [MEM-RTE-chat-history](#mem-rte-chat-history), [MEM-OBJ-container-id](#mem-obj-container-id).

## Read-back

| Retained part | Trigger / selector / selected material | Delivery and later consumer | Budget / authority / limits |
|---|---|---|---|
| Cumulative text | Next round or next problem; whole returned reference | User-message generator reference, then curator previous-reference field | Output limits and word guidance only; requested use, no observed activation. [RT-RTE-cumulative-curation](runtime.md#rt-rte-cumulative-curation). |
| Previous extracted answers | Next cumulative refinement round when flag enabled; answers accumulated for same problem | Appended PREVIOUS ANSWERS section for generator | Local within-call retention, not separate cross-problem answer list; prompt influence only. SRC-1, `dynamic_cheatsheet/language_model.py`. |
| Prior full outputs | Incoming query; cosine-ranked question indices or full zipped history | Rendered examples → generator or synthesis curator; synthesis text → generator | Top-k is count, not tokens; history grows without software trimming. [RT-RTE-context-selection](runtime.md#rt-rte-context-selection). |
| Checkpoint live reference/corpus | Caller resume file; last reference plus all full outputs | Driver reconstructs next query context | No score filter; positional alignment assumptions. [RT-RTE-checkpoint-continuation](runtime.md#rt-rte-checkpoint-continuation). |
| Steps and targets | Notebook file glob and last step selection | Answer normalizer/scorer | Evaluation, not model update authority. [RT-RTE-answer-scoring](runtime.md#rt-rte-answer-scoring). |
| Client messages | Next chat/generate; whole retained list | Provider role-bearing message list | No local trimming or disk persistence established. [MEM-RTE-chat-history](#mem-rte-chat-history). |
| Native container payload | Later native call passes handle; actual payload selection unknown | Provider tool execution, not necessarily curator text | Remote content, budget, read-back and authority unresolved. [MEM-OBJ-container-id](#mem-obj-container-id). |

Static prompt files, CSV vectors and initial dataset loads are not use-accumulated read-back. They control later context construction but are not inferred to be learned state. `get_history` provides access/export capability; the next `chat`/`generate` supplies the actual implemented consumer route. No hypothetical external saver is promoted to a shipped persistence loop. SRC-1, `run_benchmark.py`, `text_generation/simple_unified_client.py`; [RT-CMP-input-embeddings](runtime.md#rt-cmp-input-embeddings), [MEM-RTE-chat-history](#mem-rte-chat-history).

## Integration issues

- No correction to a supplied runtime fact is required. The separate client-history route extends the runtime's explicitly limited convenience-API inspection; it does not contradict the benchmark account. [MEM-RTE-chat-history](#mem-rte-chat-history), [MEM-OBJ-messages](#mem-obj-messages). SRC-1, `text_generation/simple_unified_client.py`.
- Four declarations are material parts of the existing checkpoint container, not replacements or duplicate envelopes: live reference, full response corpus, steps and retrieved-selection fields. Their differing consumers and retention controls require separate treatment. [RT-OBJ-output-dict](runtime.md#rt-obj-output-dict), [MEM-OBJ-final-cheatsheet](#mem-obj-final-cheatsheet), [MEM-OBJ-final-output](#mem-obj-final-output), [MEM-OBJ-steps](#mem-obj-steps), [MEM-OBJ-retrieved-selection](#mem-obj-retrieved-selection). SRC-1, `dynamic_cheatsheet/language_model.py`, `run_benchmark.py`.
- No new record is a possible duplicate after comparison with supplied objects/routes. Container state is an object associated with, not a redeclaration of, native dispatch. Client messages are separate from benchmark corpus. [MEM-OBJ-container-id](#mem-obj-container-id), [RT-RTE-native-execution](runtime.md#rt-rte-native-execution), [MEM-OBJ-messages](#mem-obj-messages), [RT-RTE-context-selection](runtime.md#rt-rte-context-selection).
- Native payload encoding, admission, actual remote reuse, lifecycle and authority remain unresolved; handle reuse cannot determine tool-memory classification or benefit. The Claude sentinel does not establish persistent state. [MEM-OBJ-container-id](#mem-obj-container-id), [RT-RTE-native-execution](runtime.md#rt-rte-native-execution). SRC-1, `text_generation/simple_unified_client.py`; remote implementations are outside frozen evidence.
- Caller-supplied seed/history/checkpoint content has unresolved authorship and human control. Subsequent model/software transformations remain established. [MEM-OBJ-final-cheatsheet](#mem-obj-final-cheatsheet), [MEM-OBJ-messages](#mem-obj-messages), [RT-RTE-checkpoint-continuation](runtime.md#rt-rte-checkpoint-continuation). SRC-1, `run_benchmark.py`, `text_generation/simple_unified_client.py`.
- Embedding provenance/quality, actual prompt preservation, generated rationale and beneficial behavioral activation remain uninspected. Source labels and instructions cannot settle those questions. This prevents realized-learning and content-validity conclusions, not the wired trace-fed update account. [RT-CMP-input-embeddings](runtime.md#rt-cmp-input-embeddings), [RT-RTE-cumulative-curation](runtime.md#rt-rte-cumulative-curation), [RT-RTE-context-selection](runtime.md#rt-rte-context-selection), [RT-CLM-adaptive-memory](runtime.md#rt-clm-adaptive-memory).

## Limitations and checks

The checkout HEAD was rechecked as `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`, with clean status. Source identity and boundary fields match the supplied inputs. Notebook source was extracted as text for inspection; saved outputs were not treated as observations. Source reading and searches did not execute target code, providers, tests or examples. Inspection of separate exported history methods adds implementation coverage within SRC-1, not a source or boundary change.

This report establishes reference/corpus retention, transformation, admission and later delivery. It does not establish semantic correctness, complete provenance, content-dependent activation, theory-builder operation, improved future capacity or causal benefit. Source-level counterchecks included alternate extraction fallback, default raw-output retention, failed-answer retention, hybrid indirect retrieval influence, history-entry bypass and native text-only projection. These restrict strong memory labels without erasing supported mechanisms.

Validation: passed using the invocation's role-specific content check. This checks structure, quotations and relations, not analytical correctness or workflow acceptance.
