---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Dynamic Cheatsheet memory: caller-carried reference text, raw solution retrieval, model curation, checkpoints and provider-state limits."
run-id: AAS-2026-10-20-dynamic-cheatsheet-523b6948294d-01
source-identity: "https://github.com/suzgunmirac/dynamic-cheatsheet"
reviewed-boundary: "5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9"
---

# Dynamic Cheatsheet memory report

## Boundary and evidence

This report covers the shipped inference-memory loop at SRC-1, commit `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`, under [the boundary](boundary.md#boundary-and-evidence). It includes all six approach branches, initialization and continuation, extraction, separate generator/curator contexts, raw-output retrieval, evaluation handoff and native execution state. It also inspects the provider adapter's exposed conversation-history controls as an alternative context surface, without attributing that surface to the benchmark. Model weights are covered by [RT-CMP-language-model](runtime.md#rt-cmp-language-model), not redeclared here.

Evidence is implementation and prompt doctrine/design. Direct reads cover `dynamic_cheatsheet/language_model.py` in full, `run_benchmark.py` in full, `dynamic_cheatsheet/utils/extractor.py` in full, all three `prompts/` files, and the adapter methods listed below. Notebook caller/evaluator findings and local-execution internals are supplied runtime evidence rather than independent notebook/executor reads. No target execution occurred. Dataset payloads, vector payloads, historical JSONL payloads and saved notebook outputs remain available but uninspected; no operational activation, retrieval-quality or measured-benefit conclusion follows. Remote provider state and model internals are not accessible through this frozen source. The source register remains [boundary's Source register](boundary.md#source-register); no source is added.

| Entry point or memory operation | Source paths and inspection | Records or bounded limit |
|---|---|---|
| CLI admission, initial file, resume, checkpoint | `run_benchmark.py`, direct | [RT-RTE-benchmark-cycle](runtime.md#rt-rte-benchmark-cycle); [MEM-OBJ-cheatsheet](#mem-obj-cheatsheet); [MEM-OBJ-final-output](#mem-obj-final-output) |
| Cumulative and hybrid post-answer replacement | `dynamic_cheatsheet/language_model.py`, cumulative prompt, extractor, direct | [RT-RTE-cumulative-update](runtime.md#rt-rte-cumulative-update); sheet annotation and write-side account |
| Retrieval-only, synthesis-before-answer, hybrid retrieval | wrapper and synthesis prompt, direct | [RT-RTE-context-selection](runtime.md#rt-rte-context-selection); [MEM-OBJ-input-embeddings](#mem-obj-input-embeddings) |
| Full-history and default alternatives | wrapper, direct | Context-selection annotation; default does not retain a sheet; full history reuses raw output rather than learned summaries |
| Repeated cumulative rounds, local continuation and context isolation | wrapper, direct; executor internals supplied by runtime | [MEM-OBJ-previous-answers](#mem-obj-previous-answers); [RT-RTE-local-execution](runtime.md#rt-rte-local-execution) |
| Generator's reference interpretation | generator prompt, direct | [RT-BAP-reference-context](runtime.md#rt-bap-reference-context) |
| Native execution state | wrapper and adapter `generate_with_code_interpreter`, `generate_with_code_interpreter_claude`, direct | [MEM-OBJ-container-id](#mem-obj-container-id); [RT-RTE-provider-execution](runtime.md#rt-rte-provider-execution); provider payload/lifecycle opaque |
| Exposed adapter history controls | `text_generation/simple_unified_client.py`: `generate`, `generate_from_messages`, `chat`, `reset_history`, `get_history`, `set_history`, direct | [MEM-OBJ-messages](#mem-obj-messages); [MEM-RTE-history-controls](#mem-rte-history-controls); not a benchmark persistence path |
| Notebook repeated calls and scoring | `ExampleUsage.ipynb`, `EvaluatingResults.ipynb`, supplied runtime only | [RT-RTE-benchmark-cycle](runtime.md#rt-rte-benchmark-cycle), [RT-RTE-score-answer](runtime.md#rt-rte-score-answer); saved outputs uninspected |
| Frozen vectors, datasets and result corpora | `embeddings/`, `data/`, `results/`; inventory/caller logic only | Initial vector provenance and quality unresolved; no corpus-wide observation, oracle-integrity or accuracy claim |
| Other adapter chat/search conveniences and auxiliary scoring | adapter method inventory; boundary/runtime coverage | Search-result quality and standalone provider operations are not characterized; no additional durable search-memory route established |

The inspected CLI dispatch and wrapper approach registry account for the shipped benchmark memory modes. The adapter supplies callable history setters/resetters, not a registered memory-tool or hook mechanism in those inspected dispatch paths. This is a bounded account of these paths, not a repository-wide claim that arbitrary callers cannot add memory.

## Core ideas

1. **The caller carries memory.** `LanguageModel` returns a sheet; driver/notebook handoff creates its cross-query horizon. Disk JSONL serves both recovery and a raw-output archive. The semantic sheet and raw trace have different later consumers; neither should be equated with the envelope containing them ([MEM-OBJ-cheatsheet](#mem-obj-cheatsheet), [MEM-OBJ-final-output](#mem-obj-final-output)).
2. **Curation replaces text rather than mutating structured entries.** The prompt requests reusable strategies, usage counts, references and correctness checks. Python admits a tagged replacement without checking any of those properties. Whole-sheet replacement can remove live material; archived earlier versions and raw traces are counterexamples to the prompt's absolute claim that omitted content cannot be retrieved ([RT-RTE-cumulative-update](runtime.md#rt-rte-cumulative-update)). Automatic restoration of an omitted sheet entry is nevertheless not wired.
3. **Retrieval selects experience, not verified answers.** Numerical question similarity chooses raw previous solutions. Synthesis is another model context; hybrid keeps both the cumulative sheet and selected examples. All are supplied as interpreted reference text, not executable control rules. The corpus excludes the current question's not-yet-produced answer through driver slicing, but source inspection does not establish dataset independence or vector correctness ([RT-RTE-context-selection](runtime.md#rt-rte-context-selection)).
4. **Fresh contexts bound transcript carryover, not sheet size.** Separate calls keep curator analysis and unselected old solutions out of the generator. Only selected/derived text crosses back. Prompt word advice and completion limits are not a context-window fit policy. No improved future capacity is established merely by these trace-fed writes ([RT-CLM-adaptive-memory](runtime.md#rt-clm-adaptive-memory)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-cheatsheet
Label: cheatsheet reference body

Part of: [RT-OBJ-output-dict](runtime.md#rt-obj-output-dict)

Source-native identity: `cheatsheet`, extracted `new_cheatsheet`, returned as `final_cheatsheet`. This is the reference payload, not its parent dictionary. It is an immutable Python string in process, optionally initialized from a text file and serialized into JSONL by the driver. Its operative form at generator/curator consumption is natural language, including strategy descriptions and displayed code snippets. The outer extraction tags and dictionary keys are symbolic delimiters, not an entry schema. Code displayed in a sheet is interpreted by the model; any subsequently generated executable code passes through the separate local/native execution routes, not a direct sheet evaluator. SRC-1, `dynamic_cheatsheet/language_model.py`, `run_benchmark.py`, `prompts/generator_prompt.txt`.

Lineage: `(empty)`, arbitrary caller/file input, prior resumed sheet, or model synthesis/replacement from old sheet and solution text. Initial file content authorship, correctness and human approval are unresolved; accepting a path does not prove a human approved its contents. Update consumers receive old sheet and trace; downstream generator receives the extracted replacement. Horizon: cumulative rounds, successive questions and resumed processes when callers preserve it. `final_cheatsheet` also carries full-history/retrieval display text in those branches, so the field name alone does not establish model-derived curation.

> cheatsheet = "(empty)"
> if args.initialize_cheatsheet_path is not None:
>     with open(args.initialize_cheatsheet_path, "r") as file:
>         cheatsheet = file.read()
> --- `run_benchmark.py`

> generator_prompt = generator_template.replace("[[QUESTION]]", input_txt).replace("[[CHEATSHEET]]", generator_cheatsheet_content)
> --- `dynamic_cheatsheet/language_model.py`

Retention of reasons is requested, not enforced. Descriptions, worked examples and pitfalls may accompany a strategy; no separately checked rationale field is required. Subsequent consumers read whatever prose survived extraction, not a separately retained criticism record. Prompt usage counts and question references are text under model interpretation, not software-maintained access metadata.

> - Include descriptions, annotated examples, and potential pitfalls, albeit succinctly.
> --- `prompts/curator_prompt_for_dc_cumulative.txt`

> - Each entry must include a usage count: Increase the count every time a strategy is successfully used in problem-solving.
> --- `prompts/curator_prompt_for_dc_cumulative.txt`

#### MEM-OBJ-final-output
Label: final_output solution trace

Part of: [RT-OBJ-output-dict](runtime.md#rt-obj-output-dict)

Source-native identity: `final_output`, accumulated by the driver into `generator_outputs_so_far`. Storage is Python lists and JSONL rows. Form: natural-language solution text with possible displayed code and local execution output; this is a rendered trace, not a structured complete event log. It differs from the semantic sheet and from the envelope. It is raw with respect to later curation, although code extraction/provider text flattening can already have transformed the originating interaction. Local process state and provider tool payloads are not reconstructed by this text. SRC-1, `dynamic_cheatsheet/language_model.py`, `run_benchmark.py`; execution limits also in [RT-RTE-local-execution](runtime.md#rt-rte-local-execution) and [RT-RTE-provider-execution](runtime.md#rt-rte-provider-execution).

Admission: computation appends the generator return without correctness filtering. The curator reads the current full generator output; later retrieval/full-history routes read archived final outputs paired with original inputs. Resume loads every saved row's `final_output`, not every intermediate round output. Other step text may remain archived without a normal later retrieval selector. Targets are saved alongside traces but are not inserted into the later solution-pair prompts by the inspected driver. No software-maintained per-entry success warrant follows from target co-storage.

> generator_outputs_so_far = [output["final_output"] for output in outputs]
> --- `run_benchmark.py`

> top_k_original_outputs = [generator_outputs_so_far[i] for i in top_k_indices]
> --- `dynamic_cheatsheet/language_model.py:510-514`

#### MEM-OBJ-input-embeddings
Label: original_input_embeddings retrieval index

Source-native identity: `original_input_embeddings`, loaded from task CSV `embedding` cells. Representational form: dense numerical vectors for cosine ranking (distributed representations), with symbolic array indices and paired original question strings. Storage: frozen CSV files under `embeddings/`, parsed into NumPy arrays. These are selection inputs, not a semantic memory answer body. Distinct from [RT-OBJ-output-dict](runtime.md#rt-obj-output-dict): the wrapper consumes these arrays but does not return them as the result envelope. Closest supplied mechanism is [RT-RTE-context-selection](runtime.md#rt-rte-context-selection).

The driver reorders vectors by exact original-input string lookup and slices through the current index. No runtime embedding update is performed on these inspected paths. The producing model, generation procedure, dimensional consistency, duplicate-key behavior in actual datasets and vector quality remain uninspected; the numerical payloads themselves were not read. Consequently neither embedding provenance nor correct semantic alignment is established. Admission of these files is caller/dataset selection, without a per-vector human or correctness approval gate in the loader. SRC-1, `run_benchmark.py`, `dynamic_cheatsheet/language_model.py`.

> indices = [questions.index(inp) for inp in dataset_inputs]
> embeddings = embeddings[indices]
> questions = dataset_inputs
> --- `run_benchmark.py`

#### MEM-OBJ-previous-answers
Label: previous_answers within cumulative rounds

Part of: [RT-OBJ-output-dict](runtime.md#rt-obj-output-dict)

Source-native identity: cumulative branch `previous_answers`, a Python list of strings labeling extracted final answers by round. Form: natural-language answer content with generated round-label text. It is distinct from full solution traces and curator-derived reference text. Computation appends it after every cumulative round without validating correctness. Later rounds of the same question receive it if `add_previous_answers_to_cheatsheet` is enabled; the driver does not separately reload this list for later questions. It is saved as envelope data, but its automatic read-back horizon is within that one `advanced_generate` invocation. SRC-1, `dynamic_cheatsheet/language_model.py`.

> previous_answers.append(f"Round {round_idx+1}: {generator_answer}")
> --- `dynamic_cheatsheet/language_model.py`

> previous_answers_txt = f"PREVIOUS ANSWERS:\n{'; '.join(previous_answers)}"
> generator_cheatsheet_content = f"{generator_cheatsheet_content}\n\n{previous_answers_txt}"
> --- `dynamic_cheatsheet/language_model.py`

#### MEM-OBJ-container-id
Label: container_id and opaque hosted state

Source-native identity: wrapper `container_id`, either a supplied identifier, created OpenAI container identifier, or Claude `native` sentinel. Form/storage: symbolic identifier in the Python object; hosted payload form and storage remain opaque. The identifier is not a text summary of hosted files or interpreter variables. Closest supplied record [RT-RTE-provider-execution](runtime.md#rt-rte-provider-execution) is the route, not an object counterpart. SRC-1, `dynamic_cheatsheet/language_model.py`, `text_generation/simple_unified_client.py`.

OpenAI sends the identifier on later calls in a benchmark run; the source does not expose what state actually survives or which tool invocations consume it. Claude's sentinel enables a tool request and does not establish an equivalent persistent container. The provider controls any hosted state admission, expiry and isolation; those facts are uninspected. Local admission is caller selection/session creation, not approval of individual hosted writes. Only returned text enters the sheet/trace loop. Neither hosted state nor container ID is part of the driver's saved continuation envelope. This permits a bounded statement of a requested persistent-container channel, not observed cross-query tool-state reuse.

> "tools": [{"type": "code_interpreter", "container": container_id}],
> --- `text_generation/simple_unified_client.py`

> return response.output_text
> --- `text_generation/simple_unified_client.py:1151-1151`

#### MEM-OBJ-messages
Label: UnifiedLLMClient messages history

Source-native identity: adapter `self.messages`, a process-local list of role/content mappings. Form: symbolic role/message structure containing natural-language conversational text. Distinct from [RT-OBJ-output-dict](runtime.md#rt-obj-output-dict) and from the wrapper's explicitly passed call histories. Ordinary chat turns are current conversation accumulation rather than derived retained memory under this contract. The material context-control surface is whole-list reset/replacement in [MEM-RTE-history-controls](#mem-rte-history-controls). SRC-1, `text_generation/simple_unified_client.py`.

`chat` stores original user message and assembled response; it does not store separately injected Tavily search context as a user turn. It therefore cannot be assumed to preserve every input visible to the producing call. No adapter-owned disk persistence is established by these history APIs. Human versus computational authorship of caller-supplied history is unresolved.

> self.messages.append({"role": "user", "content": message})
> self.messages.append({"role": "assistant", "content": full_response})
> --- `text_generation/simple_unified_client.py`

### Routes

#### MEM-RTE-history-controls
Label: Adapter history replacement and reset affordance

Distinct from [RT-RTE-context-selection](runtime.md#rt-rte-context-selection): this operates on adapter conversation history, not a cheatsheet or benchmark corpus. An external API caller can inspect a shallow list copy, replace history with a supplied list, or clear it. Admission of replacement is an unchecked caller-supplied list copy; the setter does not establish human content approval or any correctness oracle. No benchmark caller of these controls was found in the inspected driver/wrapper. This is an exposed context-state capability, not an established cross-session memory read-back route. SRC-1, `text_generation/simple_unified_client.py`, `dynamic_cheatsheet/language_model.py`, `run_benchmark.py`.

- Immediate return: chat returns assembled response; getter returns a shallow copy; reset/set mutate list state without returning a replacement answer.
- Later read-back: inapplicable — no shipped retained-artifact reload caller is established; ordinary subsequent chat history is current conversation state.
- Delegated visibility: adapter `generate` includes current `self.messages`; wrapper `generate_from_messages` instead consumes its explicit supplied messages without history management.
- Selection predicate: external caller decides reset/set and supplied content; `generate` includes all current list entries, with no relevance filtering.
- Invalidation or expiry: reset drops the whole list, set replaces it; discarded material has no adapter-owned recovery route here; caller may retain and later set a copy.
- Activation or effect: exposed whole-history replacement can alter subsequent adapter input; no compliance or benefit demonstrated.
- Evidence limits: unspecified external callers establish a capability only, not deployed persistence or a benchmark consumer route; shallow copying does not isolate nested mappings.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

> self.messages = messages.copy()
> --- `text_generation/simple_unified_client.py`

> self.messages = []
> logger.info("Conversation history cleared")
> --- `text_generation/simple_unified_client.py`

> messages.extend(self.messages)
> messages.append({"role": "user", "content": prompt})
> --- `text_generation/simple_unified_client.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-cumulative-update](runtime.md#rt-rte-cumulative-update)

Trace-fed transformation: current question + full generator text + old sheet → curator call → extraction → replacement sheet → next round/query generator and next curator. Local execution feedback can enter the full text; native tool details enter only insofar as returned as text. This is a wired automatic write of experience-derived guidance, not merely raw-log storage and not demonstrated improved capacity. SRC-1, `dynamic_cheatsheet/language_model.py`.

Curation is model-authored and computationally admitted; there is no per-replacement human approval gate in the inspected call. Prompt requests include correctness review, deduplication, generalization, source references and usage counts. Software accepts any extractable body, including an empty body, and keeps the old sheet only when extraction falls back. Curator prose outside the body does not cross to later generators and is not included as a separate curator-output field in these returned steps. Reasons embedded inside the body can cross, but preservation of a criticism/result/blame chain is not guaranteed. These are local update/read-back facts, not an assessment of all theory-builder conditions.

The curator receives a fresh one-message context; the generator receives a different one-message context. This resembles an isolated frame with only the extracted return escaping into live reference state. It is not heap-style liveness management: text is copied by value, earlier logged sheets do not become model-followable references, and omission has no automatic reload. `max_tokens=2 * max_tokens` bounds requested curator completion, while the prompt's circa 2000–2500 words is advice, not measured sheet trimming. Hybrid generator gets retrieved examples too, but hybrid curator directly receives only old cumulative sheet and current generator output; retrieved examples can affect it indirectly through that output.

> cheatsheet_history = [{"role": "user", "content": cheatsheet_prompt}]
> --- `dynamic_cheatsheet/language_model.py:425-425`

#### On [RT-RTE-context-selection](runtime.md#rt-rte-context-selection)

Direction: the foreground workflow requests a solution; Python automatically selects/delivers memory without a model retrieval-tool request. Vector ranking uses the current question vector and prior question vectors, selecting whole input/output pairs. It is not an entry-level search inside the sheet, nor a ranking by success. The API default `retrieve_top_k=3` is a pair-count budget; slicing does not bound token count, and unvalidated negative values would have Python slice semantics. FullHistoryAppending takes all available paired outputs, also without a token budget. SRC-1, `dynamic_cheatsheet/language_model.py`.

Synthesis gives the curator selected raw pairs, previous synthesized sheet and next question; the resulting sheet reaches the generator immediately and can reach the next synthesis through caller handoff. It does not receive the just-generated current solution before that query's generation. Missing opening-tag fallback restores selected raw pairs rather than the prior sheet. Cumulative/hybrid post-answer and synthesis pre-answer therefore share extraction but have different trace inputs, timing and fallback content. The retrieval warning explicitly denies that prior solutions are authoritative truth:

> Note: These are the most similar previous problems and their solutions. Use them as reference, but verify correctness and adapt as needed.
> --- `dynamic_cheatsheet/language_model.py`

This passage is embedded in the hybrid reference string. In pure retrieval the longer analogous warning likewise asks critical use. These are model instructions, not trust enforcement. Omitted pairs remain in the caller corpus and can be selected later; omitted sheet entries require survival elsewhere to return. The automatic selector controls what is kept out, with only chosen pairs crossing into each fresh query context. There is no pointer-based reload available to the generator in the inspected wrapper; a later Python invocation must select/copy content again.

#### On [RT-RTE-benchmark-cycle](runtime.md#rt-rte-benchmark-cycle)

Storage/lineage: disk rows retain the reference, final raw output and step snapshots. Continuation restores the last non-null sheet and all final outputs. Human/file initialization is an admission alternative, overridden by a restored non-null sheet on continuation. There is no initialized-content verification. Writes are automatic serialization, distinct from content authorship or approval. SRC-1, `run_benchmark.py`.

Scoring results affect printed counters, not subsequent sheet admission or retrieval. A wrong solution can therefore remain in both text channels. Targets remain saved evidence for the evaluator rather than trusted reference fed to the curator. Old sheets can remain in prior rows even when dropped from the live sheet. Resume uses only the latest sheet, not an automatic search/merge of archived sheet versions; raw final outputs do regain normal retrieval access. The checkpoint is a best-effort whole-file rewrite, not an independent transactional memory store, as the supplied route explains.

#### On [RT-BAP-reference-context](runtime.md#rt-bap-reference-context)

Both derived guidance and raw examples reach a generator as text inside the user-message template. Their authority is model-interpreted advice and examples over later questions, not an executable entry schema or a guaranteed truth source. At the update consumer, the same sheet instead acts as previous content to preserve/refine. This separates guidance authority during solving from retention authority during curation. SRC-1, `prompts/generator_prompt.txt`, `prompts/curator_prompt_for_dc_cumulative.txt`, `dynamic_cheatsheet/language_model.py`.

#### On [RT-RTE-local-execution](runtime.md#rt-rte-local-execution)

The local continuation grows current-query history; it does not itself compact old turns. After the call, the rendered code/result transcript can reach a curator, then survive as derived reference text, or remain raw in `final_output` for future retrieval. Subsequent programs do not inherit subprocess variables through this channel. Deleting the temporary file is cleanup of execution input, not semantic withdrawal of any trace-derived sheet entry or undoing external effects. SRC-1, `dynamic_cheatsheet/language_model.py`; executor cleanup is supplied by the runtime record.

#### On [RT-RTE-provider-execution](runtime.md#rt-rte-provider-execution)

Returned text is not a complete hosted-state checkpoint. Only that display channel flows through normal extraction/curation. OpenAI's repeated container identifier exposes a separate potential cross-call state channel whose contents and actual consumers remain opaque; Claude's per-request native-tool sentinel does not prove the same persistence. No restored provider-state horizon follows from resuming JSONL. SRC-1, `text_generation/simple_unified_client.py`, `dynamic_cheatsheet/language_model.py`, `run_benchmark.py`.

## Write side

Acquisition and admission have three distinct controls. First, an API caller supplies initial text/corpora, or the driver reads an initialization file/restored rows and task vectors. These content sources need not be human-authored or approved. Second, generator outputs enter the raw corpus by unconditional append. Third, curator proposals enter live reference state through tag extraction, not truth checking. These mechanisms are captured in [MEM-OBJ-cheatsheet](#mem-obj-cheatsheet), [MEM-OBJ-final-output](#mem-obj-final-output), and the cumulative/context-selection annotations. Starting a benchmark chooses the workflow, not each content decision.

Maintenance instructions ask to preserve useful old content, remove redundancy, revise explanations, replace inferior methods and increment successful-use counts. They establish requested semantic work, not reliable implementation of each semantic operation. The software's implemented transformation is prompt construction plus whole-body extraction/replacement. Missing tags can reject a proposal structurally; present tags bypass even a missing closing tag. Post-hoc oracle scores do not reject it ([RT-RTE-score-answer](runtime.md#rt-rte-score-answer)). No separate semantic rollback is wired. The operator could restart from an earlier file/sheet, but that is not a discovered automatic corrective route.

The trace-fed chain is explicit in the cumulative annotation; retrieval-synthesis is another chain from previously retained question/output records to derived next-question guidance. Derived reasons can survive only as selected body text. Archived step prompts expose some input lineage, but consumers do not automatically re-open those prompts when using a sheet. The repeated-round answer list supplies a smaller alternative retained form within one invocation. Neither raw logs nor these wired transformations alone establish successful learning or exercised self-improvement; this report makes neither claim.

## Read-back

[RT-RTE-benchmark-cycle](runtime.md#rt-rte-benchmark-cycle) establishes caller-owned read-back rather than a hypothetical storage API. The next example gets the updated sheet, and resume reloads sheet plus raw final outputs. [RT-RTE-context-selection](runtime.md#rt-rte-context-selection) determines the delivered parts: all prior pairs, top-k raw pairs, synthesized guidance, cumulative guidance, or hybrid guidance plus examples. Default deliberately injects `(empty)`. The notebook's passed-forward sheet is supported by supplied runtime evidence; it is not an independently inspected run observation.

The generator interprets selected retained text, while the curator interprets prior guidance and solution records for replacement. Selection and delivery are wired; reliance, correctness and performance effects are not observed here. Generator/curator freshness keeps unselected material outside the window; a model cannot follow question references or old-sheet pointers by itself because no corresponding reload tool is exposed. All-history mode avoids semantic selection but still does not establish context fit. Word advice, pair limits and completion limits are different budgets, none a validated total-input bound (SRC-1, wrapper and prompt paths cited above).

The adapter's reset/set capability is a separate context-control surface, not hidden benchmark memory. Reset removes all current list content; set can reintroduce caller-retained messages. Its hypothetical external caller does not establish a deployed reload route. Hosted containers are a separate opaque alternative, and their read-back cannot be inferred from the human-readable output summary ([MEM-OBJ-container-id](#mem-obj-container-id)).

## Integration issues

- **Qualification of irreversible loss.** The cumulative prompt's omitted-content warning applies to the live sheet, not every retained representation. Earlier JSONL sheets and raw final outputs can remain on disk; only raw final outputs have a normal retrieval reload path. This qualifies the source doctrine, not the supplied runtime, which already distinguishes archives. Evidence: SRC-1, `run_benchmark.py`; [MEM-OBJ-cheatsheet](#mem-obj-cheatsheet), [MEM-OBJ-final-output](#mem-obj-final-output), [RT-RTE-cumulative-update](runtime.md#rt-rte-cumulative-update).
- **Additional adapter surface.** [MEM-RTE-history-controls](#mem-rte-history-controls) adds inspected reset/replacement affordances left uninspected in the boundary's standalone-adapter coverage. It does not duplicate the benchmark's [RT-RTE-context-selection](runtime.md#rt-rte-context-selection), and no benchmark integration is inferred. The material missing fact is an external retained-history caller; its absence from this inspection prevents claiming a deployed reload route.
- **Opaque hosted state.** [MEM-OBJ-container-id](#mem-obj-container-id) separates ID, payload and returned display. The source does not establish payload form, persistence duration, internal admission or actual reuse; therefore a complete hosted-memory characterization is unavailable. Related route: [RT-RTE-provider-execution](runtime.md#rt-rte-provider-execution).
- **Initial vector and corpus provenance.** [MEM-OBJ-input-embeddings](#mem-obj-input-embeddings) establishes the loader/selector, not generation lineage, vector correctness or dataset independence. Available payloads/results remain uninspected; this prevents quality/leakage/benefit conclusions without weakening the positive selection wiring.
- **Identity comparison.** The sheet, final output and previous-answer list are explicit parts of [RT-OBJ-output-dict](runtime.md#rt-obj-output-dict), not replacement envelope records. Numerical inputs, hosted identifier/state and adapter messages are distinct objects, with their closest supplied counterparts stated in their declarations. No other possible duplicate and no correction to a supplied runtime fact is identified.

## Limitations and checks

The source checkout HEAD was rechecked as `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`. All new source anchors remain SRC-1; the supplied job, worker rules, member types and records contract governed this report. Source reading and static searches only were used; no target tests, fixtures, examples or provider requests ran. Historical result content was not inspected, so this report does not authenticate a worked memory update or measured outcome. Prompt instructions support requested behavior only. Provider-state uncertainty and unresolved vector provenance remain local to their records.

Deterministic validation: passed using the invocation's prepared `commonplace-validate` with the artifact directory and role `memory`. This checks content form and quotation occurrence, not semantic correctness, operation or job acceptance.
