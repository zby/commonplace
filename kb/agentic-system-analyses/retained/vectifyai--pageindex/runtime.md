---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "PageIndex runtime baseline: local indexing and document QA, alternate builders, framework tools and opaque cloud routes."
run-id: AAS-2026-10-15-pageindex-50056ef72767-01
reviewed-boundary: af92d9658a6a9c0ae31171b43198db28951af2f4
---

# PageIndex runtime report

## Runtime account

### Evidence and consequential work

PageIndex builds a document tree, stores it with page text, and equips an answering model to discover documents and read selected evidence. The repository ships orchestration, not just an index constructor. Index location and answering ownership are independent: local documents plus own-model chat, cloud documents plus own-model chat, or cloud documents plus managed chat. Local documents plus managed cloud chat is not a supported combination. This account follows the [boundary](boundary.md) and SRC-1: `pageindex/client.py`, `pageindex/local_api.py`, `pageindex/local_chat.py`.

All mechanism findings below are static implementation findings at the frozen revision. No target execution, provider call, test run or experiment was supplied or performed. Wired delivery and admission do not demonstrate model compliance, deployed isolation, retrieval quality or benefit. Additional inspection extends the boundary's initial coverage through Flash orchestration and parser dispatch, optimizer candidate admission, summary scheduling, classic verification/fallback, Markdown generation, all three chat protocol drivers and adapter gates. All use SRC-1; no new source is introduced. Deep layout heuristics, every cloud endpoint, test bodies, examples and benchmark images were not exhaustively inspected. Cloud server internals, provider weights and live MCP catalogs remain unavailable as stated in the boundary.

### Ordinary invocation: submit a PDF, then ask about it

A caller constructs a local `PageIndexClient`, supplies a PDF to `submit_document`, and calls `chat(question, doc_id=...)`. The caller is the initiating principal; no authenticated per-document human reviewer is inserted into local admission. The index driver rejects unsupported modes, non-PDFs, missing files and all-blank extracted pages. PyPDF2 produces the page text that will be stored. Flash independently extracts layout with PDFium, reconciles optional embedded bookmarks, and falls back to page nodes when it finds no hierarchy. The model is not the layout extractor. Default full optimization and summaries do introduce model calls. The local wrapper rejects unreadable/empty or oversized flat results and checks tree spans against the separately extracted page count. It assigns a `pi-` UUID, assigns node IDs, builds a description and saves tree, pages and metadata. See [RT-RTE-local-submit](#rt-rte-local-submit) and [RT-RTE-tree-refine](#rt-rte-tree-refine). SRC-1: `pageindex/local_api.py`, `pageindex/flash/api.py`, `pageindex/flash/main.py`.

The next-step owner changes by phase. Code controls parsing and admission. The optimizer asks a model for headings but code filters and prices candidates. Summary generation uses isolated calls over a leaf's text or a parent's opening text plus child summaries; the result flows into a retained tree, not back into model weights. During full Flash processing, optimizer settlement unlocks summary tasks, with bounded concurrency and children before parents. PDF parsing may use spawned process workers, returning spans and page metadata to the parent; worker failure falls back to sequential parsing. These are parser workers, not independently instructed agents. SRC-1: `pageindex/flash/api.py`, `pageindex/flash/parser_pdfium_parallel.py`, `pageindex/utils.py`.

Later `chat` selects the answering lane. For local own-model chat, code combines managed guidance, standing caller instructions and system/developer text; prepends document metadata/targeting as a user message; and creates an agent with read tools. The model chooses whether to browse, fetch structure, read pages or answer. Local tool dispatch enforces the supplied document allowlist. Structure retrieval removes full text and paginates the outline; page retrieval delivers selected page text subject to a response budget. The Agents SDK owns the repeated model/tool progression. Non-streaming ordinary `chat` returns answer text; the chat-completions lane returns final answer, finish reason and aggregated usage. Responses and Messages lanes also expose appendable tool transcripts. There is no demonstrated answer correctness check after generation. See [RT-RTE-document-chat](#rt-rte-document-chat) and [RT-RTE-protocol-history](#rt-rte-protocol-history). SRC-1: `pageindex/client.py`, `pageindex/local_chat.py`, `pageindex/agent_tools.py`.

### Guarantees and three forcing cases

**1. Local scope versus cloud own-model scope.** Owner: PageIndex local tool dispatch. Enforcement: private allowlist injection, document enumeration filtering and name resolution. Strength: invariant within those scoped tool paths; implementation conclusion status: wired; operation conclusion status: uninspected. It covers the internal Chat Completions, Responses and Messages drivers because each obtains `_local_doc_scope` and passes it to tool construction. It does not make document targeting a universal authorization boundary: cloud own-model chat explicitly drops that allowlist, and framework configuration supplies targeting text rather than the managed driver's structural scope. Direct `get_tree`/`get_ocr` calls and a caller's additional tools also do not inherit an internal chat's allowlist. Required external contract: the runner invokes the registered functions rather than unrelated host capabilities. See [RT-RTE-document-chat](#rt-rte-document-chat), [RT-RTE-cloud-tools](#rt-rte-cloud-tools), [RT-RTE-framework-tools](#rt-rte-framework-tools). SRC-1: `pageindex/client.py`, `pageindex/agent_tools.py`.

> if not getattr(self, "api_key", None):
>     return doc_id
> return None
> --- `pageindex/client.py`

**2. Managed admission versus direct builders.** Owner: local API/CLI. Enforcement: `flash_rejection_reason`; local API additionally calls `_check_page_bounds` before saving. Strength: policy for result refusal; implementation conclusion status: wired; operation conclusion status: uninspected. Both managed callers apply the Flash refusal policy. Direct `page_index_flash` instead returns oversized flat trees without summary/optimization and does not itself throw that refusal. Classic and Markdown builders have different checks; Markdown is not admitted by the local PDF store API. The local page-bound check is narrower than a complete tree validator: it checks `1 <= start` and `end <= page_count` only when both exist, not independently all endpoint ordering/type conditions. It cannot certify hierarchy or semantic fidelity. External contract: parsers supply meaningful text and compatible page ordering. SRC-1: `pageindex/flash/api.py`, `pageindex/local_api.py`, `run_pageindex.py`.

> if (start is not None and end is not None
>         and not (1 <= start and end <= page_count)):
> --- `pageindex/local_api.py`

**3. Read-only tool grant versus ambient authority.** Owner: tool registration locally; cloud endpoint remotely. Enforcement: default local read-tool list or remote `?tools=read` URL; management is opt-in. Strength: invariant for the registered local set, protocol for the requested remote set; implementation conclusion status: wired; operation conclusion status: uninspected. `include_management=True` adds local deletion and selects the ungated cloud endpoint. Direct SDK deletion remains possible regardless of a chat tool list. Hosted MCP uses `require_approval="never"`; Claude's bundle pre-approves its MCP namespace. Neither is evidence of an enclosing shell/filesystem sandbox. The inspected built-in QA agent is given PageIndex tools, not arbitrary shell execution; caller-owned frameworks can add capabilities under their own policies. Remote enforcement requires the server to honor its URL gate and credentials. See [RT-RTE-framework-tools](#rt-rte-framework-tools). SRC-1: `pageindex/agent_tools.py`, `pageindex/integrations/openai_agents.py`, `pageindex/integrations/claude_agent_sdk.py`, `pageindex/client.py`.

> return _READ_TOOLS + (_MANAGEMENT_TOOLS if include_management else ())
> --- `pageindex/agent_tools.py`

These forcing cases refute broader readings of “scoped,” “refused” and “read-only” without denying the actual covered controls. No deployment configuration or successful attack/resistance trace was observed.

### Recovery, context and effect boundaries

Local indexing writes under caller filesystem authority; answering sends selected document content to the caller-selected model backend. “Local” denotes document storage/orchestration, not necessarily on-device inference. Cloud own-model chat forwards remote tool results through the process to that model. Parameter/version limitations are recorded separately in [RT-CMP-index-model](#rt-cmp-index-model), [RT-CMP-summary-model](#rt-cmp-summary-model), [RT-CMP-chat-model](#rt-cmp-chat-model) and [RT-CMP-vision-model](#rt-cmp-vision-model). SRC-1: `pageindex/client.py`, `pageindex/local_chat.py`, `pageindex/utils.py`.

`DocStore` fsyncs a temporary JSON file and replaces each destination separately. Tree/pages precede `doc.json`, which functions as the document-presence marker. This is not a transaction across all files. Manifest writes suppress `OSError`; listing can reconstruct the manifest from metadata files, and metadata loading can fall back to valid cached metadata. A cross-process lock protects local submission's final name check/write on platforms with `fcntl`; its Windows fallback does not lock. Deletion removes the marker first and attempts directory cleanup. There is no rollback guarantee for a partially failed save. These are bounded storage/recovery properties, not measured crash durability. SRC-1: `pageindex/local_store.py`, `pageindex/local_api.py`.

> _write_json_atomic(doc_dir / "tree.json", tree)
> _write_json_atomic(doc_dir / "pages.json", pages)
> _write_json_atomic(doc_dir / "doc.json", meta)
> --- `pageindex/local_store.py`

Index-model helpers implement ten attempts, with immediate exit for selected nonretryable statuses; backend overrides can override request options. Summary failures may fall back per node, but unrecoverable failures and a run in which every requested summary call fails cause failure. The scheduler checks that settled nodes have not changed. Chat wrappers validate turn caps and translate SDK/provider failures; abandoned OpenAI streams cancel the task and close owned backends. Anthropic wrappers close per-call transports and explicitly fail when runner history cannot be read back. External SDK versions remain a dependency contract, not frozen executable evidence. SRC-1: `pageindex/utils.py`, `pageindex/local_chat.py`, `pyproject.toml`.

Working context has several controls besides turn accumulation. Code excludes full page text from structure responses, partitions large outlines, and returns only selected pages. The page-content loop always admits the first requested valid page even if it exceeds the character budget; the nominal limit is therefore not a hard maximum. Omitted pages remain reloadable through another request. Indexing calls are separate frames with selected text: expand sees at most `PAGE_CHARS` per page; parent summaries receive child summaries rather than all child text. Only returned headings/summaries escape these frames. This resembles call-frame isolation, but the model window holds values, not automatically dereferenceable store pointers. None of these inspected drivers establishes automatic removal/compaction of an already accumulated chat history. Cache marks/cache keys concern provider prefix reuse, not proven eviction or a retained summary. Callers supply later histories; Responses/Messages expose tool history for that purpose. SRC-1: `pageindex/agent_tools.py`, `pageindex/tree_optimize.py`, `pageindex/utils.py`, `pageindex/local_chat.py`.

> if not included or budget - size >= 0:
>     content.append(entry)
>     included.append(page)
>     budget -= size
> --- `pageindex/agent_tools.py`

The managed prompt cannot be replaced through the inspected high-level chat `extra_body` channel: skeleton keys are refused, while caller instructions are explicitly appended. This is a request-construction invariant, not a guarantee against conflicting caller text or document prompt injection. Raw CloudAPI request assembly merges its extras last, and caller-owned framework configs are mutable dictionaries: the higher-level guard is not a universal backend property. SRC-1: `pageindex/local_chat.py`, `pageindex/client.py`, `pageindex/cloud_api.py`.

### Remaining shipped routes

Classic/Markdown/CLI construction, dynamic cloud capabilities and the notebook's independent vision pipeline are retained below. They are material alternate routes rather than equivalent executions of the default SDK path. The optimizer CLI also exposes a builder plane that can write revised JSON without updating a local store document. No runtime source-code or package-release admission loop is established by this analysis; release automation is explicitly excluded in the boundary. Retained-document revisions are left to the memory analyst; this member establishes producers, consumers and admission controls, not a complete memory inventory.

## Shared records

### Components

#### RT-CMP-index-model
Label: Classic indexing model

Source-native identity: configured `opt.model` / `index_model`; distributed-parametric inference, weights hosted by the configured LiteLLM destination, not stored in the repository. Classic TOC detection, extraction, title verification and repair call this component. Code sends text requests; no parameter-update operation is wired in the inspected helpers. Exact deployed version is not pinned by this source; caller model strings and backend URLs are mutable and may resolve to another model. Provider-side parameter changes/training and actual endpoint resolution are uninspected. SRC-1: `pageindex/page_index_classic.py`, `pageindex/utils.py`, `pageindex/client.py`.

> response = await litellm.acompletion(**{
>     "model": model,
>     "messages": messages,
>     "drop_params": True,
> --- `pageindex/utils.py`

#### RT-CMP-summary-model
Label: Summary and expansion model

Source-native identity: `summary_model`, also passed as Flash `optimize_model` by the local wrapper. Distributed-parametric content resides at the model service; summary strings and proposed headings are distinct returned text/symbolic results, not weights. It may be the same endpoint as the index model but has different inputs and admission roles. No operation-time weight update is wired in the inspected path. Exact version is not frozen, endpoint resolution is mutable through model/backend configuration, and provider internals are uninspected. SRC-1: `pageindex/local_api.py`, `pageindex/flash/api.py`, `pageindex/utils.py`.

> optimize_model=self._summary_model,
> --- `pageindex/local_api.py`

#### RT-CMP-chat-model
Label: Answering model

Source-native identity: `chat_model` or per-call `model`; distributed-parametric content served by OpenAI-compatible/LiteLLM or native Anthropic transports. Storage of weights is external. Chat drivers and framework bundles expose model selection, not weight mutation. Exact version and weights are not pinned; configurable backend/model names can resolve to another model. Managed cloud chat's selected model and provider-side mutations are opaque. No inference about absence of provider learning follows. SRC-1: `pageindex/local_chat.py`, `pageindex/client.py`, `pageindex/cloud_api.py`.

> model_name = model or client.chat_model
> managed = _managed_instructions(client, system_texts)
> --- `pageindex/local_chat.py`

#### RT-CMP-vision-model
Label: Notebook VLM

Source-native identity: notebook `call_vlm(..., model="gpt-4.1")`; distributed-parametric provider model used for both node selection and image-conditioned answers. Weights reside externally. The notebook makes inference calls, not parameter updates. The name is a default string, not immutable weights or a pinned provider revision; it can be overridden and the service can resolve it differently. Provider internals and executed version are uninspected. SRC-1: `cookbook/pageindex-vision-rag.ipynb`.

> "async def call_vlm(prompt, image_paths=None, model=\"gpt-4.1\"):\n",
> --- `cookbook/pageindex-vision-rag.ipynb`

### Operative objects

#### RT-OBJ-agent-instructions
Label: Agent instructions

Source-native identity: `AGENT_INSTRUCTIONS`, local citation prompts and caller additions. Natural-language guidance stored in Python strings and composed into model system instructions; cloud guidance is fetched text rather than frozen local content. It requests document discovery, structure-first reading over twenty pages, persistence before concluding absence, and optional grounded citations. Delivery is wired; compliance is not observed. SRC-1: `pageindex/agent_tools.py`, `pageindex/local_chat.py`.

> - For documents over {STRUCTURE_FIRST_PAGE_THRESHOLD} pages: call get_document_structure() first to locate relevant sections, then get_page_content() with targeted page ranges.
> --- `pageindex/agent_tools.py`

#### RT-OBJ-cost-policy
Label: Tree search cost policy

Source-native identity: `S`, `tree_cost`, `expand_cost`, `TRIGGER_PAGES` and routing/token constants. Symbolic formulae and numeric constants stored in Python source, consumed by fixed comparison rules. The model proposes headings, not the selection rule. The documented explanation assumes page-granular scanning and one-page routing cost; it is not an observed answer-latency objective. SRC-1: `pageindex/tree_optimize.py`.

> ROUTING_COST = 1         # R(v), in pages
> --- `pageindex/tree_optimize.py`

### Routes

#### RT-RTE-local-submit
Label: Local PDF submission

Endpoints/progression: caller PDF → PyPDF2 page extraction plus Flash/default or classic tree construction → rejection/page checks → UUID metadata and store save. Owner: `LocalAPI.submit_document`; code owns progression, with model-produced summaries/headings supplied through subordinate routes. Context contains the submitted file and configured backend, not chat history. Filesystem writes use the host process's authority. SRC-1: `pageindex/local_api.py`, `pageindex/local_store.py`, `pageindex/flash/api.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: document ID and stored unique name after synchronous indexing/save.
- Later read-back: later list/tree/OCR/chat calls load the stored document; exact retained-part treatment belongs to memory analysis.
- Delegated visibility: parser workers receive PDF source; model calls receive selected text/tree material; no user approval delegate is inserted.
- Selection predicate: caller chooses PDF and flash/standard mode; managed Flash refusal and local span checks precede persistence.
- Invalidation or expiry: explicit deletion removes the document marker; no time expiry appears in this path.
- Activation or effect: code wires saved tree/pages into later getters; effect on model answers remains unobserved.
- Evidence limits: static implementation; text extraction quality and complete save/crash behavior not measured.

Admission: trigger is submission, proposed change is a new retained document; caller initiates but code/model produce its content. Software can reject input/result; no per-content human approval is required by this route. Guidance is Flash layout/refinement policy or classic prompts, followed by summary/description prompts. Tree/pages/metadata persist. A new submission does not overwrite an existing ID. Recovery is retry/re-submit or delete, not transactional rollback across files.

> self._check_page_bounds(structure, len(page_texts))
> --- `pageindex/local_api.py`

#### RT-RTE-tree-refine
Label: Tree refinement and summary admission

Endpoints/progression: detected tree plus page text → deterministic merge and expansion candidates → branch-specific checks → shared ownership filtering and cost comparison → child attachment → summary completion. Model candidates pass `propose_children`'s range, normalized printed-substring, deduplication and ordering checks. External cache candidates instead enter through `children_from_cache`, selected by node page span and configured heading kinds and excluding the node's own normalized title; they do not pass the model branch's printed-substring check. Owner: optimizer and `SummaryScheduler`; [RT-CMP-summary-model](#rt-cmp-summary-model) or the supplied cache provides candidates, code decides/vetoes. This runs on explicit/default full Flash optimization; `merge` and `off` omit model expansion. SRC-1: `pageindex/tree_optimize.py`, `pageindex/flash/api.py`, `pageindex/utils.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: changed tree and structural cost counters; summaries populate settled nodes.
- Later read-back: managed submission persists the resulting tree for later retrieval; direct optimizer callers own persistence.
- Delegated visibility: each expand call sees section title/range and capped page text; summary calls see selected leaf text or opening text and child summaries.
- Selection predicate: collapsed nodes above trigger; choose lowest computed candidate cost, require strict page-cost gain, gain ratio and lower estimated read tokens.
- Invalidation or expiry: decided nodes are frozen within optimization; final-state checks reject later scheduler-incompatible changes; no time expiry.
- Activation or effect: accepted children mutate the tree and summaries feed parent summaries; later answer effects are unobserved.
- Evidence limits: cost proxies are code calculations, not an external answer oracle or measured retrieval benefit; Flash wrapper omits optimizer `new_issues` from returned metrics.

Admission roles: the model or supplied cache provides candidates, but their admission checks differ. `propose_children` rejects missing titles, invalid/out-of-range page values, titles without a normalized substring match on that page, duplicate/own titles and backwards page ordering. Cache candidates are constructed from the node's page span and selected kinds, excluding its own normalized title; this branch does not independently require a printed match. Both branches pass `own_children`, which rejects headings already represented by known/ancestor nodes and headings located outside shared-page ownership boundaries when matching lines establish that position. A missing printed match alone does not veto a cache candidate. Shared `assign_ends` and cost scoring still govern spans and attachment, and cost-increasing candidates are rejected. Thus accepted headings have no universal source-occurrence guarantee. No per-candidate human approval is inserted; the external cache's authorship and prior approval are uninspected. Trigger/objective is lowering the specified structural page-cost/read-token proxy, not independently verified QA improvement. Operating mode is bounded lookahead with at most three merge/expand rounds by default, not an open self-modification request. Empty/per-prompt failures may keep a node collapsed; unrecoverable model failures propagate. Mutation is in place, with no general rollback to the original tree. Summary prompts demand concise coverage; short leaves can return raw text and unsuccessful nodes may receive fallback summaries.

> if normalize(title) not in normalize(pages[page - 1]):
>     continue                     # the heading must be printed on that page
> --- `pageindex/tree_optimize.py`

> cached = own(children_from_cache(node, args.cache, args.kinds))
>         if cached:
>             candidates.append(("cache", cached))
> --- `pageindex/tree_optimize.py`

> printed = found(page, lambda line: key in normalize(line)) if key else []
>         if (is_node(page, child["title"])
>                 or page == start and top and printed and printed[-1] < top[0]
>                 or page == end and bottom and printed and printed[0] >= bottom[-1]):
>             continue
>         kept.append(child)
> --- `pageindex/tree_optimize.py`

These passages support the cache counterpath also identified by [MEM-OBJ-headings-cache](memory.md#mem-obj-headings-cache). Whether any actual cache supplied an unprinted heading, or such a heading was accepted in execution, remains unobserved.

> keep = cost < span and ratio >= args.min_gain_ratio and read_after < read_before
> --- `pageindex/tree_optimize.py`

Theory account: the localized formal cost account in [RT-OBJ-cost-policy](#rt-obj-cost-policy) guides choices and remains unchanged; candidates are document decompositions, not revisions of that account. Theory-builder conditions 1–4: condition 1 conclusion status: wired — whole formulae are exposed; condition 2 conclusion status: wired — comparisons control merges/expands; condition 3 conclusion status: absent — within inspected `optimize`/`expand`, no criticism attributes failure to the cost account and revises it; condition 4 conclusion status: absent — iterations retain tree decisions, not criticism-driven changes to that account. Addressability: constants/formula functions are separately inspectable and source-editable, but this route does not rewrite them. Persistence: formulas persist as shipped code; changed trees can persist across sessions through submission. Learning: improved future answering capacity is unestablished; calculated proxy reduction is insufficient evidence. Reflection and reflective theory building are not established by document-tree self-inspection; no representation/update loop of the optimizer's own method is demonstrated here. Candidate generation/selection is computational, but autonomy of a theory builder is not established when criticism/iteration conditions are missing. This is a document-product improvement mechanism; exercised self-improvement of PageIndex's own organization is not demonstrated.

#### RT-RTE-document-chat
Label: Managed own-model document QA

Endpoints/progression: caller messages/doc selection → managed prologue → Agents SDK runner with PageIndex tools → model-selected calls → final answer. `chat` is the answer-text facade; internal Chat Completions driver owns construction, external runner owns repeated next steps, answering model owns semantic tool/answer choices. Context includes guidance, target metadata, caller history and delivered tool results. SRC-1: `pageindex/client.py`, `pageindex/local_chat.py`, `pageindex/agent_tools.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: answer text or chat-completion envelope; stream variants yield visible text/events and usage.
- Later read-back: tools reload retained documents; chat history must be supplied by the caller, and this lane does not return appendable tool turns.
- Delegated visibility: provider receives managed instructions, supplied history/target block and fetched tool outputs; parser/model helper calls do not share this chat window.
- Selection predicate: model chooses discovery/document/page calls under natural-language guidance; local `doc_id` additionally restricts tool lookups, cloud own-model `doc_id` only targets via text.
- Invalidation or expiry: local scope is rebuilt per call; deleted document IDs fail later resolution; no durable session history is installed by this driver.
- Activation or effect: tools deliver evidence and model returns text; compliance with grounding/citation instructions and factual answer dependence are unobserved.
- Evidence limits: SDK runner/provider implementation and successful end-to-end behavior are not supplied; citation syntax is not a correctness oracle.

Decision roles: caller provides question/model/backend and optional limits; code constructs instructions, guards request skeleton and resolves tools; model selects semantic next steps. Operating mode: open document question answering, bounded by runner turn limit rather than a training curriculum. Answer oracle: none supplied in this path; page content is evidence, not an expected-answer reference. Guidance is policy, not enforced mandatory structure-first order. Tool response envelopes carry errors/next steps; fatal cloud transport/auth/limit conditions may escape rather than become ordinary tool errors.

> Runner.run(agent, input=items, **run_kwargs)))
> --- `pageindex/local_chat.py`

#### RT-RTE-protocol-history
Label: Responses and Messages history routes

Endpoints/progression: explicit protocol choice → protocol-specific context preparation → Agents SDK Responses or Anthropic tool runner → answer plus tool transcript. Owner: PageIndex wrapper constructs tools/scope; dependency runner coordinates repeated turns. Responses reuses `_openai_agent`; Messages separately constructs native tools, system blocks and transport. SRC-1: `pageindex/local_chat.py`, `pageindex/client.py`, `pageindex/integrations/anthropic_sdk.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Responses envelope with `items`, or Messages envelope with appended `messages`; protocol streams yield protocol events.
- Later read-back: caller can append returned transcript to a later invocation; persistence outside the call is caller-owned, not automatic disk chat storage.
- Delegated visibility: native runner receives prepared history, managed guidance, target block and tool functions; history can include earlier tool outputs.
- Selection predicate: caller selects protocol and history; model selects tools; local allowlist is passed in both drivers.
- Invalidation or expiry: per-call state is rebuilt; caller determines which previous transcript survives; cache breakpoints are request metadata, not expiry of stored knowledge.
- Activation or effect: appendable history is wired for reuse but no later invocation/behavioral dependence is observed.
- Evidence limits: dependency runner history mutation is version-sensitive; wrappers detect some incompatibilities but do not prove complete portable round trips.

Working-context distinction: these paths support bringing earlier tool evidence back by value rather than silently re-running retrieval. They do not themselves select an automatic history summary. Messages strips unexecuted final tool-use blocks from appendable history and aggregates usage across runner turns. Operating mode: open QA; no expected-answer oracle. Turn limits bound each run, not long-term document authority.

> envelope["messages"] = new_messages
> return envelope
> --- `pageindex/local_chat.py`

#### RT-RTE-alternate-builders
Label: Classic Markdown and file-output builders

Endpoints/progression: CLI PDF/Markdown arguments → Flash/classic or `md_to_tree` → `results/*_structure.json`; public functions also return trees without managed-store admission. Classic detects/extracts TOC or generates it from chunks, verifies title appearances, repairs/falls back, builds and summarizes the tree. Markdown extracts heading nodes/line content, optionally thins and summarizes. Owner: shipped CLI or direct caller; classic model proposes and judges title locations, code controls fallbacks. SRC-1: `run_pageindex.py`, `pageindex/page_index_classic.py`, `pageindex/page_index_md.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: tree object from direct functions, JSON file and path message from CLI.
- Later read-back: output file is available to subsequent callers; this CLI does not install it as a `DocStore` document.
- Delegated visibility: classic calls receive selected document chunks and TOC candidates; Markdown summaries see extracted node text.
- Selection predicate: CLI file type/mode and flags; classic score thresholds choose acceptance, bounded repair or fallback; Markdown thinning/summaries are explicitly configured.
- Invalidation or expiry: file outputs can be overwritten at the same derived path; no expiry or versioned rollback in the inspected CLI writer.
- Activation or effect: construction/JSON persistence are wired; no later consumer run is supplied.
- Evidence limits: classic model yes/no judgments are not independent expected-answer oracles; direct-function guarantees differ from managed submission.

Admission: caller starts generation and selects options; software/model admit produced structure without per-content human approval. Classic verification skips exceptions when calculating its checked fraction; a reported 1.0 is therefore not proof that every attempted check succeeded. Above 0.6 with incorrect entries it retries correction up to three times and returns the result even if incorrect entries remain. Lower scores fall back from numbered TOC to unnumbered to no-TOC or fail. This challenges a reading of “verify” as a hard correctness guarantee. Guidance consists of extraction/verification/summary prompts; persisted product is the generated JSON, not a revised indexing method. No runtime answer oracle, measured improvement or change to model parameters is established. Recovery is rerun or external replacement.

> checked_count = sum(1 for r in results if not isinstance(r, BaseException))
> accuracy = correct_count / checked_count if checked_count > 0 else 0
> --- `pageindex/page_index_classic.py`

#### RT-RTE-cloud-tools
Label: Cloud indexing tools and managed chat

Endpoints/progression: HTTP PDF upload → remote ID/status/getter endpoints; or own-model agent → MCP initialization/catalog → remote tool calls; or no own model → managed chat HTTP endpoint. Owner: client constructs requests, server controls remote processing and tool semantics. SRC-1: `pageindex/cloud_api.py`, `pageindex/mcp_bridge.py`, `pageindex/agent_tools.py`, `pageindex/client.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: upload JSON, remote content/tool results or managed chat response/stream.
- Later read-back: client can request previously uploaded IDs; remote storage lifecycle and model-context retention are opaque.
- Delegated visibility: PageIndex server receives PDF/messages/credentials; own-model path additionally delivers tool results to caller's model provider.
- Selection predicate: configured index/chat modes; remote tools/prompts discovered for key and read/full endpoint; remote retrieval policy uninspected.
- Invalidation or expiry: cached bridge replaced when key/base URL changes; session 404 triggers reinitialization and one replay; document deletion exposed remotely, internals opaque.
- Activation or effect: dynamic server tools/instructions are wired into local agent construction; actual catalog, invocation and behavioral changes are unobserved.
- Evidence limits: server implementation/live catalog/model are outside the frozen source; client wiring does not establish remote approval, scoping, accuracy or durability.

Capability/instruction admission: initialization provides instructions and `tools/list` provides schemas; the client copies and materializes these into tool definitions without a human per-tool approval stage. Missing tools/instructions fail loudly rather than silently using the local subset. The server is proposal authority; client construction admits whatever the selected endpoint serves. No local content-quality oracle or historical rollback is shown. New guidance can arrive without package changes; what persists locally is bridge/session state, not a demonstrated durable learned policy. Managed HTTP chat is opaque beyond request/response handling. MCP replay assumes a session-expiry 404 means no effect occurred; ordinary 400 is not replayed. The HTTP retry policy is transport recovery, not proof of exactly-once effects.

> tools_meta = bridge.list_tools()
> --- `pageindex/agent_tools.py`

#### RT-RTE-framework-tools
Label: Caller-owned and hosted framework tools

Endpoints/progression: `agent_tools`/OpenAI/Anthropic/Claude configuration → caller-controlled agent or hosted MCP connector → PageIndex reads, optionally management. Owner: PageIndex supplies tools/guidance, caller/dependency owns model loop and extra capability grants. OpenAI hosted MCP and Claude remote MCP bypass in-process tool execution while selecting the same remote endpoint gate. SRC-1: `pageindex/client.py`, `pageindex/integrations/openai_agents.py`, `pageindex/integrations/anthropic_sdk.py`, `pageindex/integrations/claude_agent_sdk.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: functions, tool objects or mutable configuration dictionaries, not an answer run.
- Later read-back: registered tools can reload stored documents when a later caller-run agent invokes them; config delivery alone is not exercised retrieval.
- Delegated visibility: hosted connector receives credentials and contacts cloud directly; local adapters invoke callbacks in caller process; caller decides what other tools/history an agent sees.
- Selection predicate: default read-only registration/endpoint, `include_management` opt-in; caller may replace instructions/model or add unrelated capabilities.
- Invalidation or expiry: rebuilding config changes registrations; remote session/auth lifecycle depends on connector; no per-config durable expiry in these factories.
- Activation or effect: tool/config construction is wired; actual agent integration, delegation and isolation envelope remain unobserved.
- Evidence limits: preapproval is not sandboxing; framework default tools/permissions and provider-native execution are external contracts.

The capability surface includes retrieval and opt-in removal locally, and whatever catalog the cloud serves remotely. Current built-in own-model grant is read tools, whereas exposed factories allow management. No additional per-deletion user approval is introduced by the inspected local remover. A caller can also invoke ordinary SDK methods directly. Admission of other host capabilities is outside these factories; the report does not attribute shell authority to PageIndex merely because an enclosing Claude runtime might have it.

> "require_approval": "never",
> --- `pageindex/integrations/openai_agents.py`

#### RT-RTE-vision-notebook
Label: Vision RAG notebook pipeline

Endpoints/progression: downloaded PDF/page images plus cloud-generated tree → direct VLM tree-selection prompt → JSON node IDs → selected nodes' page ranges mapped to images → direct VLM answer call. Owner: notebook code controls stages; [RT-CMP-vision-model](#rt-cmp-vision-model) chooses relevant nodes and answer. This is not the SDK's tool-using chat policy. SRC-1: `cookbook/pageindex-vision-rag.ipynb`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: printed reasoning/node selection and generated answer in the notebook.
- Later read-back: local PDF/images and fetched tree can be reused by notebook state; cross-session reload and answer retention are not established by the inspected cells.
- Delegated visibility: selector receives tree without text plus question; answer call receives selected page images and question, not the SDK managed tool conversation.
- Selection predicate: model-returned node list, followed by code mapping node ranges to page images; no independent relevance oracle.
- Invalidation or expiry: notebook variables/files are caller-controlled; no automatic invalidation in this pipeline is established.
- Activation or effect: code connects selection to image inputs; executed answer dependence and usefulness are unobserved.
- Evidence limits: source cells only; embedded outputs were not used as observed-run evidence, and cloud index construction remains opaque.

Working-context control: the second call is a separate frame containing only the selected visual evidence and answer prompt. Selection reasoning does not automatically share the answering window. Its natural-language “based only on context” constraint remains a request, not a code-enforced answer restriction. Operating mode: a fixed example question, not a curriculum or causal evaluation. No expected-answer reference is used by the executable selection/answer path.

> "tree_search_result = await call_vlm(search_prompt)"
> --- `cookbook/pageindex-vision-rag.ipynb`

### Claims

#### RT-CLM-layout-extraction
Label: LLM-free extraction versus default model passes

Claimed operation: Flash's tree extraction uses layout statistics without an LLM, while default summaries/full expansion use a model. This supports distinguishing extraction from the complete default pipeline, not calling all indexing model-free. The code wires `extract_toc` before optional passes and allows `summary=False, optimize=False`. SRC-1: `pageindex/flash/api.py`, `pageindex/flash/main.py`.

> result = extract_toc(_validate_pdf(pdf), use_embedded_toc=use_embedded_toc)
> --- `pageindex/flash/api.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-managed-guidance
Label: Managed guidance to answering model

Consumer: own-model QA agent. Channel: system instructions composed from PageIndex base guidance and caller additions, with optional citation guidance. Force: natural-language policy interpreted by the model, not deterministic mandatory tool sequencing. Horizon: each constructed chat invocation; static local guidance recurs across sessions and live cloud guidance can change at later construction. Evidence of delivery is wired; compliant behavior is unobserved. SRC-1: `pageindex/local_chat.py`, `pageindex/agent_tools.py`, `pageindex/client.py`.

> return "\n\n".join([CHAT_HEADER, base,
>                     *[t for t in extra_system if t.strip()]])
> --- `pageindex/local_chat.py`

#### RT-BAP-cost-selection
Label: Cost policy to tree admission

Consumer: optimizer's merge/expand selectors. Channel: symbolic formulae/constants and code comparisons. Force: deterministic admission/rejection within the inspected route, unlike model guidance. Horizon: all optimization rounds under the shipped configuration; its accepted tree may shape later retrieval after persistence. Actual retrieval benefit is unobserved. SRC-1: `pageindex/tree_optimize.py`.

> scored.sort(key=lambda s: s["expand_cost"])
> best = scored[0]
> --- `pageindex/tree_optimize.py`

## Annotations

none
