---
type: types/agentic-system-runtime-report.md
description: "PageIndex SDK indexing-to-chat control paths, protocol alternatives, scope enforcement and provider boundaries"
run-id: AAS-2026-09-28-pageindex-01
reviewed-boundary: "619cbd89f6dd02681a8cfc5d00b1f9b4848e973e"
---

# PageIndex runtime report

## Runtime account

Evidence basis: static implementation and declared contracts at the frozen commit, inspected 2026-09-28. PageIndex is a Python document indexing and QA SDK with an embedded tool-using model loop. It also supplies returning tools to external agents. These are distinct responsibility horizons. Theory-route terminology uses Commonplace’s theory-builder definition; reflection uses its separate reflective-system definition. These analytical definitions are supplied by the pinned analysis method, not by PageIndex source evidence.

The ordinary invocation is `PageIndexClient(index=..., chat=...)`, `submit_document(pdf)`, then `chat(question, doc_id=...)`. The application principal chooses the source PDF, provider credentials, index and chat model names, local storage directory and optional backend overrides. The client defaults local storage to `.pageindex`. Submission extracts readable PDF page text, selects Flash by default or standard indexing explicitly, checks the resulting page references, assigns a UUID document ID and commits document files under the store lock. The memory member owns construction, admission and later read-back records; this account does not duplicate their findings. Entry evidence: SRC-1 `pageindex/client.py`, `pageindex/local_api.py`.

On a chat call the client validates the selected protocol, converts a string to history where appropriate, composes managed and caller guidance, resolves document targeting and constructs an agent with document tools. A remote model proposes tool calls and the external SDK runner schedules them until a final response or its turn limit. PageIndex's tool adapter executes local reads or a cloud MCP request. The result re-enters the runner, and the client returns answer text, a protocol envelope, or a stream. The prompt is natural-language policy; schemas, allowlist checks and parameter guards are symbolic controls. Intermediate messages live in the invocation; the application must supply history on a later call. Persistence and caller-controlled transcript reuse are assessed by the memory member. RTE-1 covers orchestration, RTE-2 the scope gate, RTE-3 guidance admission, and RTE-4 remote/host integration.

Material alternatives inspected:

| Path | Next-step owner and effect boundary | Consequential difference |
| --- | --- | --- |
| Own-model Chat Completions / answer lane | OpenAI Agents Runner plus model; PageIndex executes tools | Text history, final text or usage envelope; streaming can expose tool events. |
| Own-model Responses | Same runner with native model protocol | Returns native output and tool transcript for caller replay; scope uses the same local gate. |
| Own-model Messages | Anthropic beta tool runner plus model | Returns conversation blocks; max-iteration termination can return an unfinished tool-use response instead of the OpenAI exception. |
| Cloud documents with own model | Local runner, remote MCP tools and instructions | Live tool set; local document allowlist is dropped, targeting remains prompt-level. |
| Managed cloud chat | Cloud service, reached through CloudAPI | Client forwards messages and scope; loop, model choice and enforcement inside service are uninspected. Own-model-only controls are rejected here. |
| External agent adapters | Host agent/runtime | Plain functions, OpenAI MCP conversion/hosted tool, or Claude MCP config; caller supplies loop and permissions. |
| Standard indexing / legacy command paths | Index routines / command caller | Different construction route from Flash; no inference that Flash's controls cover classic or Markdown. See memory scope limitations. |

SRC-1 `pageindex/local_chat.py`, `pageindex/client.py`, `pageindex/integrations/openai_agents.py`, `pageindex/integrations/claude_agent_sdk.py`, `pageindex/agent_tools.py`.

Four forcing cases were traced statically:

1. A model requests an out-of-scope local document or injects `_allowed_ids`: `call_tool` discards underscore-prefixed arguments, injects the caller's IDs, and every registered local document lookup resolves inside the filtered catalog. Empty selection is rejected before constructing tools. This is a local tool invariant, not a host sandbox (RTE-2).
2. Caller `extra_body` tries to replace tools/messages/system: `_refuse_skeleton` rejects these keys on the built-in protocol lanes. Intentional `instructions` and system-history extension remain admitted (RTE-3).
3. The chat exceeds its turn budget: OpenAI-lane SDK exceptions become `PageIndexAPIError`; Messages supplies `max_iterations` and can return a truncated, continuable run. The same argument does not promise the same terminal shape (RTE-1).
4. Cloud MCP provides no tools or no instructions, or its session expires: the client refuses empty tool/guidance surfaces; session-bearing HTTP 404 triggers one reinitialization/replay, whereas 400 is not replayed. Transport retry policy has `read=0`, retries 429/5xx, and delegates server-side idempotence to the external contract (RTE-4).

Capability surface, grant and isolation differ. Built-in local chat registers read tools; management adapters can opt into document removal. Local effects run in the application process with its filesystem and network privileges. Cloud tools use the API key; a read-only endpoint is selected by URL, relying on the server's contract. Hosted OpenAI MCP explicitly requests no approval. The host's other tools, shell access, subprocess permissions and deployment isolation are excluded, so these SDK controls establish no system-wide sandbox. SRC-1 `pageindex/agent_tools.py`, `pageindex/integrations/openai_agents.py`, `pageindex/integrations/claude_agent_sdk.py`, `pageindex/mcp_bridge.py`.

No dynamic check planned. Considered checks: live PDF indexing, live QA, mock scope/extra-body tests and protocol-budget tests. Static control flow suffices for the stated wiring and branch conclusions; executing models would need service access and a specified fixture, while mocking a runner would not establish live provider behavior. No service credentials were inspected or used. No performance, faithfulness or activation conclusion is derived from this decision. Tests in the source inventory were not executed. Tool and package versions were not installed for a run.

## Probe evidence

None. Source inspection and Commonplace artifact validation are not PageIndex execution probes.

## Shared records

### Components

#### CMP-1 — Configurable LLM endpoints

Source-native identity: index/summary and chat model roles, resolved from caller settings, packaged configuration and defaults. Representational form: distributed-parametric; substrate: external model provider, accessed through LiteLLM/OpenAI/Anthropic interfaces. SRC-1 `pageindex/utils.py`, `pageindex/client.py`, `pageindex/local_chat.py`, `pageindex/config.yaml`.

> DEFAULT_INDEX_MODEL = "gpt-5.6-luna"
> DEFAULT_CHAT_MODEL = "gpt-5.6-sol"
> --- `pageindex/utils.py:1197-1198` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

Index and summary roles can differ; chat can differ again. Classic index prompts, Flash optimization/summaries and document descriptions call the indexing lane; the chat model selects tools and answers. The default names above are source configuration, not a claim about service availability. Component wiring conclusion status: wired. Exact-version pinning conclusion status: absent within the inspected configuration and request builders: model names/backend endpoints are caller-selectable, with no weight digest or immutable provider revision requirement. Provider parameter changes during operation conclusion status: uninspected; provider training/state is outside the source. No claim of immutable weights follows from a fixed source commit. Managed cloud model choice is uninspected. No separate embedding model was identified in the inspected local SDK routes; this is a route observation, not an exhaustive absence claim about the hosted platform. Dependency ranges in SRC-1 `pyproject.toml` allow runner implementation changes, which prevents bit-for-bit runtime reproduction from this source alone.

### Operative objects

#### OBJ-1 — Managed and caller agent guidance

Natural-language instructions stored in Python constants and client fields; cloud instructions arrive from MCP initialization. Lineage: shipped authored policy plus caller additions or externally served policy. Consumer: CMP-1 via runner instructions/system messages. It says to discover documents, use the structure first above 20 pages, read page content, and persist through discovery before reporting not found. Citation guidance optionally requests document-grounded claims and source references. It is inspectable in separate textual pieces, but no evidence here establishes that the runtime criticizes and rewrites these method texts. SRC-1 `pageindex/agent_tools.py`, `pageindex/local_chat.py`; SRC-2 `pageindex/agent_tools.py`.

> READING WORKFLOW:
> - For documents over {STRUCTURE_FIRST_PAGE_THRESHOLD} pages: call get_document_structure() first to locate relevant sections, then get_page_content() with targeted page ranges.
> - For small documents ({STRUCTURE_FIRST_PAGE_THRESHOLD} pages or fewer): call get_page_content() directly.
> --- `pageindex/agent_tools.py:1588-1590` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

#### OBJ-2 — Returned answer and protocol output

Natural-language answer with symbolic protocol metadata/tool transcript where requested; transient SDK return, with any later retention owned by the application. Produced by CMP-1 through RTE-1. Evidence of consumption by an application, correctness or later capacity improvement is uninspected. The built-in Chat Completions wrapper returns the runner's final output without an additional answer-verification stage in the inspected return path. SRC-1 `pageindex/local_chat.py`.

> "message": {"role": "assistant",
>                             "content": result.final_output or ""},
> --- `pageindex/local_chat.py:989-990` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

#### OBJ-6 — Extracted PDF page claims

Operative part of OBJ-3, split here for epistemic assessment. Natural-language page text in the local page file; acquired from the submitted PDF. The content can state source claims, while extraction fidelity and source truth are separate questions. SRC-1 `pageindex/local_api.py`; the evidence passage and acquisition finding are retained in RTE-5. Consumers and read selection are RTE-8. Conclusion status: wired. This declaration does not reclassify the specialist's bundle.

#### OBJ-7 — Section-to-page and hierarchical index assertions

Operative part of OBJ-3, split from prose summaries. Symbolic tree structure and page spans paired with source-native heading titles assert where sections occur. Stored as JSON, compiled by construction or optimizer routes RTE-5 and RTE-6, and used to navigate/reconstruct content through RTE-8. SRC-1 `pageindex/page_index_classic.py`, `pageindex/tree_optimize.py`; minimum passages are retained by those memory routes. Conclusion status: wired. Numerical/structural validity is distinct from correct interpretation of a section's role.

#### OBJ-8 — Generated summaries and document description

Operative part of OBJ-3: natural-language summary/title-description fields compiled from pages, child summaries and the cleaned tree. They can make truth-apt statements about the document. RTE-5 owns their generation and retention; RTE-8 and RTE-9 their later delivery. SRC-1 `pageindex/utils.py`, `pageindex/local_api.py`. Conclusion status: wired. Whether a particular generated statement preserves, follows from or extends its inputs needs candidate-level semantic evidence; none was executed here. A model being asked to summarize is not itself a semantic-preservation check.

#### OBJ-9 — Document identity, status and caller metadata

Operative parts of OBJ-3 and client-visible OBJ-4, distinguished from their document claims. Symbolic IDs, status and timestamps support selection/order; caller JSON fields and folder descriptions can contain arbitrary source assertions. RTE-5 and RTE-11 own admission, RTE-8 and RTE-9 consumption. SRC-1 `pageindex/local_api.py`, `pageindex/agent_tools.py`, `pageindex/cloud_api.py`; evidence remains with the corresponding memory records. Conclusion status: wired at the client boundary. Shape/identity checks do not warrant arbitrary caller assertions or opaque cloud content.

### Routes

#### RTE-1 — Built-in chat orchestration

Trigger/principal: caller question and optional history, document IDs, model and backend settings. Endpoints: client chat → validated history and targeting → configured agent/SDK runner → PageIndex document tools → model → OBJ-2. Owner: client owns assembly and tool effects; model proposes calls and answers; external runner owns repeated dispatch and termination. Context: OBJ-1, caller history and selected document material supplied by memory routes. Action effect: read local store or invoke cloud tools; no built-in general shell tool in this traced registration. Implementation conclusion status: wired; operation conclusion status: uninspected. SRC-1 `pageindex/local_chat.py`, `pageindex/client.py`.

> return Agent(
>         name="PageIndex",
>         instructions=instructions,
>         tools=build_openai_tools(client, doc_ids=doc_ids),
>         model=_openai_model(protocol, model_name, conn or None),
>         model_settings=settings,
>     )
> --- `pageindex/local_chat.py:395-401` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

Immediate return: answer, protocol envelope or lazy event stream. Later read-back: caller-mediated transcript/history route in memory member, not autonomous retention of this invocation. Delegated visibility: tools and selected arguments/results are exposed to the runner/provider; host integration differs under RTE-4. Selection predicate: model tool choice under guidance, bounded by RTE-2 and tool schemas. Invalidation/expiry: invocation ends; persisted documents follow memory routes. Activation/effect: results are wired into model context; actual behavior dependence is uninspected. Limits: model and SDK internals are external, cloud-managed loop uninspected.

Budget owner/enforcement: external runner called with caller maximum; guarantee strength: protocol; implementation conclusion status: wired. OpenAI paths forward a supplied `max_turns`, otherwise rely on SDK default; Messages explicitly defaults to ten iterations. Runtime dependency versions and provider behavior are required external contracts; no wall-clock, cost or correctness bound follows.

> max_iterations=max_turns if max_turns is not None else 10,
> --- `pageindex/local_chat.py:1441-1441` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

Operating mode: open document-QA requests, not a curriculum or improvement experiment. Proposal/decision roles: model proposes reads and final answer; code may veto invalid tool inputs, scope escapes and protocol settings. User may provide follow-up direction but is not an internal approval gate per tool call. Answer oracle: inapplicable to the implemented chat decision protocol; document contents are evidence, not supplied expected answers. Internal model reasoning remains uninspected.

Theory-builder conditions 1–4 for the chat method: condition 1 (localized OBJ-1 policy content) wired; condition 2 (policy delivery and configured consumer) wired, actual semantic adherence uninspected; condition 3 (content-directed criticism of that method) uninspected in opaque model processing, with no runtime method-revision route established by RTE-1; condition 4 (criticism shaping a subsequent method round) uninspected for the same reason. Document correction routes are assessed separately in the memory member. Addressability: shipped policy clauses individually inspectable; persistence: static method across calls, transient chat state unless caller returns it. Learning: uninspected, no capacity comparison. Reflection: uninspected, no evidenced two-way self-representation route in this loop. Autonomous qualifier: computation performs tool dispatch and response production after caller input at wired status, but a complete autonomous theory-builder claim is unestablished. Self-improvement: uninspected; returning a response does not establish revision of the method.

#### RTE-2 — Local tool scope gate

Endpoints: caller document selection → `_local_doc_scope` → `call_tool` private allowlist → filtered browse/lookup → result or error. Owner/enforcement: SDK client and local tool dispatch. Form: symbolic. Implementation conclusion status: wired; guarantee strength: invariant within these built-in local tool paths. SRC-1 `pageindex/client.py`, `pageindex/agent_tools.py`.

> from .agent_tools import _require_doc_selection
>         _require_doc_selection(doc_id)
>         if not getattr(self, "api_key", None):
>             return doc_id
>         return None
> --- `pageindex/client.py:2025-2029` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

> def _scope_documents(documents: list[dict[str, Any]],
>                      allowed_ids: Optional[frozenset]) -> list[dict[str, Any]]:
>     if allowed_ids is None:
>         return documents
>     return [doc for doc in documents if doc.get("id") in allowed_ids]
> --- `pageindex/agent_tools.py:389-393` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

Covered paths: built-in Chat Completions, Responses and Messages all call `_local_doc_scope`; browse filters the catalog and get/status/structure/page/removal resolve inside it. Caller-controlled underscore arguments cannot substitute the injected scope. Empty list fails; omitted IDs allow the whole local library. Alternate paths: direct client API methods, external host tools and cloud requests do not inherit this local gate. Required contract: caller does not mutate in-process code or supply independent effects outside these tools. Cloud own-model targeting has policy strength only; managed cloud enforcement is uninspected.

Immediate return: scoped tool result or error envelope. Later read-back: gate itself retains no learned content; it controls the memory reads it wraps. Delegated visibility: model cannot enumerate out-of-scope local catalog through these scoped handlers. Selection predicate: exact ID membership before name resolution. Expiry: current configured invocation. Activation/effect: deterministic result filtering is wired, not observed. Admission/revision: inapplicable, this filters access rather than editing retained knowledge. Answer oracle: inapplicable; scope is authorization input, not correctness evidence.

#### RTE-3 — Guidance and configuration admission

Trigger: caller configures instructions/backend/settings, provides system/developer rows, or cloud MCP supplies instructions. Proposed change: model guidance, provider routing and request parameters. Owner/admission: client type/config validation, prompt assembly and reserved-field guard. Caller selects and can replace its settings; remote service supplies its own guidance. No semantic quality comparison or human approval is imposed. Empty cloud instructions fail. Recovery: reject invalid argument before dispatch; caller can reconstruct a client/change next request. SRC-1 `pageindex/client.py`, `pageindex/local_chat.py`, `pageindex/agent_tools.py`.

> hit = sorted(_SKELETON_KEYS.intersection(extra_body))
>     if hit:
>         raise PageIndexAPIError(
>             f"extra_body cannot carry {', '.join(hit)}: the managed prompt, "
>             "conversation and tools are the SDK's. Extend the prompt with "
>             "instructions= or a leading system row; pass the conversation "
>             "as messages, the first argument.")
> --- `pageindex/local_chat.py:321-327` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

> if not getattr(client, "api_key", None):
>         base = AGENT_INSTRUCTIONS
>     else:
>         base = _cloud_bridge(
>             client, gated=not include_management).instructions()
> --- `pageindex/agent_tools.py:1680-1684` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

Implementation conclusion status: wired. Guarantee strength: invariant for reserved-key rejection on the inspected built-in lanes; best effort for guidance adherence. Immediate return: configured request or exception. Later read-back: static/client guidance persists in client/config, not use-derived memory; no runtime feedback-to-guidance write established here. Delegated visibility: provider receives composed instructions. Selection: caller settings and local/cloud mode. Expiry: call/client lifetime or changed configuration. Activation: prompt delivery wired, behavior dependence uninspected. Operating mode: explicit customization, no supplied expected-answer oracle. Guidance says how to find/read documents; retention contains instructions, not reasons learned from trials. Theory-builder conditions 1–4: localized policy wired; consumption wiring wired with semantic adherence uninspected; content criticism uninspected; criticism-driven iteration uninspected. Addressability: separate configuration fields and policy strings. Persistence: static/client scope. Learning, reflection and self-improvement: uninspected; no evaluation comparing revisions. Autonomy: caller-controlled admission; computation checks shape and assembles the request, not an autonomous policy improvement process.

#### RTE-4 — Cloud and external-agent handoff

Endpoints: client/adapters → local MCP-shaped functions, remote MCP bridge or hosted MCP configuration → external host/provider → tools/results. Owner: PageIndex builds capabilities/config, external host owns planning/approval and other effects; cloud server owns its live tool implementations. SRC-1 `pageindex/agent_tools.py`, `pageindex/mcp_bridge.py`, `pageindex/integrations/openai_agents.py`, `pageindex/integrations/claude_agent_sdk.py`. Implementation conclusion status: wired for adapter construction/transport; deployment operation conclusion status: uninspected.

> if getattr(client, "api_key", None):
>         bridge = _cloud_bridge(client, gated=not include_management)
>         tools_meta = bridge.list_tools()
> --- `pageindex/agent_tools.py:1530-1532` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

Admission: local registered read tools by default, removal with explicit management selection; cloud chooses `/mcp?tools=read` by default, unrestricted endpoint when management is requested. Discovered names/descriptions/schemas become tools; there is no local static reimplementation validating remote tool semantics. Empty discovery fails. Hosted OpenAI MCP sets `require_approval` to `never`; this is a configuration fact, not an end-to-end authorization guarantee. Selection/veto: caller chooses adapter and management flag, client rejects unusable metadata/transport failures; server controls live capabilities. Guidance: same contract family as OBJ-1; cloud's actual text is uninspected. Retention: bridge caches a session and instructions; changes to API key/base URL rebuild its bridge. Policy authority remains external.

Immediate return: tool/config or remote result. Later read-back: actual retained cloud payload semantics uninspected; adapter cache is connection machinery, not trace-derived knowledge. Delegated visibility: host/provider can receive document content and tool schemas; deployed credential scope unknown. Invalidation: auth/base URL change or expired session; one session reinitialization on 404, no retry of read timeout. Activation/effect: construction and dispatch wired; hosted execution uninspected. Guarantee strength: protocol, requiring remote endpoint and host contracts. Answer oracle: inapplicable; service contract response is not a reference answer. Operating mode: caller integrations/open requests. Theory-builder conditions 1–4: guidance localization afforded through configuration; actual host consumption afforded; criticism and iteration uninspected. Learning, reflection and self-improvement uninspected. Autonomous qualifier uninspected at host boundary; no host-level inference from exporting tools.

### Claims

#### CLM-1 — Tree indexing and reasoning retrieval

SRC-2 `README.md` declares the two-stage mechanism. Claim conclusion status: claimed. Local construction and built-in chat wiring support the operational mechanism (RTE-1 and memory records), not every analogy to human reading or superiority over vector search.

> 1. **Index**: generate a **tree-structure index** for each document
> 2. **Retrieve**: agentically **search that tree** with LLM reasoning
> --- `README.md:48-49` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

#### CLM-2 — Reported benchmark advantages

SRC-2 `README.md` reports FinanceBench accuracy, local indexing cost/time and comparison with native PDF inputs. Conclusion status: claimed. Linked benchmark repositories and runs are outside the frozen allowlist; the README is attributed reporting, not observed-run or causal evidence in this set. No effect is attributed to tree search, a model or another component separately.

> PageIndex reached a state-of-the-art [**98.7% accuracy**](https://vectify.ai/blog/Mafin2.5) on [FinanceBench](https://arxiv.org/abs/2311.11944) (financial document QA benchmark), vastly outperforming vector-based RAG.
> --- `README.md:164-164` @ `619cbd89f6dd02681a8cfc5d00b1f9b4848e973e`

### Evidenced absences

None declared in this member. Opaque model reasoning, host loops and cloud internals are limitations, not proven absences.

### Behavioral-authority paths

#### BAP-1 — Agent guidance to model

Consumer: CMP-1 through RTE-1; channel: runner instructions/system prompt OBJ-1; force: instruction/policy, not deterministic enforcement; horizon: invocation and caller-reused configuration. Delivery conclusion status: wired; activation conclusion status: uninspected. SRC-1 `pageindex/local_chat.py`, `pageindex/agent_tools.py`. Required document reading and citation rules express intended answer warrant without proving answer truth.

#### BAP-2 — Scope gate to tool execution

Consumer: local tool dispatch RTE-2; channel: private exact-ID allowlist; force: enforcing; horizon: scoped tool call/current invocation. Conclusion status: wired. SRC-1 `pageindex/agent_tools.py`, `pageindex/client.py`. The gate licenses access to selected documents, not reliance on their claims.

## Annotations

None. Memory admitting-route fields remain with the specialist's records; this member only supplies the enclosing orchestration and access controls.

## Amendments

None.
