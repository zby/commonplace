---
type: agentic-systems/types/agentic-system-epistemic-report.md
description: "Epistemic routes of Dynamic Cheatsheet at commit 5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9"
run-id: AAS-2026-10-02-dynamic-cheatsheet-01
reviewed-boundary: "5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9"
---

# Dynamic Cheatsheet epistemic report

## Source-and-claim boundary

The question is whether and how Dynamic Cheatsheet acquires or produces truth-apt content, checks it, grants reliance, retains it for later use, and changes later behavior. The frozen boundary is the implementation and design material in the supplied Source register: `SRC-1` at commit `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9` and `SRC-2` for `README.md`. The caller, model provider, search services, supplied embeddings, external persistence, host process configuration and any enclosing application are excluded. The analysis treats outputs and prior answers as candidates whose correctness is unestablished. It does not infer operation from implementation or documentation.

The README makes claims about persistent, evolving memory (`EPI-CLM-1`), experience-driven learning without labels or human feedback (`EPI-CLM-2`), and benchmark performance gains (`EPI-CLM-3`). The implementation evidence supports within-call candidate generation, tag-based admission of a returned sheet, and caller-controlled reuse; it does not show epistemic acceptance or a correctness check. No execution trace, answer oracle, benchmark evidence, or causal experiment is supplied. The runtime records establish wired implementation paths, not that a model call or any later effect occurred.

| Entry point or operation | Source path | Coverage | Exclusion, uninspected reason, or conclusion prevented |
|---|---|---|---|
| `LanguageModel.advanced_generate` and its default, cumulative, retrieval-synthesis, cumulative-retrieval, full-history, and dynamic-retrieval branches | `dynamic_cheatsheet/language_model.py`; `dynamic_cheatsheet/utils/extractor.py` | `RT-RTE-1`, `RT-RTE-2`, `RT-RTE-3`, `RT-RTE-4`, `RT-RTE-5`; `EPI-OBJ-1`, `EPI-OBJ-2`, `EPI-OBJ-3`, `EPI-OBJ-4`; source-inspected deductions | Providers, templates, embedding production, caller state and execution traces are outside the registered evidence; content correctness, source warrant, activation and benefit remain unknown. |
| `LanguageModel.generate`, local code-execution branch and provider tool dispatch | `dynamic_cheatsheet/language_model.py`; `dynamic_cheatsheet/utils/execute_code.py`; `text_generation/simple_unified_client.py` | `RT-RTE-7`, `RT-RTE-8`, `RT-BAP-1`, `RT-BAP-2`; `EPI-OBJ-5`, `EPI-OBJ-6` | The host and provider execution environments are uninspected; no execution, side effect, approval or rollback outcome is observed. |
| Direct `UnifiedLLMClient.generate`, `generate_from_messages`, and `chat` | `text_generation/simple_unified_client.py` | `RT-RTE-6`, `RT-OBJ-3`; Tavily and provider-native search source-inspected at `SRC-1` | Provider and search-service behavior is outside the boundary; no returned search result, source citation, model response or later use is observed. |
| README usage and design claims | `README.md` | `EPI-CLM-1`, `EPI-CLM-2`, `EPI-CLM-3`, `SRC-2` | Documentation establishes stated design and claims only, not operation, evaluation evidence or causal attribution. |
| CLI dispatch and hooks | No CLI or hook implementation path appears in the frozen Source register; `README.md` contains usage examples | Unassessed | Whether a separate CLI or hook route changes admission, authority or consumers cannot be determined; this prevents a system-complete claim about those entry points. |
| Embedding generation, caller persistence and external application consumers | Outside registered source paths and the stated boundary | Excluded | Their provenance, checks, storage, activation and effects cannot be attributed to this library. |

The runtime report is the supplied account for the listed `RT-*` records. This member adds source-inspected direct-client web search because the runtime account does not cover that exposed operation. Its source wiring is described below; no provider operation is inferred. No separate hook is identified in the registered source scope, which is a scope limit rather than evidence of repository-wide absence.

## Epistemic-object inventory

| object ID | candidate truth-apt content or none | claimed role | evidence source ID and local anchor | gap/limit |
|---|---|---|---|---|
| `EPI-OBJ-1` | Returned generator answer text; truth-apt when it states a proposition over the query’s domain | Answer for the current query | `SRC-1` `dynamic_cheatsheet/language_model.py`; extraction in `dynamic_cheatsheet/utils/extractor.py` | No answer oracle, evidence-consuming acceptance, provenance validation or execution trace. |
| `RT-OBJ-1` | Caller-supplied cumulative cheatsheet string; may contain claims, instructions or non-truth-apt material | Context reused by cumulative routes | `SRC-1` `dynamic_cheatsheet/language_model.py`; `SRC-2` `README.md` | The caller’s text and curator-template guidance are not registered; no retained sheet instance or correctness evidence is supplied. The model’s proposed replacement is separately inventoried as `EPI-OBJ-8`. |
| `EPI-OBJ-2` | Caller-supplied prior input strings; may state facts but their content is not established | Retrieval keys/context paired with earlier answers | `SRC-1` `dynamic_cheatsheet/language_model.py` | Part of `RT-OBJ-2`; the inputs’ source, domain and warrant are unavailable. |
| `EPI-OBJ-3` | Caller-supplied prior generator outputs; truth-apt candidate answers may be present | Retrieved examples and input to later curation | `SRC-1` `dynamic_cheatsheet/language_model.py` | Part of `RT-OBJ-2`; output provenance, correctness, acceptance and source warrant are unknown. |
| `EPI-OBJ-4` | Numeric embedding rows; no truth-apt proposition is identified in the vectors themselves | Similarity ranking signal that selects which paired examples reach a generator or curator | `SRC-1` `dynamic_cheatsheet/language_model.py` | Part of `RT-OBJ-2`; producer, representation semantics, version, alignment and any validation are outside the boundary. |
| `RT-OBJ-3` | In-memory user/assistant message dictionaries, including candidate answer text on the direct `chat` path | Later prompt context within the client object | `SRC-1` `text_generation/simple_unified_client.py` | The role and provenance of each caller-supplied message are not validated; no client-object trace is supplied. |
| `EPI-OBJ-5` | Model-proposed Python source; executable content can encode claims and instructions but is not itself shown to be true | Candidate operation admitted by the local flag/fence trigger or provider tool request | `SRC-1` `dynamic_cheatsheet/language_model.py`; `dynamic_cheatsheet/utils/execute_code.py`; `text_generation/simple_unified_client.py` | Part of `RT-OBJ-4`; no execution result or host/provider execution evidence is supplied. |
| `EPI-OBJ-6` | Captured stdout/stderr or provider-returned execution text; truth-apt only insofar as it reports a named computation or environment state | Input appended to a later model generation, or returned to caller | `SRC-1` `dynamic_cheatsheet/utils/execute_code.py`; `text_generation/simple_unified_client.py` | Part of `RT-OBJ-4`; no independent check, output trace, or evidence that a later answer relied on it. |
| `EPI-OBJ-7` | Search-result title, URL and content strings from Tavily; truth-apt claims may occur in snippets | Context prepended to a direct client query | `SRC-1` `text_generation/simple_unified_client.py` | No counterpart among supplied operative-object records after comparison; the service response, source reliability and page contents are uninspected. |
| `EPI-OBJ-8` | Model response segment bounded by `<cheatsheet>` tags; candidate truth-apt content may be present | Proposed replacement for the current cumulative sheet | `SRC-1` `dynamic_cheatsheet/language_model.py`; `dynamic_cheatsheet/utils/extractor.py` | Part of `RT-OBJ-1` as the proposal stage of that sheet route; no trace, content-level criterion or reviewer. |

## Authority-route ledger

The table separates content generation and selection from operational admission. `implemented` means source inspection supports the wiring. No `observed` or causal status is assigned because the boundary supplies no execution trace or experiment.

| route ID | route function | architectural status | object/candidate ID | content/update relation | transition or check target | evaluator/condition and domain | activation and timing | possible or observed result | implemented force | epistemic authority and scope | operational authority: behavior permitted, blocked, or changed | behavioral-authority path: consumer, channel, force, horizon | evidence source ID and local anchor | claim IDs or none | mismatch marker or none | gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `RT-RTE-1` | content transformation | implemented | `EPI-OBJ-1`; current sheet `RT-OBJ-1` | `truth-apt transformation: indeterminate` — the model may restate supplied content, derive from it, or add claims; inspected output is unavailable to distinguish these | query plus current sheet to model response | Configured model proposes; no reference answer, evidence test or acceptance criterion is provided | Each selected generation call; operation unobserved | Candidate answer text | Returned as text to caller; no epistemic acceptance | None established beyond candidate status for this query | Caller may present or use the answer | Caller, returned text, advisory by interface, current call; later horizon depends on caller | `SRC-1` `dynamic_cheatsheet/language_model.py`; see `RT-RTE-1` | `EPI-CLM-1`, `EPI-CLM-2`, `EPI-CLM-3` | none | No provider response, answer check, or consumer trace. |
| `RT-RTE-1` | disposition/acceptance | implemented | `EPI-OBJ-8` | `truth-apt transformation: non-ampliative reshaping` — code trims and extracts the tagged segment; it does not establish that the model’s content preserves or improves the sheet’s meaning | Presence of `<cheatsheet>` in response; old string is fallback | Program checks tag syntax only, not truth, entailment, evidential fit or intended use | Immediately after the curator response in each cumulative round | Tagged segment replaces the in-call value, otherwise the previous value is returned | Automatic admission to returned string and later rounds | No epistemic authority licensed; syntax is the entire check domain | Allows the extracted string into the next round and return value; caller separately decides cross-call reuse | Wrapper, prompt context, permissive string admission, later round in same call; later calls only if caller resubmits | `SRC-1` `dynamic_cheatsheet/utils/extractor.py`, `dynamic_cheatsheet/language_model.py`; see `RT-RTE-1` | `EPI-CLM-1`, `EPI-CLM-2` | none | This is operational admission, not evidence-consuming acceptance for a stated use or scope. |
| `RT-RTE-2` | content transformation | implemented | `EPI-OBJ-2`, `EPI-OBJ-3`, `EPI-OBJ-4`; temporary sheet | `truth-apt transformation: indeterminate` — the curator may reorder, summarize, derive or add claims; no returned content is available to distinguish these | Selected input/output pairs and prior sheet to a curator response; tags bound returned segment | Similarity code selects examples; configured model proposes synthesis; neither is an answer oracle or content evaluator | Per retrieval-synthesis call before generation; operation unobserved | Query-specific candidate sheet | Delivered to current generator; not retained internally | No epistemic authority established for retrieved examples or synthesized claims | Changes the current generator prompt only; no durable write by the wrapper | Wrapper to generator, prompt context, permissive, current call | `SRC-1` `dynamic_cheatsheet/language_model.py`; see `RT-RTE-2` | `EPI-CLM-1`, `EPI-CLM-2` | none | Embedding producer, pair alignment, prompt content, provenance and activation are uninspected. |
| `RT-RTE-2`, `RT-RTE-3`, `RT-RTE-5` | operational admission/selection/consumption | implemented | `EPI-OBJ-2`, `EPI-OBJ-3`, `EPI-OBJ-4` | `no content change` to selected strings; rank/order selects supplied pairs, without checking their claims | Current embedding against earlier supplied vectors; top-k indices select paired input/output rows | Program computes cosine similarity and sorts; no human veto, expected-answer oracle, or correctness evaluator | At each retrieval call; cumulative retrieval only ranks when at least two rows exist | A selected, ordered subset of caller-supplied pairs | Prompt inclusion in generator or curator input | Similarity licenses relevance ranking under the supplied vector space only; it does not license truth or correctness | Determines which examples the current call consumes | Wrapper to generator/curator, prompt context, ranking and permissive inclusion, current call | `SRC-1` `dynamic_cheatsheet/language_model.py`; see `RT-RTE-2`, `RT-RTE-3`, `RT-RTE-5` | `EPI-CLM-1` | none | Vector semantics, alignment and retrieval effect are not established. |
| `RT-RTE-4` | operational admission/selection/consumption | implemented | Prior strings in `RT-OBJ-2` | `truth-apt transformation: non-ampliative reshaping` — pairs are serialized into a prompt; their truth is not changed or checked by serialization | All caller-supplied prior inputs and outputs | Program appends supplied pairs; no selection check or correctness criterion | Each chosen full-history call; operation unobserved | Formatted prior pairs and query are sent to the model | Prompt context only | No epistemic authority is added; supplied answers remain unchecked candidates | Changes current prompt context | Wrapper to generator, advisory context, current call | `SRC-1` `dynamic_cheatsheet/language_model.py`; see `RT-RTE-4` | `EPI-CLM-1`, `EPI-CLM-2` | none | Supplied history provenance, alignment and effect are unobserved. |
| `RT-RTE-6` | content transformation | implemented | `RT-OBJ-3`; answer candidate `EPI-OBJ-1` | `truth-apt transformation: indeterminate` — provider response may derive, import or conjecture; no output evidence distinguishes the possibilities | Raw caller prompt and optional prior messages to provider response | Provider model is opaque; no answer oracle or acceptance criterion is wired by the client | Each direct generation/chat request; operation unobserved | Text or stream returned; `chat` appends user and assistant turns | Returned to caller and available as later in-object chat context | No epistemic authority beyond unverified candidate text | Later chat requests may consume stored messages until caller clears, replaces or discards the object | Client object to provider, message channel, advisory context, object lifetime | `SRC-1` `text_generation/simple_unified_client.py`; see `RT-RTE-6` | none | none | Provider behavior, response correctness and later effects are unobserved. |
| `EPI-RTE-1` | content transformation | implemented | `EPI-OBJ-7` | `truth-apt transformation: acquisition/import` (source warrant unknown): Tavily result strings enter the prompt; provider-native search is also wired for supported client paths | Query to returned titles, URLs and snippets; then supplied as search context to model | Tavily service supplies results; code formats them. Native tools are provider-managed. Neither path includes an inspected source-quality check or answer oracle | Direct client `generate` only when caller enables configured Tavily search, or enables supported provider-native search; operation unobserved | Search context is prepended to prompt, or provider tool request is made; model response is returned | Search text can inform the generated answer; no separate acceptance gate | At most imported candidate material with unknown source warrant; no endorsement is established | Can change current prompt and model response; not automatically retained by this library’s chat list unless included in the prompt history by another caller action | `UnifiedLLMClient` to provider model, prompt/tool channel, permissive context, current request | `SRC-1` `text_generation/simple_unified_client.py` | none | none | Tavily/provider responses, cited page contents, provider tool execution and output provenance are unavailable. In OpenAI chat-completions code, native web search proceeds only for search-preview models; regular models log a warning and continue without a tool. |
| `RT-RTE-7` | behavior/policy adaptation | implemented | `EPI-OBJ-5`, `EPI-OBJ-6`, `RT-OBJ-4` | `non-truth-apt policy/content update: model text is admitted as executable code after the configured flag and fence checks` | Proposed Python source and its host-process effects | Wrapper checks a textual trigger only; host Python executes; no content check, approval, sandbox or rollback is established | When caller enables execution and response has the configured flag after a code fence | Captured output is appended to generation text; external effects are possible but unobserved | Automatic subprocess launch with host process authority | No epistemic license; output is an unchecked candidate result | Can execute operations allowed to the host and change the next generation context; side effects may outlast the request | `LanguageModel.generate` to host Python, execution channel, enforcing launch, recursive call and possible host-side horizon | `SRC-1` `dynamic_cheatsheet/language_model.py`, `dynamic_cheatsheet/utils/execute_code.py`; see `RT-RTE-7`, `RT-BAP-1` | none | none | Runtime permissions, actual execution, output correctness and effects are unknown. |
| `RT-RTE-8` | behavior/policy adaptation | implemented | `EPI-OBJ-5`, `EPI-OBJ-6`, `RT-OBJ-4` | `non-truth-apt policy/content update: caller-selected tool request delegates code execution to a provider` | Provider tool request and returned output | Wrapper constructs OpenAI/Claude requests; provider owns tool execution; no source-inspected result check or rollback | When caller selects supported provider option and required container/sentinel state; operation unobserved | Provider may return execution-informed text | Request wiring only; provider-side effects and control are outside inspected layer | No epistemic license established | Provider tool use may change returned text and provider environment; local wrapper does not admit a checked result | Client to provider tool, request channel, provider-controlled force and horizon | `SRC-1` `text_generation/simple_unified_client.py`; see `RT-RTE-8`, `RT-BAP-2` | none | none | Provider execution, visibility, persistence, isolation and outcome are uninspected. |

The deterministic extraction classifications above are source-inspected deductions from the inspected code. The tag parser can preserve the selected substring’s literal text, but that does not establish semantic preservation relative to a previous sheet because a model supplied the candidate text. Similarity ranking likewise establishes only computational ordering, not the quality of the paired answer.

> new_cheatsheet = extract_cheatsheet(response=cheatsheet_output, old_cheatsheet=current_cheatsheet)
>                 cheatsheet = new_cheatsheet
> --- `dynamic_cheatsheet/language_model.py:434-435` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> if "<cheatsheet>" in response:
>         try:
>             txt = response.split("<cheatsheet>")[1].strip()
>             txt = txt.split("</cheatsheet>")[0].strip()
>             return txt
>         except:
>             return old_cheatsheet
>     else:
>         return old_cheatsheet
> --- `dynamic_cheatsheet/utils/extractor.py:78-86` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> similarities = cosine_similarity([current_original_input_embedding], prev_original_input_embeddings)
>                 top_k_indices = np.argsort(similarities[0])[::-1][:retrieve_top_k]
> --- `dynamic_cheatsheet/language_model.py:510-511` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> if use_web_search and self.web_search_enabled:
>             query = search_query or prompt
>             search_context = self._web_search(query)
>             if search_context and not search_context.startswith("Web search failed"):
>                 prompt = f"Web Search Results:\n{search_context}\n\nUser Query: {prompt}"
> --- `text_generation/simple_unified_client.py:470-474` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> results.append(
>                     f"{idx}. {result.get('title', 'No title')}\n"
>                     f"   URL: {result.get('url', 'N/A')}\n"
>                     f"   {result.get('content', 'No content')}\n"
>                 )
> --- `text_generation/simple_unified_client.py:383-387` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> web_search_enabled: bool = False,
>         tavily_api_key: Optional[str] = None,
>         default_web_search: bool = False,
> --- `text_generation/simple_unified_client.py:105-107` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

## System-claim versus route comparison

| claim ID | claimed operation or warrant | claim source ID/anchor and evidence layer | doctrine/design support | implemented route IDs | observed-run support | causal support and design limits | supported conclusion | mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| `EPI-CLM-1` | Persistent, evolving memory across queries | `SRC-2` `README.md` (doctrine/design) | The README describes a growing knowledge base and demonstrates passing the returned sheet to a later call. | `RT-RTE-1`, `RT-RTE-3`; caller-owned handoff in `RT-RTE-1` | None supplied | None supplied; no comparison or persistence trace | The implementation returns an extracted candidate sheet and later calls can consume caller-resubmitted text. This supports a caller-mediated memory affordance, not library-owned durable persistence, truth, or successful evolution. | The README’s “persistent” wording is broader than the inspected library’s storage responsibility; no operation is observed. |
| `EPI-CLM-2` | Experience-driven learning without ground-truth labels or human feedback | `SRC-2` `README.md` (doctrine/design) | The README states the experience-driven learning and zero-shot claims. | `RT-RTE-1`, `RT-RTE-2`, `RT-RTE-3`, `RT-RTE-4`, `RT-RTE-5` | None supplied | None supplied; there is no capability measure, control comparison or attribution evidence | The routes can place caller-resubmitted sheets or prior examples into later prompts. No evidence shows improved future capacity or that a candidate update is correct. | The implementation has no evidence-consuming acceptance gate for learned content; whether the resulting behavior improves is unknown. |
| `EPI-CLM-3` | Benchmark performance gains, including Game of 24 and knowledge-intensive tasks | `SRC-2` `README.md` (doctrine/design) | Performance figures are stated in README; the boundary excludes benchmark notebooks, datasets and paper evidence. | `RT-RTE-1`, `RT-RTE-7` | None supplied | No inspected benchmark run, comparison design or causal evidence | Only that the README reports those outcomes. This run cannot validate the numbers or attribute them to a route or component. | Reported outcomes remain unsupported by the frozen evidence set. |

> A lightweight framework that gives language models (LMs) a persistent, evolving memory during inference time.
> --- `README.md:9-9` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> * **Experience-Driven Learning**: Bridges the gap between isolated inference events and cumulative learning
> --- `README.md:21-21` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> * **Puzzles**: GPT-4o's success rate on Game of 24 increased from approximately 10% to 99% after discovering and reusing Python-based solutions
> --- `README.md:26-26` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

## Bounded conclusion

The inspected library produces model-written answer candidates and, in cumulative modes, model-proposed cheatsheet text. Its only inspected check on a sheet proposal is whether expected tags appear; a successful parse admits the enclosed string for later rounds and return. That check does not assess truth, evidence, intended use or scope. The wrapper does not implement an answer oracle or an evidence-consuming acceptance decision. Returned text becomes later context only through another within-call round or caller resubmission.

Retrieval imports caller-supplied input/output strings with unknown provenance and warrant. Similarity ranks their paired vectors and chooses which examples enter a prompt. That rank licenses relevance only within the supplied vector space. Search-enabled direct clients can also insert external result snippets or request provider-native search; source warrant and the returned content were not observed. Neither path verifies imported claims. The client’s direct chat history can retain returned candidate text in the client object, but that does not endorse it.

Local Python execution is a consequential operational route. Caller configuration and a response trigger can launch model-proposed code with the host process’s authority, and captured output can enter another model request. This creates operational authority without an epistemic check; the actual execution environment and effects are unobserved. The provider-native tool route is wired but its execution, authority and persistence remain provider-owned and uninspected.

The README’s persistent-memory claim is supported only as caller-mediated reuse of returned text. The evidence does not establish durable library storage, accurate accumulated knowledge, experience-driven improvement, or the reported performance gains. CLI dispatch and hooks are outside the registered implementation paths, so their routes remain unassessed. No single epistemic verdict extends beyond these inspected paths.

## Shared records

### Operative objects

#### EPI-OBJ-1 — Returned answer candidate

- Source-native identity: answer text returned by `advanced_generate` or a direct client generation call.
- Representational form: natural-language model response, sometimes parsed from answer tags or a legacy answer format.
- Storage substrate: return value and, on `chat`, optionally the client’s in-memory message list.
- Distinct identity comparison: `RT-OBJ-3` covers the client message history, which can contain an assistant response, but not every `advanced_generate` return; this record denotes the returned answer candidate across the wrapper path. No distinct correctness or lineage record was supplied.
- Evidence: `SRC-1` at `dynamic_cheatsheet/language_model.py`, `dynamic_cheatsheet/utils/extractor.py`, and `text_generation/simple_unified_client.py`; see `RT-RTE-1` and `RT-RTE-6`.

#### EPI-OBJ-2 — Prior input strings

Part of: RT-OBJ-2

- Source-native identity: `original_input_corpus` entries aligned by index with supplied outputs and embeddings.
- Representational form: caller-provided text; propositions, questions and non-truth-apt task instructions may coexist.
- Storage substrate: caller-owned in-memory argument arrays/lists.
- Evidence: `SRC-1` at `dynamic_cheatsheet/language_model.py`; parent `RT-OBJ-2` is a broader heterogeneous grouping.

#### EPI-OBJ-3 — Prior generated output strings

Part of: RT-OBJ-2

- Source-native identity: entries in `generator_outputs_so_far` paired by index with prior inputs.
- Representational form: natural-language model output; may contain truth-apt answer candidates.
- Storage substrate: caller-owned in-memory list supplied to a call.
- Evidence: `SRC-1` at `dynamic_cheatsheet/language_model.py`; parent `RT-OBJ-2` groups these with inputs and embeddings despite their distinct content and epistemic role.

#### EPI-OBJ-4 — Supplied embedding rows

Part of: RT-OBJ-2

- Source-native identity: rows in `original_input_embeddings`, including the final current-query row.
- Representational form: numeric vectors; no proposition or truth condition can be identified from the registered implementation.
- Storage substrate: caller-provided numeric array consumed in process memory.
- Evidence: `SRC-1` at `dynamic_cheatsheet/language_model.py`; parent `RT-OBJ-2` also groups the paired text and output records. The producer remains unidentified (`RT-CMP-2`).

#### EPI-OBJ-5 — Proposed executable code

Part of: RT-OBJ-4

- Source-native identity: Python code extracted from model response or instructions submitted to a provider-native execution tool.
- Representational form: executable source text; its instructions may have effects, but no truth-apt claim is established by its syntax alone.
- Storage substrate: model response, temporary local Python file, or provider tool request.
- Evidence: `SRC-1` at `dynamic_cheatsheet/language_model.py`, `dynamic_cheatsheet/utils/execute_code.py`, and `text_generation/simple_unified_client.py`; parent `RT-OBJ-4` combines proposal text with execution environments and results.

#### EPI-OBJ-6 — Execution output text

Part of: RT-OBJ-4

- Source-native identity: captured stdout/stderr or provider-returned execution-related response.
- Representational form: plain text that may state a computation result or environment observation.
- Storage substrate: return string and, in recursive local execution, the next generation prompt; provider output otherwise returns to caller.
- Evidence: `SRC-1` at `dynamic_cheatsheet/utils/execute_code.py` and `text_generation/simple_unified_client.py`; parent `RT-OBJ-4` is heterogeneous across local and provider-controlled substrates.

#### EPI-OBJ-7 — Search result strings

- Source-native identity: title, URL and content values formatted from Tavily results for direct client generation; native provider search results are not exposed as inspectable strings in the registered code.
- Representational form: external natural-language snippets, potentially containing truth-apt claims.
- Storage substrate: temporary prompt string constructed by `UnifiedLLMClient.generate`.
- Distinct identity comparison: no supplied operative-object record covers this direct search-result prompt material; it is separate from the cumulative-sheet and example-array records.
- Evidence: `SRC-1` at `text_generation/simple_unified_client.py`; the result-formatting and prompt-insertion passages above support the implementation path.

#### EPI-OBJ-8 — Proposed cumulative sheet segment

Part of: RT-OBJ-1

- Source-native identity: the substring selected from a curator response between `<cheatsheet>` and `</cheatsheet>`.
- Representational form: model-authored plain text, potentially mixing factual propositions, strategies and instructions.
- Storage substrate: curator response, then local variable; on a successful tag parse it replaces the in-call sheet and is returned to the caller.
- Evidence: `SRC-1` at `dynamic_cheatsheet/language_model.py` and `dynamic_cheatsheet/utils/extractor.py`; the transient proposal is a part of the broader cumulative sheet route, not evidence of an accepted fact.

### Routes

#### EPI-RTE-1 — Direct-client web search

- Endpoints and progression: caller invokes `UnifiedLLMClient.generate` with Tavily search enabled or supported provider-native search selected; a query is sent to Tavily or a provider tool, result context is placed into the current prompt or provider request, and a model response returns to the caller.
- Owner: caller configures search and query; client formats Tavily snippets and assembles provider requests; external service and provider control retrieval and generation.
- Context, state and action effects: Tavily title, URL and content strings are prepended to the prompt; native provider search is requested only through supported provider paths. The library does not itself retain a validated source record.
- Decision roles: Tavily/provider retrieval chooses returned material; code performs formatting and insertion. No human reviewer, source-quality evaluator, expected-answer oracle or claim-level acceptance gate is wired.
- Answer oracle: none wired; search results serve as context, not a known-answer criterion.
- Operating mode and improvement trigger: caller-triggered open query; no bounded curriculum or correctness-feedback update is implemented. Search config can include provider-specific limits/filter settings, but no source validation method is registered.
- Admission: result strings are included when returned without the failure prefix; native provider tool use is requested according to client options and provider/model route. No epistemic check precedes prompt inclusion.
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Guarantee strength: no claimed guarantee
- Immediate return: provider response text or stream; Tavily snippets are intermediate prompt context.
- Later read-back: inapplicable — this route does not retain search results as library memory; caller may retain the returned answer outside the inspected boundary.
- Delegated visibility: uninspected — provider-native search internals and visibility are provider-owned.
- Selection predicate: Tavily query is `search_query` or prompt; provider-native search depends on caller option/configuration and provider-specific branch. OpenAI chat-completions only uses automatic search for search-preview models; ordinary models continue without a search tool.
- Invalidation or expiry: inapplicable — no local result cache or expiry is implemented in this route.
- Activation or effect: source code inserts Tavily result strings into the model prompt or requests native search; actual retrieval and effect on response are unobserved.
- Evidence limits: `SRC-1` at `text_generation/simple_unified_client.py`. Source inspection establishes request and prompt wiring only; external results, source reliability, provider behavior, operation, answer correctness and later effect are unknown.

### Claims

#### EPI-CLM-1 — Persistent, evolving memory

- Claimed operation: language models receive persistent and evolving memory during inference, including reuse of a returned sheet on a later query.
- Source: `SRC-2` at `README.md`; doctrine/design.
- Evidence: the README claim passage above and its two-call example; implementation paths `RT-RTE-1` and `RT-RTE-3`.

#### EPI-CLM-2 — Experience-driven learning without labels or feedback

- Claimed operation: repeated query experience yields cumulative learning without ground-truth labels or human feedback.
- Source: `SRC-2` at `README.md`; doctrine/design.
- Evidence: `README.md` feature claims; implementation candidate routes `RT-RTE-1`, `RT-RTE-2`, `RT-RTE-3`, `RT-RTE-4`, `RT-RTE-5`. The source contains no checked capability update or learning result in this boundary.

#### EPI-CLM-3 — Benchmark performance gains

- Claimed operation: performance improved on named mathematics, puzzle, arithmetic and knowledge-intensive benchmarks.
- Source: `SRC-2` at `README.md`; doctrine/design.
- Evidence: README performance claims, including the retained Game of 24 passage above. The boundary explicitly excludes the paper, benchmark notebooks, datasets and execution results.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
