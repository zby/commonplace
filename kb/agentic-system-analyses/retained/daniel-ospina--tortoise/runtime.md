---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Tortoise runtime baseline: session capture, model extraction, hosted admission and graph-to-prompt volunteering at the frozen revision."
run-id: AAS-2026-10-30-tortoise-0c919b4ca77d-01
reviewed-boundary: "54922a800f96858935b58ef250da569a4896df44"
---

# Tortoise runtime report

## Runtime account

Tortoise is a memory service with model-dependent writes and a deterministic context-delivery path, not the enclosing agent's action scheduler. This report retains the boundary's **complete artifact, partial loop** scope. All findings below use SRC-1 at the frozen revision. They describe implementation or attributed design, not observed executions. No target code, tests, providers or services were run. Loading, successful activation in a host model and benefit remain unobserved.

### Entry paths and ordinary work

The shipped server dispatcher starts stdio MCP by default, or a self-host HTTP daemon for `http`; the daemon passes a five-second graceful-shutdown setting to uvicorn (SRC-1, `tortoise/deployment.py`). Package/CLI, ingest and harness-facing paths are identified in [the boundary](boundary.md#boundary-and-evidence). They are not all interchangeable: the hosted MCP session-capture tool explicitly refuses self-hosted/stdio capture, whereas an in-process SDK has its own capture method (SRC-1, `tortoise/mcp_server.py`, `tortoise/sdk.py`). Running the MCP server does not imply every tool is available in every mode.

An ordinary inspected write is a fresh SDK `capture_session(conversation, session_id, harness=...)`, followed by a later framework callback using the same graph through `sdk_reflex`. The caller supplies role/content turns and optionally an identity; code rejects invalid session IDs before mutation, mints an absent ID, resolves the extraction provider and obtains the projection. The turn cap and empty stored-window gate precede session/turn writes. The shared writer persists a Session and deterministic turn Points; source materialization precedes extraction so derived Points can acquire a source-version anchor. The next-step owner is SDK code, not the model: code calls the selected extractor, writes returned entities/Points/operators, stamps provenance and invokes bounded promotion/calibration. The model supplies extraction proposals; it does not itself own graph I/O. The return is a structured receipt, not an answer to the original conversation. See [RT-RTE-session-capture](#rt-rte-session-capture).

The ordinary later read is a framework before-model callback. The adapter builds a bounded window, calls the SDK or HTTP reflex, takes only a nondegraded response's block, then mutates the host request. The canonical volunteering pipeline parses retrieval intent, searches a bounded graph pool, assembles confidence/why data, gates candidates, suppresses prior mentions and applies a pointer budget. ADK appends instructions where its mutator exists, with a user-content fallback; LangGraph returns a trailing HumanMessage by default; Semantic Kernel prepends the block to the rendered prompt after the remaining render pipeline. The host owns the subsequent model call and effects. Delivery is not evidence that the model obeyed or even used that memory. See [RT-RTE-context-delivery](#rt-rte-context-delivery) and [RT-BAP-framework-block](#rt-bap-framework-block).

### Four forcing cases and control coverage

1. **No provider versus extraction failure.** A missing provider does not prevent storing session turns. It yields no extracted memory Points and a `no-provider` receipt. A later v2 attempt may retry a failed/keyless capture; M2 is deliberately excluded from that retry rule. Therefore provider availability gates extraction, not capture or searchability. The alternate M2 lane uses `TORTOISE_SESSION_EXTRACTOR=m2`; its separate implementation was not fully traced, so v2-specific deduplication conclusions do not extend to it (SRC-1, `tortoise/sdk.py`; [RT-RTE-session-capture](#rt-rte-session-capture)).
2. **Hosted REST versus MCP versus local SDK.** REST requires write scope and reserves a capture slot; hosted MCP constructs the same SessionRequest and reserves a slot before calling the shared hosted implementation. The implementation checks recording policy, cap, empty transcript and quota. The SDK's local capture lacks that hosted auth/quota plane. Hosted recording-off is thus a policy on the hosted capture routes, not a repository-wide prohibition on all graph writes. Per-graph/org recording defaults and extraction-off are separate controls. See [RT-RTE-hosted-capture](#rt-rte-hosted-capture).
3. **`why=False`, silence and errors.** The volunteering path still assembles why blocks to obtain confidence before selection; `why=False` only omits why entries from the response. No retrieval intent returns clean silence without search. Invalid SDK input raises before graph work, and a miswired unbound search deliberately raises; retrieval/assembly failures within the guarded pipeline degrade to an empty block. The broad phrase “never raises” therefore does not cover every entry shape or initialization failure. HTTP catches additional failures but auth/validation can still reject. See [RT-RTE-context-delivery](#rt-rte-context-delivery).
4. **Fast read versus hard deadline.** Hosted HTTP uses `wait_for(to_thread(...))` with an eight-times-300-ms ceiling; the worker can continue after the await times out. The stricter completion-time 300-ms empty-response rule is opt-in. Direct SDK use has no equivalent outer HTTP ceiling; the Semantic Kernel adapter invokes its synchronous reflex on the event loop. Neither the source's latency objective nor HTTP timeout establishes universal sub-300-ms completion or worker cancellation (SRC-1, `tortoise/hosted_api.py`, `tortoise/framework.py`).

These cases challenge provider, policy, fail-open and latency generalizations. They are source traces, not experiments. Alternate direct writes and production commits are separately identified below; hook/daemon/store-sync, pack maintenance, rebuild and UI paths remain an inspection frontier, not proven equivalent routes.

### State, guarantees and effect boundaries

The retained graph combines natural-language content, symbolic IDs/kinds/edges/status and numerical embeddings/posteriors; these must not be treated as one representational form. The extraction model and local embedding model have different fixity properties ([RT-CMP-extraction-model](#rt-cmp-extraction-model), [RT-CMP-embedding-model](#rt-cmp-embedding-model)). Route records describe update and delivery authority, leaving detailed memory transformations and epistemic assessment to their specialists.

Load-bearing controls have limited owners and coverage:

| Guarantee | Owner and enforcement | Strength and scope | External contract / limit | Conclusion statuses |
|---|---|---|---|---|
| Empty capture writes nothing | SDK gate after stored-window transcript construction, before shared writer | invariant for this inspected SDK entry; hosted has a separate gate | Assumes transcript/window helpers implement their represented contract; does not cover arbitrary direct graph calls | implementation: wired; operation: uninspected |
| Hosted recording policy can refuse capture | shared hosted implementation before session writes | policy for hosted REST and hosted MCP capture | Requires correct authenticated org/graph resolution; local SDK has no such hosted policy plane | implementation: wired; operation: uninspected |
| Retrieval trouble should not break ordinary prompt work | pipeline try/except, HTTP degradation, framework `_safe_block` and callback catches | best effort, not universal no-throw | SDK projection initialization and input validation are outside pipeline error catch; Semantic Kernel's external `next` errors propagate | implementation: wired; operation: uninspected |
| State can be reconstructed from events | configured journal and optional record seam | best effort, not an all-writes durability invariant | JSONL configuration, filesystem availability, graph and Postgres operation are external requirements; independently failing stores and journal-less paths exist | implementation: wired; operation: uninspected |

Persistence is not one atomic transaction across stores. `_emit_event` has a graph feed branch, a configured JSONL branch and a subsequent optional record write. It returns `None` with no meaningful record or no journal, `False` on configured append failure and `True` on successful append; a supplied record sink receives a separate outcome. Capture turn writers can use that distinction. The emitter's best-effort contract is not a claim that every higher-level mutation disregards journal failure. Some callers journal before folding; this report does not infer all write ordering from the emitter alone. See [RT-OBJ-event-emission](#rt-obj-event-emission).

Capability surface and deployed grant set differ. The package can read/write a graph, transmit conversations to a model provider and send commits to a Tortoise endpoint. Hosted scope checks and recording/quota policy grant or refuse particular requests. An embedded SDK's possession of a projection is not evidence of equivalent hosted authorization. Database isolation, provider retention, container isolation, actual granted credentials and deployed resource limits are not established by source wiring. No general shell/subprocess sandbox or host-agent tool-approval guarantee is inferred from this memory-service boundary.

### Change admission and remaining coverage

Session extraction is automatic content admission after entry-policy checks, not per-item human approval. The caller triggers capture; model/code propose retained memory; code validates/writes and attempts promotion. Hosted recording/extraction settings can veto stages, not review individual propositions. `commit_session` is a distinct production-commit route, with a consent predicate before extraction, alternate v1/v2 dispatch and API/provider credential separation ([RT-RTE-production-commit](#rt-rte-production-commit)). Direct `create_point` is another admission door, with its own kind/namespace/shape checks, not proof of extracted provenance or human endorsement ([RT-RTE-direct-point](#rt-rte-direct-point)).

Additional inspection beyond the boundary's initial scope covered the implementations cited here: volunteering's entire canonical pipeline; framework block providers/window builder and three injection adapters; SDK capture entry, replay and extractor dispatch, selected write/promotion/emission seams; hosted capture admission and context deadline branches; MCP capture bridge; model/embedding initialization and the extractor backend gate. These supply implementation evidence only. Unread internal branches are not counted as verified by their docstrings.

The repository's other shipped hook/plugins, spool/store-sync recovery, pack installation and maintenance, dream/rebuild/backup, hosted deletion and UI writers, ingest variants, evaluator drivers and production deployment admission have not been traced end-to-end here. Their availability prevents any evidenced-absence or whole-system coverage claim. This report establishes selected consequential routes, not every mechanism that changes knowledge, capabilities or machinery. It does not establish an automatic product-code/weight improvement loop. Neither an absent such loop nor successful learning follows from that inspection limit.

## Shared records

### Components

#### RT-CMP-extraction-model
Label: Configured session extraction model

Source-native identity: `_model_adapter` / model `complete`, default model string `deepseek/deepseek-v4-flash`, with `TORTOISE_EXTRACT_MODEL` override and direct/aggregator routing (SRC-1, `tortoise/sdk.py`, `tortoise/model_adapters.py`). Representational form: distributed-parametric model; provider-side weights, not stored in this repository or graph. Its input/output text is a separate natural-language/structured interface. The inspected client sends system/user messages and generation settings; it exposes no parameter-training step on this route. Parameter mutation inside the remote service is uninspected. Exact weights/version are not pinned by the default model alias; a mutable endpoint can resolve to a different provider implementation/model revision. Routing/failover further prevents equating the configured alias with an immutable weight identity. The offline mock is a separate seam, not evidence of real inference.

> model = (_model_adapter(configured) if configured
>                      else _model_adapter("deepseek/deepseek-v4-flash",
>                                          max_tokens=None, temperature=0.0))
> --- `tortoise/sdk.py`

> "messages": [
>                 {"role": "system", "content": system},
>                 {"role": "user", "content": user},
>             ],
> --- `tortoise/model_adapters.py:125-128`

#### RT-CMP-embedding-model
Label: Local BGE embedding model

Source-native identity: `EmbeddingModel`, `BAAI/bge-small-en-v1.5`; distributed-parametric encoder loaded into local process memory from external model storage. The configured model revision is pinned; this is not a mutable hosted-model alias. Runtime rebinding of identity constants or replacement/injected model machinery would be a different configuration, not proof that the default floats. The inspected load/encode path does not train parameters; external model internals/training provenance remain uninspected. Encoded numerical vectors are stored as graph/journal data, not weight changes (SRC-1, `tortoise/embeddings.py`, `tortoise/sdk.py`).

> EMBEDDING_MODEL_REVISION = "5c38ec7c405ec4b44b94cc5a9bb96e735b38267a"
> --- `tortoise/embeddings.py`

> result["model"] = SentenceTransformer(
>                     EMBEDDING_MODEL, revision=EMBEDDING_MODEL_REVISION)
> --- `tortoise/embeddings.py`

### Operative objects

#### RT-OBJ-event-emission
Label: SDK event emission surfaces

Source-native identity: `_emit_event` event envelopes. Symbolic records contain natural-language content snapshots and possibly numerical vectors as distinct fields; substrates are graph event storage, optional JSONL journal and optional Postgres record projection. They are not one atomic durable object. This container records runtime emission semantics, not complete replay/memory semantics (SRC-1, `tortoise/sdk.py`). Graph feed failures record degraded state where possible; append failures log/count and return false. No configured journal returns none before the record-projection branch. Successful JSONL append is followed by the record-write attempt, with an independent sink outcome.

> if point is None and id is None:
>             return None  # nothing meaningful to log
>         log = self._get_event_log()
>         if log is None:
> --- `tortoise/sdk.py`

> if record_sink is not None:
>             # #10000: the outcome travels to the caller that has to decide
>             # whether the record holds this write (`_write_capture_turns`).
>             record_sink.append(self._write_record_projection(event, seq=seq))
>         else:
>             self._write_record_projection(event, seq=seq)
>         return True
> --- `tortoise/sdk.py`

### Routes

#### RT-RTE-session-capture
Label: SDK session capture and v2 extraction

Owner/endpoints: caller → `TortoiseSDK.capture_session` → shared session/turn writer → selected extractor → SDK graph writers → capture receipt (SRC-1, `tortoise/sdk.py`, `tortoise/extractor_v2.py`). Code owns progression. User/agent conversation content is input, not a human per-proposition admission decision. Operating mode is open session capture, not an answer-labelled curriculum; no expected-answer oracle is used on this route. The model proposes entities/claims/operators; code emits effects into the projection. A fresh keyed request defaults to v2 S1 story, S2 mapping, S3 graph search, S4 gap review, S5 payload execution. Embedded-backend S3 is deliberately skipped, even if an environment label says hosted; a real resolvable SDK backend wins over that label.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: structured session receipt with extraction mode, counts, points, errors/warnings and additive write metadata; not a final task answer.
- Later read-back: session turns and admitted claims are available to graph retrieval and later context delivery; exact memory selection is separate from successful storage.
- Delegated visibility: model adapter receives a bounded/redacted conversation for extraction; graph-search results enter v2 review. No enclosing agent's full context is delegated by this SDK call.
- Selection predicate: fresh sessions extract when a provider exists; successful/legacy existing sessions replay; failed sessions retry only for recorded retryable lanes and a current non-M2 configuration.
- Invalidation or expiry: same-session re-capture can change stored turns even when extraction replays; v2 supersession application is best-effort, not a transactional replacement of all session-derived knowledge. No universal expiry follows.
- Activation or effect: code writes Session/turns, then entities/Points/operators, provenance and bounded promotion/calibration; later behavioral use is unobserved.
- Evidence limits: selected capture and v2 interfaces traced; M2 internal emission, all concurrent races, full link/supersession and replay consumers not exhaustively traced; no execution evidence.

Admission trigger is caller capture. Guidance comes from extractor prompts/master vocabulary and the supplied transcript; the output persists as graph data, not a changed model. Entry validation can reject the request; extraction errors/warnings survive into the receipt. Storage can precede extraction failure, and best-effort provenance/calibration can leave incomplete effects. Retry is conditional recovery, not rollback of all prior writes. In particular a successful capture with a nonfatal provenance gap may replay without healing it. No per-content human approval is inserted between model proposal and graph write.

> if no_provider:
> --- `tortoise/sdk.py:12245-12334`

> "mode": _CAPTURE_NO_PROVIDER_MODE,
> --- `tortoise/sdk.py:12245-12334`

> elif os.environ.get("TORTOISE_SESSION_EXTRACTOR") == "m2":
>             extracted, meta = self._extract_session_llm(
>                 extraction, session_id, now)
>         else:
>             extracted, meta = self._extract_session_v2(
>                 extraction, session_id, now)
> --- `tortoise/sdk.py`

> embedded = _sdk_backend_is_embedded(sdk)
>     if embedded is not None:
>         return not embedded
>     return mode in ("real", "hosted")
> --- `tortoise/extractor_v2.py`

> out = extract_session_v2(model, _redact_turn_contents(conversation)[0],
>                                  sdk=self,
>                                  session_id=session_id, master=master)
> --- `tortoise/sdk.py`

#### RT-RTE-hosted-capture
Label: Hosted REST and MCP capture admission

Owner/endpoints: authenticated request → REST handler or hosted MCP bridge → slot reservation → `_capture_session_impl` → tenant SDK/state writes → receipt. REST begins with write-scope enforcement; the shared implementation receives a resolved org, checks recording policy before writes, and resolves extraction configuration independently (SRC-1, `tortoise/hosted_api.py`, `tortoise/mcp_server.py`). The bridge carries graph/actor/limit context and validates via SessionRequest. Host identity is supplied through server resolution, but harness attribution is a caller declaration/first stored value, not verified runtime provenance.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: hosted receipt or explicit validation/policy/quota/capacity/in-flight rejection; MCP maps invalid body construction to a 422-equivalent error.
- Later read-back: captured state enters the resolved data graph and hosted receipt/error bookkeeping; detailed dashboard consumption is uninspected.
- Delegated visibility: shared implementation receives org/graph context; model extraction sees transformed conversation, not proof of a verified harness identity.
- Selection predicate: authenticated/authorized route, available reservation, recording enabled, bounded nonempty transcript and applicable quota; missing model key is not a storage gate.
- Invalidation or expiry: slot released in finally; REST cancellation attempts an abandoned-capture marker while holding the key until marker work lands. This is recovery bookkeeping, not automatic deletion of partial data.
- Activation or effect: permits or refuses hosted capture and records partial/success outcomes; extraction-disabled can store without model extraction.
- Evidence limits: auth resolvers, every gate helper and marker worker not audited end-to-end; MCP cancellation handler is documented defensive under current sync dispatch, not demonstrated reachable cancellation.

Operating mode is open capture. Caller supplies conversation; model/code propose/admit memory, with recording/extraction settings and request gates as vetoes. No per-item expected-answer oracle or per-item human review appears in the inspected dispatch. Policy is default-on opt-out, not affirmative content consent. This guarantee covers these capture routes, not direct SDK writes or all import/commit surfaces. Recovery uses conditional retries/markers, not a cross-store rollback.

> _require_scope(org, "graphs:write", "capture_session")
> --- `tortoise/hosted_api.py`

> recording_ok, rec_layer, _onboard_state = (
>         await _session_recording_allowed_off_loop(org))
>     if not recording_ok:
> --- `tortoise/hosted_api.py`

> slot = _reserve_capture_slot(_capture_session_key(org, session_id))
> --- `tortoise/mcp_server.py`

> return asyncio.run(_capture_session_impl(body, None, org,
>                                                      slot=slot,
>                                                      state=_state))
> --- `tortoise/mcp_server.py`

#### RT-RTE-context-delivery
Label: Volunteering graph content into framework prompts

Owner/endpoints: framework callback → bounded window → SDK/HTTP reflex → `run_volunteer_pipeline` → selected pointer block → host request mutation (SRC-1, `tortoise/framework.py`, `tortoise/volunteer.py`, `tortoise/sdk.py`, `tortoise/hosted_api.py`). Code chooses retrieval intent, pool sizes, confidence gate and ordering; model/human judgment is not the immediate selector. Natural-language snippets/pointers are the delivered form; symbolic IDs and numerical confidence control selection. The operating mode is a current request with prior context, not an evaluation answer oracle.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: pointers, optional why entries, surfaced bands, markdown block and degradation reason; framework consumers reduce this to a string/message mutation.
- Later read-back: this route reads previously retained graph material; it performs no canonical pipeline graph write. Re-mention continuity is supplied by prior_context rather than persisted per-call session state.
- Delegated visibility: framework sends a filtered bounded window to the reflex; host receives selected snippets rather than the full graph or all retrieved candidates.
- Selection predicate: retrieval intent then bounded current-view search; optional supersession arm when live pool is small; confidence/contentiousness gate, prior-mention suppression, live-first/confidence-first ordering and max_pointers cap.
- Invalidation or expiry: current-view excludes terminal states; alternate superseded arm can deliberately surface flagged predecessors. Prior mention is suppression, not deletion; explicit re-asks may re-fire.
- Activation or effect: ADK instruction append/user fallback, LangGraph appended message, or Semantic Kernel rendered-prompt prepend; compliance and downstream decisions remain unobserved.
- Evidence limits: provider/database ranking and full why assembly internals not audited here; no observed delivery, latency or benefit; unsupported raw SDK shapes may raise.

Working-context control is code-driven selection and tail retention, not a subagent frame. Framework window building drops older turns first, keeps the end of an oversized turn and rejects noncanonical roles/empty content. This bounds the reflex's view, not the enclosing model's entire window. Callback output is appended/prepended without evicting the host's original conversation. Pointers identify externally retrievable material, but are not automatically dereferenced language-model memory addresses. `why=False` does not remove the confidence-read stage: it only prevents response why entries after selection.

The HTTP deadline guards the await, not the continued worker. Fail-open content is a best-effort runtime property; validation is intentionally fail-closed, and external Semantic Kernel `next` failures propagate. The error-to-empty adapter avoids turning retrieval failures into ordinary host-turn failures, while potentially making absence of memory unobtrusive.

> blocks = assemble_why_blocks(proj, order)
> --- `tortoise/volunteer.py`

> if why:
>                 why_entries.append(_assemble_entry(cand["block"]))
> --- `tortoise/volunteer.py`

> except _UnboundSearchError:
>         # A miswired transport (no SDK-bound search) must fail LOUDLY, never
>         # degrade quietly — a programming error the operator should see.
>         raise
> --- `tortoise/volunteer.py`

> timeout=SLO_MS * 8 / 1000.0,
> --- `tortoise/hosted_api.py:30440-30544`

> if (result.get("degraded_reason") is None and enforce_slo
>             and elapsed_ms > SLO_MS):
> --- `tortoise/hosted_api.py`

#### RT-RTE-production-commit
Label: SDK production session commit door

Owner/endpoints: caller → `commit_session` → consent check → v1/v2 dispatch → production commit response. This is distinct from local `capture_session`: source documents a Layer-1 payload POST and endpoint-unreachable local payload return (SRC-1, `tortoise/sdk.py`). Only the entry and selection contract, not the entire remote commit consumer, were traced here.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: early structured refusal, selected commit method result, or documented local result/payload when endpoint unreachable; local payload availability alone does not establish remote admission.
- Later read-back: uninspected — remote commit storage and consumer paths not traced end-to-end here.
- Delegated visibility: extraction provider and Tortoise commit endpoint have different credentials; API base_url/api_key do not select the model provider.
- Selection predicate: raw session ID validation and consent refusal first; supplied summary selects v1, otherwise explicit/env extractor selects v1 or default v2.
- Invalidation or expiry: extractor selector is reversible; this is not a rollback of already committed graph changes.
- Activation or effect: permits extraction/commit dispatch after consent; full remote application is outside this route's demonstrated coverage.
- Evidence limits: downstream validation/POST behavior beyond entry documentation not independently established here; no all-surfaces consent guarantee.

Trigger is caller commit; proposal guidance is extraction input/model or a supplied v1 summary. Entry code can refuse before provider egress; caller-supplied summary can bypass generation, not prove bypass of downstream validation. Caller identity alone does not establish human authorship or per-content approval. Open session processing has no established expected-answer oracle. Persisted knowledge, recovery after remote failure and remote rejection details require the commit consumer trace; no product-code or weight update is inferred.

> declined = capture_declined_reason()
>         if declined is not None:
> --- `tortoise/sdk.py:11419-11518`

> return {"session_id": session_id, "ok": False,
>                     "errors": [declined], "error": declined,
>                     "payload": None}
> --- `tortoise/sdk.py`

#### RT-RTE-direct-point
Label: Direct Point admission door

Owner/endpoints: SDK caller, including extraction → `create_point` → graph mutation/receipt. Natural-language content plus symbolic kinds/props are supplied directly; numerical priors/vectors are separate downstream parts. This door does not require that every proposition was extracted from a session (SRC-1, `tortoise/sdk.py`). Inspection establishes input gating and the documented admission posture, not every mutation/replay branch.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Point write result or validation exception; source/provenance advisories are not equivalent to rejection.
- Later read-back: admitted Points become graph-query candidates subject to reader filters; exact later selection is not guaranteed by creation.
- Delegated visibility: inapplicable — this door itself is a caller-to-store operation, not a model delegation.
- Selection predicate: invisible-kind refusal, namespace approval checks over positional and coerced props, content string validation; source describes default live status unless explicit draft.
- Invalidation or expiry: explicit status and later update/retraction routes affect eligibility; those routes are not completely traced here.
- Activation or effect: admits caller content to graph state; direct creation is not proof of a human decision or empirically warranted proposition.
- Evidence limits: full write transaction, dedup and later update paths uninspected; default/advisory semantics attributed to the method contract, not a demonstrated live run.

Trigger/proposal is supplied kind/content/props. Computational gates can veto malformed/unapproved kinds; a mismatch advisory is deliberately nonblocking. Source describes a no-source advisory after admission rather than a universal provenance gate. Human contribution is unresolved for a generic caller. This is open content admission with no expected-answer oracle. Persistence/recovery depends on the actual writer path and configured stores, not the label “live.”

> self._refuse_unapproved_kind("pointKind", kind)
>         _coerce_props(props)
> --- `tortoise/sdk.py`

> self._refuse_unapproved_kinds_in_props(props)
> --- `tortoise/sdk.py:10204-10298`

> if not isinstance(content, str):
>             raise TypeError(
>                 "create_point: content must be a str, got "
>                 f"{type(content).__name__} — `content` is required and "
>                 "cannot be None (every write path hashes it)"
>             )
> --- `tortoise/sdk.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-framework-block
Label: Retrieved block as host model input

Consumer: host framework's forthcoming model invocation. Channel: instruction append where ADK supports it, ADK user-content fallback, default LangGraph HumanMessage, or Semantic Kernel rendered prompt. Force: natural-language advisory/context through model interpretation, not a runtime-enforced action prohibition. Horizon: forthcoming invocation and whatever host persistence carries forward; cross-session host retention is uninspected. This path makes retained graph content capable of influencing work without proving activation or correctness. It is distinct from admission authority at graph writes (SRC-1, `tortoise/framework.py`; [RT-RTE-context-delivery](#rt-rte-context-delivery)).

> append([block])
>         return
> --- `tortoise/framework.py`

> make = message_factory or _langchain_human_message
>             return {"messages": [make(block)]}
> --- `tortoise/framework.py`

> if block:
>                 context.rendered_prompt = f"{block}\n\n{rendered}"
> --- `tortoise/framework.py`

## Annotations

none
