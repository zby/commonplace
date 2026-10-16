---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "OS-Copilot memory: separately retained tool code, descriptions and vectors, curriculum read-back, and bounded working-context transformations."
run-id: AAS-2026-10-16-os-copilot-7cef03148c53-01
source-identity: "https://github.com/OS-Copilot/OS-Copilot"
reviewed-boundary: "f720af8807e49a92dda64572d2c6bc6c0ac7ee7e"
---

# OS-Copilot memory report

## Boundary and evidence

The included memory boundary follows FRIDAY's task, repair, tool-retention, maintenance and course routes, plus the shipped example and service context paths. Durable reusable code is not the only retained material: descriptions select it, vectors index descriptions, and course text becomes later curriculum context and executable task input. Ordinary graph state, logs, interpreter state and external file effects are distinguished from those read-back mechanisms.

All source references are SRC-1 at the frozen commit in [boundary](boundary.md). Direct reads covered `oscopilot/tool_repository/manager/tool_manager.py`, `oscopilot/modules/retriever/vector_retriever.py`, `oscopilot/agents/self_learning.py`, `oscopilot/modules/learner/self_learner.py`, `oscopilot/tool_repository/basic_tools/text_extractor.py`, responsibility-bearing portions of `oscopilot/agents/friday_agent.py`, `oscopilot/modules/executor/friday_executor.py`, `oscopilot/utils/utils.py`, `oscopilot/prompts/friday_pt.py`, and the Bing files and API server listed below. Scoped searches covered task/course entry points, modules, examples, tests and package setup for store writers, alternative retrieval, histories and summaries. These are implementation evidence, with prompt strings also supplying doctrine/design. Runtime findings supply the remaining entry-point, example, environment and UI details; they are not independent observations.

No target code, tests, providers or services were executed. External provider state and dependency internals are opaque; no access gap prevents reading the registered repository. Available but uninspected implementation remains an inspection limit. Linked external material, live desktop state, downloaded benchmarks and arbitrary generated programs are outside the evidence. This prevents empirical retrieval-quality, task-success, provider-retention and improvement conclusions.

| Entry point or memory operation | Source path, SRC-1 | Coverage and limits |
| --- | --- | --- |
| Task planning, Python generation and critique-based replanning | `oscopilot/agents/friday_agent.py`; `oscopilot/modules/retriever/vector_retriever.py` | Direct reads/search; [RT-RTE-task-execution](runtime.md#rt-rte-task-execution), [RT-BAP-tool-context](runtime.md#rt-bap-tool-context), annotations below. Different query inputs and payloads reach different calls. |
| Automatic admission and description extraction | `oscopilot/agents/friday_agent.py`; `oscopilot/modules/executor/friday_executor.py` | Direct reads; [RT-RTE-tool-admission](runtime.md#rt-rte-tool-admission), [MEM-OBJ-tool-code](#mem-obj-tool-code), [MEM-OBJ-tool-description](#mem-obj-tool-description). Repair-score/original-code mismatch remains consequential. |
| Reload, embeddings, metadata, add/overwrite/delete and maintenance CLI | `oscopilot/tool_repository/manager/tool_manager.py` | Entire file directly read; [MEM-OBJ-tool-vectordb](#mem-obj-tool-vectordb), [RT-RTE-manual-maintenance](runtime.md#rt-rte-manual-maintenance). Storage assertions are counts, not semantic or transactional consistency. |
| Direct getters, concatenated programs, all descriptions and model filter | `oscopilot/tool_repository/manager/tool_manager.py`; `oscopilot/modules/retriever/vector_retriever.py`; `oscopilot/modules/planner/friday_planner.py` | Manager/retriever directly read; scoped search found filter definition but no caller in searched roots. These exposed operations are capabilities, not additional established later-consumer routes. Planner helper's all-description access was searched, not traced as an alternate shipped invocation. |
| Curriculum initialization, lesson dispatch, save/merge and later design | `oscopilot/agents/self_learning.py`; `oscopilot/modules/learner/self_learner.py`; `oscopilot/utils/utils.py` | Direct reads; [MEM-OBJ-course](#mem-obj-course), [RT-RTE-course-learning](runtime.md#rt-rte-course-learning). One-stage and continuous paths differ in in-memory update. |
| Demo extraction | `oscopilot/tool_repository/basic_tools/text_extractor.py` | Entire file directly read; course annotation below. Last planner node's return value is used, not verified full-file extraction. |
| Explicit call frames, prerequisite context, judge truncation and reset | `oscopilot/utils/utils.py`; `oscopilot/modules/executor/friday_executor.py`; `oscopilot/modules/planner/friday_planner.py`; `oscopilot/environments/env.py` | Helper/reset directly read; prerequisite/judge/environment details also supplied by [RT-OBJ-tool-graph](runtime.md#rt-obj-tool-graph), [RT-RTE-feedback-repair](runtime.md#rt-rte-feedback-repair) and runtime account. No automatic conversational transcript reload established. |
| Registered service page cleaning, summary or query selection | `oscopilot/tool_repository/manager/api_server.py`; `oscopilot/tool_repository/api_tools/bing/bing_service.py`; `oscopilot/tool_repository/api_tools/bing/bing_api_v2.py`; `oscopilot/tool_repository/api_tools/bing/web_loader.py` | Entire files directly read; [MEM-RTE-page-context](#mem-rte-page-context). Adds an alternative context-reduction path beyond main-agent truncation. Dependency persistence/collection behavior uninspected. |
| Audio/image services, QA/API nodes | `oscopilot/tool_repository/manager/api_server.py`; `oscopilot/modules/executor/friday_executor.py` | Server directly read; remaining findings supplied by [RT-RTE-api-qa](runtime.md#rt-rte-api-qa), [RT-CMP-image-caption](runtime.md#rt-cmp-image-caption), [RT-CMP-audio2text](runtime.md#rt-cmp-audio2text). No separate durable service-memory consumer established; provider retention unknown. |
| LightFriday/vision histories, screenshots and OCR | `examples/light_friday/light_friday.py`; `examples/friday_vision/friday_vision.py` | Supplied [RT-RTE-example-loops](runtime.md#rt-rte-example-loops), [RT-CMP-ocr-service](runtime.md#rt-cmp-ocr-service), plus scoped search. Plain growing histories and saved images are not evidence of a later-session memory store. Full example internals not reread. |
| UI/log and evaluation output | `fronted/src/interface/api.js`; `examples/GAIA/run_GAIA.py`; `examples/SheetCopilot/run_sheet_task.py` | Supplied runtime/boundary findings. UI consumes raw log records for display; no checked route transforms benchmark results or UI logs into durable agent guidance. Full output-file semantics not independently inspected. |
| Static methods and providers | `oscopilot/prompts/friday_pt.py`; `oscopilot/modules/base_module.py`; `oscopilot/utils/llms.py` | Course prompt directly read; other method/provider findings supplied by [RT-OBJ-friday-prompts](runtime.md#rt-obj-friday-prompts), [RT-CMP-chat-model](runtime.md#rt-cmp-chat-model), [RT-CMP-tool-embeddings](runtime.md#rt-cmp-tool-embeddings). Static instructions are not accumulated experience; remote retention or training is uninspected. |

## Core ideas

1. **Retention and selection preserve different things.** Tool code and its extracted description persist in JSON and mirrored files. Chroma embeds the description, not the code or execution trace. Similarity selects names; JSON lookups supply payloads. Vectors therefore have access authority, while readable text has model-context authority ([MEM-OBJ-tool-vectordb](#mem-obj-tool-vectordb), [RT-BAP-tool-context](runtime.md#rt-bap-tool-context)).
2. **Feedback gates a candidate but does not become its durable explanation.** Automatic admission is completion/score-driven. The store keeps code and a docstring fragment, not the judge's score, critique, original task or outcome record as structured lineage. The repair identity defect also prevents treating the store as an archive of successfully tested programs ([RT-RTE-tool-admission](runtime.md#rt-rte-tool-admission)). Manual writes bypass that gate.
3. **Course memory records proposed lesson content, not demonstrated mastery.** Its next reader is told that prior courses are completed, although saving is not conditioned on verified lesson success. The last fifty dictionary entries bound the number of prior lessons in curriculum context; this is neither a token budget nor a recency-by-success policy ([MEM-OBJ-course](#mem-obj-course)).
4. **Main-agent context is assembled per call.** Graph dependency results, retrieved tools and explicit critique cross call boundaries; whole transcripts do not automatically cross. A registered page service supplies additional summary/query filtering. In contrast, examples accumulate turns rather than implementing the same frames. These mechanisms must not be conflated ([RT-RTE-task-execution](runtime.md#rt-rte-task-execution), [MEM-RTE-page-context](#mem-rte-page-context)).

## Shared records

### Components

#### MEM-CMP-web-summarizer
Label: BingAPIV2 web summarizer

Source-native identity: BingAPIV2.web_summarizer, a LangChain OpenAI completion wrapper. Distributed-parametric inference resides behind an external provider; text summaries are natural-language outputs in process memory. It is distinct from [RT-CMP-chat-model](runtime.md#rt-cmp-chat-model): separately constructed wrapper used by the page service's map-reduce chain, not BaseModule's configured chat adapter. No counterpart for this instance is declared in the supplied runtime. Evidence: SRC-1, `oscopilot/tool_repository/api_tools/bing/bing_api_v2.py`.

> self.web_summarizer = OpenAI(
>             temperature=0,
>             )
> --- `oscopilot/tool_repository/api_tools/bing/bing_api_v2.py`

This adapter requests inference, not parameter changes. Exact model/weights are not pinned here; dependency defaults and a mutable endpoint can select/change the implementation. Provider-side updates and actual defaults remain uninspected. Requested summarization is not evidence of faithful coverage.

#### MEM-CMP-web-sniptter-embed
Label: BingAPIV2 page chunk embeddings

Source-native identity: BingAPIV2.web_sniptter_embed. Distributed-parametric external embedding inference produces dense vectors used by request-time Chroma chunk search. It is a separate instance and corpus from [RT-CMP-tool-embeddings](runtime.md#rt-cmp-tool-embeddings), which embeds retained tool descriptions. Evidence: SRC-1, `oscopilot/tool_repository/api_tools/bing/bing_api_v2.py`.

> self.web_sniptter_embed = OpenAIEmbeddings()
> --- `oscopilot/tool_repository/api_tools/bing/bing_api_v2.py`

No parameter-update request is present in this path. Exact model/version is unpinned in this constructor; dependency defaults and provider endpoint mutability remain external. Provider-side changes are uninspected. These vectors do not demonstrate a persisted learned skill or cross-request page cache.

### Operative objects

#### MEM-OBJ-tool-code
Label: Retained tool code

Source-native identity: generated_tools[name]['code'], mirrored under tool_code/name.py. Symbolic Python source is stored in local JSON/files and an in-memory dictionary. At its established later consumer it is serialized text interpreted by a generation model, rather than automatically imported or invoked. This object is the retained output of [RT-RTE-tool-admission](runtime.md#rt-rte-tool-admission) and [RT-RTE-manual-maintenance](runtime.md#rt-rte-manual-maintenance), not a duplicate of either route or of the current-run [RT-OBJ-tool-graph](runtime.md#rt-obj-tool-graph). No supplied operative-object counterpart exists.

Lineage is generated candidate code or caller-supplied file content. Automatic scoring uses execution feedback, making this a trace-responsive retained-artifact write; raw feedback is not itself the stored payload. Generic manager callers leave initial authorship/human editing unresolved. New instances reload JSON; ordinary reads use the dictionary, not the mirrored Python file. Evidence: SRC-1, `oscopilot/tool_repository/manager/tool_manager.py`, `oscopilot/modules/executor/friday_executor.py`.

> self.generated_tools[program_name] = {
>             "code": program_code,
>             "description": program_description,
>         }
> --- `oscopilot/tool_repository/manager/tool_manager.py`

> with open(f"{self.generated_tool_repo_dir}/tool_code/{program_name}.py", "w") as fa:
>             fa.write(program_code)
> --- `oscopilot/tool_repository/manager/tool_manager.py`

The same code may contain comments or docstrings, but no structured admission rationale, score, critique, version or source-task field is persisted by this assignment. Reasons incidentally present in generated code remain candidate-dependent and unobserved. Count assertions cannot certify candidate identity or meaning.

#### MEM-OBJ-tool-description
Label: Retained tool description

Source-native identity: generated_tools[name]['description'], mirrored under tool_description/name.txt and embedded as Chroma document text. Natural language in local JSON/text files receives model interpretation during planning; it also supplies the input to embedding-based access. It is a distinct material part from [MEM-OBJ-tool-code](#mem-obj-tool-code): a first matching docstring fragment, not the full program, execution summary or admission rationale. Closest supplied record is [RT-BAP-tool-context](runtime.md#rt-bap-tool-context), a consumer path rather than this object.

Automatic extraction and manual add use equivalent regex patterns; direct add_new_tool callers can supply a description independently. Thus not every stored description has demonstrable docstring provenance. Evidence: SRC-1, `oscopilot/modules/executor/friday_executor.py`, `oscopilot/tool_repository/manager/tool_manager.py`.

> match = re.search(r'"""\s*\n\s*(.*?)[\.\n]', class_code)
>         if match:
>             first_sentence = match.group(1)
> --- `oscopilot/modules/executor/friday_executor.py`

This deterministic extraction is curation by truncating/selecting existing prose, not a model-generated explanation of generality. Failure to match raises NotImplementedError in automatic extraction; manual helper exits with an error. Natural-language description trust follows writer admission, not independent verification. Later planning receives description content from JSON, not similarity scores or a record of why the tool was admitted.

#### MEM-OBJ-tool-vectordb
Label: Tool description vector index

Source-native identity: Chroma collection tool_vectordb under generated_tool_repo_dir/vectordb. Dense embeddings support similarity; symbolic name IDs/metadata join the results to JSON. Local persistent Chroma storage is distinct from content files and from the external embedding model [RT-CMP-tool-embeddings](runtime.md#rt-cmp-tool-embeddings). Closest supplied referents are that model and the admission/retrieval routes, not this index object.

Lineage: add_new_tool embeds program_description and records name metadata. Manager initialization attaches to the persistent collection; equality of collection count and JSON length is asserted. No content-equivalence proof or dependency-internal persistence semantics follows. Evidence: SRC-1, `oscopilot/tool_repository/manager/tool_manager.py`.

> self.vectordb.add_texts(
>             texts=[program_description],
>             ids=[program_name],
>             metadatas=[{"name": program_name}],
>         )
> --- `oscopilot/tool_repository/manager/tool_manager.py`

At retrieval the query is embedded/searches this corpus; similarity scores are returned by the dependency but the manager discards them and keeps metadata names. No confidence threshold is applied in this function. Index authority is eligibility/ranking, not an instruction consumer and not evidence that selected code is correct.

> for doc, _ in docs_and_scores:
>             tool_name.append(doc.metadata["name"])
>         return tool_name
> --- `oscopilot/tool_repository/manager/tool_manager.py`

#### MEM-OBJ-course
Label: Retained course lessons

Source-native identity: SelfLearning.course and courses/software_package.json. Symbolic dictionary keys address natural-language lesson values; local JSON and in-process dictionaries retain them. Lesson values contain requested tasks, Input/Output and optional file path. They are not observed outcomes. This is the state traversing [RT-RTE-course-learning](runtime.md#rt-rte-course-learning), distinct from that route and from [RT-BAP-course-tasks](runtime.md#rt-bap-course-tasks); no supplied object counterpart exists.

Lineage: model design from software/package, optional demo-derived content and prior course. JSON extraction yields a dictionary; save_json merges keys into existing disk content. A reused key replaces text without maintaining old versions. Initial local file authorship/edits are unconstrained by this loader. Continuous mode updates self.course before attempting lessons; one-stage mode saves new content without updating that dictionary. Evidence: SRC-1, `oscopilot/agents/self_learning.py`, `oscopilot/modules/learner/self_learner.py`, `oscopilot/utils/utils.py`.

> json_content.update(new_json_content)
> --- `oscopilot/utils/utils.py`

> prior_course = json.dumps(dict(list(self.course.items())[-50:]), indent=4)
> --- `oscopilot/agents/self_learning.py`

Dictionary insertion order selects the last fifty entries, not timestamps or lesson outcomes. Existing-key replacement does not itself move that key to the end. Older entries remain on disk; the prompt truncation removes them only from the current design call. Reload exists at initialization, not as a demonstrated semantic search over old courses. The next model is explicitly instructed to regard Prior Course as completed:

> 9. Prior Course refers to the courses that have already been completed. If the Prior Course is not empty, you need to design new lessons based on the existing ones to learn more complex operations of the package, ensuring that these new lessons do not duplicate any lessons that are already in Prior Course.
> --- `oscopilot/prompts/friday_pt.py`

That claim has no corresponding checked pass/fail field in the persisted course dictionary. The course's next-design authority and task authority must remain separate from learned-capacity claims.

### Routes

#### MEM-RTE-page-context
Label: Service page context reduction
Part of: [RT-RTE-api-qa](runtime.md#rt-rte-api-qa)

This is the registered Bing load_pagev2 service subroute, a material part of the API/service route, not another task controller. HTTP caller URL/query → WebPageLoader cleaned HTML or PDF text → token count → whole text, map-reduce summary, or three query-similar chunks → page_content response. Service code owns branch selection; the summarizer model proposes summary text, while Chroma ranks chunks. The caller chooses URL/query. Generic API callers do not establish human authorship or per-response approval. Open information request, no expected-answer oracle or improvement experiment. Evidence: SRC-1, `oscopilot/tool_repository/manager/api_server.py`, `oscopilot/tool_repository/api_tools/bing/bing_service.py`, `oscopilot/tool_repository/api_tools/bing/bing_api_v2.py`, `oscopilot/tool_repository/api_tools/bing/web_loader.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: HTTP page_content containing cleaned full text at <=4096 counted tokens; otherwise a map-reduce summary when query is None, or joined retrieved chunks when a query is supplied.
- Later read-back: uninspected — the service wires transformed response delivery, not a durable page-memory reload; a generated API caller determines what is printed and hence what a later agent call actually receives. No concrete generated request/response trace is supplied.
- Delegated visibility: service receives URL/query; fetch host receives the URL request; external summary/embedding providers receive cleaned page content or chunks/query. This is not agent delegation.
- Selection predicate: GPT-4 tokenizer length chooses the 4096 threshold; query presence selects summary versus similarity. Chunk size is 4500 characters with zero overlap; similarity returns k=3 and joins page_content with literal ellipsis separators. No final model-context token cap is enforced here.
- Invalidation or expiry: raw/derived text is request-local in inspected code; no explicit persistent page cache, version history or reload is configured. Chroma dependency defaults and collection lifecycle are uninspected, so cross-request isolation is not guaranteed.
- Activation or effect: delivers reduced external content to HTTP caller; downstream interpretation and behavior change are unobserved. The summary is a requested lossy transformation, not an authenticated fact.
- Evidence limits: provider/dependency behavior and actual caller consumption remain unobserved; the endpoint's existence does not establish a persisted trace-learning loop.

> if(page_token_num <= 4096):
>             result = {"page_content": raw_page_content}
>         else:
>             if item.query == None:
> --- `oscopilot/tool_repository/api_tools/bing/bing_service.py`

> summarize_chain = load_summarize_chain(self.web_summarizer, chain_type="map_reduce")
>         main_web_content = summarize_chain.run(web_chunks)
> --- `oscopilot/tool_repository/api_tools/bing/bing_api_v2.py`

> chunSearch = Chroma.from_documents(web_chunks, self.web_sniptter_embed)
>         relatedChunks = chunSearch.similarity_search(query_str, k=3)
>         attended_content = '...'.join([chunk.page_content for chunk in relatedChunks])
> --- `oscopilot/tool_repository/api_tools/bing/bing_api_v2.py`

The loader removes selected HTML tags, IDs and classes and normalizes characters/whitespace before these branches. PDF text is extracted page by page. Its URL metadata and content+URL digest are not included in the returned page_content string by BingAPIV2.load_page. Thus the downstream text is not the raw page plus complete provenance. Empty-text fallback can also represent a loader exception rather than an empty source. There is no independent semantic approval, quality-based rejection or rollback of a summary. This is information/context curation, not admission of a durable capability.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-tool-admission](runtime.md#rt-rte-tool-admission)

The retained transformation chain is generated code plus task execution feedback → completion/generality score gate → original candidate code and extracted description → JSON/files/description vectors → later model context. Raw stdout, errors, judge critique and score affect admission but are not stored as structured evidence by ToolManager.add_new_tool. This preserves a behavior-shaping artifact without its evaluated lineage. The supplied record's repair-score/original-code counterexample applies before all these stores; copying to multiple substrates does not fix it. Evidence: SRC-1, `oscopilot/agents/friday_agent.py`, `oscopilot/modules/executor/friday_executor.py`, `oscopilot/tool_repository/manager/tool_manager.py`; the supplied route holds the minimum passages for the gate and defect.

Admission is software/model-controlled, not human approval merely because a person starts a task. Model authorship, software threshold selection, regex curation and filesystem I/O are separate contributions. Existing-name rejection is executor-level; direct manager writes can replace the same name. No atomic multi-store recovery or automatic expiry was established. Embeddings derive from description text rather than execution evidence ([MEM-OBJ-tool-vectordb](#mem-obj-tool-vectordb)).

#### On [RT-BAP-tool-context](runtime.md#rt-bap-tool-context)

Read-back is request-driven selection, even though the runtime automatically initiates it at planning/generation transitions. Initial task text selects up to ten names for descriptions; replanning critique selects description candidates; Python subtask description selects up to three names for code. Metadata names are dereferenced into in-memory JSON content. Scores, original admission reasons and separate mirror files are not delivered by these getters. No token/byte budget supplements these item limits in the inspected manager/retriever functions. Evidence: SRC-1, `oscopilot/agents/friday_agent.py`, `oscopilot/modules/retriever/vector_retriever.py`, `oscopilot/tool_repository/manager/tool_manager.py`.

Retained code is a model-facing example; future generated code, not retrieved-code identity, reaches Env. The consumer authority therefore depends on model interpretation and subsequent execution. Storage, retrieval and prompt delivery establish neither activation nor improved performance. Alternative exact getters and programs concatenation expose storage capabilities. The model-based tool_code_filter helper serializes candidates, requests an action name and fetches its code, but the scoped searches found no consumer call; it cannot replace the established similarity-to-generation route.

#### On [RT-RTE-manual-maintenance](runtime.md#rt-rte-manual-maintenance)

Manual add reads the selected file and extracts the first matching docstring fragment, contrary to its docstring's self._description description. Direct add_new_tool accepts supplied code/description without either extraction or agent scoring. CLI flags dispatch add first, else delete; they do not introduce a separate semantic approval gate. A tutorial-following human may supply/edit content, but generic library use leaves human control unresolved. Evidence: SRC-1, `oscopilot/tool_repository/manager/tool_manager.py`.

Withdrawal has distinct consequences for access and content. delete_tool removes the vector ID and disk JSON entry and mirror files, but leaves self.generated_tools unchanged. A current instance can still return deleted code through direct getters and report the name as existing. Moreover, a subsequent add writes the whole stale dictionary to JSON and can reintroduce the deleted metadata without reintroducing its vector; the count assertion may instead stop that add after partial index mutation. This follows from the deletion and full-dictionary write order, not from an observed crash. It qualifies global withdrawal, not the narrower normal search removal claim. The constructor requires the preexisting JSON file; making storage directories does not initialize it. Evidence: SRC-1, `oscopilot/tool_repository/manager/tool_manager.py`; [MEM-OBJ-tool-code](#mem-obj-tool-code) and [MEM-OBJ-tool-vectordb](#mem-obj-tool-vectordb) distinguish the affected substrates.

#### On [RT-RTE-course-learning](runtime.md#rt-rte-course-learning)

Acquisition combines supplied software/package labels, optional demo content and previously saved lesson text. TextExtractor runs the same task agent and takes the last planner node's return_val; it does not independently verify completeness or success. That call can also admit tools through the ordinary gate. SelfLearner extracts JSON from a two-message design request and SelfLearning dispatches each lesson as agent.run input. No lesson-success signal is read before save_json; routine caught failures can therefore be saved as prior course. The retained result is curriculum content, not a compacted trace of learned results. Evidence: SRC-1, `oscopilot/tool_repository/basic_tools/text_extractor.py`, `oscopilot/agents/self_learning.py`, `oscopilot/modules/learner/self_learner.py`.

> file_content = list(self.agent.planner.tool_node.values())[-1].return_val
> --- `oscopilot/tool_repository/basic_tools/text_extractor.py`

Selection keeps only the last fifty dictionary entries in later design prompts; older entries remain reachable by initialization reload but are again subject to the same selection rule. There is no corresponding semantic lookup over old lessons in these functions. New curriculum is model-authored and software-admitted; initialization can reload externally edited content, but no human decision is required for each new lesson. The later design consumer is asked to avoid duplicates and advance difficulty; the task consumer directly executes each lesson through the main agent. Neither requested progression nor saved courses establishes mastery ([MEM-OBJ-course](#mem-obj-course)).

#### On [RT-OBJ-tool-graph](runtime.md#rt-obj-tool-graph)

Working context retains selected dependency descriptions/return values rather than all intermediate traces. The graph and inner monologue reset on run; successor prompts receive direct prerequisite fields. Python-return extraction and selective serialization are current-run coordination, not a demonstrated cross-session memory route. A model call resembles an isolated frame only in selected-input delivery: no worker stack, reference-following heap or automatic full transcript exists. Values are copied to model messages, while explicit tool reload provides an independent store-access path. Evidence: SRC-1, `oscopilot/agents/friday_agent.py`, `oscopilot/modules/planner/friday_planner.py`, `oscopilot/utils/utils.py`; supplied runtime account and [RT-RTE-task-execution](runtime.md#rt-rte-task-execution).

> message = [
>             {"role": "system", "content": sys_prompt},
>             {"role": "user", "content": user_prompt},
>         ]
>     return llm.chat(message, prefix=prefix)
> --- `oscopilot/utils/utils.py`

#### On [RT-RTE-feedback-repair](runtime.md#rt-rte-feedback-repair)

Judge context drops the output suffix after the first 999 characters when output exceeds 1000; repair instead receives state.result. This is a code-selected lossy view, not learned summarization, and it leaves the fuller current execution state available locally. Critique and amended code feed later calls in the same repair loop; the durable store does not retain this sequence as rationale. Existing route quotations establish the cutoff and candidate flow. Evidence: SRC-1, `oscopilot/modules/executor/friday_executor.py`, `oscopilot/agents/friday_agent.py`.

#### On [RT-RTE-example-loops](runtime.md#rt-rte-example-loops)

Supplied implementation shows plain history accumulation of model response and result; vision adds screenshots/OCR. There is no demonstrated host compaction or later-session reload in that account. Saved PNGs and logs are raw artifacts until an actual later reader is established. These examples therefore do not support projecting FRIDAY's two-message context policy onto all shipped invocations. Evidence and limits: SRC-1, `examples/light_friday/light_friday.py`, `examples/friday_vision/friday_vision.py`, as quoted and traced in the supplied route; full internals were not independently reread.

## Write side

The two tool writers share physical storage but not admission. Automatic admission uses model judgment and a fixed threshold; executor refuses an existing name. Manual helper admission uses caller-selected file/name plus successful regex extraction; the lower manager operation can overwrite a name directly. None of these writes implies that a human approved the particular content. The extracted description is a deterministic content selection; embedding transforms that prose for search. Code/description files, JSON and index writes are sequential, with no demonstrated transactional rollback ([RT-RTE-tool-admission](runtime.md#rt-rte-tool-admission), [RT-RTE-manual-maintenance](runtime.md#rt-rte-manual-maintenance), annotations above).

The trace-responsive durable result is reusable code/description admitted using task feedback. It is not raw-log retention or a synthesized explanation of what went wrong. A repaired verdict can admit the original candidate. Rationale may exist transiently in critiques or logs but no later store reader receives it through tool lookup. Direct caller writes have unresolved original provenance; that uncertainty does not erase known subsequent extraction, embedding or overwrite behavior (SRC-1, `oscopilot/agents/friday_agent.py`, `oscopilot/modules/executor/friday_executor.py`, `oscopilot/tool_repository/manager/tool_manager.py`).

Course generation is a separate write mechanism. Model-proposed lesson JSON is used as task content, merged into disk state, and later described as completed. Save-after-dispatch is not success-conditioned admission, and continuous mode adds entries in memory before dispatch. Key replacement is maintenance without a versioned rejection history. No explicit withdrawal or quality rollback is present in these inspected course functions; older lessons excluded from the prompt remain on disk ([MEM-OBJ-course](#mem-obj-course)).

Page cleaning, summary and query selection operate on external content rather than task traces. They are context transformations, not evidence-responsive skill admission. Provider weights and static method prompts have no inspected update path from these writes. Host files/packages may persist after generated programs, but arbitrary generated payloads and their later consumers are unobserved; persistence alone cannot turn them into characterized memory mechanisms ([MEM-RTE-page-context](#mem-rte-page-context), [RT-OBJ-friday-prompts](runtime.md#rt-obj-friday-prompts), [RT-CMP-chat-model](runtime.md#rt-cmp-chat-model)).

## Read-back

Tool read-back is fully connected in source from manager initialization to similarity names, JSON payloads and planner/generator model inputs. It is a pull chain initiated automatically by task/replan/subtask transitions, not independent unsolicited memory supply. Query targeting and item limits are explicit; semantic correctness, model reliance and benefit are not. Direct APIs without a traced caller remain storage capabilities. A new manager requires JSON and an index whose counts agree; no guarantee follows that they describe identical tool content (SRC-1, `oscopilot/tool_repository/manager/tool_manager.py`; [RT-BAP-tool-context](runtime.md#rt-bap-tool-context)).

Course read-back is filename selection by software/package at initialization followed by last-fifty dictionary serialization at design time. Lesson values go to two consumers with different authority: design context for the learner and operative tasks for the agent. Neither gets a verified completion record. Demo extraction reuses the agent, so the extracted value is selected agent output, not independently trusted source text ([RT-RTE-course-learning](runtime.md#rt-rte-course-learning), annotation above).

Working-context removal is selective and local: main calls omit previous conversational turns, graph dependencies select predecessor fields, judge truncates output, and run reset discards graph/monologue. Stored tools can be reloaded explicitly; discarded full transcripts have no established analogous reload. Example histories are a different policy. Page service reduction supplies an HTTP response, but no concrete generated caller establishes how much reaches a later model; its natural-language result cannot be classified as a demonstrated durable memory update ([RT-OBJ-tool-graph](runtime.md#rt-obj-tool-graph), [RT-RTE-feedback-repair](runtime.md#rt-rte-feedback-repair), [MEM-RTE-page-context](#mem-rte-page-context)).

## Integration issues

- **Additional included service mechanism:** [MEM-RTE-page-context](#mem-rte-page-context) is explicitly a part of [RT-RTE-api-qa](runtime.md#rt-rte-api-qa), not a duplicate. It prevents treating output-prefix truncation as the only shipped context reduction. Its two external model instances are distinct from supplied chat/tool-embedding components. SRC-1, `oscopilot/tool_repository/api_tools/bing/bing_api_v2.py`, `oscopilot/tool_repository/api_tools/bing/bing_service.py`.
- **Withdrawal qualification:** the supplied [RT-RTE-manual-maintenance](runtime.md#rt-rte-manual-maintenance) already notes stale in-memory metadata. This report extends the consequence to possible reserialization by a later add, plus exact-getter/existence behavior. It does not contradict normal index removal. Global durable withdrawal and safe recovery are not established. SRC-1, `oscopilot/tool_repository/manager/tool_manager.py`.
- **Course truth boundary:** [MEM-OBJ-course](#mem-obj-course) and [RT-RTE-course-learning](runtime.md#rt-rte-course-learning) agree that saved prior-course text is not checked learning evidence. Dictionary order is insertion order, not timestamp recency; overlapping-key replacement does not refresh its position. The next-design prompt nevertheless labels prior material completed. This limits nonduplication/progression claims. SRC-1, `oscopilot/agents/self_learning.py`, `oscopilot/prompts/friday_pt.py`.
- **Unresolved service persistence/caller:** Chroma defaults, collection lifecycle and any actual generated caller output are uninspected for [MEM-RTE-page-context](#mem-rte-page-context). No cross-request cache, isolation guarantee or later-model uptake should be inferred. Source supports request-time transformation and response only. SRC-1, `oscopilot/tool_repository/api_tools/bing/bing_api_v2.py`.
- **Unresolved alternative consumer wiring:** exposed getters/programs/filter operations are not additional established later-consumer routes. The searched definition-only filter and planner helper remain available source, not evidenced absence. Their deployment would require caller tracing before expanding [RT-BAP-tool-context](runtime.md#rt-bap-tool-context). SRC-1, `oscopilot/modules/retriever/vector_retriever.py`, `oscopilot/modules/planner/friday_planner.py`, `oscopilot/tool_repository/manager/tool_manager.py`.
- **Record identity:** new tool objects and course object describe stored material, not replacements for supplied routes/authority paths; comparisons appear in each declaration. No possible duplicate requiring supersession was found. No correction to a supplied fact is required; these are added coverage and qualifications.

## Limitations and checks

The source checkout HEAD was rechecked as f720af8807e49a92dda64572d2c6bc6c0ac7ee7e and git status was empty before inspection. The supplied run/source identities and memory member contract were retained. Inspection remained read-only and within SRC-1; no prior analysis, target execution or external source was used. Supplied runtime findings remain explicitly distinguished from independent reads.

No observed activation, capacity comparison or causal intervention was supplied. Model compliance, retrieval quality, successful maintenance, persistence consistency, curriculum mastery, arbitrary generated-file reuse and provider-side retention remain unestablished. Known transformations and consumers are not erased by those limits. Static shipped method text, raw UI/benchmark logs, ordinary graph state and surviving host files are not automatically classified as retained experience. Full dependency/provider internals and alternative helper callers remain uninspected.

Validation: the required validate-output command passed: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” A content pass establishes structural and quotation checks, not semantic acceptance or benefit.
