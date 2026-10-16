---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Synthadoc runtime baseline: queued knowledge compilation, bounded answering, maintenance tool loops and alternate admission paths at the frozen Git boundary."
run-id: AAS-2026-10-15-synthadoc-a3cae9152fff-01
reviewed-boundary: b80d9388a3013e8051baf2854c7250942c46e91a
---

# Synthadoc runtime report

## Runtime account

Synthadoc combines returning model computations with a server-owned work queue and a model-directed maintenance loop. A source normally becomes a queued ingest job, extracted text, an analysis, a create/update/flag/skip decision, and persisted wiki content or a staged candidate. A later question retrieves persisted pages and asks a model to synthesize an answer. Maintenance can instead enter a repeated model/tool loop, with Python executing registered functions and some writes waiting for client confirmation. These are distinct control paths, not one universal agent loop. The purpose and whole-system scope are fixed in [the boundary](boundary.md); its source register supplies SRC-1 throughout this report.

All findings below concern inspected implementation or attributed design at the registered commit. No target execution, model response, deployed configuration, production wiki, supplied trace or causal experiment was observed. An implemented consumer receives inputs; this does not demonstrate that a model follows them or that retained knowledge improves answers. Memory content, detailed revision lineage and retention inventories are left to the memory member.

### Ordinary shipped invocation

A concrete ordinary route is `synthadoc ingest raw_sources/report.pdf` against a running server, followed by a question after maintenance has made the resulting page query-eligible. The CLI resolves the wiki and local source, posts to `/jobs/ingest`, and prints a job ID rather than waiting for a completed wiki. HTTP stores the source, force flag and applicable overrides in a job payload. Its worker dequeues that identity, dispatches `_run_ingest`, and imposes the configured job timeout. There is no per-content approval merely because this worker supplies `auto_confirm=True`: the orchestrator explicitly reserves that argument for future prompts ([RT-RTE-source-ingest](#rt-rte-source-ingest); SRC-1, `synthadoc/cli/ingest.py`, `synthadoc/integration/http_server.py`, `synthadoc/core/orchestrator.py`).

The ingest job reloads configuration, checks local-source containment and deduplication, selects an extraction skill, and limits extracted text before model analysis. Analysis supplies entities and tags to BM25 selection; up to five candidate snippets enter a second model call. That call proposes an action under the shipped decision prompt and optional wiki purpose. Python interprets the returned JSON. Flagging changes page status; updates merge a section; creates write a draft page or a candidate. Source provenance, citation annotations, logs and audit entries accompany writes. Live new pages also enter the index and optional routing structure; a live write can regenerate the overview. Models propose text and action fields, but Python owns progression and filesystem effects (SRC-1, `synthadoc/agents/ingest_agent.py`).

The new page is not immediately part of ordinary search simply because it exists: the BM25 corpus admits `active` and `stale`, not `draft`, `contradicted` or `archived`. Lint and explicit lifecycle operations supply additional admission routes. A later ordinary question reaches `QueryAgent`: action detection can divert it; otherwise decomposition and retrieval select a ranked pool, code budgets page text and history, and a synthesis call returns answer text, citations and gap metadata. The blocking query and streaming query are not identical: the orchestrator passes `ROUTING.md` only to its streaming agent in the inspected constructors. Streaming also supports conversational action workflows and session identity ([RT-RTE-wiki-query](#rt-rte-wiki-query), [RT-RTE-lint-repair](#rt-rte-lint-repair); SRC-1, `synthadoc/storage/search.py`, `synthadoc/core/orchestrator.py`, `synthadoc/agents/query_agent.py`).

### Material loops and control owners

| Loop | Trigger/principal and identity | Next-step owner and policy | Context, state and executor | Return, recovery and terminal result |
|---|---|---|---|---|
| Ingest | Caller supplies source; server assigns job ID; pages use slugs and source references. | Python sequences extraction, analysis, retrieval, decision and writes. Model supplies semantic analysis/action proposals; code supplies dispatch, deduplication and staging rules. | Source text and page snippets are natural language; action JSON and configuration have fixed consumers. Queue, audit/cache databases and Markdown outlive the call. Python skills and storage execute effects. | Immediate enqueue result; later job result lists created/updated/flagged pages and child jobs. Classified errors skip, fail, requeue or permanently fail; retry does not imply multi-file rollback. |
| Query | Caller supplies question and optionally a session/history. | Code detects actions, decomposes and searches; model synthesizes selected context. | New QueryAgent/provider per orchestrator invocation; bounded wiki text, purpose/help/live data and trimmed history. Search is BM25 with optional embedding rerank. | Answer/citations/gap suggestions or streamed events. Timeout/error handling is external to the synthesis result. |
| Maintenance | Natural-language request or named CLI workflow; session ID keys confirmation. | ActionAgent fast matching or model extraction selects workflow. Model chooses registered tools in the normal loop; Python dispatches and enforces applicable gates. CLI-provider alternatives can use Python-owned progression. | Workflow system text, current user request, accumulating tool results, closure-held gate/read sets; functions act on stores and queue. | SSE progress, confirmation, tokens and final text; budget exhaustion, parse retries, cancellation and snapshots bound recovery. No successful repair inferred. |
| Scheduled operation | Configured cron entry and operation string; scheduled run ID. | Scheduler code spawns a Synthadoc CLI command when due. | Child process runs in wiki root with inherited environment; output and result are recorded. | Exit code and truncated output, timeout/cancellation kill/drain. This is an operational driver, not an independent model decision policy. |

The source anchors and precise decision, admission, read-back and evidence limits for these loops are in [RT-RTE-source-ingest](#rt-rte-source-ingest), [RT-RTE-wiki-query](#rt-rte-wiki-query), [RT-RTE-workflow-loop](#rt-rte-workflow-loop) and [RT-RTE-scheduled-operation](#rt-rte-scheduled-operation).

### Four forcing cases and guarantee coverage

1. **Call a declared gated write without first calling confirm.** The workflow registry wrapper invokes a fallback confirmation itself. Content-health repair additionally tracks discovered/read slugs and resets its write gate per call. This is executable enforcement on wrapped functions, stronger than a prompt saying “confirm first.” However, a gate can be shared across a workflow batch; read-set checks are not a proof that generated text preserves truth. When the discovered set is empty, the content-health membership checks are conditional on its being nonempty; the unconditional prerequisite is a successful content read. Calling the underlying helper outside that registry does not inherit the wrapper. See [RT-RTE-workflow-loop](#rt-rte-workflow-loop) and [RT-CLM-confirm-scope](#rt-clm-confirm-scope) (SRC-1, `synthadoc/agents/workflows/_base.py`, `synthadoc/agents/workflows/content_health_resolver.py`).
2. **Update an existing page with force, or flag a page while staging is enabled.** Existing-page force paths explicitly substitute staging policy `off`; flagging directly writes contradiction state. Staging is therefore not an invariant that all model-originated changes receive human review. Default staging is also `off`. See [RT-RTE-source-ingest](#rt-rte-source-ingest) and [RT-RTE-candidate-admission](#rt-rte-candidate-admission) (SRC-1, `synthadoc/config.py`, `synthadoc/agents/ingest_agent.py`).
3. **Write through MCP or auto-resolve lint instead of an interactive workflow.** MCP exposes direct content writes with no workflow confirmation; lint can accept a model's resolvable response and rewrite/activate a page. Ordinary search state filtering also does not govern direct reads or export: default OKF export includes contradicted pages. These counterexamples defeat a system-wide approval or active-only-consumption claim. See [RT-RTE-lint-repair](#rt-rte-lint-repair), [RT-RTE-client-write](#rt-rte-client-write) and [RT-RTE-context-export](#rt-rte-context-export) (SRC-1, `synthadoc/integration/mcp_server.py`, `synthadoc/agents/lint_agent.py`, `synthadoc/core/export.py`).
4. **Select a coding-tool provider rather than a text API.** ActionAgent diverts supported workflows to their CLI-provider implementations and rejects unsupported ones, rather than assuming the JSON loop works. Nevertheless, ordinary completion can spawn Claude Code with `--dangerously-skip-permissions`. Python's workflow tool allowlist is not a grant boundary for that child agent's native tools. Configured shell hooks and dynamically imported skills provide further alternate executors. See [RT-RTE-provider-delegation](#rt-rte-provider-delegation), [RT-RTE-extension-loading](#rt-rte-extension-loading) and [RT-CLM-effect-boundary](#rt-clm-effect-boundary) (SRC-1, `synthadoc/agents/action_agent.py`, `synthadoc/providers/coding_tool.py`, `synthadoc/agents/skill_agent.py`, `synthadoc/core/hooks.py`).

These are source-traced forcing cases, not experiments. Native tools in external providers, all workflow subclasses, every direct filesystem operation and deployment isolation remain unobserved or incompletely audited. Capability surface means what shipped entry points can invoke; the current grant set depends on configured providers, extensions, hooks and exposed endpoints. The deployed isolation envelope depends on process credentials, mounts, network exposure and external host contracts, none of which was supplied as execution evidence. WikiStorage's resolved-root check is a local path check, not a sandbox for every effect ([RT-CLM-effect-boundary](#rt-clm-effect-boundary)).

### Working context and change admission

Ingest clips source text to `max_source_chars`; candidate context uses five 600-character snippets. Query gathers candidates, greedily fills a wiki character budget, can include a partial final page, and trims history from the newest end until the next turn would overflow. Help or live-data matches can replace the wiki context rather than supplement it. Context packs separately extract the first 120 words per selected page and account for approximate tokens. These are code-controlled inclusion and eviction mechanisms, not model-generated durable summaries. Separate analysis/decision/synthesis calls resemble isolated frames: selected inputs enter, structured results escape, and later calls do not automatically inherit all preceding text. The analogy stops at by-value strings: a slug or source pointer is not automatically dereferenced by a model window; explicit search/read code must reload it (SRC-1, `synthadoc/agents/ingest_agent.py`, `synthadoc/agents/query_agent.py`, `synthadoc/agents/_query_utils.py`, `synthadoc/agents/context_agent.py`).

The maintenance JSON loop instead accumulates its current messages and tool results, subject to call and completion budgets and parse-recovery behavior; no compaction conclusion is drawn for external coding-agent contexts. Retained conversational sessions and detailed knowledge revision are specialist topics. Fixed workflow prompts shape model proposals; the inspected loops do not establish that the system rewrites those prompts, its own package or its model weights. Capability changes can be admitted by installing discoverable Python skills or changing configuration/hooks, but those are trusted installation/configuration paths, not demonstrated autonomous code improvement. Model fix generation, operator veto, default automatic writes and recovery must be assessed by their particular route, not by the product's “agent” terminology.

Added implementation coverage under SRC-1 includes the CLI ingest/workflow drivers, provider factory and Anthropic/coding-tool adapters, skill selection/import, sanitizer, search embedding/reranking, gate construction, content-health wrapper, proposed-edit tool, MCP direct write, candidate movement, scheduler subprocess and hook executor. Source reading here extends the boundary's initial inventory, not its frozen source identity. Exported-bundle consumption and context budgeting were inspected as code; their success and comparative benefit were not tested.

## Shared records

### Components

#### RT-CMP-provider-model
Label: Configured completion provider/model roles

The source-native `LLMProvider`/`AgentConfig` pair supplies model completions for separately configurable roles. This record identifies the configurable completion service family, not one asserted shared weight set. The operative model is distributed-parametric; prompt/response strings and model identifiers are not weights. Provider-side substrate and numerical parameters are outside the repository. Config is held in Python and loaded from TOML (SRC-1, `synthadoc/config.py`, `synthadoc/providers/__init__.py`, `synthadoc/providers/anthropic.py`, `synthadoc/providers/coding_tool.py`).

| Operative role | Parameter changes in inspected operation | Exact version pin | Mutable resolution |
|---|---|---|---|
| ingest | Calls completion; inspected route does not train weights; provider internals uninspected. | User model string, not a verified weight digest. | Config/default and remote endpoint or coding CLI can select another model. |
| query, also used by ActionAgent and ContextAgent | Same inference-only integration; external mutation unresolved. | Same configuration-level pin limit. | Config/provider selection can change; endpoint identity does not fix weights. |
| lint | Same integration limit; page changes are not weight updates. | Same configuration-level pin limit. | Role override/default and endpoint resolution can change. |
| adversarial | Separately configured optional audit provider; no inspected training operation. | Same configuration-level pin limit. | Role override/default and endpoint resolution can change. |
| skill | Configured role available to extraction machinery; full skill/provider call coverage uninspected. | No exact numerical version established. | Role/default selection and external resolution remain mutable. |

> override = getattr(self, agent_name, None)
> if override is None:
>     return self.default
> --- `synthadoc/config.py`

> "model": self._config.model,
> "max_tokens": max_tokens,
> "messages": [{"role": m.role, "content": m.content} for m in messages],
> --- `synthadoc/providers/anthropic.py:38-40`

No runtime observation establishes the deployed grant set, provider compliance or provider-state persistence. Coding-agent delegation has its own route because its effect boundary differs from a text API.

#### RT-CMP-text-embedding
Label: Optional fastembed TextEmbedding model

`HybridSearch` lazily constructs `TextEmbedding` using the model name `BAAI/bge-small-en-v1.5`. The model is distributed-parametric and externally loaded; its exact weights are not pinned by a digest in the inspected loader. There is no parameter-training step in that loader or rerank path. The local cached instance is reused; dependency/model distribution resolution can change the numerical artifact across installations. These limits are distinct from changes to stored page vectors. VectorStore persists float32 embedding blobs in SQLite; embedding input is clipped to 512 characters, and vectors rerank BM25 candidates rather than search the complete corpus independently (SRC-1, `synthadoc/storage/search.py`).

> self._embed_model = TextEmbedding(_EMBED_MODEL_NAME)
> --- `synthadoc/storage/search.py`

> result = list(model.embed([text[:512]]))
> --- `synthadoc/storage/search.py`

### Operative objects

#### RT-OBJ-workflow-protocol
Label: Workflow tool registry and text protocol

The registry is a symbolic Python mapping from tool names to async callables, with fixed parsing and dispatch rules. JSON tool-call strings become symbolic action requests through parsing; prose final responses remain natural-language output. Registry, counters, mandatory-next signal and messages are per-loop process state, not an asserted durable memory store. Workflow prompt strings are a separate natural-language part identified below (SRC-1, `synthadoc/agents/workflows/_loop.py`, `synthadoc/agents/workflows/_base.py`).

> if tool_name not in tool_fns:
>     tool_result: dict = {"error": f"Unknown tool: {tool_name!r}"}
> else:
>     try:
>         tool_result = await tool_fns[tool_name](**tool_input)
> --- `synthadoc/agents/workflows/_loop.py`

#### RT-OBJ-workflow-guidance
Label: Shipped workflow guidance strings

Workflow modules contain natural-language system prompts naming steps, permitted repair strategies and reporting/confirmation instructions. Python source files are their substrate; `build_system_prompt` supplies them at invocation. They guide model interpretation but do not themselves enforce all stated requirements. This object is distinct from the executable registry and gates. It is shipped static guidance, not evidence of method revision from operational traces (SRC-1, `synthadoc/agents/workflows/content_health_resolver.py`, `synthadoc/agents/workflows/contradiction_resolver.py`).

> 3. ALWAYS follow the exact per-page sequence: get_page_content → confirm → write_content_health_fix.
> --- `synthadoc/agents/workflows/content_health_resolver.py`

### Routes

#### RT-RTE-source-ingest
Label: Source extraction and wiki compilation

Endpoints: caller source → CLI/HTTP/MCP enqueue → worker/orchestrator → extraction skill → model analysis → candidate search → model decision → store/candidate/audit. Python owns sequencing and physical writes; model analysis and decision fields supply semantic proposals. See [RT-CMP-provider-model](#rt-cmp-provider-model). The caller starts an open ingest request, not an experiment with an expected-answer oracle. No reference-answer oracle is used in the inspected dispatch. Human control over each resulting text is unresolved unless a separate candidate approval path is invoked.

Admission: source/force or a child job triggers the proposed page change. Decision prompt, optional purpose, source and candidate snippets shape the proposal. Code dispatches skip/flag/update/create and applies configured staging. Existing-page force bypasses staging; create drafts have confidence `medium`; flag writes directly. Source clipping and citation annotation transform delivered text, so the complete source is not necessarily considered. Model skip/rejection and code deduplication can stop work. Operators can reject candidates later; this route does not guarantee a pre-write human veto. Recovery consists of job states/retry and available page history, not a demonstrated atomic transaction across Markdown, index, routing, logs and audit (SRC-1, `synthadoc/agents/ingest_agent.py`, `synthadoc/core/orchestrator.py`, `synthadoc/integration/http_server.py`).

- Immediate return: CLI/HTTP enqueue returns job ID; worker eventually records pages and child jobs or terminal failure/skip.
- Later read-back: live retained page text can enter later queries once eligible; staged text awaits promotion. Audit hash/size can suppress re-ingest.
- Delegated visibility: extraction skill receives source; analysis receives clipped sanitized text; decision receives text, entities and selected page snippets. Child jobs receive source/force payloads, not the parent's whole context.
- Selection predicate: source trigger chooses skill; dedup uses source hash/size; BM25 uses entities/tags; action/target fields plus code existence checks choose writes.
- Invalidation or expiry: force/bust-cache can bypass dedup/cache; decision key includes source hash, candidate slugs and prompt hash. It does not include candidate page bodies, so unchanged slugs need not invalidate changed snippets.
- Activation or effect: wired Python writes to wiki/candidates and metadata, and live writes can refresh overview/routing. Actual model response, persisted result and later behavioral dependence are unobserved.
- Evidence limits: analysis/decision cache and fallback code establish available paths, not source fidelity, successful citations or review quality.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> # auto_confirm is reserved for when user-facing confirmation prompts are added.
> --- `synthadoc/core/orchestrator.py`

> # --force on an existing wiki page bypasses staging: the user is
> # explicitly updating a page they already own (e.g. clearing a
> # truncated-source flag). Routing to candidates/ would silently
> # leave the old page in wiki/ and confuse lint/report.
> policy = "off" if force else self._staging_policy()
> --- `synthadoc/agents/ingest_agent.py`

> {"text_hash": text_hash, "slugs": slugs, "prompt_hash": prompt_hash},
> --- `synthadoc/agents/ingest_agent.py`

The force quote is scoped to the checked existing-update branch; a separate existing-slug fallback also bypasses staging. Sanitization is bounded regex redaction, not a guarantee that source instructions cannot influence a model. It occurs after extraction: extraction skills can have their own model processing (SRC-1, `synthadoc/core/sanitizer.py`, `synthadoc/agents/ingest_agent.py`).

#### RT-RTE-wiki-query
Label: Wiki retrieval and answer synthesis

Endpoints: caller question → orchestrator QueryAgent → action preflight or retrieval/synthesis → QueryResult/SSE. Code owns routing, context budgets and postprocessing; model supplies decomposition and answer content. HybridSearch admits active/stale pages into its BM25 corpus; optional vectors only rerank that candidate set. QueryAgent can instead use bundled help and audit/live data. The streaming constructor supplies routing while the blocking orchestrator constructor does not. This is an open question-answering mode, without an expected-answer oracle. Gap scores and model sentinels are not reference answers (SRC-1, `synthadoc/agents/query_agent.py`, `synthadoc/core/orchestrator.py`, `synthadoc/storage/search.py`).

- Immediate return: answer, retrieved-slug citations, token/gap/routing metadata, or streamed events; detected actions may return uncached action results instead.
- Later read-back: reads persisted wiki pages and caller-supplied conversational history; detailed session retention is not established by this route alone.
- Delegated visibility: synthesis receives budgeted selected pages or replacement help/live context, optional purpose and trimmed history; not every retrieved page necessarily survives the budget.
- Selection predicate: alias expansion, optional translation/decomposition, ranked hybrid candidates, optional streaming routing scope and low-score full-corpus fallback.
- Invalidation or expiry: corpus invalidation is explicit; history uses a character budget and discards older turns from this model input without summarizing them. HTTP caching and every invalidation caller are not exhaustively audited here.
- Activation or effect: code delivers context to completion and produces answer fields; semantic reliance on a particular retained claim remains unobserved.
- Evidence limits: citation list is initially candidate slugs, whereas context can omit/truncate pages; citation presence alone is not verified answer support. External provider internals are uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> _QUERY_STATES: frozenset[str] = frozenset({"active", "stale"})
> --- `synthadoc/storage/search.py`

> remaining = budget - used
> if remaining > 100:
>     parts.append(chunk[:remaining])
> break
> --- `synthadoc/agents/query_agent.py`

#### RT-RTE-workflow-loop
Label: Interactive maintenance tool-call loop

Endpoints: streamed request or CLI named workflow → ActionAgent/workflow registry → model call/parsed tool calls → Python tools → messages → next model call or final text. Normal mode uses [RT-OBJ-workflow-protocol](#rt-obj-workflow-protocol) and [RT-OBJ-workflow-guidance](#rt-obj-workflow-guidance); the model chooses the next registered action, while Python controls execution and termination. Multiple calls can be parsed from one response and executed sequentially; confirmation calls are separated from mixed data-tool batches. Parse failures receive bounded corrective retries; each tool attempt consumes budget, and a plain-text response normally ends the loop (SRC-1, `synthadoc/agents/workflows/_loop.py`, `synthadoc/agents/action_agent.py`, `synthadoc/cli/workflow.py`).

Admission and rejection differ by tool. `tool_propose_and_apply` computes a diff, asks the client and writes only on confirmation; rejection leaves content unchanged. Declarative GATED_TOOLS wrappers provide fallback confirmation, sharing a session gate unless the tool is per-call gated. Content-health uses per-call reset plus discovery/read guards, snapshots/fix records and rollback tools. The HTTP confirmation endpoint accepts a session-keyed boolean and wakes the waiting Event; timeout or event-delivery failure declines. This is a client-response protocol, not independently authenticated proof of human authorship or evidence that the displayed diff fully captures a large proposal: the proposed-edit preview truncates after 80 diff lines. Operators can veto proposals through that channel. Other tools and direct endpoints do not inherit this guarantee (SRC-1, `synthadoc/agents/workflows/_tools.py`, `synthadoc/agents/workflows/_base.py`, `synthadoc/agents/workflows/content_health_resolver.py`, `synthadoc/agents/workflows/tools/content_health_tools.py`, `synthadoc/integration/http_server.py`).

Operating mode: open maintenance request, not a reference-answer curriculum. Scanners/re-lint supply structural checks or model assessments, not an expected-answer oracle for factual correctness. Workflow method text shapes proposed fixes and can remain unchanged while page products change. Whether a particular page encodes a formulated explanatory theory is content-dependent; this implementation account does not classify every editorial repair as theory revision.

- Immediate return: progress/confirm/token/final-text events, plus tool-result messages to the loop; named CLI workflow consumes the same streamed query interface.
- Later read-back: successful tools alter persistent pages, lifecycle/audit state or jobs; later store/search tools reload them. Loop messages themselves are current-run state, not evidence of cross-run memory.
- Delegated visibility: model sees selected initial request and accumulating tool results; registered tools receive explicit kwargs and WorkflowContext, not arbitrary model-native capabilities.
- Selection predicate: regex fast match or model-extracted action selects workflow; parsed tool name chooses callable; guards and per-tool checks constrain writes.
- Invalidation or expiry: tool budget and parse-retry limits stop work; confirmations expire after 300 seconds and registries are removed in finally. Content-health gates reset after each successful gated call.
- Activation or effect: registry dispatch and approved write branches are wired; observed compliance with guidance and actual repair are not established.
- Evidence limits: guarantee applies only to registered/wrapped or internally confirming helpers; closure read sets do not bind every approval to a cryptographic content identity. Provider-native tools and direct writes are alternate paths.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if reset_after_call:
>     gate_open[0] = False
> --- `synthadoc/agents/workflows/_base.py`

> await asyncio.wait_for(gate.wait(), timeout=_CONFIRM_TIMEOUT)
> confirmed = ctx.confirm_result_registry.get(ctx.session_id, False)
> return {"confirmed": confirmed}
> --- `synthadoc/agents/workflows/_tools.py`

> messages.append(Message(role="user", content=_tool_result_message(combined)))
> --- `synthadoc/agents/workflows/_loop.py`

#### RT-RTE-lint-repair
Label: Lint diagnosis and automatic repair

Endpoints: queued lint parameters → worker LintAgent → deterministic checks and optional adversarial/model resolution → page/audit/report. Caller chooses scope and automatic resolution; worker passes settings. Code owns checks, status transitions and writes. The model proposes whether a contradicted page is resolvable and its rewritten text; code accepts its boolean after the applicable gate checks. Fixed instructions ask it to represent both perspectives rather than pick a winner. No per-proposal confirmation appears in this accepted-response branch. This differs from interactive [RT-RTE-workflow-loop](#rt-rte-workflow-loop) (SRC-1, `synthadoc/agents/lint_agent.py`, `synthadoc/integration/http_server.py`).

Admission: contradiction state/maintenance request triggers diagnosis. `auto_resolve` enables rewriting; false/unparseable responses leave an unresolved reason. Accepted output can replace the page and set it active; logs and lifecycle content snapshots support inspection/recovery but the shown snapshot is the resulting content, not proof of a pre-write snapshot. Structural lint also removes dangling links and updates flags. This is open corpus maintenance with optional model criticism, not a factual expected-answer oracle. Full adversarial gate semantics, faithfulness audit, all lifecycle branches and sensitive-data retraction are included system responsibilities but are not fully traced here; no uniform correctness or retraction guarantee is inferred.

- Immediate return: enqueue job ID, then report counts and terminal job state.
- Later read-back: rewritten pages and lifecycle states affect later search eligibility; unresolved notes and audit records remain inspectable.
- Delegated visibility: the inspected auto-resolution prompt supplies contradiction note and first 2000 characters of current content, not both complete raw sources.
- Selection predicate: requested scope, page contradiction state, auto_resolve option and gate outcome; model resolvable field chooses accepted rewrite.
- Invalidation or expiry: later lint/re-ingest/manual edits can revise the result; full cache/recovery coverage is uninspected.
- Activation or effect: write and active-state transition are executable branches; successful factual reconciliation is unobserved.
- Evidence limits: model judgment and structural checks do not establish accurate representation of all sources or improved future answers.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if decision.get("resolvable"):
>     page.status = LifecycleState.ACTIVE
>     page.contradiction_note = None
>     page.unresolved_note = None
>     resolution = decision.get("resolution", "").strip()
>     if resolution:
>         page.content = resolution
> --- `synthadoc/agents/lint_agent.py`

#### RT-RTE-candidate-admission
Label: Staged candidate promotion or discard

Endpoints: ingest-created candidate files → caller promotion/discard endpoint → live wiki or deletion. Ingest staging is configuration-controlled; promotion is software file movement under a caller request, not a second model review. Whether that caller is human is unresolved at the API boundary. Single and bulk promotion are supported; promotion can replace an existing live page. Guidance that shaped the text remains the ingest prompt/purpose; no candidate-specific answer oracle or content test is in the inspected promotion handler. Mode is open review/maintenance, with caller rejection through discard. Rollback of replacement is not established by that handler (SRC-1, `synthadoc/agents/ingest_agent.py`, `synthadoc/integration/http_server.py`).

- Immediate return: promoted/discarded slugs or count; missing single candidate returns 404.
- Later read-back: moved content becomes a live wiki file for later eligible retrieval; promotion alone need not make a draft active.
- Delegated visibility: promotion handler consumes filenames and page title; full human review before the call is not evidenced.
- Selection predicate: caller slug or all candidate Markdown files; ingest policy all/threshold controls earlier staging.
- Invalidation or expiry: discard removes candidate; promotion moves it out and queues overview refresh when none remain. Complete query-cache coherence of this path is not established.
- Activation or effect: filesystem move and optional new-page index update are wired; downstream consumption remains unobserved.
- Evidence limits: staging and promotion provide a review affordance, not universal or verified human approval of all knowledge changes.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> shutil.move(str(src), str(dest))
> if is_new:
>     _cand_add_to_index(wd, [(slug, title)])
> --- `synthadoc/integration/http_server.py`

#### RT-RTE-client-write
Label: Direct MCP content update

Endpoints: MCP client content/title/reason → `synthadoc_write_page` → existing WikiPage → storage and audit. The client supplies the proposed content; Python decides nonempty/existing-page checks and writes. The client can be an external agent, so calling this route does not establish human authorship or veto. It preserves lifecycle state, clears contradiction note, bumps epoch and records a changed snapshot for non-system pages. This is an open edit path without an answer oracle or interactive workflow gate. Caller abstention is the available pre-write rejection; snapshot/history interfaces provide potential recovery, not demonstrated undo (SRC-1, `synthadoc/integration/mcp_server.py`, `synthadoc/storage/wiki.py`).

- Immediate return: page slug/title/status/snapshot flag, or empty-content/missing-page error.
- Later read-back: new persisted body can reach subsequent page reads and eligible queries; clearing contradiction note changes later maintenance input.
- Delegated visibility: external MCP host receives API return; its context construction and safety policy are outside the source boundary.
- Selection predicate: explicit existing slug and nonempty content; no retrieved ranking or confidence test.
- Invalidation or expiry: epoch bump and later edits; snapshot retention/rollback completeness is not proven here.
- Activation or effect: direct write is wired without the workflow confirmation helper.
- Evidence limits: snapshot creation is not factual validation, and lifecycle preservation can leave edited content under an already active state.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> page.content = content
> if title:
>     page.title = title
> page.contradiction_note = None
> page.updated = date.today().isoformat()
> orchestrator._store.write_page(slug, page)
> --- `synthadoc/integration/mcp_server.py`

#### RT-RTE-context-export
Label: Context pack and exported-bundle consumption

Two returning alternatives bypass answer synthesis: ContextAgent uses QueryAgent decomposition and hybrid retrieval to build a budgeted pack; ExportEngine formats retained pages, and the shipped OKF consumer reloads that bundle and calls its own provider. They share knowledge delivery, not the same selector. Context packs use rank and first-120-word excerpts; OKF consumer uses sorted files with a `type` field, optional type filter and character cap. Default OKF export selects active and contradicted; a specific status filter can choose another state. Neither path proves external model compliance (SRC-1, `synthadoc/agents/context_agent.py`, `synthadoc/integration/mcp_server.py`, `synthadoc/core/export.py`, `tests/integration/okf_consumer_agent.py`).

- Immediate return: pack with selected and omitted page metadata, or export artifact and later consumer answer.
- Later read-back: pack reads persisted wiki; standalone consumer reads persisted exported Markdown on a subsequent invocation. An export is not automatically refreshed after wiki edits.
- Delegated visibility: MCP receives excerpts and provenance metadata; standalone consumer gets type-filtered, budgeted bundle context, not the live wiki or complete audit database.
- Selection predicate: pack decomposition/hybrid ranking/budget versus export status filter and consumer type/file-order/cap.
- Invalidation or expiry: new pack recomputes selection; exported bundle remains a separate snapshot unless regenerated. Its later freshness is not guaranteed.
- Activation or effect: text is delivered to caller/provider; actual behavioral reliance or portability across arbitrary consumers is unobserved.
- Evidence limits: approximate token estimates and excerpt truncation limit completeness; the shipped consumer is one implementation, not a successful universal interoperability test.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> excerpt = " ".join(content.split()[:120])
> --- `synthadoc/agents/context_agent.py`

> _OKF_ELIGIBLE = {LifecycleState.ACTIVE, LifecycleState.CONTRADICTED}
> pages = {s: p for s, p in pages.items() if p.status in _OKF_ELIGIBLE}
> --- `synthadoc/core/export.py`

#### RT-RTE-provider-delegation
Label: Coding-agent subprocess completion

Endpoints: configured completion → CodingToolCLIProvider → CLI subprocess → parsed stdout. `claude-code`/`opencode` are not merely remote text endpoints: their enclosing agent machinery is external. ActionAgent detects this provider class, uses `run_for_cli_provider` only when supported, and otherwise returns unsupported-workflow guidance. Python alternatives may gather, request a bounded rewrite and ask client approval rather than asking a child agent to simulate the JSON tool registry. In the base completion path stdin carries prompt text, a timeout kills/drains the process, and Claude's command includes permission skipping. No process sandbox or child-native tool allowlist appears in the inspected Popen launch (SRC-1, `synthadoc/agents/action_agent.py`, `synthadoc/providers/coding_tool.py`).

- Immediate return: parsed CompletionResponse or provider error; streaming can be synthesized after child completion.
- Later read-back: uninspected — child-agent retained state and incidental effects are outside the frozen implementation; parent text results alone do not establish them.
- Delegated visibility: serialized messages; Claude gets system through --system-prompt when supplied, otherwise its default agent context can apply. Other inherited environment/host context is not comprehensively known.
- Selection predicate: configured provider/model, supported-workflow class flag and specific CLI-provider implementation.
- Invalidation or expiry: per-call timeout/process cleanup; external session/weight/context expiry is uninspected.
- Activation or effect: subprocess invocation and permission flag are wired; actual tool use, approvals or side effects by that child are unobserved.
- Evidence limits: registry restrictions and source sanitizer do not bound all possible native child-agent effects; external agent/runtime contract is required.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> cmd = [binary, "-p", "--output-format", "json", "--dangerously-skip-permissions"]
> --- `synthadoc/providers/coding_tool.py`

#### RT-RTE-extension-loading
Label: Skill installation and configured shell hooks

Endpoints: installed skill directories/entry points or configured hook command → Python import/skill invocation or shell subprocess. These are separate executors grouped here as trusted extension admission, not a single safe plugin interface. SkillAgent discovers metadata, selects by extension/prefix or intent, imports the named class, and constructs the skill. Installed files/configuration supply capability changes; no model-generated installation or content-review gate is established. Registry priority comments should not be treated as a verified total precedence contract: multiple early tiers use `override=True`. Hook commands come from configuration; event context is passed as JSON stdin. A configured blocking hook can raise on nonzero exit, but errors/timeouts are also caught/logged, so “blocking” is not a universal rollback guarantee (SRC-1, `synthadoc/agents/skill_agent.py`, `synthadoc/core/hooks.py`).

Admission: the filesystem/package/configuration writer installs executable capability. Software discovers/loads it; who has that write authority in deployment is unresolved. No semantic answer oracle, code review, per-execution human approval or automatic capability rollback is established by these loaders. Open extraction/event handling is the operating mode; changed inputs or configuration are triggers, not an improvement experiment.

- Immediate return: extraction output to ingest, import/error, or hook completion/logging; nonblocking hooks run in daemon threads.
- Later read-back: later registry construction/invocation can reload installed capability or configuration. Hook-written retained state depends on user code and is not frozen evidence.
- Delegated visibility: skill receives source and configured kwargs; shell hook receives serialized event context with parent process access rights.
- Selection predicate: discovered metadata triggers choose skill; event name and configured command choose hook; empty hook is skipped.
- Invalidation or expiry: loaded skill classes are cached per SkillAgent; replacement/restart and extension-specific recovery are deployment concerns. Hook subprocess timeout is 60 seconds.
- Activation or effect: dynamic Python execution and shell invocation are wired; deployed extensions and effects remain unobserved.
- Evidence limits: no isolation claim extends from the workflow registry to imported extension code or shell hooks.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> mod = importlib.util.module_from_spec(spec)
> spec.loader.exec_module(mod)
> --- `synthadoc/agents/skill_agent.py`

> result = subprocess.run(cmd, shell=True, input=json.dumps(context).encode(),
>                         capture_output=True, timeout=60)
> --- `synthadoc/core/hooks.py`

#### RT-RTE-scheduled-operation
Label: Scheduled Synthadoc command execution

Endpoints: cron entry containing operation string → scheduler → Python module subprocess → audit run record. Scheduler code owns due-time triggering, run identity and process control; the scheduled command owns any later model decisions. The process uses wiki root as cwd, inherited environment and `shlex.split(op)` argv, not a shell evaluation of that string. Schedule configuration admits production-operation changes through caller/configuration control; it is not per-content human approval of later ingest or lint results. No answer oracle or proposed method improvement is part of this generic executor (SRC-1, `synthadoc/core/scheduler.py`).

- Immediate return: scheduled-run record with success/failure, duration and truncated command output after child termination.
- Later read-back: durable scheduled-run history is recorded; knowledge changes depend on the invoked command, such as ingest/lint routes above.
- Delegated visibility: child gets command args, cwd and inherited environment; captured output is truncated before audit storage.
- Selection predicate: matching cron schedule and enabled scheduler loop; operation is the configured command string.
- Invalidation or expiry: command timeout/cancellation kills and drains subprocess; schedule can be replaced/removed; no automatic page rollback follows generic process failure.
- Activation or effect: command execution machinery is wired, not observed running on a production schedule.
- Evidence limits: exit-code success does not prove command output quality or model benefit; coordination with every external writer is uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> sys.executable, "-m", "synthadoc", "-w", wiki,
> *shlex.split(op),
> cwd=str(wiki_root),
> --- `synthadoc/core/scheduler.py`

### Claims

#### RT-CLM-confirm-scope
Label: Confirmation is a scoped protocol

The load-bearing guarantee is refusal to run an applicable wrapped write before an accepted client response. Owner: AgenticWorkflow wrappers or internally confirming tool. Enforcement point: callable wrapper or `tool_propose_and_apply`, not model obedience. Guarantee strength: protocol. Covered paths: supplied guarded registry calls and helpers that internally confirm, including fallback when the model skips explicit confirmation. Per-call versus shared-batch gating differs by workflow. Required external contract: session confirmation is delivered to an authorized, appropriately reviewing client, whose boolean represents the intended decision. The server Event alone proves neither human identity nor review completeness (SRC-1, `synthadoc/agents/workflows/_base.py`, `synthadoc/agents/workflows/_tools.py`, `synthadoc/integration/http_server.py`).

> if not fallback.get("confirmed"):
>     return {
>         "status": "cancelled",
>         "message": f"`{tool_name}` cancelled by user.",
>     }
> --- `synthadoc/agents/workflows/_base.py`

Alternate paths: automatic ingest/lint, direct MCP/HTTP edits, candidate movement, raw filesystem edits, custom extensions/hooks and coding-tool native actions are not generally covered. The block on unknown registry names only prevents dispatch through that registry. See [RT-RTE-workflow-loop](#rt-rte-workflow-loop), [RT-RTE-client-write](#rt-rte-client-write), [RT-RTE-lint-repair](#rt-rte-lint-repair) and [RT-RTE-provider-delegation](#rt-rte-provider-delegation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- benefit conclusion status: uninspected

#### RT-CLM-effect-boundary
Label: Root checking is not universal process isolation

WikiStorage owns resolved containment checking for its `_page_path` operations. Guarantee strength: invariant within that checked function's ordinary execution, not a deployment guarantee. It rejects resolved paths outside its root before returning a page path. Source ingestion separately checks local files against wiki root unless allowed; HTTP honors the external-path override only from recognized localhost addresses. Required external contracts include trustworthy request peer identity and filesystem/process isolation; concurrent adversarial filesystem mutation was not assessed (SRC-1, `synthadoc/storage/wiki.py`, `synthadoc/agents/ingest_agent.py`, `synthadoc/integration/http_server.py`).

> page_path = self._root / f"{slug}.md"
> self._assert_in_root(page_path)
> return page_path
> --- `synthadoc/storage/wiki.py`

> if req.allow_external_paths and client_host in _LOCALHOST_ADDRS:
>     payload["allow_external_paths"] = True
> --- `synthadoc/integration/http_server.py`

Covered: reads/writes that obtain their target through `_page_path`, plus the separately checked ingest branch. Alternate: candidate `shutil.move`, configured shell hooks, dynamically imported skills and coding-agent subprocesses have other enforcement points or external contracts. Thus the current configuration/grant set is not established, and no system-wide sandbox is claimed. See [RT-RTE-candidate-admission](#rt-rte-candidate-admission), [RT-RTE-extension-loading](#rt-rte-extension-loading) and [RT-RTE-provider-delegation](#rt-rte-provider-delegation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- deployment conclusion status: uninspected

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-source-decision
Label: Source text and wiki purpose influence write proposals

Consumer: ingest analysis and decision model. Channel: sanitized/clipped extracted source, retrieved snippets and optional purpose injected into user prompt. Force: natural-language interpretation, followed by symbolic action dispatch that can persist text; not a trusted-code instruction boundary. Horizon: current compilation and, if its output is later consumed, later wiki invocations. Presence is wired; actual influence, malicious activation and beneficial dependence are unobserved. The source sanitizer's specific phrase patterns do not prove isolation of untrusted content (SRC-1, `synthadoc/agents/ingest_agent.py`, `synthadoc/core/sanitizer.py`; [RT-RTE-source-ingest](#rt-rte-source-ingest)).

> messages=[Message(role="user", content=decision_prompt.format(
>     pages=pages_str,
>     source_text=text,
>     entities=entities,
> ))],
> --- `synthadoc/agents/ingest_agent.py`

#### RT-BAP-workflow-guidance
Label: Fixed workflow method delivered to action model

Consumer: workflow model loop. Channel: system prompt plus protocol footer and tool-result reminders. Force: requested interpretation of steps and repair constraints; code separately grants callable access and gates some writes. Horizon: repeated turns of one workflow; shipped guidance can be supplied again in later invocations. No route here demonstrates rewriting that method based on its operational records (SRC-1, `synthadoc/agents/workflows/_loop.py`; [RT-OBJ-workflow-guidance](#rt-obj-workflow-guidance), [RT-RTE-workflow-loop](#rt-rte-workflow-loop)).

> system_prompt = system_prompt + _protocol_footer(tool_fns)
> --- `synthadoc/agents/workflows/_loop.py`

#### RT-BAP-extension-code
Label: Installed extension code has executable force

Consumer: Python interpreter or subprocess shell. Channel: imported skill module or configured hook command. Force: executable code with the process's available rights, not merely model advice. Horizon: installation/configuration lifetime and each triggered invocation. The installed grant set and deployed isolation remain unobserved. Evidence and minimum passages are retained in [RT-RTE-extension-loading](#rt-rte-extension-loading) (SRC-1, `synthadoc/agents/skill_agent.py`, `synthadoc/core/hooks.py`).

## Annotations

none
