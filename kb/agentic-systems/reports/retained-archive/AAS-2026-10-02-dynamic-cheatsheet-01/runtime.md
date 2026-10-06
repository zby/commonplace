---
type: agentic-systems/types/agentic-system-runtime-report.md
description: "Runtime baseline of Dynamic Cheatsheet's caller-supplied query memory, generation routes and execution paths"
run-id: AAS-2026-10-02-dynamic-cheatsheet-01
reviewed-boundary: "5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9"
---

# Dynamic Cheatsheet runtime report

## Runtime account

### Ordinary shipped invocation

The repository exposes `LanguageModel.advanced_generate` as the main query interface and documents a sequential cumulative-cheatsheet call. The caller supplies the model name, current question, generator and curator templates, and current cheatsheet. The wrapper resolves the provider prefix and model identifier, constructs a `UnifiedLLMClient`, then submits the rendered generator prompt as a one-message user history. The configured model produces a response; `extract_answer` derives the returned answer field. In the cumulative route the same wrapper then calls the configured model again with the question, complete generator response and old cheatsheet. `extract_cheatsheet` accepts the text between `<cheatsheet>` tags, otherwise retaining the old string. `max(1, max_num_rounds)` controls repetitions; later rounds use the cheatsheet from the previous round and may add prior answers. The method returns output, extracted answer, per-round strings, and final cheatsheet. The implementation does not own storage between calls: a caller must pass the returned string on a later invocation. The README shows this handoff. The implementation is inspected (`SRC-1`: `dynamic_cheatsheet/language_model.py`, `dynamic_cheatsheet/utils/extractor.py`); the handoff is documented (`SRC-2`: `README.md`). No execution trace or provider call was supplied, so operation, activation and benefit are unobserved.

> # Pass the updated cheatsheet to the next query to accumulate knowledge
> next_results = model.advanced_generate(
>     approach_name="DynamicCheatsheet_Cumulative",
>     input_txt="Question #2: 1 3 8 9",
>     cheatsheet=results['final_cheatsheet'],  # Reuse the cheatsheet
> --- `README.md:113-117` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> generator_output = self.generate(
>                     history=generator_history,
>                     temperature=temperature,
>                     max_tokens=max_tokens,
>                     allow_code_execution=allow_code_execution,
>                     code_execution_flag=code_execution_flag,
>                     use_code_interpreter=use_code_interpreter,
>                 )
>                 # Extract the output from the generator model
>                 generator_answer = extract_answer(generator_output)
>
>                 ## STEP 2: Run the cheatsheet extraction model with the generator output and the current cheatsheet
> --- `dynamic_cheatsheet/language_model.py:411-422` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> new_cheatsheet = extract_cheatsheet(response=cheatsheet_output, old_cheatsheet=current_cheatsheet)
>                 cheatsheet = new_cheatsheet
> --- `dynamic_cheatsheet/language_model.py:434-435` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

The triggering principal is the caller invoking the library. The caller owns each next-step choice, including whether to save and resubmit the returned cheatsheet. Within one call the wrapper owns deterministic ordering of generation, extraction, and (where selected) curation; the configured language model supplies generated content. The representation is caller-provided text for the cumulative cheatsheet and prompt, and strings of prior input/output pairs for history routes. Retrieval routes additionally consume caller-provided input embeddings. The library has no account, shared database, human approval UI, or durable cross-query memory service in the inspected boundary.

### Provider and execution boundary

The public `LanguageModel.generate` and `advanced_generate` paths call `UnifiedLLMClient.generate_from_messages`, which routes to provider-specific SDK clients with automatic retry. Provider selection is derived from the caller's model-name prefix; Together AI, DeepSeek and Ollama are routed through OpenAI-compatible base URLs, while OpenAI, Anthropic/Claude, Gemini, and xAI have separate branches. Provider request semantics, model versions behind mutable names, remote retention, and remote tool isolation are outside the frozen implementation boundary (`SRC-1`: `dynamic_cheatsheet/language_model.py`, `text_generation/simple_unified_client.py`). The code wrapper uses one selected model for both answer generation and curation; no separate critic, router model or embedding invocation is configured in the inspected core.

> _PROVIDER_MAP = {
>     "openai": "openai",
>     "anthropic": "claude",
>     "claude": "claude",
>     "gemini": "gemini",
>     "google": "gemini",
>     "xai": "xai",
>     "grok": "xai",
> --- `dynamic_cheatsheet/language_model.py:18-25` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> client_kwargs = {"provider": provider, "model": model_id, "max_retries": 3, "retry_delay": 10}
> --- `dynamic_cheatsheet/language_model.py:91-91` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

There are materially different execution paths. With ordinary `allow_code_execution=True`, code runs only when the model response contains the configured flag after a Python fence. The wrapper writes extracted text to a temporary `.py` file and starts `python3` as a local subprocess, collecting stdout and stderr with a three-second default timeout. The timeout and output capture do not establish a sandbox; the source itself marks security hardening as unfinished. The subprocess runs with the host process's available authority, and source inspection does not establish a deployed isolation envelope. This path can therefore perform side effects available to that process. Setting `use_code_interpreter=True` disables this local path. If a container ID exists, OpenAI uses a Responses API code interpreter tool with that ID; Claude uses its native code-execution tool. These remote environments and their persistence or isolation guarantees are provider-owned and uninspected. `create_container` is implemented only for OpenAI; Claude uses a sentinel ID. Gemini, xAI and OpenAI-compatible routes have no corresponding code-interpreter branch in this wrapper. Provider-native tools configured directly through `UnifiedLLMClient` also remain provider behavior, not a guarantee of the cheatsheet layer.

> if allow_code_execution and code_execution_flag in output:
>             pre_flag_text = output.split(code_execution_flag)[0].strip()
> --- `dynamic_cheatsheet/language_model.py:250-251` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> process = Popen(["python3", temp_file.name], stdout=PIPE, stderr=PIPE)
>         stdout, stderr = process.communicate(timeout=timeout)
> --- `dynamic_cheatsheet/utils/execute_code.py:83-84` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> "tools": [{"type": "code_interpreter", "container": container_id}],
> --- `text_generation/simple_unified_client.py:1131-1131` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> code_execution_tool = {"type": "code_execution_20250825", "name": "code_execution"}
> --- `text_generation/simple_unified_client.py:1191-1191` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

### Alternate query and state paths

`DynamicCheatsheet_RetrievalSynthesis` takes the final row of a caller-supplied embedding array as the current query embedding, computes cosine similarity against earlier rows, sorts descending and selects up to `retrieve_top_k` prior examples. It gives those input/output pairs, the next question, and the caller's previous cheatsheet to a curator call, then sends the extracted query-specific sheet to the generator. The synthesized sheet is returned; the wrapper does not retain it for later calls. `Dynamic_Retrieval` uses the same similarity-ranked prior pairs but skips synthesis. In `DynamicCheatsheet_CumulativeRetrieval`, the generator receives both the caller's cumulative sheet and retrieved examples; a curator updates the cumulative sheet after the answer. `FullHistoryAppending` constructs a prompt from prior inputs and outputs without curation. These variants differ in supplied state, selection and call sequence; all are method calls in one process and depend on callers supplying aligned input, embedding and output collections (`SRC-1`: `dynamic_cheatsheet/language_model.py`; `SRC-2`: `README.md`). No embedding producer or correctness oracle is inspected. The code uses similarity ranking as a selector, not an answer oracle.

> similarities = cosine_similarity([current_original_input_embedding], prev_original_input_embeddings)
>                 top_k_indices = np.argsort(similarities[0])[::-1][:retrieve_top_k]
> --- `dynamic_cheatsheet/language_model.py:510-511` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> combined_cheatsheet = cheatsheet
>             if retrieved_section:
>                 combined_cheatsheet = f"{cheatsheet}\n{retrieved_section}"
> --- `dynamic_cheatsheet/language_model.py:611-613` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

A separate lower-level route is the `UnifiedLLMClient` conversational interface. `chat` appends user and assistant turns to an in-memory `messages` list; callers can inspect, replace or clear it. `generate_from_messages` accepts a caller-owned message list without managing history and dispatches directly to a provider adapter. These routes bypass `advanced_generate`'s cheatsheet selection and curation logic. They expose a broader client surface, including search options, provider-specific request parameters, streaming, native code tools and raw prompts; controls at the advanced wrapper do not constrain direct client users (`SRC-1`: `text_generation/simple_unified_client.py`). The history list exists only in the client object unless the caller serializes it.

> # Update history
>         self.messages.append({"role": "user", "content": message})
>         self.messages.append({"role": "assistant", "content": full_response})
> --- `text_generation/simple_unified_client.py:1248-1250` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> Generate a response from a pre-built message list (no conversation history management).
> --- `text_generation/simple_unified_client.py:542-542` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

### Change admission, control and evidence limits

The cumulative curator proposes a changed cheatsheet after each answer. The wrapper admits its proposal inside the current call when the response includes the expected tags; otherwise `extract_cheatsheet` returns the previous cheatsheet. A later round in the same call consumes the admitted string. Across calls, the library only returns the string, so caller action determines whether it reaches another invocation; the caller can retain the previous returned step value or decline to resubmit the new string. No rollback store, version history or separate reviewer is implemented. The README-specified generator and curator templates are caller-supplied; template content is outside this boundary's Source register, so their substantive guidance and any persisted rationale are uninspected. Retrieval synthesis similarly returns a query-specific candidate sheet after tag extraction but does not write it to durable memory. The retrieval route's ranked candidates are chosen computationally by cosine similarity; no human adjudication or expected-answer oracle is wired in the inspected method (`SRC-1`: `dynamic_cheatsheet/language_model.py`).

Code execution admission is controlled by caller options and a textual trigger. In the local path, the caller can disable `allow_code_execution`; when enabled, the model's output must contain the configured flag and the preceding text must end in a code fence. The wrapper then runs the code without an approval prompt, with no source-grounded rollback or filesystem/network restriction. This enables capability use and possible production-environment side effects; which effects are available depends on the host process and deployment and is not established here. The alternate provider-native path is admitted by caller-selected `use_code_interpreter` and a previously available container or Claude sentinel. Tool execution and external recovery remain provider responsibilities.

The strongest implementation guarantees are local control-flow facts only: the cumulative route calls the curator after generation, the extractor returns the old sheet on missing tags, similarity code sorts candidates, and local subprocess execution is gated by a flag check. These are code properties, not evidence that model output is correct, that a provider honors a request, or that a cheatsheet changes later answers (`SRC-1`: `dynamic_cheatsheet/language_model.py`, `dynamic_cheatsheet/utils/extractor.py`, `dynamic_cheatsheet/utils/execute_code.py`). There is no inspected enforcement of durable storage, privacy, curation quality, reliable answer extraction, model pinning, or provider isolation. The source register includes no traces or experiments; all operational behavior and any performance benefit remain unobserved. The actual prompt templates, benchmark outcomes, dependencies' internals, and caller application state are outside this runtime evidence.

## Shared records

### Components


#### RT-CMP-1 — Configured language-model endpoint

- Source-native identity: the provider/model pair selected by `LanguageModel(model_name=...)`; this same configured endpoint handles answer generation, curation and retrieval synthesis in the wrapper.
- Representational form: distributed parametric language model accessed through provider SDK requests.
- Storage substrate: provider-operated model service or caller-selected local Ollama endpoint; endpoint internals are outside the boundary.
- Parameters change during operation: no parameter-update path appears in the inspected wrapper; prompts and supplied text vary per call.
- Exact version pinned: no. The wrapper sends a model identifier string and no immutable provider revision is registered.
- Mutable endpoint can resolve to another model: yes, for provider aliases or service deployments; actual resolution is uninspected.
- Evidence: `SRC-1` at `dynamic_cheatsheet/language_model.py` and `text_generation/simple_unified_client.py`; `SRC-2` at `README.md`. See the provider mapping and client configuration passages in Runtime account.

#### RT-CMP-2 — Caller-supplied embedding producer (identity unknown)

- Source-native identity: not identified; the inspected routes accept precomputed vectors and do not produce them.
- Representational form: an undisclosed distributed-parametric embedding model may have produced the supplied vectors; the inspected runtime consumes numeric vectors only.
- Storage substrate: caller-provided `original_input_embeddings` array in process memory; model endpoint and vector provenance are outside the boundary.
- Parameters change during operation: uninspected; no producer or version is available in the registered scope.
- Exact version pinned: uninspected; no producer identity or immutable version is supplied.
- Mutable endpoint can resolve to another model: uninspected; no endpoint is visible to the inspected route.
- Evidence: `SRC-1` at `dynamic_cheatsheet/language_model.py` consumes the supplied embedding array and computes cosine similarity. The boundary excludes embedding production, so no claim about its model or update behavior is made.

### Operative objects


#### RT-OBJ-1 — Cumulative cheatsheet string

- Source-native identity: the `cheatsheet` argument and returned `final_cheatsheet` value of cumulative routes.
- Representational form: caller-provided plain text, replaced by text extracted from a tagged curator response.
- Storage substrate: method arguments, local variables and returned dictionary during the call; durable storage is caller-managed and outside the inspected core.
- Evidence: `SRC-1` at `dynamic_cheatsheet/language_model.py` and `dynamic_cheatsheet/utils/extractor.py`; `SRC-2` at `README.md`. The return/handoff and tag extraction passages above show the mechanism; no backing store is present in the registered implementation scope.

#### RT-OBJ-2 — Retrieval corpus and embeddings

- Source-native identity: `original_input_corpus`, `generator_outputs_so_far` and `original_input_embeddings` arguments.
- Representational form: ordered strings and a caller-supplied numeric embedding matrix aligned by row.
- Storage substrate: passed in memory to `advanced_generate`; producer and durable backing store are caller-owned and excluded.
- Evidence: `SRC-1` at `dynamic_cheatsheet/language_model.py`, retrieval route. No validation of embedding provenance or corpus alignment is evidenced in the inspected route.

#### RT-OBJ-3 — Unified client chat history

- Source-native identity: `UnifiedLLMClient.messages`.
- Representational form: ordered user/assistant message dictionaries held in a Python list.
- Storage substrate: client-object memory; `get_history` returns a shallow copy, while `set_history` replaces it. Durable storage is not implemented by this object.
- Evidence: `SRC-1` at `text_generation/simple_unified_client.py`, chat and history methods.

#### RT-OBJ-4 — Code execution environment

- Source-native identity: local Python subprocess path or provider-native tool/container selected by the wrapper.
- Representational form: Python source extracted from a model response or tool instruction; captured output is returned as text.
- Storage substrate: local temporary file and host subprocess, or provider-managed code interpreter environment. Provider substrate and actual deployment isolation are uninspected.
- Evidence: `SRC-1` at `dynamic_cheatsheet/utils/execute_code.py` and `text_generation/simple_unified_client.py`.

### Routes


#### RT-RTE-1 — Cumulative cheatsheet generation and update

- Endpoints and progression: caller → `LanguageModel.advanced_generate` → configured LLM answer request → answer extraction → configured LLM curation request → tagged string extraction → returned result; repeated up to `max(1, max_num_rounds)`.
- Owner: caller supplies question, templates, initial sheet and cross-call persistence; wrapper orders requests and extracts fields; model proposes answer and candidate sheet.
- Context, state and action effects: generator receives question plus current sheet; curator receives question, full model answer and prior sheet. Successful tag parsing replaces the in-call sheet; subsequent rounds receive it.
- Decision roles: computational proposal is generated by the configured model; code decides admission by tag parsing and retains the prior sheet if tags are absent. No human reviewer or veto is wired. Across calls the caller decides whether to pass the returned sheet again.
- Answer oracle: none wired; no expected answer or reference outcome is passed to the route.
- Operating mode and improvement trigger: caller-triggered open query with a bounded, configurable within-call round loop; curator is invoked after each answer, with additional rounds only when configured above one. The prompt templates' guidance is uninspected because those template files are outside the Source register.
- Admission: proposed change is the curator's tagged sheet; extraction admits it automatically within the call. Missing tags reject the proposal by falling back to the old value. A caller can decline to persist or resubmit it; the previous per-step sheet is returned for caller-side recovery. No internal versioning or rollback store exists. The content that guided the proposal is the supplied curator template, whose inspected content and persistence cannot be determined from this boundary.
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Guarantee strength: protocol
- Immediate return: generated answer/output, extracted answer, each round's old/new sheet strings, and the final sheet are returned in a dictionary.
- Later read-back: within-call later rounds consume the extracted sheet; a later invocation reads it only if the caller supplies it.
- Delegated visibility: inapplicable — no delegated agent or worker is created by this route.
- Selection predicate: caller-selected approach and the supplied current cheatsheet; the wrapper iterates through the configured round count.
- Invalidation or expiry: inapplicable — the wrapper defines no expiry or invalidation rule; the caller selects the value supplied on the next call.
- Activation or effect: the string is delivered in the next in-call prompt, or in a later call if the caller resubmits it; whether it changes model behavior is unobserved.
- Evidence limits: `SRC-1` at `dynamic_cheatsheet/language_model.py` and `dynamic_cheatsheet/utils/extractor.py`; implementation is source-inspected; no generation trace, curator output, caller persistence, activation evidence or outcome comparison was supplied. The prompt template content is outside the registered evidence.

#### RT-RTE-2 — Retrieval-synthesis query route

- Endpoints and progression: caller → similarity ranking of prior embeddings → curator request over selected input/output examples and next question → tag extraction → generator request using the resulting query-specific sheet → returned answer and sheet.
- Owner: caller supplies corpus, embeddings, prior outputs, templates and current query; code ranks and serializes candidates; model synthesizes and answers.
- Context, state and action effects: the route reads earlier embedding rows and corresponding corpus/output entries, selects up to `retrieve_top_k`, then constructs a temporary sheet. It does not write persistent state.
- Decision roles: computation ranks candidates by cosine similarity and descending score; the model proposes the synthesized sheet and answer. No human selection, veto or adjudication is wired. No expected-answer oracle is supplied.
- Operating mode and improvement trigger: caller-triggered open query; one retrieval/synthesis/generation sequence per call. It has no bounded curriculum or adaptation trigger beyond the next caller request. Template content is uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: answer, selected inputs/outputs and a final sheet containing the current retrieved/synthesized context.
- Later read-back: inapplicable — the synthesized query-specific sheet is not internally retained; a later call can consume it only if the caller separately passes it as state.
- Delegated visibility: inapplicable — no delegated agent or worker is created by this route.
- Selection predicate: cosine similarity between the current query vector and earlier supplied vectors; descending top-k indices select examples.
- Invalidation or expiry: inapplicable — no cache invalidation or expiry is implemented; selection is recomputed from each supplied array.
- Activation or effect: selected examples and synthesized text are delivered to the generator; behavioral effect is unobserved.
- Evidence limits: `SRC-1` at `dynamic_cheatsheet/language_model.py`; only array-based ranking and call wiring are inspected. Embedding production, alignment correctness, model operation, prompt guidance, and answer quality are unobserved. No execution trace or oracle was supplied.

#### RT-RTE-3 — Cumulative cheatsheet with retrieval

- Endpoints and progression: caller → optional ranking of previous embeddings → generator with cumulative sheet plus retrieved examples → curator with answer and prior cumulative sheet → tagged extraction → returned result.
- Owner: caller controls all supplied state and cross-call persistence; wrapper assembles retrieved context and orders calls; configured model proposes answer and sheet update.
- Context, state and action effects: cumulative sheet is supplied state; retrieved examples are appended when more than one embedding row is present. The curator's accepted string becomes the returned cumulative candidate, not an automatic durable write.
- Decision roles: computation ranks retrieval candidates; model proposes answer/update; tag parser admits or rejects the update inside the call. Caller controls cross-call acceptance by whether it supplies the returned value. No human veto or answer oracle is wired.
- Operating mode and improvement trigger: caller-triggered open query, with optional retrieval and a curator call after each answer. No curriculum, correctness feedback loop or deployment update is established. Curator template content is uninspected.
- Admission: proposal is the curator's tagged cumulative string; successful extraction accepts it for return, missing tags retain the old sheet. Caller can decline to resubmit or recover the prior per-step string; no internal durable rollback exists. Supplied template is the only visible guidance interface, but its content is outside the Source register.
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: generated answer and final cumulative sheet, plus retrieved inputs and outputs.
- Later read-back: within-call generation reads the supplied cumulative sheet and examples; across calls the returned sheet is read only if caller persists and resubmits it.
- Delegated visibility: inapplicable — no delegated agent or worker is created by this route.
- Selection predicate: caller selects the cumulative-retrieval approach; if at least two embedding rows are supplied, code ranks earlier rows by cosine similarity and takes descending top-k.
- Invalidation or expiry: inapplicable — no built-in expiry or invalidation exists; caller supplies the next state.
- Activation or effect: retrieved examples and cumulative sheet are delivered in the generator prompt; activation is unobserved.
- Evidence limits: `SRC-1` at `dynamic_cheatsheet/language_model.py`; implementation call sequence and similarity code are inspected; no supplied execution trace, persistence evidence, activation or benefit measurement exists. Embedding and prompt producers are out of scope.

#### RT-RTE-4 — Full-history appending

- Endpoints and progression: caller → method formats prior input/output strings as previous solutions → generator request → returned answer.
- Owner: caller supplies aligned history; wrapper serializes it; model responds.
- Context, state and action effects: all supplied prior examples are appended verbatim to the current prompt; this path does not curate or update them.
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: answer/output and the formatted history prompt.
- Later read-back: later invocations consume history only when caller supplies it again.
- Delegated visibility: inapplicable — no delegated agent or worker is created by this route.
- Selection predicate: caller selects `FullHistoryAppending`; implementation formats supplied prior inputs and outputs without similarity filtering.
- Invalidation or expiry: inapplicable — no pruning or expiry is defined in the inspected method.
- Activation or effect: prior pairs are delivered to the model; behavioral effect is unobserved.
- Evidence limits: `SRC-1` at `dynamic_cheatsheet/language_model.py`; source establishes serialization only. No execution, activation or outcome evidence was supplied; caller storage and history alignment are uninspected.

#### RT-RTE-5 — Dynamic retrieval without synthesis

- Endpoints and progression: caller → cosine ranking over supplied prior embeddings → selected input/output pairs serialized with the current query → generator request → returned answer.
- Owner: caller supplies corpus, embeddings and prior outputs; code selects and formats examples; model answers.
- Context, state and action effects: selected prior examples form a temporary prompt section; no curator call or persistent update occurs.
- Decision roles: code ranks candidate examples by cosine similarity and descending score; no human adjudicator, model critic or expected-answer oracle participates in selection.
- Operating mode and improvement trigger: caller-triggered open query; selection reruns for each call. No bounded curriculum or retained selection history is implemented.
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: answer and selected input/output examples.
- Later read-back: inapplicable — selected examples are not retained by this route; a later call recomputes from caller-supplied arrays.
- Delegated visibility: inapplicable — no delegated agent or worker is created by this route.
- Selection predicate: descending cosine similarity of the current supplied vector to previous supplied vectors, limited by `retrieve_top_k`.
- Invalidation or expiry: inapplicable — no cache or expiry mechanism exists in the inspected method.
- Activation or effect: examples are delivered to the generator; any effect on the answer is unobserved.
- Evidence limits: `SRC-1` at `dynamic_cheatsheet/language_model.py`; embedding origin, row alignment and model behavior are outside the inspected evidence; no trace or oracle was supplied.

#### RT-RTE-6 — Direct unified-client generation and chat history

- Endpoints and progression: caller → `UnifiedLLMClient.generate` or `chat` → provider adapter and retry wrapper → returned provider text; `chat` appends the user and assistant turns to the in-memory list.
- Owner: caller constructs raw prompts and parameters; client assembles requests and routes them; provider generates output.
- Context, state and action effects: `generate` can combine an optional system message with stored messages and the new prompt; `generate_from_messages` accepts a prebuilt history without managing it; `chat` retains turns in the client object.
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: provider text or stream, with chat history updated after response.
- Later read-back: later `chat` calls read the in-memory message list until caller clears/replaces it or the client object is discarded; cross-process read-back requires caller persistence.
- Delegated visibility: inapplicable — the client does not create delegated agents or workers.
- Selection predicate: caller chooses direct client method, model/provider, message history and request options; no cheatsheet filter applies.
- Invalidation or expiry: inapplicable — no automatic expiry; caller may reset or replace history, and object lifetime bounds in-memory state.
- Activation or effect: stored messages are added to subsequent chat requests; effect on responses is unobserved.
- Evidence limits: `SRC-1` at `text_generation/simple_unified_client.py`; only client-side wiring and history mutations are inspected. Provider internals, external retention, execution traces and response effects are unobserved. This route bypasses `advanced_generate` controls.

#### RT-RTE-7 — Flag-triggered local Python subprocess

- Endpoints and progression: generated text → flag and terminal-fence checks in `LanguageModel.generate` → code extraction and temporary script → host `python3` subprocess → captured output appended to messages → another generation round or final return.
- Owner: caller enables or disables execution and configures the flag/depth; model proposes code; wrapper checks the text trigger and launches it; host operating system supplies process authority.
- Context, state and action effects: the prompt history is extended with code and execution output; script runs with whatever filesystem, network and process authority the host grants. Timeout defaults to three seconds; no sandbox or explicit approval is implemented.
- Admission: proposed change/action is model-generated Python. The caller's `allow_code_execution` value and the output flag/fence gate admission; there is no human approval step. Rejection is possible by disabling the option or not producing the trigger. No source-grounded rollback or recovery exists for external side effects; wrapper only returns stdout/stderr or timeout text. Prompts may shape the proposal, but prompt template contents are out of boundary. Any effects of executed code may persist according to host behavior, which is deployment-dependent and uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: execution output is appended to the returned model text; recursive generation continues while configured depth allows.
- Later read-back: current invocation sees appended execution output; effects outside the process may persist according to host behavior, but later consumers and persistence are uninspected.
- Delegated visibility: inapplicable — execution is a subprocess, not a delegated agent with a shared-memory protocol.
- Selection predicate: `allow_code_execution` must be true, the configured flag must occur, and the text before it must end in a code fence.
- Invalidation or expiry: inapplicable — no sandbox rollback or side-effect expiry is implemented; temporary script cleanup does not reverse process side effects.
- Activation or effect: source code is launched by the host process; actual effects are unobserved.
- Evidence limits: `SRC-1` at `dynamic_cheatsheet/language_model.py` and `dynamic_cheatsheet/utils/execute_code.py`; source inspection establishes the trigger and subprocess path, not a deployed security boundary or any execution result. No trace, host configuration or experiment was supplied.

#### RT-RTE-8 — Provider-native code interpreter

- Endpoints and progression: caller opts into `use_code_interpreter` and supplies/creates a supported identifier; `LanguageModel.generate` submits message history and tool selection to the OpenAI Responses API or Claude code-execution API; returned text goes to the caller.
- Owner: caller selects the option and provider; wrapper constructs provider tool requests; remote provider controls execution and environment.
- Context, state and action effects: OpenAI receives a container ID and messages; Claude receives a native code execution tool declaration. The wrapper disables local subprocess execution for this mode. Remote environment state, storage and isolation are provider-owned and uninspected.
- Admission: caller option and supported provider/container state admit the tool path; the model/provider determines tool use inside the request. The local wrapper offers no approval UI or rollback. Provider-side recovery and persistence are outside this boundary. Prompt contents that guide code proposals are uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: provider-returned output text.
- Later read-back: uninspected — the remote execution environment's persistence and later consumer are provider-controlled and excluded from the boundary.
- Delegated visibility: uninspected — remote tool execution is provider-owned; no access-control or visibility contract is registered here.
- Selection predicate: caller sets `use_code_interpreter`; OpenAI additionally requires a container identifier while Claude uses a sentinel; other provider prefixes take the ordinary generation path.
- Invalidation or expiry: uninspected — provider-side container lifecycle and tool-state expiry are not specified by the inspected wrapper.
- Activation or effect: request wiring is present; actual tool invocation and effects are unobserved.
- Evidence limits: `SRC-1` at `text_generation/simple_unified_client.py`; source establishes API request construction only. No provider call, container state, deployed isolation or execution trace was supplied.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-1 — Model-text authority to launch local Python

- Consumer: `LanguageModel.generate`.
- Channel: model response containing the configured execution flag after a Python code fence, when `allow_code_execution` is enabled.
- Force: automatic launch of a local Python subprocess after wrapper checks; no human approval or sandbox is established.
- Horizon: one recursive generation sequence, with host-side effects potentially outlasting the request depending on host behavior.
- Evidence: `SRC-1` at `dynamic_cheatsheet/language_model.py` and `dynamic_cheatsheet/utils/execute_code.py`. The trigger and subprocess passages in Runtime account support the path; actual host authority and effects are unobserved.

#### RT-BAP-2 — Model/provider tool authority to request remote code execution

- Consumer: provider API request assembled by `UnifiedLLMClient`.
- Channel: OpenAI code interpreter tool with a container ID or Claude native code execution tool, selected by caller options.
- Force: provider-side tool behavior after request; the wrapper does not mediate tool internals or offer a separate approval stage.
- Horizon: request and provider-managed environment; retention and lifecycle uninspected.
- Evidence: `SRC-1` at `text_generation/simple_unified_client.py`; no provider execution trace or isolation evidence is supplied.

## Annotations

none
