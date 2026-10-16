---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "A-MEM runtime baseline tracing note admission, model-mediated evolution, retrieval and direct mutation at its frozen library boundary."
run-id: AAS-2026-10-16-a-mem-sys-eff95cd80440-01
reviewed-boundary: f303dfc71e07bdc787f4bc135d4cea328ae30e99
---

# A-MEM runtime report

## Runtime account

### Scope and entry paths

This is a synchronous memory library, not a task-solving agent executor. The shipped entry path is Python import and construction of `AgenticMemorySystem`, followed by `add_note`, `read`, `search`, `search_agentic`, `update` or `delete`. README examples and test callers belong to this account. Packaging declares a library and no executable script entry point (SRC-1, `README.md`, `pyproject.toml`, `tests/test_memory_system.py`). The source-native claim of automatic organization is recorded in [RT-CLM-memory-organization](#rt-clm-memory-organization).

The evidence is inspected implementation and source-native design, not a supplied run. No target code, tests or examples were executed. Successful provider calls, actual metadata quality, activation in a downstream task and performance benefit remain unobserved. This member inspected the complete three nonempty package modules, packaging, README usage examples and the first part of the memory tests. These are already registered SRC-1 paths; no new source or evidence layer is introduced.

### Ordinary invocation, end to end

The principal is the calling Python application. It chooses the content and constructor settings, including embedding model, LLM backend/model, credentials or SGLang address, and consolidation threshold. Construction starts an empty `memories` dictionary, attempts a Chroma client reset, constructs a fresh retriever and selects an adapter. The reset exception is logged and ignored; later constructor failures can still escape. The fixed collection name is `memories`; this is not per-user or per-tenant namespace isolation (SRC-1, `agentic_memory/memory_system.py`, `agentic_memory/retrievers.py`).

An ordinary first `add_note(content)` creates a UUID note and minute-resolution timestamps. Missing keywords, default context or missing tags trigger a metadata model call. Natural-language instructions and content become the model input; JSON is the requested output representation. Code parses that output and fills only empty/default fields. The first note skips relationship evolution because the object map is empty. Code puts the note into the map, constructs metadata, and asks Chroma to add it. The retriever appends nondefault context, keywords and tags to the embedding document, serializes list/dict metadata to JSON strings, and stringifies scalar metadata. The immediate terminal result is the note ID, not an answer to the enclosing application's task. [RT-RTE-note-admission](#rt-rte-note-admission) records the decision and admission controls; [RT-CMP-sentence-transformer](#rt-cmp-sentence-transformer) records the embedding dependency (SRC-1, `agentic_memory/memory_system.py`, `agentic_memory/retrievers.py`).

A subsequent add can invoke [RT-RTE-neighbor-evolution](#rt-rte-neighbor-evolution): retrieve up to five neighbors, supply their metadata and content with the new note to the LLM, parse its decision, and apply recognized actions. The LLM proposes and decides within that fixed action vocabulary; Python owns iteration and execution. This is not an open-ended tool loop. A positive evolution decision increments `evo_cnt`; every threshold multiple invokes consolidation. That routine constructs another get-or-create retriever and calls `add_document` for every object. Despite its reset comment, it contains no explicit reset, delete or upsert. Its ability to refresh preexisting IDs therefore depends on external Chroma behavior and is not a demonstrated repair guarantee (SRC-1, `agentic_memory/memory_system.py`, `agentic_memory/retrievers.py`).

The caller can then retrieve by ID or similarity. `search` uses Chroma-selected IDs but returns fields from the live object map; `search_agentic` first returns Chroma metadata and may append linked live objects before truncating to `k`. `find_related_memories` builds the evolution model's neighbor text from Chroma metadata, not the live objects. These differences matter after neighbor mutation. Retrieval returns data to the caller; there is no shipped agent answer-generation stage. [RT-RTE-memory-retrieval](#rt-rte-memory-retrieval) records selection, context supply and limits (SRC-1, `agentic_memory/memory_system.py`).

### Forcing cases and control coverage

Four inspected cases qualify the ordinary path; none was experimentally run.

1. **Complete caller metadata / direct mutation.** Complete nondefault semantic fields bypass metadata analysis, but do not bypass evolution on a populated system. `update` bypasses both model-mediated paths. `read` returns the actual object, permitting caller mutation without retriever synchronization. Test callers exercise this API pattern in source when editing links before calling `update`. There is no universal model approval gate for note changes: [RT-RTE-direct-mutation](#rt-rte-direct-mutation) (SRC-1, `agentic_memory/memory_system.py`, `tests/test_memory_system.py`).
2. **Provider failure or malformed response.** OpenAI delegates errors to the outer analysis/evolution handlers. Ollama, OpenRouter and SGLang can instead return schema-shaped empty values. A metadata call can then install empty strings/lists rather than the `General` exception fallback. Evolution failures normally return `False, note`; this is not transactional rollback if an earlier action already mutated a note or neighbor. The caller is not given a structured degraded-result flag (SRC-1, `agentic_memory/llm_controller.py`, `agentic_memory/memory_system.py`).
3. **Neighbor update followed by retrieval.** `update_neighbor` changes the object map without an immediate Chroma write. Thus `read` and map-backed `search` can expose changed context/tags while evolution's next neighbor prompt and metadata-backed `search_agentic` receive older metadata. Consolidation is deferred, threshold-dependent and not proven to replace existing collection records. No single read-consistency guarantee spans these routes (SRC-1, `agentic_memory/memory_system.py`, `agentic_memory/retrievers.py`).
4. **Linked search at a full result budget.** `search_agentic` appends neighbors after the selected direct results and finally returns `memories[:k]`. If direct hits already occupy `k` slots, the appended neighbors do not reach the caller. The raw formatted related-memory helper has different behavior: it can add up to `k` live links per hit. The private `_search` calls the same retriever twice and then treats the second returned dictionary as iterable result objects; it is not evidence of a working independent hybrid ranking path (SRC-1, `agentic_memory/memory_system.py`).

### Guarantees, authority and operating envelope

The load-bearing bounded control is a fixed mutation vocabulary, not correctness of model judgment. Owner: `AgenticMemorySystem.process_memory`. Enforcement point: its action dispatch and neighbor-ID lookup. Guarantee strength: invariant for this dispatch's recognized branches. Covered path: automatic evolution can extend the new note's links, replace its tags, and replace selected neighbors' context/tags; it does not interpret model text as executable Python or a shell command. Alternate paths: direct Python mutation, public CRUD and calls to the adapter/retriever are outside this dispatch. Required external contract: a parseable response with values compatible with the operations; failures can leave partial effects. Implementation conclusion status: wired. Operation conclusion status: uninspected (SRC-1, `agentic_memory/memory_system.py`).

> if action == "strengthen":
>     suggest_connections = response_json["suggested_connections"]
>     new_tags = response_json["tags_to_update"]
>     note.links.extend(suggest_connections)
>     note.tags = new_tags
> elif action == "update_neighbor":
> --- `agentic_memory/memory_system.py`

JSON-schema requests are not a local semantic safety guarantee. Owner: adapter/provider for requested output shape; local owner: `json.loads` and subsequent Python operations. Guarantee strength: best effort across backends. Covered paths: both internal model calls request schemas; OpenAI/LiteLLM forward `response_format`, while SGLang sends a serialized schema to `/generate`. The source does not locally validate all schema properties, connection IDs, tag meaning, or the prompt's required neighborhood lengths. Direct CRUD and object mutation do not pass this schema request. Required external contract: backend support for structured generation and suitable output. Implementation conclusion status: wired. Operation conclusion status: uninspected (SRC-1, `agentic_memory/memory_system.py`, `agentic_memory/llm_controller.py`).

The capability surface is Python memory operations plus model/network and embedding/storage calls. The internal model is granted no provider-native tools, host callbacks, shell executor, subprocess runner, dynamic extension loader, delegation interface or remote worker control in the inspected three package modules. This bounds the shipped internal loop, not what an arbitrary Python host could add. The configured grant set is backend credentials/address and in-process access to the retriever and object map. No deployment configuration or execution evidence establishes a sandbox, tenant boundary or external authorization policy. OpenRouter additionally writes its key into the process environment. An enclosing application's privileges are not inferred from this library (SRC-1, `agentic_memory/llm_controller.py`, `agentic_memory/memory_system.py`, `agentic_memory/retrievers.py`).

There is no coordinator beyond synchronous caller control: no shipped queue, lock or concurrent worker protocol appears in these paths. Failures are logged or printed in selected handlers; there is no route-wide transaction joining map mutations and Chroma operations. An add writes the map before Chroma; an update mutates the object before delete-and-add; a delete performs the retriever delete before removing the map entry. This order prevents claiming atomicity or recoverable isolation. No save/load path is established; the constructor's empty map and reset attempt prevent assuming cross-session restoration. Dependency-level persistence remains outside inspected implementation (SRC-1, `agentic_memory/memory_system.py`, `agentic_memory/retrievers.py`).

Model calls use separately assembled, stateless request payloads rather than accumulated chat histories. Metadata analysis supplies the current content and static instructions. Evolution supplies the new note plus selected neighbor text. The code rule `k=5` controls which retained material enters this model context; no compaction or sub-agent frame mechanism is involved. Material not selected stays in the library stores, reachable through later searches or ID reads. Provider-internal context handling is uninspected (SRC-1, `agentic_memory/memory_system.py`, `agentic_memory/llm_controller.py`).

The automatic change-admission surface here is retained metadata and relationships, not shipped code, model parameters or production machinery. Direct callers can replace note fields. No runtime product/capability deployment path is established by these modules or packaging. The natural-language evolution guidance remains static during these paths; the mechanism requests relational/category updates, not explicit criticism and revision of a formulated explanatory theory. Memory-specific revision findings are left to the memory analyst. Behavioral authority is separated into evolution-consumer delivery and caller retrieval in [RT-BAP-neighbor-context](#rt-bap-neighbor-context) and [RT-BAP-caller-results](#rt-bap-caller-results).

## Shared records

### Components

#### RT-CMP-openai
Label: OpenAIController inference backend

Source-native identity: `OpenAIController`, selected by `LLMController` for `openai`. Distributed-parametric model inference is accessed through an external OpenAI client; weights and provider storage are uninspected. Local strings and dictionaries encode the symbolic request. Default system model is `gpt-4o-mini`; the caller can replace it. Parameters are not updated by this library's operations; provider-side changes remain uninspected. Exact model version is not pinned. The model string and mutable service endpoint may resolve to a changed model. Evidence: SRC-1, `agentic_memory/llm_controller.py`, `agentic_memory/memory_system.py`.

> response = self.client.chat.completions.create(**kwargs)
> return response.choices[0].message.content
> --- `agentic_memory/llm_controller.py`

#### RT-CMP-ollama
Label: OllamaController inference backend

Source-native identity: `OllamaController`; distributed-parametric model inference through LiteLLM `ollama_chat/{model}`. Local instance stores the model string; provider-side weights/storage are uninspected. No parameter update is implemented in this library; exact version is not pinned and the mutable local service/model alias can resolve differently. The adapter catches exceptions and returns generated empty schema values. Evidence: SRC-1, `agentic_memory/llm_controller.py`.

> model="ollama_chat/{}".format(self.model),
> --- `agentic_memory/llm_controller.py`

#### RT-CMP-sglang
Label: SGLangController inference backend

Source-native identity: `SGLangController`; distributed-parametric inference behind a caller-configurable HTTP service. The local instance stores host, port and model label, but its generation payload does not send that model label. The deployed server determines actual weights; their substrate and parameter changes are uninspected. No training path is implemented locally. Exact model version is not pinned; mutable server configuration can select different weights. Evidence: SRC-1, `agentic_memory/llm_controller.py`.

> response = requests.post(
>     f"{self.base_url}/generate",
>     headers={"Content-Type": "application/json"},
>     json=payload,
>     timeout=60
> )
> --- `agentic_memory/llm_controller.py`

#### RT-CMP-open-router
Label: OpenRouterController inference backend

Source-native identity: `OpenRouterController`; distributed-parametric inference selected through LiteLLM and an `openrouter/` model identifier. Weights and service storage are external and uninspected. This library does not update parameters. Exact version is not pinned; provider routing, aliases and service configuration may resolve to another model. Local model/key strings are held in the adapter; the key is also installed in the environment. Evidence: SRC-1, `agentic_memory/llm_controller.py`.

> os.environ['OPENROUTER_API_KEY'] = api_key
> self.api_key = api_key
> --- `agentic_memory/llm_controller.py`

#### RT-CMP-sentence-transformer
Label: SentenceTransformerEmbeddingFunction

Source-native identity: Chroma's `SentenceTransformerEmbeddingFunction`, configured by `model_name` (default `all-MiniLM-L6-v2`). Its learned representation is distributed-parametric; emitted dense vectors are stored/indexed through Chroma. The library does not train or update embedding parameters. The exact artifact version is not pinned, and a mutable model name/artifact resolution can change the embedding model between constructions. No ongoing hot replacement is implemented in the inspected code. Dependency-internal artifact storage and resolution are uninspected. Evidence: SRC-1, `agentic_memory/retrievers.py`.

> self.client = chromadb.Client(Settings(allow_reset=True))
> self.embedding_function = SentenceTransformerEmbeddingFunction(model_name=model_name)
> self.collection = self.client.get_or_create_collection(name=collection_name,embedding_function=self.embedding_function)
> --- `agentic_memory/retrievers.py`

### Operative objects

none declared in this member

### Routes

#### RT-RTE-note-admission
Label: Note creation and metadata admission

Endpoints/progression: caller content/kwargs → `MemoryNote` → conditional `analyze_content` → `process_memory` → object map → `ChromaRetriever.add_document` → note ID. Python owns progression; the model proposes metadata and code admits it for missing/default fields without a human content-approval step. Caller identity does not establish human authorship. Natural-language instructions request salient keywords, a one-sentence context and categorical tags; symbolic JSON values are applied by code. Operating mode: open caller requests, not a bounded experiment. Answer oracle: none supplied by this route. Caller-supplied complete metadata can veto metadata generation by avoiding its predicate; the caller may subsequently update/delete. Failure recovery uses analysis defaults but there is no transactional rollback across evolution, map and vector writes. What persists within the instance is the note and retriever representation, not proposal reasoning. Evidence: SRC-1, `agentic_memory/memory_system.py`, `agentic_memory/retrievers.py`.

- Immediate return: note ID after successful completion; uncaught downstream failures can prevent the return.
- Later read-back: note data can reach later ID reads, similarity results and evolution prompts through distinct map/metadata consumers.
- Delegated visibility: selected model backend receives current content and static metadata instructions; Chroma/embedding dependency receives enhanced content and metadata.
- Selection predicate: metadata analysis runs when keywords or tags are empty, or context equals `General`; only corresponding fields are filled.
- Invalidation or expiry: explicit update/delete; new construction clears the map and attempts a client reset; no time expiry is implemented here.
- Activation or effect: code assigns generated fields and stores an enhanced embedding document; actual semantic correctness and downstream behavioral activation are unobserved.
- Evidence limits: source wiring only; provider success, dependency behavior and cross-session restoration are not observed.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if not note.keywords:
>     note.keywords = analysis.get("keywords", [])
> if note.context == "General":
>     note.context = analysis.get("context", "General")
> if not note.tags:
>     note.tags = analysis.get("tags", [])
> --- `agentic_memory/memory_system.py`

#### RT-RTE-neighbor-evolution
Label: Model-directed neighbor evolution

Endpoints/progression: populated map and new note → Chroma nearest-neighbor text/IDs → evolution model → parsed decision → action dispatch → mutated note/neighbors → add continuation. Trigger: a new note with available neighbors. Code selects context; the model proposes and decides `should_evolve` and actions. Code can reject malformed output by exception and ignores unknown action strings; there is no per-proposal human approval. The guidance asks for relationships, new tags and neighbor contexts, including equal neighborhood-array lengths. It does not provide an expected answer/reference outcome. Operating mode: open ingestion, not an evaluator-guided curriculum. Improvement trigger is new content, not measured task failure. What persists is links/tags/context; neither criticism nor the model's rationale is retained by this path. Manual update/delete can change results but no automatic rollback is provided. This declares runtime dispatch, not a separate claim of improved memory quality. Evidence: SRC-1, `agentic_memory/memory_system.py`.

- Immediate return: `(should_evolve, note)` to `add_note`, or `(False, note)` on handled failures/early exits.
- Later read-back: live neighbor changes reach map readers; later evolution and metadata-backed retrieval use Chroma snapshots until a successful refresh, which is not guaranteed by the inspected consolidation implementation.
- Delegated visibility: configured LLM receives new-note content/context/keywords and up to five retrieved neighbors' IDs, content, context, keywords, tags and times.
- Selection predicate: populated map, nonempty retrieved neighbor text/IDs, then model `should_evolve` and recognized action strings; existing neighbor IDs bound neighbor writes.
- Invalidation or expiry: later overwrites/deletes or instance reset; no automatic expiry; caller can change retained fields.
- Activation or effect: dispatch can extend new-note links, replace its tags and replace neighbors' tags/context; positive decisions increment the consolidation counter.
- Evidence limits: no executed evolution, reliable prompt compliance, successful synchronization or quality benefit is established; exceptions can occur after partial mutation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> # Save the updated memory back
> self.memories[memory_id] = neighbor_memory
> --- `agentic_memory/memory_system.py`

> self.evo_cnt += 1
> if self.evo_cnt % self.evo_threshold == 0:
>     self.consolidate_memories()
> --- `agentic_memory/memory_system.py`

#### RT-RTE-memory-retrieval
Label: ID and similarity read delivery

Endpoints/progression: caller ID/query → map lookup or Chroma query → mapping/formatting, optional link expansion → caller result or evolution prompt input. Python controls selection and return; Chroma controls nearest-neighbor IDs/distances using the embedding dependency. `search` and `search_agentic` consume different representations after selection. The related-memory formatter is the evolution consumer's context supply route. No model-generated query or autonomous scheduled retrieval is implemented in these paths. Evidence: SRC-1, `agentic_memory/memory_system.py`, `agentic_memory/retrievers.py`.

- Immediate return: `read` returns a live note or `None`; searches return result dictionaries; related-memory helpers return formatted strings (and IDs for the evolution helper).
- Later read-back: this is the delivery path for previously admitted note material; the route itself does not record retrieval outcomes into later decision state.
- Delegated visibility: evolution receives selected neighbor text; ordinary search returns data to the caller, whose later model use is outside the shipped loop.
- Selection predicate: exact map key for `read`; Chroma `query_texts=[query]`, `n_results=k` for similarity; link membership for optional expansion, followed by route-specific limits.
- Invalidation or expiry: deletion/update/reset can change subsequent selection; no TTL or invalidation of previously returned caller values is implemented.
- Activation or effect: selected retained content is delivered, not evidence that an enclosing agent obeyed it or improved its answer.
- Evidence limits: ranking quality and dependency execution are unobserved; full direct-result budgets can exclude appended links, and map/metadata differences can yield inconsistent fields.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> results = self.collection.query(
>     query_texts=[query],
>     n_results=k
> )
> --- `agentic_memory/retrievers.py`

> # Try to get links from memory object
> mem_obj = self.memories.get(memory['id'])
> if mem_obj:
>     links = mem_obj.links
> --- `agentic_memory/memory_system.py`

#### RT-RTE-direct-mutation
Label: Caller-controlled note mutation

Endpoints/progression: caller `update`/`delete` or mutable `read` result → object changes and, for CRUD methods, Chroma operations. Caller supplies and decides the proposed change; `update` admits existing attribute names using `hasattr`, not semantic validation. Missing IDs return `False`; delete similarly checks membership. Caller identity leaves human participation unresolved. Operating mode: direct open API requests; answer oracle: inapplicable to these operational writes. No automatic quality/improvement trigger is used. Guidance is API field selection, not an LLM proposal. Existing content, metadata and even identity attributes can be replaced through this broad mechanism. Updating content does not regenerate its semantic metadata. No old value checkpoint or rollback is maintained. Evidence: SRC-1, `agentic_memory/memory_system.py`, `tests/test_memory_system.py`.

- Immediate return: CRUD success boolean; `read` supplies a live object that the caller can mutate without a separate library call.
- Later read-back: changes can affect later map reads and vector-backed retrieval; mutations through a live object alone do not synchronize Chroma.
- Delegated visibility: CRUD writes pass content and metadata to Chroma/embedding code; direct object mutation remains local until another synchronization call.
- Selection predicate: map membership, then existing attribute names for `update`; direct object references permit ordinary Python mutations.
- Invalidation or expiry: delete removes an entry after retriever deletion; later updates overwrite fields; no automatic expiry or rollback.
- Activation or effect: local note mutation, delete-and-add retriever update, or removal; direct paths bypass model metadata analysis and evolution decisions.
- Evidence limits: no transactions join stores; exceptions can leave partial state, and mutable identifiers can diverge from original map keys. No concurrent or recovery execution was supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> for key, value in kwargs.items():
>     if hasattr(note, key):
>         setattr(note, key, value)
> --- `agentic_memory/memory_system.py`

> self.retriever.delete_document(memory_id)
> self.retriever.add_document(document=note.content, metadata=metadata, doc_id=memory_id)
> --- `agentic_memory/memory_system.py`

### Claims

#### RT-CLM-memory-organization
Label: Dynamic agentic organization claim

Claimed operation: the README advertises automatic semantic attributes, intelligent links and continuing memory evolution. The source wires requests for metadata and relationship decisions, but not reliable decisions or superior retrieval. The README's comparative experiments statement is reported operation only; no inspectable result trace or causal experiment was supplied in this boundary. Evidence: SRC-1, `README.md`; implementation qualification: `agentic_memory/memory_system.py`, `agentic_memory/retrievers.py`.

> - 🧬 Continuous memory evolution and refinement
> - 🤖 Agent-driven decision making for adaptive memory management
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-neighbor-context
Label: Retained neighbor text to evolution decisions

Consumer: the configured evolution LLM, followed by Python's `process_memory` action dispatcher. Channel: neighbor records formatted from Chroma metadata and interpolated into the same natural-language prompt as evolution guidance. Force: model-interpreted context, not executable commands; generated symbolic action fields can authorize fixed map mutations. Horizon: later adds within the initialized system; cross-session reconstruction is not established. A stale metadata snapshot can constrain what actually reaches the consumer. This is the authority path of [RT-RTE-neighbor-evolution](#rt-rte-neighbor-evolution), not proof of actual model reliance. Evidence: SRC-1, `agentic_memory/memory_system.py`.

> prompt = self._evolution_system_prompt.format(
>     content=note.content,
>     context=note.context,
>     keywords=note.keywords,
>     nearest_neighbors_memories=neighbors_text,
>     neighbor_number=len(memory_ids)
> )
> --- `agentic_memory/memory_system.py`

#### RT-BAP-caller-results
Label: Retained results to calling application

Consumer: calling Python application. Channel: live `MemoryNote` or selected result dictionaries/formatted text. Force: returned data; no shipped application interprets it as instructions or produces a task answer. Horizon: later API calls within the current initialized system; subsequent caller retention/use is uninspected. This is the outward authority limit of [RT-RTE-memory-retrieval](#rt-rte-memory-retrieval). Evidence: SRC-1, `agentic_memory/memory_system.py`, `README.md`.

> return self.memories.get(memory_id)
> --- `agentic_memory/memory_system.py`

## Annotations

none
