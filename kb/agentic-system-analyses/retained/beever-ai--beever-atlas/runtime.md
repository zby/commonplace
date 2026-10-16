---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Beever Atlas runtime: ingestion, wiki maintenance, QA and alternate MCP/control paths at the frozen whole-system boundary."
run-id: AAS-2026-10-15-beever-atlas-10a3512c094c-01
reviewed-boundary: "7d791af27ef4aa19644cb385c7ca24619bc4f848"
---

# Beever Atlas runtime report

## Runtime account

### Evidence and consequential work

Atlas ships a knowledge-production and consumption loop: platform or pushed messages become extracted facts and graph data, those feed maintained wiki pages, and QA or direct retrieval serves later consumers. This account uses SRC-1 at the revision in [the boundary](boundary.md). All findings below are implementation or explicitly attributed design evidence. No target execution, tests, model calls or experiments were performed. Deployment configuration, exercised controls, answer quality, latency, benefit and isolation under attack remain unobserved.

Added inspection within SRC-1 includes `src/beever_atlas/agents/query/qa_agent.py`, `src/beever_atlas/agents/mcp_registry.py`, `src/beever_atlas/agents/tools/orchestration_tools.py`, `src/beever_atlas/agents/tools/_citation_decorator.py`, `src/beever_atlas/api/mcp_server/_ask_runner.py`, `src/beever_atlas/api/assignments.py`, `src/beever_atlas/llm/provider.py`, `src/beever_atlas/llm/embeddings.py`, `src/beever_atlas/services/reconciler.py` and the paths cited in the records. These are implementation evidence, not additional sources or observed runs. Remaining included producers, migration scripts, builder variants and evaluation surfaces are not exhaustively audited here; no system-wide completeness or safety conclusion rests on their omission.

### Composition and ordinary invocation

The shipped server composes stores and provider configuration, starts the scheduler, installs extraction/settlement subscribers, and loads outbound tool registrations. These responsibilities belong to Atlas, not an excluded host. Initialization of several maintenance subscribers is non-fatal, so the existence of their code does not prove every deployment has an active downstream maintenance chain (SRC-1: `src/beever_atlas/server/app.py`, `src/beever_atlas/services/scheduler.py`).

An ordinary dashboard question enters `POST /api/ask`; the older channel-scoped ask endpoint used by the bot reaches the same `_run_agent_stream`. The v2 route authenticates a user principal, checks channel access, verifies ownership of a supplied session identifier and invokes the stream. The older route can separately use a caller-supplied platform user identity for history keying while retaining the authenticated principal for tool authorization. The shipped web hook posts to v2; the bot posts to the channel-scoped endpoint (SRC-1: `web/src/hooks/useAskSession.ts`, `bot/src/index.ts`, `src/beever_atlas/api/ask.py`).

[RT-RTE-dashboard-ask](#rt-rte-dashboard-ask) owns the detailed loop. Atlas creates a fresh ADK working session for each HTTP turn, loads selected durable chat context, constructs the user prompt from question/channel, optional decomposition, attachments and prior turns, and attaches the mode-specific QA agent. The model chooses tool calls and completion; ADK drives the call/result loop. Atlas binds principal and channel-scope context variables before driving the runner and resets them afterward. Selected tool results are model context, not independent answer verification. Atlas streams progress, response text, citations and terminal events; the HTTP path persists answer/history metadata. A direct cached wiki read is one possible tool choice, not a mandatory first stage.

The mode grants differ: quick exposes two wiki/overview tools; summarize exposes a four-tool base subset plus registered external tools; deep exposes the base list, orchestration tools and registered external tools. The stated two/four/eight tool-call budgets are instructions constructed into the prompt, not an inspected counter-based runtime limit (SRC-1: `src/beever_atlas/agents/query/qa_agent.py`, `src/beever_atlas/agents/query/prompts.py`). The actual grant also depends on request-disabled tool names, feature flags and outbound configuration. Skills can be attached through an ADK `SkillToolset`, but underlying QA tools remain callable siblings; this is not isolation of those tools in a delegated worker.

### Production, maintenance and change admission

[RT-RTE-message-ingestion](#rt-rte-message-ingestion) traces the producer loop. Platform synchronization writes normalized messages first, then either runs extraction inline or leaves pending rows for the scheduler's extraction worker. Signed push admission also writes pending rows and returns before extraction. The worker claims durable queue rows, groups them by channel and delegates batches to `BatchProcessor`. Each batch has a system-owned working session seeded with messages, channel/job identity, known-entity candidates and policy settings. The explicit workflow fans out fact/entity extraction, joins, fans out embedding/deterministic validation, joins again, then persists. The model proposes extracted text/structure; callbacks and code admit the representation, not an operator approving each fact. Checkpoints and retry branches make this more than a single completion call.

[RT-RTE-wiki-maintenance](#rt-rte-wiki-maintenance) covers one consequential successor stage. Server subscribers connect memory-change and memory-settled events to maintenance, with configuration-dependent consolidation ordering. The maintainer loads new fact records and an existing page, requests affected sections from a model, parses them, preserves untouched sections and saves. Automatic content admission is bounded by page curation mode and parser behavior. It is not universal validation of semantic truth. [RT-RTE-page-curation](#rt-rte-page-curation) is the separate operator-facing control path: manual/frozen modes, explicit application of pending updates, splits and merges. Memory revision details beyond these runtime enforcement boundaries are left to the memory member.

[RT-RTE-model-assignment](#rt-rte-model-assignment) changes production machinery: authenticated settings callers can replace persisted model/endpoint assignments, with compatibility checks and a force option. Provider reload and QA cache reset attempt to make the change effective. [RT-RTE-outbound-tools](#rt-rte-outbound-tools) admits configured remote tool capabilities by HTTP catalog discovery at startup. Neither route is an autonomous modification of Atlas source code. Caller identity alone does not prove a human authored or approved the settings request. No inference of learned weights or exercised self-improvement follows from either change path.

### Four forcing cases and bounded guarantees

1. **Deferred versus inline production.** A successful sync or push response is not evidence of extracted knowledge or a refreshed wiki. The decoupled sync branch synthesizes an empty batch result and advances normal job/cursor logic; the worker and subscribers own later work. The HMAC push endpoint returns `202` with `extraction="queued"`. [RT-RTE-message-ingestion](#rt-rte-message-ingestion) distinguishes these terminals.
2. **HTTP ask versus MCP ask.** MCP `ask_channel` authenticates/checks its requested channel upstream, but uses another runner wrapper. It reuses an in-memory principal-namespaced session and binds the principal, not the HTTP turn's authorized-channel set. An unbound tool gate permits the channel. Thus HTTP turn isolation cannot be generalized to MCP or standalone tool calls. This is an implementation coverage finding, not an observed cross-tenant exploit; upstream ACLs, tool-specific checks and deployment assumptions still matter. See [RT-RTE-mcp-ask](#rt-rte-mcp-ask) and [RT-CLM-channel-isolation](#rt-clm-channel-isolation).
3. **Local tools versus dynamic remote tools.** A function intended to remove write/egress tools from untrusted contexts exists, but the inspected QA construction and HTTP/MCP call paths do not invoke it. A scoped SRC-1 search for `_filter_tools_for_untrusted` found its definition, comments and tests, not a production call. Deep and summarize append registry tools directly. A disabled base tool name or a textual untrusted-content warning therefore does not establish a complete output-side effect barrier. Remote wrappers POST arbitrary model-supplied keyword arguments using configured credentials. See [RT-RTE-outbound-tools](#rt-rte-outbound-tools) and [RT-CLM-untrusted-tools](#rt-clm-untrusted-tools).
4. **Partial persistence or degraded wiki output.** Graph and vector writes are gathered independently. Graph errors alone do not prevent the persister's final `mark_intent_complete`; vector errors do. A write-intent mechanism therefore is not an atomic dual-store guarantee. Separately, two schema-validation failures in kind-specific wiki maintenance can still admit markdown with `kind_schema=None`. See [RT-CLM-write-completion](#rt-clm-write-completion) and [RT-RTE-wiki-maintenance](#rt-rte-wiki-maintenance).

Load-bearing guarantee owners and limits:

| Guarantee | Owner and enforcement point | Strength and covered paths | Alternate paths and required external contract | Conclusion statuses |
|---|---|---|---|---|
| One downstream trigger per extraction/enrichment fan-in | Atlas workflow constructor inserts `JoinNode`s before enrichment and persistence | invariant at the declared graph topology | Does not cover independent batch retries, outbox replay or direct store writes; actual one-shot fan-in relies on ADK `JoinNode` semantics | implementation conclusion status: wired; operation conclusion status: uninspected |
| Channel-scoped HTTP tool reads | HTTP stream binds `{channel_id}`; participating tools call `channel_blocked` | policy, enforced by code on participating local tools | Unbound context opens this gate; outbound tools do not inherit a local store guard; principal ACLs have deliberate single-tenant fallbacks; correct async context propagation is an external ADK/Python contract | implementation conclusion status: wired; operation conclusion status: uninspected |
| Push source authentication and channel pattern | push endpoint verifies signed raw body then tests configured pattern | protocol on this endpoint | Not the platform/import path and not truth validation; depends on HMAC secret protection, clock/skew verification and backing store/index behavior | implementation conclusion status: wired; operation conclusion status: uninspected |
| Frozen/manual pages resist automatic incremental rewrite | maintainer `_apply_update_inner` checks curation before calling model | invariant for the inspected incremental path | Explicit operator paths can change modes/apply updates; full refresh/build variants need separate coverage before claiming universal protection | implementation conclusion status: wired; operation conclusion status: uninspected |
| Recovery of incomplete cross-store writes | persister intent plus `WriteReconciler` replay methods | best effort, not atomic commit | Completion branches differ by store failure; live reconciler scheduling was not established by inspected app/scheduler wiring; depends on durable intents and idempotent store upserts | implementation conclusion status: afforded; operation conclusion status: uninspected |

Evidence for these scopes is retained in the route and claim records below (SRC-1). No deployed OS/container sandbox or remote-server isolation envelope is established. The capability surface includes model-selected local tools and configured remote effects; the current deployment's actual credentials, enabled flags, endpoints and isolation are unsupplied. An enclosing external MCP client's own shell, provider-native tools, callbacks or remote workers are outside this boundary, not additional powers attributed to Atlas. The inspected QA constructor does not itself establish a generic shell or subprocess tool; this is not an exhaustive absence claim over all shipped scripts and dependencies.

## Shared records

### Components

#### RT-CMP-qa-agent
Label: QA agent model

Source-native identity: `qa_agent`, resolved when the `LlmAgent` is built. Representational form: distributed-parametric model; parameters reside behind a provider endpoint, not in the Atlas session store. Atlas sends natural-language instructions and tool schemas. Parameters are not updated by the inspected QA route; provider-internal mutation is uninspected. Exact weights/version are not pinned by the frozen application revision. Assignments, endpoint routing and provider aliases can resolve to another model; QA agent instances are cached and reset on assignment refresh. SRC-1: `src/beever_atlas/agents/query/qa_agent.py`, `src/beever_atlas/llm/provider.py`, `src/beever_atlas/api/assignments.py`.

> model = provider.resolve_model("qa_agent")
> --- `src/beever_atlas/agents/query/qa_agent.py`

#### RT-CMP-fact-extractor
Label: Fact extractor model

Source-native identity: `fact_extractor`; distributed-parametric endpoint model, provider-owned storage. The constructor supplies `FACT_EXTRACTOR_INSTRUCTION`, output key `extracted_facts` and recovery callbacks. No parameter training occurs in this inspected constructor/ingestion route; provider internals are uninspected. Exact version is not pinned; explicit constructor override or provider assignment/alias resolution can change the model. SRC-1: `src/beever_atlas/agents/ingestion/fact_extractor.py`, `src/beever_atlas/llm/provider.py`.

> "model": model or get_llm_provider().resolve_model("fact_extractor"),
> --- `src/beever_atlas/agents/ingestion/fact_extractor.py`

#### RT-CMP-entity-extractor
Label: Entity extractor model

Source-native identity: `entity_extractor`; distributed-parametric endpoint model with provider-owned parameters. Produces the `extracted_entities` working-state part using shipped entity instructions and recovery callback. No training is wired in the inspected extraction route; provider-side parameter changes remain uninspected. Exact version is not pinned. Constructor override and mutable provider assignments/endpoints can change resolution. SRC-1: `src/beever_atlas/agents/ingestion/entity_extractor.py`, `src/beever_atlas/llm/provider.py`.

> "model": model or get_llm_provider().resolve_model("entity_extractor"),
> --- `src/beever_atlas/agents/ingestion/entity_extractor.py`

#### RT-CMP-wiki-maintainer
Label: Wiki maintainer model

Source-native identity: `wiki_maintainer`; distributed-parametric completion model, remote/provider substrate. Unlike QA, this inspected path uses direct `dispatch_completion`, JSON mode, a 4096-token request and the resolved model string. No local parameter update is wired; provider internals are uninspected. The exact version is not pinned; mutable assignments, model strings and endpoint service behavior can change it. This route should not be assumed to inherit all ADK agent controls or endpoint-resolution behavior merely because it shares `LLMProvider`. SRC-1: `src/beever_atlas/services/wiki_maintainer.py`, `src/beever_atlas/llm/provider.py`.

> model_name = provider.get_model_string("wiki_maintainer")
> --- `src/beever_atlas/services/wiki_maintainer.py`

#### RT-CMP-embedding-model
Label: Embedding model

Source-native identity: configured embedding provider/model, called through `embed_texts`. Distributed-parametric parameters live behind the selected provider; returned numerical text vectors are another distributed representation retained with facts. Atlas does not train embedding parameters in this inspected route. Exact weights/version are not pinned; configuration and mutable endpoint resolution can change the model. Migration guards can suppress vector generation and emit empty vectors rather than halt the whole batch. Embedding lineage beyond configured identifiers is unresolved. SRC-1: `src/beever_atlas/llm/embeddings.py`, `src/beever_atlas/agents/ingestion/embedder.py`.

> vectors = await embed_texts(texts)
> --- `src/beever_atlas/agents/ingestion/embedder.py`

### Operative objects

#### RT-OBJ-session-state
Label: ADK working session state

Source-native identity: `InMemorySessionService` session state. Representational form: symbolic dictionary keys/structured values; message and generated-text values are natural-language model context. Substrate: application-process memory. The runner helper uses application name `beever_atlas`, with distinct `agent=` and `node=` construction for agents versus workflow nodes. HTTP QA creates a fresh session per turn; MCP can reuse a supplied/default principal-namespaced identifier. Ingestion seeds a fresh session, with selected checkpoint data restored from MongoDB. This is not itself proof that any stored value is later activated as knowledge. SRC-1: `src/beever_atlas/agents/runner.py`, `src/beever_atlas/api/ask.py`, `src/beever_atlas/api/mcp_server/_ask_runner.py`, `src/beever_atlas/services/batch_processor.py`.

> _session_service = InMemorySessionService()
> --- `src/beever_atlas/agents/runner.py`

### Routes

#### RT-RTE-dashboard-ask
Label: HTTP QA turn

Endpoints/progression: authenticated `/api/ask` or channel-scoped `/ask` to `_run_agent_stream`, QA `LlmAgent`, ADK runner, local/remote tools, SSE client and durable QA/chat history. Principal: authenticated key-derived user; channel-scoped bridge-style callers can supply a separate acting user for conversation keying. Next-step owner: model for tool selection, ADK for iteration, Atlas for prompt assembly and event shaping. Symbolic controls include mode subsets, known disabled-name filtering, ownership checks and bound context variables. Natural-language policy includes grounded-answer instructions, untrusted-content note, recall hint and tool budgets. Distributed decision component: [RT-CMP-qa-agent](#rt-cmp-qa-agent).

- Immediate return: SSE progress, answer deltas, citations, metadata, errors and terminal done; tool calls execute inside the backend.
- Later read-back: HTTP history persistence is reloaded by `_load_chat_history_parts` for later turns, subject to user/channel provenance checks; attachments retain metadata rather than full extracted text in history.
- Delegated visibility: QA model receives selected history, question, channel marker, attachment extraction and tool results; client receives shaped events, not the entire working session.
- Selection predicate: request mode selects tool set; supplied session/user/channel select history; model chooses subsequent retrieval/tools; optional decomposition annotates the prompt.
- Invalidation or expiry: fresh ADK session each HTTP turn; context variables reset in finally; durable history retention/expiry is not established here.
- Activation or effect: tool invocations can retrieve data or invoke permitted orchestration/remote effects; delivery of evidence to the model does not prove grounded compliance or changed answers.
- Evidence limits: implementation inspected, not exercised; model compliance, actual grants and successful end-to-end return remain unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Working-context control: host code rebuilds each turn from selected durable context rather than resuming the HTTP ADK frame. It inserts history as `<prior_conversation>` and drops extracted attachment text from persisted attachment metadata. Optional skills use ADK's loader/toolset; Atlas keeps underlying tools as siblings. No inspected HTTP host compaction algorithm or separate sub-agent return-only frame is established. Answer oracle: none established in this open-question route; retrieved material is evidence, not a reference answer. Recovery includes tool-error soft handling, heartbeat/event shaping, fallback finalization and logged persistence failures; these are not guarantees of successful answers. SRC-1: `src/beever_atlas/api/ask.py`, `src/beever_atlas/agents/query/qa_agent.py`, `src/beever_atlas/agents/runner.py`.

> session = await create_session(user_id=user_id)
> --- `src/beever_atlas/api/ask.py`

> _authorized_token = bind_authorized_channels({channel_id})
> --- `src/beever_atlas/api/ask.py`

#### RT-RTE-message-ingestion
Label: Message production and extraction

Endpoints/progression: platform `SyncRunner` or HMAC push endpoint → MongoDB channel messages → inline `BatchProcessor` or background `ExtractionWorker` → ADK workflow → MongoDB intent and vector/graph writes. Trigger/principal: sync job/scheduler or a source holding its signing secret; batch execution uses user `system`, plus channel/job/batch state. Next-step owner: code graph, not a model choosing the pipeline topology. Fact/entity models propose output; callbacks and deterministic stages admit downstream representations. Models: [RT-CMP-fact-extractor](#rt-cmp-fact-extractor), [RT-CMP-entity-extractor](#rt-cmp-entity-extractor), [RT-CMP-embedding-model](#rt-cmp-embedding-model).

- Immediate return: push returns accepted/deduplicated counters and queued extraction; sync updates status/cursor; batch returns persistence counts/errors and stage information.
- Later read-back: pending durable messages are claimed by later worker ticks; batch checkpoints can seed retry sessions; retained facts feed maintenance and QA.
- Delegated visibility: each extraction batch receives messages, channel identity, known entities/similarity candidates and policy settings, not the entire global store; join stages share selected state outputs.
- Selection predicate: source channel pattern and payload validation for push; durable pending-row claim, per-channel grouping and batch policy for extraction; explicit graph edges select execution order.
- Invalidation or expiry: successful pipeline completion deletes its checkpoint; worker stale sweep/retry logic recovers extracting/failed rows subject to retry policy; push idempotency response cache is optional and time-bounded.
- Activation or effect: writes messages, numerical vectors, fact/entity/relationship representations, write intents and status; queues downstream maintenance events.
- Evidence limits: storage-engine atomicity, ADK JoinNode semantics, provider behavior and successful worker operation are external/unobserved; manual import/batch-provider variants are not exhaustively traced.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: caller/source authors messages; extraction models propose derived knowledge; software callbacks/validators and persistence code decide admission without per-fact human approval. Open incoming-message processing, not an answer-key curriculum. No expected-answer oracle is established. The push endpoint can reject unknown source/signature, excessive body, malformed data or disallowed channel. Recovery combines retry/checkpoint paths, stale-row sweep and an afforded outbox reconciler; atomic cross-store success is explicitly not established. Guidance is shipped extraction instructions plus runtime policy; persisted outputs are extracted artifacts, not revised extraction instructions. SRC-1: `src/beever_atlas/api/sources.py`, `src/beever_atlas/services/sync_runner.py`, `src/beever_atlas/services/extraction_worker.py`, `src/beever_atlas/services/batch_processor.py`, `src/beever_atlas/agents/ingestion/pipeline.py`, `src/beever_atlas/agents/ingestion/persister.py`.

> join_extract = JoinNode(name="join_extract")
> join_enrich = JoinNode(name="join_enrich")
> --- `src/beever_atlas/agents/ingestion/pipeline.py`

> if decouple_extraction:
> --- `src/beever_atlas/services/sync_runner.py`

> extraction="queued",
> --- `src/beever_atlas/api/sources.py`

#### RT-RTE-wiki-maintenance
Label: Incremental wiki update

Endpoints/progression: subscribed memory events and dirty-page flush → maintainer → load current page/new facts → direct completion → parse affected sections → merge/save page. Code routes facts and schedules work; model proposes prose/structured content. Trigger includes new facts and settlement/consolidation paths wired by the server. Model component: [RT-CMP-wiki-maintainer](#rt-cmp-wiki-maintainer).

- Immediate return: update boolean/counters and maintenance events, not a user-facing QA answer.
- Later read-back: saved page is read by later wiki/API/MCP consumers and subsequent maintenance invocations; compatibility QA tools select supported fixed page types through `WikiCache`.
- Delegated visibility: completion receives rendered current-page/new-fact context and kind-specific or legacy guidance; downstream consumer receives selected persisted content, not the raw completion response.
- Selection predicate: fact routing/dirty sets, truly-new IDs and curation mode; redesign flag and page kind select prompt/schema dispatch.
- Invalidation or expiry: `last_facts_seen` deduplicates inputs; successful merge clears dirty state; persistence/version handling and operator controls bound later replacement, not a universal content TTL.
- Activation or effect: section replacement preserves untouched sections and saves changed content; this can reach later QA context but answer effects are not observed.
- Evidence limits: no semantic-truth guarantee, exercised page update or quality benefit established; full builder/refresh alternatives require separate treatment before universalizing incremental invariants.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission/rejection: code skips frozen pages and defers manual ones; model proposes affected sections; parser rejects empty/unusable updates; exceptions return failure. In kind dispatch, schema validation retries once, then admits available markdown with null structured schema. The operator can change curation mode or explicitly apply updates through [RT-RTE-page-curation](#rt-rte-page-curation). Existing page remains on the inspected LLM-error paths; no universal automatic content rollback is established. The route applies shipped guidance, not a demonstrated revision of its own method theory. Operating mode: ongoing external knowledge maintenance. Answer oracle: no expected-answer/reference outcome established; schema is a format check. SRC-1: `src/beever_atlas/services/wiki_maintainer.py`, `src/beever_atlas/server/app.py`, `src/beever_atlas/agents/tools/wiki_tools.py`.

> return affected_sections, None
> --- `src/beever_atlas/services/wiki_maintainer.py`

> await self._page_store.save_page(page)
> --- `src/beever_atlas/services/wiki_maintainer.py`

#### RT-RTE-page-curation
Label: Operator page control

Endpoints/progression: authenticated wiki routes → channel ACL → page store/maintainer. Requests set pin/hidden state, change auto/manual/frozen mode, apply pending updates, split or merge pages. The caller proposes exact control values or structural changes; code validates and applies them. A UI operation can be human-directed, but generic authenticated API calls do not prove human authorship.

- Immediate return: updated state/page payload or operation result; explicit update flush invokes maintenance rather than approving each generated section.
- Later read-back: maintainer reloads curation modes; merge routing follows persisted redirects; page readers consume altered content/visibility.
- Delegated visibility: explicit pending-update flush temporarily exposes eligible manual pages to automatic maintainer processing.
- Selection predicate: channel/slug, request mode and dirty/manual page selection; ACL precedes the inspected curation effects.
- Invalidation or expiry: pending-update handler temporarily changes manual to auto and restores manual in finally; further requests can replace curation values.
- Activation or effect: durable control and structural page changes alter later update eligibility, routing and presentation.
- Evidence limits: caller's human/computational origin and actual use are unknown; not an exhaustive audit of all builder, deletion or rollback routes.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: caller decides requested control/structure; software rejects invalid values, denied channels or missing pages. No model/answer oracle decides the curation request. Operating mode is explicit API work, not a bounded experiment. Guidance is the endpoint schema/control semantics; the retained artifacts are page/control state. Recovery includes finally-based restoration on explicit manual flush; full refresh snapshots are another shipped recovery surface, not proof of automatic restoration after every mutation. SRC-1: `src/beever_atlas/api/wiki.py`.

> await store.update_curation_mode(channel_id, page.slug, "auto", target_lang=lang)
> --- `src/beever_atlas/api/wiki.py`

> await store.update_curation_mode(channel_id, page.slug, "manual", target_lang=lang)
> --- `src/beever_atlas/api/wiki.py`

#### RT-RTE-mcp-ask
Label: MCP answer invocation

Endpoints/progression: mounted FastMCP `ask_channel` validates principal/requested channel → `run_ask_channel` → cached mode agent and principal-owned in-memory session → ADK event accumulation → structured response. Atlas owns this loop; the external MCP client's next use is excluded.

- Immediate return: answer, parsed citations, follow-ups field, metadata/tool latencies or structured validation/access/timeout error.
- Later read-back: default or accepted supplied session identifier reuses process-memory ADK session under the principal; this wrapper does not write HTTP chat history.
- Delegated visibility: tools/model receive session context and channel-marked question; client receives accumulated answer and summaries, with tool-start progress messages.
- Selection predicate: requested channel is checked upstream; mode chooses tool set; session ID must start with the principal namespace; model selects tools.
- Invalidation or expiry: in-memory state is process-local; hard timeout bounds drive; principal binding resets in finally; no durable session expiry policy is established by this wrapper.
- Activation or effect: tools can run, and accumulated non-partial model text is returned; citations are parsed text, not a separate evidence-verification verdict.
- Evidence limits: unlike HTTP, wrapper does not bind authorized-channel scope or build the same history/citation registry path; namespace prefix test alone is not a full security proof.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Operating mode: open question answering, no established reference-answer oracle. Model is [RT-CMP-qa-agent](#rt-cmp-qa-agent). SRC-1: `src/beever_atlas/api/mcp_server/_tools_retrieval.py`, `src/beever_atlas/api/mcp_server/_ask_runner.py`, `src/beever_atlas/agents/runner.py`.

> session = await create_session(user_id=principal_id, session_id=effective_session_id)
> --- `src/beever_atlas/api/mcp_server/_ask_runner.py`

> principal_token = bind_principal(principal_id)
> --- `src/beever_atlas/api/mcp_server/_ask_runner.py`

#### RT-RTE-outbound-tools
Label: Configured remote capability admission

Endpoints/progression: environment JSON configuration → startup registry → GET remote `/tools` → callable wrappers → QA model function selection → POST remote `/tools/{tool_name}`. Configurer supplies endpoint/token; remote catalog supplies names/descriptions; Atlas wraps them without inspecting remote implementation. These are HTTP catalog/POST semantics, not proof of arbitrary standard MCP transport support.

- Immediate return: loaded callable catalog at initialization; selected calls return remote JSON or raise HTTP failure.
- Later read-back: registry remains in process and is copied into constructed deep/summarize agents; remote service retention is uninspected.
- Delegated visibility: configured remote endpoint receives model-supplied keyword arguments and its configured bearer credential; Atlas/model receive returned JSON.
- Selection predicate: configured servers and successful discovery; nonempty tool names; deep/summarize include registry tools, quick does not; model chooses execution.
- Invalidation or expiry: process initialization and QA instance construction govern loading; no per-call permission renewal, catalog TTL or automatic rollback was established in inspected registry code.
- Activation or effect: POST may cause external effects according to the remote server; local channel guard and base-tool disabled list are not demonstrated mediation of those effects.
- Evidence limits: actual configured servers/grants and remote implementations unavailable; no observed invocation or exhaustive safety finding.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission/rejection: configurer grants endpoint credential; registry skips failed discovery and missing names; model chooses calls later. Human per-tool approval is not established. Recovery is startup error logging/skipping and request timeout/error propagation; removal/reconfiguration/restart rather than transactional undo is the inspected control surface. Guidance retained in wrapper docstrings includes remote descriptions; capabilities persist in the process, not as generated source code. Answer oracle: none. Operating mode: dynamically configured tool use during open QA. SRC-1: `src/beever_atlas/agents/mcp_registry.py`, `src/beever_atlas/agents/query/qa_agent.py`, `src/beever_atlas/server/app.py`.

> resp = await client.post(url, headers=headers, json=kwargs)
> --- `src/beever_atlas/agents/mcp_registry.py`

> all_tools = [*base_tools, *orch_tools, *registry.tools]
> --- `src/beever_atlas/agents/query/qa_agent.py`

#### RT-RTE-model-assignment
Label: Runtime model assignment change

Endpoints/progression: authenticated settings PUT/DELETE assignment → validate/build Assignment → MongoDB upsert/delete → QA cache reset and provider reload. Trigger is an explicit request, not a model's self-evaluation. Proposed change is consumer-to-model/endpoint mapping plus generation parameters.

- Immediate return: persisted assignment response or validation error; reload failures are logged non-fatally.
- Later read-back: provider hydrates persisted assignments/legacy overrides; rebuilt agent or later completion consumer resolves configuration.
- Delegated visibility: provider resolver receives assignment and endpoint metadata/credentials; model consumer receives the selected model interface rather than the whole configuration database.
- Selection predicate: known consumer, existing endpoint, compatibility check unless `force`; fallback endpoint must exist and differ from primary.
- Invalidation or expiry: QA cache reset precedes reload; deletion restores default resolution; concurrent requests and reload failures prevent an unconditional next-call guarantee.
- Activation or effect: configuration can change subsequent model choice; successful save alone does not prove that a live call used the new model.
- Evidence limits: caller may be human or software; model/provider deployment identity and exercised changes unobserved; direct completion and embedding consumers need their own resolution tracing.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: caller proposes/selects; deterministic validation can veto; `force` can bypass capability mismatch. Compatibility metadata is not an expected-answer oracle or capability experiment. Operating mode: explicit production configuration. Guidance is consumer/endpoint capability metadata. The persisted artifact is Assignment data, not model parameters or revised method text. Recovery: resubmit/delete mappings, rebuild caches/reload; these are not atomic rollback of in-flight work. SRC-1: `src/beever_atlas/api/assignments.py`, `src/beever_atlas/llm/provider.py`, `src/beever_atlas/server/app.py`.

> if missing and not req.force:
> --- `src/beever_atlas/api/assignments.py`

> Best-effort — never let a hydration failure fail the save.
> --- `src/beever_atlas/api/assignments.py`

### Claims

#### RT-CLM-channel-isolation
Label: Scope of channel isolation

Claimed operation: participating QA tools refuse channels outside the current turn's set. Owner/enforcement: HTTP stream binding and `channel_blocked`. Guarantee strength: policy, code-enforced for bound participating tools; not a deployment guarantee. Implementation conclusion status: wired. Operation conclusion status: uninspected. The alternate MCP wrapper binds only principal; standalone calls may be unbound. `get_wiki_page` itself reads the cache after the channel gate, without independently invoking a principal capability ACL. The channel-access helper also deliberately allows broad MCP access in single-tenant mode. A blanket cross-path channel isolation conclusion would therefore be false. SRC-1: `src/beever_atlas/api/ask.py`, `src/beever_atlas/agents/tools/orchestration_tools.py`, `src/beever_atlas/agents/tools/wiki_tools.py`, `src/beever_atlas/api/mcp_server/_ask_runner.py`, `src/beever_atlas/infra/channel_access.py`.

> if not authorized:
>     return True
> return channel_id in authorized
> --- `src/beever_atlas/agents/tools/orchestration_tools.py`

> if single_tenant and kind == "mcp":
>     return
> --- `src/beever_atlas/infra/channel_access.py:153-154`

#### RT-CLM-untrusted-tools
Label: Untrusted-context output filtering claim

Claimed operation: `_filter_tools_for_untrusted` removes write/egress names for prompt-injection defense. Its helper implementation is afforded; production invocation is not established by the inspected constructor/HTTP/MCP paths and scoped symbol search. Actual construction appends orchestration and remote tools directly. The model always receives a natural-language untrusted-content note, which is a policy request, not removal of tools. No global no-egress/no-write guarantee follows. The helper's substring classification would itself need coverage of actual external names even if called. SRC-1: `src/beever_atlas/agents/query/qa_agent.py`, `src/beever_atlas/api/ask.py`, `src/beever_atlas/api/mcp_server/_ask_runner.py`, `src/beever_atlas/agents/mcp_registry.py`.

> Drop write/egress tools when the prompt contains untrusted content.
> --- `src/beever_atlas/agents/query/qa_agent.py`

> extra_instruction = f"\n\n{UNTRUSTED_SYSTEM_NOTE}\n{extra_instruction}"
> --- `src/beever_atlas/agents/query/qa_agent.py`

#### RT-CLM-write-completion
Label: Partial persistence and intent completion

Claimed operation: intent bookkeeping and replay recover missing vector/graph writes. Owner: persister and afforded `WriteReconciler`. Guarantee strength: best effort. The implemented persister gathers independent store writes and records errors. Final completion tests vector failure only, so graph failure alone is not a universal pending-replay condition. Reconciler methods replay missing-store flags, but inspection did not establish a live call site in the server/scheduler examined; this is a scheduling limit, not an absence claim. External contracts include durable MongoDB intent state and idempotent upsert semantics. Cross-store atomicity and eventual recovery in deployment are not established. SRC-1: `src/beever_atlas/agents/ingestion/persister.py`, `src/beever_atlas/services/reconciler.py`, `src/beever_atlas/server/app.py`, `src/beever_atlas/services/scheduler.py`.

> if not weaviate_failed(persist_errors):
>     await stores.mongodb.mark_intent_complete(intent_id)
> --- `src/beever_atlas/agents/ingestion/persister.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-qa-guidance
Label: QA instructions and grants

Consumer: QA model plus ADK tool executor. Channel: constructed natural-language instructions, user/context message and symbolic tool list. Force: instructions request behavior; tool list defines executable choices while tool-specific checks mediate local effects. Horizon: current invocation, with cached agent construction across turns until flags/cache refresh change it. Durable history and retrieved evidence can enter future invocations, but their precise memory transformation is not redefined here. SRC-1: `src/beever_atlas/agents/query/qa_agent.py`, `src/beever_atlas/api/ask.py`. Evidence and bounded effect scope: [RT-RTE-dashboard-ask](#rt-rte-dashboard-ask), [RT-RTE-outbound-tools](#rt-rte-outbound-tools), [RT-CLM-untrusted-tools](#rt-clm-untrusted-tools).

#### RT-BAP-page-curation
Label: Page curation controls

Consumer: incremental wiki maintainer. Channel: persisted symbolic `curation_mode`/legacy pin state read before model invocation. Force: automatic update eligibility changes by code rule; manual marks dirty without invoking model, frozen skips. Horizon: later updates on the same retained page until changed. This is stronger than a prose request but scoped to the inspected incremental consumer, not all page writers. SRC-1: `src/beever_atlas/services/wiki_maintainer.py`, `src/beever_atlas/api/wiki.py`; evidence: [RT-RTE-wiki-maintenance](#rt-rte-wiki-maintenance), [RT-RTE-page-curation](#rt-rte-page-curation).

#### RT-BAP-model-assignment
Label: Persisted model routing authority

Consumer: provider resolver and rebuilt model clients. Channel: symbolic Assignment/endpoint data persisted in MongoDB and loaded into provider/cache state. Force: selects model interface/credentials for covered consumers; non-fatal reload and in-flight clients limit immediacy. Horizon: subsequent requests/restarts until overwritten/deleted. No implication of weight learning or successful improvement. SRC-1: `src/beever_atlas/api/assignments.py`, `src/beever_atlas/llm/provider.py`; evidence: [RT-RTE-model-assignment](#rt-rte-model-assignment).

## Annotations

none
