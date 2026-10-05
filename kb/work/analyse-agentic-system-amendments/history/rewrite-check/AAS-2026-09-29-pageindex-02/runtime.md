---
type: types/agentic-system-runtime-report.md
description: "Runtime baseline of PageIndex local mode at d2693d80: flash and standard PDF indexing into a stored page-range tree, a read-only tool-using chat agent over that tree, host-framework adapters, and the cloud client half"
run-id: AAS-2026-09-29-pageindex-02
reviewed-boundary: "d2693d80791a86345ef78b3234834f5fe53a70a0"
---

# PageIndex runtime report

## Runtime account

All anchors are commit-relative paths in SRC-1 (implementation) unless another source is named. No dynamic check was run; see the end of this section.

### Mode matrix and shipped entry paths

`PageIndexClient` (`pageindex/client.py`) has two independent sides. The index side is local when no `api_key` is given (documents indexed on the caller's machine, stored under `storage_path`, default `./.pageindex`) and cloud when one is. The chat side is "own-model" when a chat model is configured (the default local client always has one) and "managed cloud chat" only on a cloud client with no chat model. The source states the excluded combination itself:

> The fourth combination
>     (local documents + managed chat) cannot be expressed — the managed
>     chat cannot read your disk.
> --- `pageindex/client.py:333-335` @ `d2693d80791a86345ef78b3234834f5fe53a70a0`

Shipped entry paths: `PageIndexClient().submit_document(pdf)` then `client.chat(...)` or `client.chat_completions(...)` (the ordinary local invocation, traced below); `chat(protocol="responses")` and `chat(protocol="messages")` (own-model lanes over the OpenAI Responses and Anthropic Messages wires); `client.agent_tools()`, `as_openai_tools()`, `as_anthropic_tools()`, `as_claude_mcp()` and the `*_agent_config()` bundles (tools and instructions handed to a host runtime); the CLI `run_pageindex.py` (flash, standard, and a Markdown pipeline that the SDK does not expose); and cloud-mode calls that go through `pageindex/cloud_api.py` and `pageindex/mcp_bridge.py`.

### Loop 1 — local indexing (ordinary invocation, first half)

- **Trigger and principal.** A caller (developer program or the CLI) calls `submit_document(file_path)`. The caller supplies the PDF and, optionally, `metadata`, an index model, `optimize` mode, summary knobs.
- **Identities.** The caller's process; the LLM provider key read by LiteLLM from the environment or `index_backend`. There is no PageIndex-side identity in local mode.
- **Next-step owner.** Fixed program code: `LocalAPI.submit_document` in `pageindex/local_api.py` calls `_index_flash` (default) or `_index_standard`, then writes the store. The model never chooses the next step in flash mode.
- **Decision policy and form.** Flash tree extraction is symbolic (layout statistics, embedded-bookmark use, clustering and heading detection under `pageindex/flash/`; no model). The refinement pass in `pageindex/tree_optimize.py` is symbolic (cost-driven merge and expand admission) with a model proposing candidate subsections (see RT-RTE-8). Node summaries and the document description are model output written into the tree (RT-CMP-1). Standard mode makes the model propose and verify the structure (RT-RTE-9).
- **Context.** Per call, only the prompt text of that call: page text truncated to 6000 characters per page for expand, node text or child summaries for summaries, the structure for the description.
- **State.** In-memory tree during the run; on success, three JSON files per document plus a manifest (RT-OBJ-1, RT-OBJ-2, RT-OBJ-3).
- **Executor and effect boundary.** In-process Python; PDF read from disk by `pypdfium2` (structure) and `PyPDF2` (page text); page text is sent to the LLM provider; writes only under `storage_path`. Flash extraction may use worker processes (`pageindex/flash/parser_pdfium_parallel.py`); `submit_document` refuses re-entry inside a spawned worker.
- **Runtime-client controls.** `optimize` (`full`, `merge`, `off`), `use_embedded_toc`, `summary_max_words`, `summary_concurrency`, `mode` (`flash` or `standard`), `index_model`, `index_backend`. The refusal policy `flash_rejection_reason` in `pageindex/flash/api.py` rejects scanned or image-only PDFs, and layout-less PDFs of more than 10 pages, instead of storing a degraded tree.
- **Persistence.** Store write at the end of the call. The `optimize` report (merges, expands, before and after search cost) is returned by the flash function but `_index_flash` in `pageindex/local_api.py` keeps only `structure` and the description, so the local store does not retain it; the CLI writes the whole result.
- **Coordination and return.** Synchronous; summaries and expand run concurrently under semaphores (defaults 64 and up to 32 in flight). Returns `{doc_id, name}`.
- **Recovery.** LLM calls retry up to 10 times with a 1 s delay; statuses 400, 401, 403, 404 do not retry (`pageindex/utils.py`). A per-node summary failure is absorbed and the node gets an empty summary unless every node fails or the failure is unrecoverable. The store writes `tree.json`, `pages.json` and then `doc.json` atomically per file, and `list_metas` requires `doc.json`, so an interrupted write leaves an unlisted directory rather than a half-visible document.
- **Terminal output.** A stored document with status `completed`.

The store write set:

> _write_json_atomic(doc_dir / "tree.json", tree)
>         _write_json_atomic(doc_dir / "pages.json", pages)
>         _write_json_atomic(doc_dir / "doc.json", meta)
> --- `pageindex/local_store.py:120-122` @ `d2693d80791a86345ef78b3234834f5fe53a70a0`

### Loop 2 — own-model chat over the local tree (ordinary invocation, second half)

- **Trigger and principal.** A caller passes a question or message history to `chat` or `chat_completions`, optionally with `doc_id`, `instructions`, `citations=True`, `max_turns`.
- **Identities.** The caller's process; the LLM provider key for the chat model. No end-user identity is modeled.
- **Next-step owner.** The chat model (RT-CMP-2) decides each next tool call inside an OpenAI Agents SDK `Runner` loop that PageIndex constructs (`_openai_agent` and `_chat_agent` in `pageindex/local_chat.py`). The host loop belongs to `openai-agents`; PageIndex fixes its inputs.
- **Decision policy and form.** Distributed-parametric (the model) steered by natural-language instructions and tool descriptions (RT-OBJ-4). Local discovery has no ranking: `browse_documents` lists documents newest first and the model matches names and descriptions itself; semantic ranking and folders are refused in local mode. Retrieval is therefore model reasoning over the outline that `get_document_structure` returns, followed by page reads that `get_page_content` serves by page number.
- **Context.** The system prompt (`CHAT_HEADER`, `AGENT_INSTRUCTIONS`, optional client and per-call `instructions`, optional citation prompt), a leading user message with the targeted documents' metadata when `doc_id` is set, the caller's history, and tool results. Tool results carry the outline without node text, or page markdown up to a 95,000 character budget per response. Nothing else enters.
- **State.** The run's transcript in the Agents SDK; no PageIndex-side conversation store. Multi-turn is caller-owned: the caller passes the history back.
- **Executor and effect boundary.** The four read tools execute in-process against the store and never write. The model call goes to the provider. There is no shell, filesystem or network tool. `remove_document` exists but is registered only with `include_management=True`, and the chat lanes never pass it (see Guarantee B).
- **Runtime-client controls.** `max_turns` (unset uses the Agents SDK default; the source comments give 10), `reasoning_effort`, `temperature`, `top_p`, `max_tokens`, `backend`, `extra_body`, `show_process`. Tracing is turned off.
- **Persistence.** None beyond the provider's own prompt cache, which PageIndex keys with a per-conversation `prompt_cache_key` for OpenAI destinations.
- **Coordination and return.** Single agent, no delegation. Returns the answer string, a chat-completions envelope, a `ChatStream` of typed events, or the Responses or Messages envelope.
- **Recovery.** Tools never raise: errors come back as a JSON envelope with `next_steps` options. A cap on turns raises `PageIndexAPIError` on the OpenAI lanes. The Messages lane fails fast on re-raised transport failures between turns.
- **Terminal output.** The final answer text; with `citations=True` the model is instructed to emit `<cite doc=... page=.../>` tags, and page-level citations are checked only by `get_citations` and `resolve_citations`, which this pass did not trace.

### Alternate and equivalent paths

- **Direct model calls.** `client.get_page_content`, `get_tree`, `get_ocr` and friends read the store with no scope and no model. The whole-library store is also readable as plain files.
- **Provider-native tools.** Cloud `as_openai_tools(hosted=True)` hands a hosted MCP tool to OpenAI; nothing comparable exists locally.
- **Host callbacks and manual graph control.** The adapters in `pageindex/integrations/` give a host runtime the same four tools; the host owns the loop, memory and approvals (RT-RTE-4). `chat(protocol="responses")` and `chat(protocol="messages")` accept a caller-round-tripped transcript (RT-RTE-5).
- **Shell, extension code, subprocess, remote workers.** PageIndex ships no shell or extension mechanism. Flash parsing may use subprocess workers. Cloud mode moves indexing and storage to a remote service outside the boundary (RT-RTE-6).
- **Durable variants.** The store is durable across processes and guarded by an `fcntl` lock only for name uniquing; there is no resumable run state.

### Guarantees

- **Guarantee A, document scope for local own-model chat.** Owner: SDK. Enforcement point: `call_tool` in `pageindex/agent_tools.py` builds a frozenset from `doc_ids`, and `_resolve_document`, `_browse_documents` and the other read tools filter on it; the scope key starts with an underscore and `call_tool` strips underscore keys from model arguments, so the model cannot supply it. Guarantee strength: `invariant`, covering only agent tool calls made through the chat lanes and `_tool_specs` with `doc_ids` set on a local client. Not covered: the direct client methods, the host adapters `as_openai_tools`, `as_anthropic_tools`, `as_claude_mcp` and `agent_tools` (their public signatures take no document scope, so scoping there is the `document_context` prompt text), cloud own-model chat (`_local_doc_scope` returns `None` on a cloud client and the source says targeting is prompt-level only), and any call without `doc_id`. Required external contract: none locally. Implementation conclusion status: `wired`. Operation conclusion status: `uninspected`.
- **Guarantee B, read-only agent tool set by default.** Owner: SDK. Enforcement point: `_READ_TOOLS` and `_MANAGEMENT_TOOLS` and `tool_names`; the chat lanes call `build_openai_tools(client, doc_ids=doc_ids)` and `build_anthropic_tools(client, doc_ids=scope, failures=failures)` with `include_management` left at its default false. Strength: `invariant` for the chat lanes; `policy` for host adapters, where the caller opts in with `include_management=True` and then the model can call irreversible `remove_document`. The tool description says to delete only after the user names the documents and confirms, which is prompt-level guidance. Implementation conclusion status: `wired`. Operation conclusion status: `uninspected`.
- **Guarantee C, tools do not raise into the agent loop.** Enforcement point: `call_tool` catches exceptions and converts them to error envelopes; the stated exceptions are cloud 401/403, exhausted 429/5xx, unreachable server and rate-limit tool errors. Strength: `best effort` (it is a coded catch, but the cloud exceptions re-raise by design). Implementation conclusion status: `wired`. Operation conclusion status: `uninspected`.
- **Guarantee D, a stored expanded node names only headings printed on its page.** Enforcement point: `propose_children` in `pageindex/tree_optimize.py` (see RT-RTE-8). Strength: `invariant` for LLM-proposed children on the flash expand path; the alternative "cache" candidate source is not from the model. It does not cover summaries, titles rewritten by the leaf summary call, or the standard pipeline. Implementation conclusion status: `wired`. Operation conclusion status: `uninspected`.

### Forcing cases traced

1. **Document scope under model control** (Guarantee A). Traced `call_tool`, `_resolve_document`, `_browse_documents`. Result: scope is structural for the chat lanes, and absent on the adapter and cloud paths named above.
2. **Write authority of the agent** (Guarantee B). Traced the four registration sites. Result: the chat agent cannot delete or upload; a host that sets `include_management=True` gives its model deletion.
3. **Expand and merge admission at index time** (RT-RTE-8). Traced `optimize`, `merge`, `expand`, `propose_children`.
4. **Standard-mode verify and fix** (RT-RTE-9). Traced `meta_processor`, `verify_toc`, `fix_incorrect_toc_with_retries`.

### Execution preflight

`no dynamic check planned`. Checks considered: the Python test suite (`tests/`, about 11,000 lines; it stubs the LLM key and builds minimal PDFs), a flash extraction with `summary=False, optimize=False` on an example PDF (no model, needs `pypdfium2`), and a scripted `call_tool` probe against a temporary store. Static inspection sufficed for the traced guarantees, which are code paths visible in the frozen blobs; a run would show the same branches without adding evidence about model behavior, and the model-dependent quality claims cannot be checked without provider credentials and cost. No conclusion here depends on a run. Conclusions about operation (as opposed to implementation) are therefore `uninspected`, and none is stated as `observed`.

## Probe evidence

none

## Shared records

### Components

#### RT-CMP-1 — Index and summary model
- **Source-native identity.** The LiteLLM model named by `index_model`, `summary_model` or legacy `model`; SDK default `DEFAULT_INDEX_MODEL = "gpt-5.6-luna"`. SRC-1 `pageindex/utils.py`, `pageindex/config.yaml`.
- **Representational form and storage.** Distributed-parametric, provider-hosted; its outputs are stored as `summary` fields and the document `description`.
- **Used by.** RT-RTE-1 (summaries, expand proposals, description), RT-RTE-3 (all classic prompts), RT-RTE-8, RT-RTE-9.
- **Fixity, parameter change during operation.** No PageIndex code updates model parameters (RT-ABS-1). Provider-side change is `uninspected`. Conclusion status: `uninspected`.
- **Fixity, version pinning.** The name is passed to LiteLLM as given; bare names route to `openai/<name>`. No dated snapshot or hash is required or checked, so resolution is a mutable provider endpoint. Conclusion status: `wired`.
- **Evidence limits.** Provider internals uninspected. The README states the pipeline "is designed not to rely heavily on the model used at index time" (SRC-3, reported), which this pass did not test.

#### RT-CMP-2 — Chat model
- **Source-native identity.** The model named by `chat_model`, `retrieve_model`, per-call `model`, or `DEFAULT_CHAT_MODEL = "gpt-5.6-sol"`; the Anthropic Messages lane takes a Claude model from `chat_model` and never sends the stock default. SRC-1 `pageindex/utils.py`, `pageindex/local_chat.py`.
- **Representational form and storage.** Distributed-parametric, provider-hosted or user-endpoint; the transcript lives only in the host loop.
- **Used by.** RT-RTE-2, RT-RTE-5.
- **Fixity, parameter change during operation.** No PageIndex code updates parameters (RT-ABS-1). Conclusion status: `uninspected` for the provider.
- **Fixity, version pinning.** As for RT-CMP-1, mutable endpoint resolution, no pin. Conclusion status: `wired`.
- **Evidence limits.** Retrieval quality depends on this model; README figures are reported only (RT-CLM-2, RT-CLM-3).

### Operative objects

#### RT-OBJ-1 — Tree index (`tree.json`)
- **Source-native identity.** A list of nodes `{title, node_id, start_index, end_index, summary, key_items?, nodes?}` with 1-based inclusive page ranges. SRC-1 `pageindex/local_store.py`, `pageindex/local_api.py`; README schema in SRC-2 `pageindex/flash/README.md`.
- **Form and substrate.** Natural-language titles and summaries in JSON on disk; the page ranges are symbolic. Node `text` is removed before saving.
- **Evidence.** Implementation: `wired`. Sample outputs in SRC-4 exist but carry no run provenance and the sampled file has no summaries, so they say nothing about the frozen pipeline.

#### RT-OBJ-2 — Page text store (`pages.json`)
- **Source-native identity.** One record per page, `{page_index, markdown}`, from `PyPDF2` text extraction with surrogates replaced. SRC-1 `pageindex/local_api.py`.
- **Form and substrate.** Natural language in JSON. This is the only text the agent can read; `get_page_content` serves it by page number.
- **Evidence.** `wired`. The tree parser (pdfium) and the page text parser (PyPDF2) differ; `_check_page_bounds` refuses stores whose node ranges fall outside the readable pages.

#### RT-OBJ-3 — Document metadata and manifest (`doc.json`, `manifest.json`)
- **Source-native identity.** `{id, name, description, status, createdAt, pageNum, folderId, metadata, mode}` per document; the manifest is a cache rebuilt from `doc.json` files by `list_metas`. `description` is model-written (`generate_doc_description`). SRC-1 `pageindex/local_store.py`.
- **Form and substrate.** Mixed: symbolic fields plus one natural-language description. `browse_documents` and the targeting message show name and description to the chat model.
- **Evidence.** `wired`.

#### RT-OBJ-4 — Agent instruction text and tool contract
- **Source-native identity.** `AGENT_INSTRUCTIONS` (reading workflow, tool rules, discovery, persistence) and `TOOL_CONTRACT` descriptions and schemas in `pageindex/agent_tools.py`; `CHAT_HEADER` in `pageindex/local_chat.py`; frozen citation prompts `LOCAL_CITATION_PROMPTS`.
- **Form and substrate.** Natural language inside Python constants; schemas are symbolic. Local descriptions are adapted so they do not teach cloud-only capabilities.
- **Evidence.** `wired` into the system prompt and tool registration (RT-RTE-2).

#### RT-OBJ-5 — Index-time prompts and constants
- **Source-native identity.** Summary prompts and `SUMMARY_*` constants in `pageindex/utils.py`; `EXPAND_PROMPT` and the cost constants `TRIGGER_PAGES`, `ROUTING_COST`, `PAGE_CHARS` in `pageindex/tree_optimize.py`; classic prompts and `_SYSTEM_HARDENING` in `pageindex/page_index_classic.py`.
- **Form and substrate.** Natural-language prompts and numeric constants in code; not editable at run time except through the exposed knobs.
- **Evidence.** `wired`.

### Routes

#### RT-RTE-1 — Flash indexing (default local)
- **Endpoints and progression.** `submit_document` → `_index_flash` → `page_index_flash` → `extract_toc` (layout statistics, embedded bookmarks when trusted) → page-node fallback if no hierarchy → `optimize` and summaries overlapped by `SummaryScheduler` → `write_node_id` → `generate_doc_description` → `save_document`. SRC-1 `pageindex/local_api.py`, `pageindex/flash/api.py`.
- **Owner.** Program code; model called for summaries, expand proposals and description (RT-CMP-1).
- **Effects.** Context: none persists between calls. State: writes RT-OBJ-1, RT-OBJ-2, RT-OBJ-3. Action: provider calls and disk writes only.
- **Implementation conclusion status:** `wired`. **Operation conclusion status:** `uninspected`.
- **Immediate return.** `{doc_id, name}`.
- **Later read-back.** Every later chat or tool call reads the stored tree and pages. This is the persisted product of an indexing run, not material accumulated through use.
- **Delegated visibility.** Not applicable: no delegate.
- **Selection predicate.** The whole document is indexed; refusal when `flash_rejection_reason` matches. Leaves under 200 tokens reuse raw text as the summary; a parent summary sees at most the first 3 uncovered pages plus child summaries.
- **Invalidation or expiry.** None; a document is replaced only by deleting and resubmitting (a repeated name gets a `_1` to `_99` suffix).
- **Activation or effect.** Not established: evidence that the summaries or outline changed answer quality is README-reported only (RT-CLM-2, RT-CLM-3).
- **Evidence limits.** No indexing run was performed. Cloud OCR and image handling are outside the boundary; local mode refuses scanned PDFs.

#### RT-RTE-2 — Own-model chat agent over local tools
- **Endpoints and progression.** `chat` or `chat_completions` → `run_chat_completions` → `_chat_agent` (validate history, targeting block, `_openai_agent`) → `Runner.run` or `run_streamed` → model turns and tool calls → answer. SRC-1 `pageindex/client.py`, `pageindex/local_chat.py`, `pageindex/chat_stream.py`.
- **Owner.** The chat model (RT-CMP-2) chooses tool calls; the host loop is `openai-agents`.
- **Effects.** Context: instructions plus tool results as described in Loop 2. State: none written. Action: read-only tools. The registration site is one line:

> tools=build_openai_tools(client, doc_ids=doc_ids),
> --- `pageindex/local_chat.py:398-398` @ `d2693d80791a86345ef78b3234834f5fe53a70a0`

- **Discovery is model matching, not ranking.** Local `browse_documents` refuses `sort="relevance"` and `query` with the comment:

> Semantic ranking is a cloud capability; like folders, it is not
> --- `pageindex/agent_tools.py:739-739` @ `d2693d80791a86345ef78b3234834f5fe53a70a0`

- **No telemetry.** The run config disables tracing:

> No traces — the caller opted into QA, not telemetry.
> --- `pageindex/local_chat.py:484-484` @ `d2693d80791a86345ef78b3234834f5fe53a70a0`

- **Implementation conclusion status:** `wired`. **Operation conclusion status:** `uninspected`.
- **Immediate return.** Answer text, envelope or event stream.
- **Later read-back.** None from PageIndex. The caller may pass the visible history back; that is caller-owned session state, not read-back through use.
- **Delegated visibility.** Not applicable.
- **Selection predicate.** Model choice, bounded by the instructions in RT-OBJ-4 and the doc scope of Guarantee A. `get_page_content` keeps whole pages until the character budget fills and reports the pages it omitted.
- **Invalidation or expiry.** Not applicable: no retained state.
- **Activation or effect.** Not established: whether the model follows the reading workflow and persistence protocol is unobserved here.
- **Evidence limits.** No model call was run. Accuracy, cost and turn counts are README-reported (RT-CLM-2, RT-CLM-3).

#### RT-RTE-3 — Standard (classic) indexing
- **Endpoints and progression.** `submit_document(mode="standard")` → `_index_standard` → `page_index_main` → `tree_parser`: `check_toc` (model detects TOC pages) → `meta_processor` in mode with page numbers, without, or no TOC → `verify_toc` and repair (RT-RTE-9) → title-at-start checks → `post_processing` → recursive splitting of nodes over 10 pages and 20,000 tokens → `merge_tree` → summaries and description. SRC-1 `pageindex/page_index_classic.py`, `pageindex/local_api.py`.
- **Owner.** Program code sequences; the model (RT-CMP-1) proposes structure, page numbers and verification answers.
- **Effects.** Same stores as RT-RTE-1. Prompts wrap PDF text in `<user_document>` delimiters, redact a keyword list and prepend `_SYSTEM_HARDENING`.
- **Implementation conclusion status:** `wired`. **Operation conclusion status:** `uninspected`.
- **Immediate return, later read-back, delegated visibility, invalidation.** As RT-RTE-1.
- **Selection predicate.** TOC detection and the accuracy thresholds of RT-RTE-9.
- **Activation or effect.** Not established.
- **Evidence limits.** The keyword redaction is a fixed list; its effectiveness against injection was not tested.

#### RT-RTE-4 — Host-framework tool adapters
- **Endpoints and progression.** `agent_tools`, `as_openai_tools` (`pageindex/integrations/openai_agents.py`), `as_claude_mcp` (`pageindex/integrations/claude_agent_sdk.py`), `as_anthropic_tools` (`pageindex/integrations/anthropic_sdk.py`), `agent_instructions`, `document_context`. Each wraps `_tool_specs`, which on a local client calls `call_tool` over the store.
- **Owner.** The host runtime's model and loop; PageIndex supplies tools, schemas and instruction text.
- **Effects.** Context and state are the host's. Action: the same four read tools; `include_management=True` adds `remove_document` (`_MANAGEMENT_TOOLS`):

> _MANAGEMENT_TOOLS = ("remove_document",)
> --- `pageindex/agent_tools.py:307-307` @ `d2693d80791a86345ef78b3234834f5fe53a70a0`

- **Implementation conclusion status:** `wired`. **Operation conclusion status:** `uninspected`.
- **Immediate return.** JSON envelopes as text content.
- **Later read-back.** Host-owned; not traced.
- **Delegated visibility.** Host-owned; PageIndex adds none.
- **Selection predicate.** No document scope on these public methods (Guarantee A limits).
- **Invalidation or expiry.** Not applicable.
- **Activation or effect.** Not established.
- **Evidence limits.** Host loops, approval flows and persistence are excluded by the boundary and were not inspected.

#### RT-RTE-5 — Responses and Messages protocol lanes
- **Endpoints and progression.** `chat(protocol="responses")` → `run_responses`; `chat(protocol="messages")` → `run_messages` using the Anthropic `beta.messages.tool_runner` with `max_iterations` defaulting to 10. SRC-1 `pageindex/local_chat.py`.
- **Owner.** The chat model chooses tool calls; PageIndex drives the runner.
- **Effects.** Same read tools with `doc_ids` scope; the caller may round-trip the provider transcript so a follow-up "re-reads the run" instead of redoing tool work, according to the `chat` docstring.
- **Implementation conclusion status:** `wired`. **Operation conclusion status:** `uninspected`.
- **Immediate return.** Provider-native envelope or events.
- **Later read-back.** The transcript is returned to the caller and only re-enters if the caller passes it back. That is caller-held session state.
- **Delegated visibility.** Not applicable.
- **Selection predicate.** Caller decides what history to pass.
- **Invalidation or expiry.** Provider cache lifetime, uninspected.
- **Activation or effect.** Not established.
- **Evidence limits.** Provider cache behavior and Bedrock and Vertex variants were not traced.

#### RT-RTE-6 — Cloud-mode client half
- **Endpoints and progression.** With an `api_key`, `PageIndexClient` uses `pageindex/cloud_api.py` for documents and `McpBridge` in `pageindex/mcp_bridge.py` for tools; the instruction text and tool list come from the server:

> Cloud: the live instructions the MCP server serves for the tool set
>     actually shipped. Local: the built-in subset instructions.
> --- `pageindex/agent_tools.py:1678-1679` @ `d2693d80791a86345ef78b3234834f5fe53a70a0`

- **Owner.** The remote service for indexing, storage, and served instructions; the caller's chat model (or the managed chat) for retrieval.
- **Effects.** Action crosses to a remote service; own-model chat over cloud documents sends page content through the caller's process to the caller's model provider.
- **Implementation conclusion status:** `wired` for the client. **Operation conclusion status:** `uninspected`.
- **Immediate return, later read-back, delegated visibility, selection predicate, invalidation or expiry, activation or effect.** `uninspected`: server behavior and served instructions are outside the boundary (Boundary and evidence, exclusions).
- **Evidence limits.** Only client code was read. The client refuses to substitute local instructions when the server returns none.

#### RT-RTE-7 — Markdown pipeline (CLI only)
- **Endpoints and progression.** `run_pageindex.py --md_path` → `md_to_tree` in `pageindex/page_index_md.py`: parse `#` headings, optional token-based thinning, optional model summaries, write `results/<name>_structure.json`.
- **Owner.** Program code; model only for summaries.
- **Effects.** Writes a JSON file; does not enter the local store, and `submit_document` accepts only PDFs.
- **Implementation conclusion status:** `wired`. **Operation conclusion status:** `uninspected`.
- **Immediate return, later read-back.** The file is read only if a caller loads it; no shipped route does.
- **Delegated visibility, invalidation or expiry.** Not applicable.
- **Selection predicate.** Heading levels.
- **Activation or effect.** Not established.
- **Evidence limits.** Not traced beyond structure.

#### RT-RTE-8 — Flash merge and expand admission (index-time product change)
- **Endpoints and progression.** `optimize` in `pageindex/tree_optimize.py`: deterministic `merge_same_page` and cost-driven `merge`, then `expand` for collapsed nodes whose page span exceeds `TRIGGER_PAGES` (5). `propose_children` prompts RT-CMP-1 with up to 6000 characters per page and validates the answer; `expand` scores every candidate level (the model's, and a cached detection when present) by `expand_cost` and keeps the cheapest. Merge and expand repeat for up to 3 rounds until neither changes the tree, and nodes decided once are frozen so they cannot flip between rounds. Structural checks (`validate`) are reported as `new_issues` in the returned report and do not block storing the tree. `SummaryScheduler` starts a node's summary once `mark_final` says its children are settled.
- **Trigger.** A node larger than 5 pages with no children.
- **Proposed change.** A model-listed set of subsection headings with start pages; a merge of a subtree into its parent with removed titles kept as `key_items`.
- **Decision role, proposer.** The model (RT-CMP-1) for expand candidates. **Decision role, decider and veto.** Computation: the cost rule and the printed-heading check. **Human contribution.** The caller picks `optimize` mode and supplies the documents; no human decides per node.
- **Admission.** The rule is stated in the module docstring:

> expand iff     expand_cost < collapse_cost                  (ties keep collapsed)
> --- `pageindex/tree_optimize.py:15-15` @ `d2693d80791a86345ef78b3234834f5fe53a70a0`

  Code also requires a minimum gain ratio (`min_gain_ratio`). Proposed headings are dropped unless printed on the claimed page:

> if normalize(title) not in normalize(pages[page - 1]):
>             continue                     # the heading must be printed on that page
> --- `pageindex/tree_optimize.py:643-644` @ `d2693d80791a86345ef78b3234834f5fe53a70a0`

- **Rejection ability.** Yes: `keep_collapsed`, and empty model answers are retried then trusted as none. A node that is kept collapsed is frozen.
- **Rollback or recovery.** None: the pre-optimize tree is not retained locally and `optimize` failures raise only for unrecoverable model errors. `optimize="off"` skips the pass.
- **Answer oracle.** None. The page text is the reference for whether a heading exists, not an expected answer to a question. Model judgment is not an answer oracle.
- **Operating mode.** A bounded, per-document, one-shot refinement; not an open request or curriculum.
- **Guidance and persistence.** The guidance is `EXPAND_PROMPT` plus the cost formulas (RT-OBJ-5). What persists is the resulting tree (RT-OBJ-1) with `key_items`; the cost metrics report is returned but not stored locally.
- **Theory route.** The theory is that retrieval cost is well approximated by pages scanned plus one page per routing step, with the parameters `ROUTING_COST` and `TRIGGER_PAGES`. Addressability: the rule and its constants are separately named and documented in one file, so an assumption can be changed by editing one constant or one expression, and the docstring retains the rationale, but no later route reads that docstring. Boundary of this judgment: `pageindex/tree_optimize.py`.
- **Theory-builder condition 1, localized content.** `wired`. **Condition 2, consumption.** `wired` (admission depends on the formulas). **Condition 3, content-directed criticism with resulting revision.** `absent` (RT-ABS-2). **Condition 4, iteration.** `absent` (RT-ABS-2).
- **Persistence grade.** The tree persists across runs of chat on the same document; the rule set does not change with use.
- **Learning.** `absent`: no retained result of criticism changes future capacity (RT-ABS-1, RT-ABS-2). **Reflection.** `absent` (RT-ABS-2). **Autonomy, role by role.** Proposer: computation with a model. Decider: computation. Configuration and inputs: user. Status: `wired`.
- **Implementation conclusion status:** `wired`. **Operation conclusion status:** `uninspected`.
- **Immediate return.** The optimized structure and a report dict.
- **Later read-back.** The tree is read by every chat run; the report is not.
- **Delegated visibility.** Not applicable.
- **Selection predicate.** Span above trigger and cost rule; model proposals filtered by printed-heading, page-range and order checks.
- **Invalidation or expiry.** None.
- **Activation or effect.** Not established: the effect on retrieval is README-reported only (RT-CLM-2).
- **Evidence limits.** No run; the "cache" candidate source is fed by a detection cache the SDK path does not pass, so only the model candidate applies there.

#### RT-RTE-9 — Standard-mode TOC verify and fix admission
- **Endpoints and progression.** `meta_processor` → model proposes TOC entries with physical page numbers → `verify_toc` asks the model, per entry, whether the title appears on that page (`check_title_appearance`) → branch on the share of confirmed entries → `fix_incorrect_toc_with_retries` (up to 3 attempts) or fall back from the with-page-numbers mode to without, then to no-TOC.
- **Trigger.** Any standard-mode run.
- **Proposed change.** A structure with page numbers, and per-entry repairs.
- **Decision role, proposer and decider.** The model proposes the structure and also verifies it (same RT-CMP-1); computation applies thresholds. **Veto.** Computation: accuracy of exactly 1.0 accepts. Accuracy above 0.6 with mistakes goes to repair and the result is then returned whether or not mistakes remain. Otherwise the mode falls back and the last mode raises `Processing failed`:

> if accuracy > 0.6 and len(incorrect_results) > 0:
> --- `pageindex/page_index_classic.py:1156-1156` @ `d2693d80791a86345ef78b3234834f5fe53a70a0`

- **Rejection ability.** Yes, at the mode level. **Rollback or recovery.** Fallback to the next mode; no retained prior tree.
- **Answer oracle.** None. The page text is the reference, checked by a model.
- **Operating mode.** Bounded per-document repair.
- **Guidance and persistence.** Classic prompts (RT-OBJ-5); the resulting tree persists.
- **Theory route.** Not a theory route: no stated theory is applied, criticized or revised; the check is a per-entry model judgment. Theory-builder conditions 1 to 4: `absent` for each under RT-ABS-2.
- **Implementation conclusion status:** `wired`. **Operation conclusion status:** `uninspected`.
- **Immediate return.** Structure and accuracy log.
- **Later read-back.** The tree, as RT-RTE-1.
- **Delegated visibility.** Not applicable.
- **Selection predicate.** Confirmed by a model on the page text; an early return of accuracy 0 applies when the last located page lies in the first half of the document.
- **Invalidation or expiry.** None.
- **Activation or effect.** Not established.
- **Evidence limits.** A failing check call is skipped rather than counted, so accuracy is computed over answered checks only.

### Claims

#### RT-CLM-1 — Vectorless, reasoning-based retrieval
- **Claimed operation.** A tree index replaces the vector index and an LLM searches it agentically; no vector database or chunking (README title and introduction). SRC-2 `README.md`. Conclusion status: `claimed`; implementation support is in RT-RTE-2 and RT-ABS-4.

#### RT-CLM-2 — Indexing and query cost and time, accuracy on a 62-question benchmark
- **Claimed operation.** About $0.001 per page to index with the default index model, 13 seconds to 4.5 minutes for 9 to 1,098 pages, and reported accuracy and cost per question for the OSS benchmark and native-PDF comparison. SRC-3 `README.md`, `assets/results-light.png`, `assets/index-cost-light.png`, `assets/query-cost-light.png`. Conclusion status: `claimed`. Not observed: runners live in external repositories not frozen here.

#### RT-CLM-3 — FinanceBench accuracy
- **Claimed operation.** The README reports a state-of-the-art result on FinanceBench:

> PageIndex reached a state-of-the-art [**98.7% accuracy**](https://vectify.ai/blog/Mafin2.5) on
> --- `README.md:164-164` @ `d2693d80791a86345ef78b3234834f5fe53a70a0`

- SRC-3. Conclusion status: `claimed`. The linked blog names Mafin 2.5, not necessarily this open-source SDK's local mode; that link is outside the boundary.

#### RT-CLM-4 — Local mode runs entirely on the caller's machine with their own LLM key
- **Claimed operation.** "index, retrieve, and chat entirely on your machine with your own LLM key" (README news item). SRC-2 `README.md`. Conclusion status: `wired` for the storage and tool path; page text still goes to the caller's chosen provider, which is the claim's own qualification. Operation: `uninspected`.

#### RT-CLM-5 — Traceable and explainable retrieval
- **Claimed operation.** README describes retrieval as traceable and explainable. SRC-2 `README.md`. Conclusion status: `afforded`: page-level citations and `show_process` event streams exist (RT-RTE-2), but this pass did not trace citation resolution or observe a run.

### Evidenced absences

#### RT-ABS-1 — No write-back from use into the store or model parameters
- **Searched boundary.** SRC-1 `pageindex/` at the frozen commit, all `.py` files (excluding `pageindex/flash/` for store writes), searched for writers (`save_document`, `_write_json_atomic`, `json.dump`, `open(..., "w")`) and for training or fine-tuning calls. The only store writers are `save_document` (called once, from `submit_document`) and `delete_document` (called from `remove_document` and the client method); the CLI and `tree_optimize` command-line entry write user-named result files.
- **Conclusion status:** `absent`.
- **Conclusion supported.** No query, tool call or chat turn changes retained documents, trees, instructions or model parameters; chat history is caller-held. **Conclusion prevented.** Nothing about cloud-side behavior, host runtimes, or provider-side learning.

#### RT-ABS-2 — No criticism or revision loop over index-time rules or prompts
- **Searched boundary.** SRC-1 `pageindex/` at the frozen commit: `tree_optimize.py`, `page_index_classic.py`, `utils.py`, `local_api.py`, `flash/api.py`. Query: any code path that changes `EXPAND_PROMPT`, cost constants, thresholds or summary prompts from run outcomes, or that stores criticism of them. The optimize report and classic `accuracy` are computed and logged or returned and not read by a later round.
- **Conclusion status:** `absent`.
- **Conclusion supported.** Neither RT-RTE-8 nor RT-RTE-9 iterates on criticism of its rules. **Prevented.** Human edits to the repository over time (commit history) were not examined and may revise these rules.

#### RT-ABS-3 — No query-time sanitization of page text
- **Searched boundary.** SRC-1 `pageindex/`: `_secure_doc_text`, `_SYSTEM_HARDENING` and `user_document` occur only in `pageindex/page_index_classic.py`. `get_page_content` and `get_document_structure` return page text and summaries as JSON string fields.
- **Conclusion status:** `absent`.
- **Conclusion supported.** Page text and stored summaries reach the chat model without delimiter framing or redaction. **Prevented.** It says nothing about whether the model follows injected instructions, or about provider-side defenses.

#### RT-ABS-4 — No vector index or embedding component
- **Searched boundary.** SRC-1 `pageindex/` and `pyproject.toml`, `requirements.txt`: case-insensitive search for embedding, faiss, chroma, cosine, vector. Hits are only in flash PDF parsing (text direction and vector graphics), not in retrieval.
- **Conclusion status:** `absent`.
- **Conclusion supported.** Local retrieval uses no embedding similarity; cloud `sort="relevance"` ranking is a server feature not inspected. **Prevented.** Any claim about cloud-side retrieval.

### Behavioral-authority paths

#### RT-BAP-1 — Agent instructions and tool descriptions to the chat model
- **Consumer.** The chat model in RT-RTE-2 and host models in RT-RTE-4. **Channel.** System prompt text and tool descriptions (RT-OBJ-4). **Force.** Prompt-level guidance the model may or may not follow. **Horizon.** Every run. An example of its directive strength:

> Do NOT fall back to general knowledge — if the user's question references their own documents, exhaust every discovery path first.
> --- `pageindex/agent_tools.py:1617-1617` @ `d2693d80791a86345ef78b3234834f5fe53a70a0`

- Conclusion status: `afforded`.

#### RT-BAP-2 — Document text and summaries as model-visible data
- **Consumer.** The chat model in RT-RTE-2. **Channel.** Tool results carrying page markdown, node summaries, and the document `description`. **Force.** None intended; the text is data, but it is model-visible without framing at query time (RT-ABS-3). **Horizon.** One run. Conclusion status: `afforded`.

#### RT-BAP-3 — Caller `instructions`
- **Consumer.** The chat model. **Channel.** Client-level `instructions` and per-call `instructions` appended after the managed prompt. **Force.** Prompt-level, caller-controlled. **Horizon.** Every call on that client, or one call. Conclusion status: `wired`.

#### RT-BAP-4 — Server-served instructions in cloud mode
- **Consumer.** Own-model chat over cloud documents and host models using cloud tools. **Channel.** MCP `initialize` instructions and prompts fetched by `McpBridge`. **Force.** Prompt-level. **Horizon.** Per run, live. Content is outside the boundary. Conclusion status: `uninspected`.

## Annotations

none
