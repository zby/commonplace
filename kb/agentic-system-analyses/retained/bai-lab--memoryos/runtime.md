---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "MemoryOS runtime baseline across JSON libraries, MCP, Playground, ChromaDB and evaluation at the frozen repository revision."
run-id: AAS-2026-10-16-memoryos-bb72a1b70e03-01
reviewed-boundary: "587ed7755c7aed179965792830ff1b5ad9a6fa92"
---

# MemoryOS runtime report

## Runtime account

### Work and evidence basis

MemoryOS implements memory-assisted dialogue and memory maintenance, not an enclosing autonomous tool-execution agent. A caller supplies identities, credentials, storage location and model configuration. Python code selects retained context, requests a textual completion and admits the resulting exchange. Additional model calls summarize dialogue, judge continuity and derive profile/knowledge content. These are fixed orchestration paths, not a model-controlled next-tool loop. The consequential work claimed is personalized, coherent dialogue; benchmark gains are separately attributed in [RT-CLM-dialogue-benefit](#rt-clm-dialogue-benefit).

All implementation findings below use SRC-1 at the boundary's commit. Inspection adds full Python orchestration, updater, retriever, storage and prompt reads; full MCP server and Flask application reads; ChromaDB orchestration, provider, retriever, long-term and short-term modules plus mid-term search and new-session/merge insertion; and the evaluation driver, scorer and selected utilities/update passages. Comparisons checked the JSON variants rather than presuming equivalence. No providers, tests, examples or target applications were executed. No supplied execution trace supports operation, activation, crash recovery or benefit. Correction inspection traces ChromaDB's shared session dictionary through insertion, backup-fed extraction and response enrichment. Evaluation storage internals still limit deeper evaluation claims; they are not unavailable evidence.

### Ordinary invocation and next-step ownership

The shipped Python demo constructs `Memoryos`, calls `add_memory` on supplied dialogue and then calls `get_response` (SRC-1: `memoryos-pypi/test.py`, `README.md`). Construction binds `user_id` and `assistant_id` to separate user/assistant JSON paths, reloads memory modules and binds an OpenAI-compatible client. The default assistant ID is shared unless overridden. Those identifiers select storage; they are not authenticated principals. [RT-RTE-dialogue-response](#rt-rte-dialogue-response) follows one turn end to end; [RT-RTE-memory-admission](#rt-rte-memory-admission) and [RT-RTE-profile-analysis](#rt-rte-profile-analysis) close its maintenance loop.

The foreground caller owns the request. The orchestrator owns every next step: three concurrent retrieval tasks, prompt formatting, one final model call, then admission before return. The model supplies answer content but does not choose an executor or issue executable tools through this interface. The executor's effects are provider requests and local memory I/O under the hosting process's authority. Context is reconstructed for each call, not maintained as an ever-growing provider conversation. Recent dialogue is included verbatim; older dialogue is selected through session/page similarity and a bounded result heap. The full current user profile is included separately. Assistant knowledge enters the system message; user facts, recent dialogue and historical pages enter the user message. These different authority channels are recorded in [RT-BAP-assistant-context](#rt-bap-assistant-context) and [RT-BAP-user-context](#rt-bap-user-context).

Working-context control is therefore code-owned selection and replacement of the input window, with externally stored pages reachable by later retrieval. Summaries guide selection without replacing all original pages. The system creates no sub-agent context frame in this route: worker threads perform fixed retrieval or analysis tasks, and their return values are combined by Python. This resembles retaining selected external state rather than a stack of delegated agents. No total input-token budget is enforced by the inspected prompt assembly; item-count bounds do not bound text length (SRC-1: `memoryos-pypi/memoryos.py`, `memoryos-pypi/retriever.py`).

The model components and their mutability limits are [RT-CMP-openai-client](#rt-cmp-openai-client), [RT-CMP-sentence-transformer](#rt-cmp-sentence-transformer) and [RT-CMP-bgem3-flag-model](#rt-cmp-bgem3-flag-model). Retained dialogue/profile updates are not weight training. Memory-specific revision assessments belong to the memory member; this baseline establishes callers, admission points and later consumers without equating extraction with learning or theory criticism.

### Alternate paths and forcing cases

Four source-level forcing cases challenge stronger readings of the ordinary path:

1. **Provider failure is still admissible dialogue.** The JSON client's exception handler returns an ordinary error string. `get_response` then calls `add_memory` without distinguishing it from a successful answer. Retrieval-task failures instead become empty lists. Thus a returned response or completed tool wrapper does not certify provider success or complete context. See [RT-RTE-dialogue-response](#rt-rte-dialogue-response).
2. **MCP retrieval does not close the response loop.** The server exposes add, retrieval and profile tools, not its bundled `get_response`. Retrieval delivers data to an external host, and a separate host call must store the subsequent interaction. `max_results` slices three retrieved lists but does not limit short-term history or profile output; the profile tool can return all knowledge. See [RT-RTE-mcp-access](#rt-rte-mcp-access).
3. **Playground imports and resets bypass dialogue generation.** Import admits caller-supplied assistant text; force-analysis bypasses the normal heat threshold; clear deletes user and assistant directories. Session selection is not identity ownership validation, and the import path proves that retained assistant text need not have come from the final-response model. See [RT-RTE-playground-control](#rt-rte-playground-control).
4. **Durable ChromaDB is not one atomic memory commit.** Vector collections use a persistent client, while short-term/profile/session metadata is accumulated in memory and written by `close`/`atexit`. A vector write and JSON metadata save have separate failure windows. Retrieval has additional keyword-model calls and attempts backup-fed chain enrichment, but successful new-session insertion deterministically overwrites its own page backup through a shared dictionary. Vector dialogue remains queryable subject to dependency success; those pages are unavailable to backup-fed extraction and chain enrichment even after a successful metadata save. See [RT-RTE-chroma-dialogue](#rt-rte-chroma-dialogue).

The evaluation driver is a further material alternate, not an execution trace of the Python product. It uses separate modules, imports benchmark dialogue into persistent files and answers benchmark questions without feeding those answers through the Python response-admission loop. Its reference-answer scorer is not a runtime admission oracle: [RT-RTE-locomo-evaluation](#rt-rte-locomo-evaluation).

### Guarantees, controls and external contracts

| Load-bearing property | Owner and enforcement point | Strength, coverage and counter-path | Separate conclusions and required external contract |
|---|---|---|---|
| Migrate before short-term deque eviction | `Memoryos.add_memory` checks fullness before append | protocol for the orchestrated JSON and ChromaDB add paths; direct short-term append still has bounded-deque eviction. Migration removes an old pair before model-assisted insertion succeeds, so this is not a no-loss invariant. | implementation conclusion status: wired. operation conclusion status: uninspected. Durable success requires successful embedding/model calls and storage writes; see [RT-RTE-memory-admission](#rt-rte-memory-admission). |
| Return after admitting the generated exchange | JSON/ChromaDB `get_response` | protocol on those response paths, not MCP retrieval, evaluation answers or raw provider calls. Admission may itself fail after model generation; storage save handlers can suppress I/O errors. | implementation conclusion status: wired. operation conclusion status: uninspected. No transactional end-to-end durability follows; see [RT-RTE-dialogue-response](#rt-rte-dialogue-response). |
| Bound retrieved page count | Retriever's heap and queue capacity | invariant on successful positive-capacity heap selection, not on total model tokens or all entry paths. MCP profile reads and direct short-term/profile inclusion are alternate channels. | implementation conclusion status: wired. operation conclusion status: uninspected. Assumes configured positive capacities and well-formed state; see [RT-RTE-mcp-access](#rt-rte-mcp-access). |
| Match response style, language and temporal relevance | Shipped natural-language generation prompt, interpreted by model | policy, not a local output validator. Provider token cap does not enforce 30 words or English. | implementation conclusion status: wired. operation conclusion status: uninspected. Requires external model compliance; see [RT-OBJ-generation-prompts](#rt-obj-generation-prompts). |
| Persist/reload retained state | JSON module save/load or ChromaDB provider plus `close` | best effort; per-file locks cover JSON writes within an instance, not the full read-modify-write operation or cross-instance/cross-file transactions. ChromaDB metadata has a different save horizon. | implementation conclusion status: wired. operation conclusion status: uninspected. Requires filesystem/dependency behavior and successful saves; see [RT-RTE-memory-admission](#rt-rte-memory-admission) and [RT-RTE-chroma-dialogue](#rt-rte-chroma-dialogue). |

The capability surface is local read/write/delete plus configurable model-network access, not a grant set of model tools. Current grants are credentials, configured endpoint and the hosting process's filesystem authority. Deployed isolation is unobserved: stdio MCP does not establish host approval policy, and Flask session lookup does not establish authorization to a claimed user ID. The inspected application accepts user IDs as strings, passes them into library storage paths, and runs its development server with `debug=True` on `0.0.0.0`; no deployment safety conclusion follows (SRC-1: `memoryos-playground/memdemo/app.py`, `memoryos-pypi/memoryos.py`, `memoryos-mcp/server_new.py`).

For materially equivalent escape/control paths, inspection covered final and maintenance model-client calls, direct memory APIs, MCP callbacks, Flask imports/clear, the durable variant and evaluation's separate provider client. A bounded search for tool/function dispatch, subprocess/exec, approval, sandbox and training tokens in these Python roots found the three MCP decorators and no model tool-dispatch implementation; this supports the narrow fixed-call account, not a claim about excluded hosts or dependency internals. No route here installs generated code, tools or production machinery. Static code/prompt changes remain repository maintenance; configurable endpoints can change externally supplied models. Docker copies the Python variant and installs dependencies but supplies no application `CMD` or `ENTRYPOINT` (SRC-1: `Dockerfile`). Package-registry equivalence and deployment launch success remain unobserved.

## Shared records

### Components

#### RT-CMP-openai-client
Label: OpenAI-compatible generation and maintenance models

Source-native identity: `OpenAIClient`, selected `llm_model` (default `gpt-4o-mini`). Representational form: distributed-parametric generation behavior behind a remote API; request/response envelopes are symbolic and their text is natural language. Storage substrate: provider-held weights, outside the checkout. Used by answer generation, summarization, continuity judgments and profile/knowledge analysis. The evaluation variant uses its module-global `gpt_client` rather than the instance's own OpenAI object (SRC-1: `memoryos-pypi/utils.py`, `memoryos-pypi/memoryos.py`, `memoryos-chromadb/utils.py`, `eval/utils.py`).

Parameters changing during operation: no training/update operation in these inspected callers; provider-side changes are uninspected. Exact version pinned: no immutable model revision is required by the default model name. Mutable endpoint: yes, the Python constructor and Playground accept base URLs/model names, and a provider may resolve the same name differently. This establishes model selection, not source-verified backend identity.

> self.client = OpenAI(api_key=self.api_key, base_url=self.base_url)
> --- `memoryos-pypi/utils.py`

> response = gpt_client.chat.completions.create(
>             model=model,
>             messages=messages,
>             temperature=temperature,
>             max_tokens=max_tokens
>         )
> --- `eval/utils.py`

#### RT-CMP-sentence-transformer
Label: SentenceTransformer embedding models

Source-native identity: `SentenceTransformer(model_name, **init_kwargs)` in the Python and ChromaDB utilities, with `all-MiniLM-L6-v2` as default; evaluation directly constructs `SentenceTransformer(model_name)`. Representational form: distributed-parametric encoder weights; its dense-vector outputs guide symbolic thresholds and ranking. Storage substrate: external model distribution/local loader cache, with in-process model and embedding caches in the main library (SRC-1: `memoryos-pypi/utils.py`, `memoryos-chromadb/utils.py`, `eval/utils.py`).

Parameters changing during operation: inspected route calls encode, not training. Exact version pinned: the default name supplies no immutable revision; caller kwargs may alter loading but actual resolved weights were not supplied. Mutable endpoint: no remote inference endpoint in this loader path, but resolving an unpinned model name/cache on a future load may supply different weights. Evaluation reloads a model per embedding call; main-library caching does not establish measured speedup.

> _model_cache[model_init_key] = SentenceTransformer(model_name, **init_kwargs)
> --- `memoryos-pypi/utils.py`

> embedding = model.encode([text], **encode_kwargs)[0]
> --- `memoryos-pypi/utils.py`

#### RT-CMP-bgem3-flag-model
Label: BGE-M3 alternative embedding model

Source-native identity: `BGEM3FlagModel`, selected when `bge-m3` appears in the configured embedding model name. Representational form: distributed-parametric weights and dense outputs. Storage substrate: externally loaded weights and process cache. Parameters changing during operation: encoding only in the inspected utility. Exact version pinned: no immutable default BGE revision is enforced by the library. Mutable endpoint: no inference endpoint in this loader path; model-name resolution remains external. Playground names a specific snapshot directory, but its unavailable local contents do not verify those weights (SRC-1: `memoryos-pypi/utils.py`, `memoryos-chromadb/utils.py`, `memoryos-playground/memdemo/app.py`).

> _model_cache[model_init_key] = BGEM3FlagModel(model_name, **init_kwargs)
> --- `memoryos-pypi/utils.py`

> result = model.encode([text], **encode_kwargs)
>         embedding = result['dense_vecs'][0]
> --- `memoryos-pypi/utils.py`

### Operative objects

#### RT-OBJ-generation-prompts
Label: Shipped generation prompts

Source-native identity: `GENERATE_SYSTEM_RESPONSE_SYSTEM_PROMPT` and `GENERATE_SYSTEM_RESPONSE_USER_PROMPT`. Representational form: natural-language instructions with symbolic formatting placeholders. Storage substrate: static Python source, formatted into two messages each turn. These are shipped method text, not accumulated read-back. They supply role, assistant knowledge, recent and retrieved dialogue, profile, query and optional metadata. `style_hint` is accepted but not interpolated by the inspected response method (SRC-1: `memoryos-pypi/prompts.py`, `memoryos-pypi/memoryos.py`).

> "Your task is to generate responses that align with these traits and maintain the tone.\n"
> --- `memoryos-pypi/prompts.py`

> "Please respond to the user's statement using the following format (maximum 30 words, must be in English):\n "
>     "When answering questions, be sure to check whether the timestamp of the referenced information matches the timeframe of the question"
> --- `memoryos-pypi/prompts.py`

### Routes

#### RT-RTE-dialogue-response
Label: JSON memory-assisted response

Endpoints/progression: caller query → `Memoryos.get_response` → parallel retriever → prompt assembly → `OpenAIClient.chat_completion` → `add_memory` → response string. Owner: Python orchestrator, not model-selected workflow. Construction reloads user JSON files and separate assistant JSON; caller chooses identities and model settings. The response request uses temperature 0.7 and `max_tokens=1500`. Retriever uses default session/page thresholds 0.1, knowledge threshold 0.01, five sessions, twenty knowledge entries per knowledge task, and seven final pages unless configured otherwise. Successful mid-term matches update access counts/heat and save state, so retrieval is not purely read-only (SRC-1: `memoryos-pypi/memoryos.py`, `memoryos-pypi/retriever.py`, `memoryos-pypi/mid_term.py`).

- Immediate return: generated/cleaned string after synchronous admission, including the client's error sentinel on a caught provider failure.
- Later read-back: admitted exchange and subsequently derived material can enter future query contexts after reload or same-instance retrieval.
- Delegated visibility: provider receives the assembled two-message context; retrieval threads receive the query and their corresponding memory module, not independent agent tasks.
- Selection predicate: semantic session/page thresholds and top-k/heap page selection; knowledge vector thresholds/top-k; all recent history and full profile bypass query ranking.
- Invalidation or expiry: short-term deque limits, mid-term LFU and long-term deque eviction affect future availability; no provider-side expiry contract is established.
- Activation or effect: code supplies memory to generation and writes its output; changed answers or successful personalization are unobserved.
- Evidence limits: implementation only; model compliance, provider success and save durability are not certified by return.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Operating mode: open dialogue requests, with caller/model computational contributions as above and no answer oracle. The raw query is a problem input, not a reference answer. Recovery: failed retrieval tasks become empty context lists; provider exceptions become text; prompt/admission exceptions outside these handlers may escape. There is no retry policy in the inspected wrapper.

> except Exception as e:
>             print(f"Error calling OpenAI API: {e}")
>             # Fallback or error handling
>             return "Error: Could not get response from LLM."
> --- `memoryos-pypi/utils.py`

> # 10. Add this interaction to memory
>         self.add_memory(user_input=query, agent_response=response_content, timestamp=get_timestamp())
>         
>         return response_content
> --- `memoryos-pypi/memoryos.py`

#### RT-RTE-memory-admission
Label: Dialogue admission and overflow migration

Endpoints/progression: direct caller or response path → `add_memory` → pre-append fullness check → updater migration if full → short-term append/save → heat analysis check. Owner: caller supplies the pair; code owns admission and model-assisted migration. Symbolic QA dictionaries hold natural-language dialogue. The updater pops while full, discards popped pairs missing either nonempty side, creates page/link metadata, requests continuity and multi-summary outputs, and inserts pages into matched or new sessions. A failed JSON summary parse uses a general-session fallback. The same batch is supplied to each returned theme, not proven partitioned by topic (SRC-1: `memoryos-pypi/memoryos.py`, `memoryos-pypi/updater.py`, `memoryos-pypi/utils.py`).

- Immediate return: no payload from `add_memory`; logs and in-memory changes, with JSON save attempts.
- Later read-back: short-term JSON reload and mid-term session/page reload feed future prompts, retrieval and analysis.
- Delegated visibility: maintenance model calls receive the dialogue needed for continuity, metadata and summary; local storage classes receive the derived dictionaries.
- Selection predicate: fullness triggers oldest-pair removal until no longer full; session merge uses embedding similarity plus keyword overlap against configured threshold.
- Invalidation or expiry: oldest short-term entries migrate; session count overflow invokes LFU eviction; continuity pointer is process-local rather than restored by initialization.
- Activation or effect: retained content becomes reachable for future retrieval; benefit and actual subsequent activation are unobserved.
- Evidence limits: pre-migration prevents the specific append-first deque loss but is not an atomic migration or completeness guarantee.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: caller proposes raw text; code admits without per-content human approval. Generic caller identity does not resolve human authorship. The model proposes summaries/continuity, code parses and applies them; malformed or empty summary output can select a fallback rather than reject the raw content. Guidance requests at most two themes and concise JSON summaries. No expected-answer oracle or candidate-quality experiment is used. Operating mode: ordinary admission under capacity rules. Rejection/rollback: no content-quality veto on the top-level pair and no transactional rollback across pop/embedding/insertion; direct storage mutation APIs remain callable. JSON saves catch `IOError`; malformed load can initialize empty state (SRC-1: `memoryos-pypi/short_term.py`, `memoryos-pypi/mid_term.py`, `memoryos-pypi/long_term.py`).

> if self.short_term_memory.is_full():
>             print("Memoryos: Short-term memory full. Processing to mid-term.")
>             self.updater.process_short_term_to_mid_term()
> 
>         self.short_term_memory.add_qa_pair(qa_pair)
> --- `memoryos-pypi/memoryos.py`

> qa = self.short_term_memory.pop_oldest()
>             if qa and qa.get("user_input") and qa.get("agent_response"):
>                 evicted_qas.append(qa)
> --- `memoryos-pypi/updater.py`

#### RT-RTE-profile-analysis
Label: Heat-triggered profile and knowledge admission

Endpoints/progression: after add or forced call → hottest heap session → unanalyzed pages → two concurrent model tasks → profile replacement and user/assistant knowledge append → mark analyzed/reset heat/save. Owner: `Memoryos` orchestrator. Model proposes integrated profile and extracted facts; code admits. Existing profile is supplied to the profile task, while knowledge extraction receives dialogue. The process persists natural-language interpretations and embedded knowledge, not model parameters (SRC-1: `memoryos-pypi/memoryos.py`, `memoryos-pypi/utils.py`, `memoryos-pypi/long_term.py`).

- Immediate return: no output payload; profile/knowledge and session metadata may change.
- Later read-back: full profile and selected user/assistant knowledge feed subsequent response prompts; old profile also informs later analysis.
- Delegated visibility: two fixed worker tasks receive existing profile plus dialogue, or dialogue alone, and send them to the configured provider.
- Selection predicate: heap-top heat at least configured threshold and nonempty unanalyzed pages; force method temporarily sets threshold to zero, still selecting one hottest session.
- Invalidation or expiry: profile is replaced with `merge=False`; knowledge deques evict oldest entries at capacity; analyzed flags prevent repeat analysis of the same pages on the ordinary path.
- Activation or effect: writes alter later eligible context; observed changed behavior and improvement are uninspected.
- Evidence limits: extraction instructions and structural guards establish admission wiring, not factual warrant, retention of every old insight or successful learning.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission/rejection: profile must be nonempty, not `none`, and at least thirty stripped characters; knowledge is split by lines and filters empty/none-like values. No human reviews each admitted item. No answer oracle adjudicates truth. Operating mode: routine trace-fed maintenance, also manually triggerable, not an improvement experiment. Guidance asks for personality dimensions grounded in dialogue, preservation of existing insights and concise facts. What persists is the resulting profile/facts and analyzed/access metadata, not an inspected criticism of the extraction method. Rollback is not supplied by this path; partial writes can precede a failure, and the forced threshold restoration is not protected by `finally`.

> if (updated_user_profile and
>                         updated_user_profile.lower() != "none" and
>                         len(updated_user_profile.strip()) >= 30):
> --- `memoryos-pypi/memoryos.py`

> 6. Maintain existing insights from the old profile while incorporating new observations
> 7. If a dimension cannot be inferred from either the old profile or new conversation, do not include it
> --- `memoryos-pypi/prompts.py`

#### RT-RTE-mcp-access
Label: MCP tool-mediated storage and retrieval

Endpoints/progression: stdio host → FastMCP tool → configured singleton `Memoryos` → add, retrieval or profile access → structured dictionary. Owner: server callbacks; host selects whether/when to invoke tools. Initialization checks required configuration fields, not authenticated end-user identity. The bundled orchestrator matches the ordinary JSON response/admission logic except for the Python-only stats helper. Differences in bundled helpers include optional keyword extraction and different direct `search_sessions` defaults; the identical retriever still passes its own explicit thresholds/top-k (SRC-1: `memoryos-mcp/server_new.py`, `memoryos-mcp/memoryos/memoryos.py`, `memoryos-mcp/memoryos/mid_term.py`, `memoryos-mcp/memoryos/retriever.py`).

- Immediate return: success/error dictionaries; retrieval includes full recent history/profile and sliced page/user-knowledge/assistant-knowledge lists; profile tool can return complete knowledge lists.
- Later read-back: add persists host-supplied pairs; later retrieval can read them; retrieval alone does not store the external host's answer.
- Delegated visibility: external MCP host receives returned data; its final prompt construction, model grants and retention are outside the boundary.
- Selection predicate: nonempty add/query checks, normal retriever selection and Python list slicing by `max_results`; profile include flags control all-knowledge delivery.
- Invalidation or expiry: bundled JSON capacities apply; no server-level retention horizon or authenticated per-request user switching is implemented in these callbacks.
- Activation or effect: local writes and context delivery are wired; host consumption/compliance is unobserved.
- Evidence limits: stdio transport and wrappers do not establish working host configuration, approval gates or end-to-end personalized answers.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: host proposes the pair, code decides nonempty validity and delegates to normal add. No per-item human veto or answer oracle appears. Operating mode: host-requested memory tools. Caught callback exceptions produce error dictionaries without rollback of already-performed effects. `relationship_with_user` and `style_hint` accepted by retrieval do not govern any response generation there.

> mcp.run(transport="stdio")
> --- `memoryos-mcp/server_new.py`

> for page in retrieval_results["retrieved_pages"][:max_results]],
> --- `memoryos-mcp/server_new.py`

#### RT-RTE-playground-control
Label: Playground dialogue and administrative controls

Endpoints/progression: browser HTTP routes → Flask session → in-process `memory_systems` instance → chat, import, force-analysis, state inspection or clear/reconstruction. Owner: Flask callbacks; browser/caller chooses operation and supplies user ID, credentials, endpoint and model on initialization. JSON library helpers in this variant match the Python helpers by file comparison; the orchestrator omits the Python stats helper (SRC-1: `memoryos-playground/memdemo/app.py`, `memoryos-playground/memoryos.py`).

- Immediate return: JSON answer/timestamp, import count, state, administrative acknowledgement or HTTP error.
- Later read-back: imported/generated pairs and derived profile/knowledge reach later chat; clear removes both selected identity directories and constructs a new instance.
- Delegated visibility: browser gets route-specific response data, including memory-state/profile data; provider sees ordinary generation or maintenance context.
- Selection predicate: valid memory-session lookup; import skips pairs missing a side; force route checks existence of any unanalyzed pages, then underlying force method still selects the hottest session.
- Invalidation or expiry: clear deletes persistent user/assistant directories; process restart loses the in-process session map and newly generated signing key, while library files can remain.
- Activation or effect: local memory creation/deletion and provider request wiring; launched application and browser outcomes are unobserved.
- Evidence limits: import layout and fixed embedding-cache path may prevent launch; user ID selection is not evidence of identity ownership or deployed isolation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission/control: supplied import dialogue is accepted by code, not approved for truth by a human/model reviewer. Explicit clear is a destructive control, not versioned rollback. Normal init uses knowledge capacity 1000, heat threshold 10 and a machine-specific embedding snapshot; clear reconstructs with capacity 100, heat 5 and default embedding settings. Thus clear changes configuration as well as state. Exceptions become HTTP errors and can occur after partial import/deletion. No expected-answer oracle; operating mode is interactive demo/admin use. Session lookup grants access to the selected instance, but initialization does not bind the claimed user ID to an authenticated identity.

> memory_system.add_memory(
>                     user_input=user_input,
>                     agent_response=agent_response,
>                     timestamp=timestamp
>                 )
> --- `memoryos-playground/memdemo/app.py`

> if os.path.exists(user_data_dir):
>             shutil.rmtree(user_data_dir)
> --- `memoryos-playground/memdemo/app.py`

#### RT-RTE-chroma-dialogue
Label: ChromaDB-backed dialogue and maintenance

Endpoints/progression: `Memoryos` → shared `ChromaStorageProvider` → persistent collections plus in-memory metadata → retrieval/prompt/provider → add → metadata save on `close`. Owner: orchestrator and provider. Collection names use user ID for mid-term/user facts and assistant ID for assistant facts; metadata filename uses both. Queries filter session/page records by user and attempt to join vector-selected pages to JSON backups for chain information; the new-session overwrite below prevents that enrichment for the newly inserted pages. Unlike the JSON retriever, mid-term search calls model-assisted keyword extraction and adds keyword overlap to session relevance. The constructor accepts `long_term_knowledge_capacity` but does not pass it into the two long-term objects, whose default is 100 (SRC-1: `memoryos-chromadb/memoryos.py`, `memoryos-chromadb/storage_provider.py`, `memoryos-chromadb/mid_term.py`, `memoryos-chromadb/long_term.py`, `memoryos-chromadb/retriever.py`).

- Immediate return: response string after memory admission; `close` requests metadata serialization.
- Later read-back: persistent vector collections support later dialogue retrieval subject to dependency success. Profile and short-term reload depend on metadata saving. New-session pages do not survive in the JSON backup even in memory; saving/reloading that overwritten slot does not restore backup-fed extraction or chain enrichment.
- Delegated visibility: local fixed retrieval/analysis threads and external completion provider; no remote agent worker is created.
- Selection predicate: session vector candidates plus keyword overlap and threshold, per-session top twenty page candidates, page threshold and final capacity heap; knowledge similarity threshold/top-k.
- Invalidation or expiry: LFU mid-term route and timestamp-based knowledge-capacity enforcement; profile update replaces provider metadata, parsing JSON or wrapping raw text.
- Activation or effect: code can deliver vector-selected dialogue and independently admitted profile/knowledge, but the new-session backup overwrite blocks that session's pages from heat-fed extraction and response chain enrichment; activation, performance and crash consistency are not observed.
- Evidence limits: shared-dictionary overwrite is established by implementation, independently of save success or ChromaDB merge behavior. ChromaDB duplicate-add behavior and actual operation remain uninspected; persistent client does not imply atomic metadata/vector consistency.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Insertion and backup consumers: `MidTermMemory.sessions` receives the provider's actual `mid_term_sessions` dictionary, not a copy. `add_mid_term_session` first installs a backup containing `pages_backup` and `page_count`, and submits session/page vectors. After that call returns, `add_session` assigns its `session_obj` into the same dictionary slot. That object has no `pages_backup` or `page_count`, so successful new-session insertion deterministically discards the just-created backup. This affects both initial insertion and the no-suitable-session branch. `MidTermMemory.save` updates frequency/heap metadata only; `close` serializes the already-overwritten dictionary rather than reconstructing pages (SRC-1: `memoryos-chromadb/mid_term.py`, `memoryos-chromadb/storage_provider.py`).

The heat updater reads only `get_pages_from_json_backup(sid)` for unanalyzed pages. For such a newly created session this returns an empty list, so even a hot or forced session skips extraction/profile updating. Response assembly can still use user/assistant text returned from vector-page metadata, but `get_page_full_info` searches that missing backup and returns no chain metadata. Direct profile/knowledge APIs remain separate capabilities; this defect does not establish their absence. The merge branch reads only the surviving backup, concatenates new pages and calls the provider again without the final local-slot overwrite. It can therefore establish a backup for newly merged pages, but does not recover the original new-session pages already lost from that backup. This loss is not contingent on duplicate-ID handling in ChromaDB (SRC-1: `memoryos-chromadb/memoryos.py`, `memoryos-chromadb/mid_term.py`, `memoryos-chromadb/storage_provider.py`).

> self.sessions: dict = self.storage.get_mid_term_sessions()
> --- `memoryos-chromadb/mid_term.py`

> def get_mid_term_sessions(self) -> dict:
>         return self.metadata.get("mid_term_sessions", {})
> --- `memoryos-chromadb/storage_provider.py`

> self.metadata["mid_term_sessions"][session_id] = session_backup
> --- `memoryos-chromadb/storage_provider.py`

> # Add to storage
>         self.storage.add_mid_term_session(session_obj, processed_details)
>         
>         # Update local data structures
>         self.sessions[session_id] = session_obj
> --- `memoryos-chromadb/mid_term.py`

> def get_pages_from_json_backup(self, session_id: str) -> List[dict]:
>         return self.metadata.get("mid_term_sessions", {}).get(session_id, {}).get("pages_backup", [])
> --- `memoryos-chromadb/storage_provider.py`

> unanalyzed_pages = [
>                 page for page in self.mid_term_memory.storage.get_pages_from_json_backup(sid)
>                 if not page.get("analyzed")
>             ]
> --- `memoryos-chromadb/memoryos.py`

> full_page_info = self.storage_provider.get_page_full_info(page_id, session_id)
>                 if full_page_info:
>                     meta_info = full_page_info.get('meta_info', '')
> --- `memoryos-chromadb/memoryos.py`

Admission: same top-level add/heat controls, subject to the missing-backup extraction gate above, but long-term profile updater accepts truthy parsed/wrapped output rather than the JSON variant's thirty-character guard. Knowledge helpers filter empty/none-like text, embed and add to selected collection. Code/model own content admission; no human quality veto or expected-answer oracle. Operating mode: ordinary requests plus threshold/forced maintenance. Guidance is the shipped profile/extraction prompts; raw non-JSON profile text can persist under `raw_text_profile`. Recovery uses provider exception handling and explicit `close`/normal-exit save, not a cross-store transaction. Metadata save catches I/O errors, so a close message is not a durable-commit certificate.

> self.client = chromadb.PersistentClient(path=path)
> --- `memoryos-chromadb/storage_provider.py`

> # Register save handler to be called on exit
>         atexit.register(self.close)
> --- `memoryos-chromadb/memoryos.py`

> def add_short_term_memory(self, qa_pair: dict):
>         if 'timestamp' not in qa_pair or not qa_pair['timestamp']:
>             qa_pair["timestamp"] = get_timestamp()
>         
>         self.metadata.setdefault("short_term_memory", []).append(qa_pair)
> --- `memoryos-chromadb/storage_provider.py`

> return {"raw_text_profile": result_text}
> --- `memoryos-chromadb/utils.py`

#### RT-RTE-locomo-evaluation
Label: LoCoMo import, question answering and scoring

Endpoints/progression: `locomo10.json` → conversation preprocessing → separate evaluation memories → imported-dialogue updates → question retrieval → model answer → `all_loco_results.json` → separate category scorer. Owner: fixed `main` loop and scorer. Sample IDs name persistent memory files; speaker identities are rewritten into answer prompts. Captions are appended to text. Capacity-one short-term storage is processed after each insertion; malformed pairs can be removed without migration, and summary input in `DynamicUpdate` uses user inputs only. Unlike Python updater, its inspected insertion loop has no general-summary fallback (SRC-1: `eval/main_loco_parse.py`, `eval/dynamic_update.py`, `eval/retrieval_and_answer.py`, `eval/evalution_loco.py`).

- Immediate return: main writes answer/reference/category records after samples; scorer prints mean token-set F1 by category.
- Later read-back: sample-specific memory files are reused by the initialized storage objects; scorer reads retained result JSON. Generated benchmark answers are not added to memory by the inspected question loop.
- Delegated visibility: provider gets formatted recent/retrieved dialogue, profile and knowledge; reference answer is retained in results for scoring rather than supplied as the generation answer.
- Selection predicate: dataset/sample/question loops; retrieval thresholds 0.1 and page queue ten; scoring compares lowercase regex word-token sets against `answer` or fallback `adversarial_answer`.
- Invalidation or expiry: results file is rewritten after each sample and at completion; driver does not clear sample memory files before processing, so a clean-start assumption is not guaranteed by this driver.
- Activation or effect: source wires memory-assisted answers and offline scoring; no supplied result demonstrates that this workflow was exercised successfully.
- Evidence limits: reference validity, reproduced scores, benchmark improvement, BLEU calculation and causal component attribution are not established by this inspected driver/scorer.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Operating mode: bounded benchmark question set, not runtime self-modification. Answer oracle: dataset reference/adversarial answer, provided by the shipped dataset and consumed by the offline scorer. It computes set-based F1; it neither selects replacement models/methods nor vetoes knowledge admission. Humans supply/configure the workflow but do not approve each derived item. Model proposals populate summaries/profiles/facts under automatic update rules. Failure handling is partial dataset/output-file exception handling; model-client failures in this evaluation utility are not converted to the main library's sentinel. No experiment independently varies memory components in these inspected files.

> pred_tokens = set(simple_tokenize(prediction))
>     ref_tokens = set(simple_tokenize(reference))
> --- `eval/evalution_loco.py`

> input_text = "\n".join([f"User: {page.get('user_input','')}\n" for page in pages])
> --- `eval/dynamic_update.py`

### Claims

#### RT-CLM-dialogue-benefit
Label: Personalized dialogue and reported benchmark gains

Claimed operation: hierarchical storage, updating, retrieval and generation improve coherent, personalized, context-aware interaction. Claimed benchmark improvements are 49.11% F1 and 46.18% BLEU-1. Source: SRC-1, `README.md` (doctrine/design and reported operation). Implemented context/admission paths support a mechanism for conditioning responses, not these quality or causal magnitudes. The inspected offline F1 scorer and absent supplied runs do not reproduce the reported comparison; its BLEU claim remains attributed, not validated.

- design conclusion status: claimed
- implementation conclusion status: wired
- operation conclusion status: uninspected

> **MemoryOS** is designed to provide a memory operating system for personalized AI agents, enabling more coherent, personalized, and context-aware interactions. Drawing inspiration from memory management principles in operating systems, it adopts a hierarchical storage architecture with four core modules: Storage, Updating, Retrieval, and Generation, to achieve comprehensive and efficient memory management. On the LoCoMo benchmark, the model achieved average improvements of **49.11%** and **46.18%** in F1 and BLEU-1 scores.
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-assistant-context
Label: Assistant knowledge to system-message conditioning

Consumer: configured response model. Channel: retrieved assistant knowledge formatted into `GENERATE_SYSTEM_RESPONSE_SYSTEM_PROMPT`. Force: natural-language role/trait conditioning at the system-message position, not executable capability, output validation or guaranteed compliance. Horizon: later calls and reloads until knowledge removal or nonselection. The source text originates in dialogue extraction or direct storage writes, not necessarily provider-certified facts. The generation channel differs from user-background placement; its effect is wired but activation is unobserved (SRC-1: `memoryos-pypi/memoryos.py`, `memoryos-pypi/prompts.py`; ChromaDB analogue in `memoryos-chromadb/memoryos.py`).

> system_prompt_text = prompts.GENERATE_SYSTEM_RESPONSE_SYSTEM_PROMPT.format(
>             relationship=relationship_with_user,
>             assistant_knowledge_text=assistant_knowledge_text_for_prompt,
>             meta_data_text=meta_data_text_for_prompt # Using meta_data_text placeholder for user_conversation_meta_data
>         )
> --- `memoryos-pypi/memoryos.py`

#### RT-BAP-user-context
Label: Recent and recalled user context to response conditioning

Consumer: configured response model. Channel: user-message body combining recent dialogue, selected historical pages, profile and selected user knowledge with current query. Force: natural-language information and persona context, not a factuality gate or independent instruction-isolation boundary. Horizon: subsequent turns and reloads while material remains retained and selected; full profile bypasses query ranking. MCP instead delivers these objects to an external host, whose actual model channel and use are unresolved. These placements establish a live code path capable of influencing later output, not observed improvement (SRC-1: `memoryos-pypi/memoryos.py`, `memoryos-mcp/server_new.py`).

> user_prompt_text = prompts.GENERATE_SYSTEM_RESPONSE_USER_PROMPT.format(
>             history_text=history_text,
>             retrieval_text=retrieval_text,
>             background=background_context,
>             relationship=relationship_with_user,
>             query=query
>         )
> --- `memoryos-pypi/memoryos.py`

## Annotations

none
