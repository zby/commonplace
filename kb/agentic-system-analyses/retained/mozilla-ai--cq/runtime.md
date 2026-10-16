---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "CQ runtime baseline: host-led knowledge use, MCP and CLI routes, local fallback, remote review, and optional embedding retrieval."
run-id: AAS-2026-10-14-cq-8fb3dc41c334-01
reviewed-boundary: "5765494a3840e5f5a7223c42101f41e85cb9d898"
---

# CQ runtime report

## Runtime account

### Work and ownership

CQ supplies structured advice and knowledge-sharing operations to an external agent. It does not own that agent's next application action, model invocation, session history, shell permissions or approval interface. Its shipped skill requests a query–verify–apply–confirm/flag loop and mid-task proposals. Its reflection command requests retrospective candidate extraction by the foreground agent. The MCP implementation registers query, propose, confirm, flag and status, not a reflection-model endpoint. The Python default reflector returns a guidance message rather than extracted candidates. These are inspected implementation and requested behavior, not evidence of actual agent compliance. SRC-1: `sdk/go/prompts/SKILL.md`, `sdk/go/prompts/reflect.md`, `cli/mcpserver/server.go`, `sdk/python/src/cq/reflect.py`; [RT-RTE-session-reflection](#rt-rte-session-reflection).

> Reflection is agent-led — there is no MCP tool for this step. Using your own reasoning, scan the session for insights worth sharing.
> --- `sdk/go/prompts/reflect.md`

The decision policy has two distinct forms. Natural-language skill and command instructions guide the host model; compiled Go/Python and SQL rules select, serialize, validate and persist knowledge. Optional dense embeddings affect server retrieval, not candidate authorship. The external host model and embedding provider have different responsibilities and fixity limits: [RT-CMP-host-model](#rt-cmp-host-model), [RT-CMP-token-embedding](#rt-cmp-token-embedding). Retrieved action text has advisory rather than code-enforced authority: [RT-BAP-knowledge-guidance](#rt-bap-knowledge-guidance).

### Ordinary shipped invocation

The plugin manifest points its MCP server to the `cq` executable with `mcp` as its argument and distributes commands and skills. The CLI builds a Go client using resolved remote address, API key, database path and timeout. SQLite is the default local store; an injected Store takes priority over a database URL, which takes priority over the database path. CLI timeout defaults to 30 seconds, versus the SDK's five-second default. MCP starts an optional background drain and then serves stdio. The foreground host supplies the query tags, accepts the tool result and decides the next application action. CQ coordinates a local store and optional HTTP service, not an agent delegation tree. SRC-1: `plugins/cq/.claude-plugin/plugin.json`, `cli/main.go`, `cli/cmd/cli.go`, `cli/cmd/mcp.go`, `sdk/go/client.go`, `sdk/go/options.go`.

A task beginning in unfamiliar territory is the skill's trigger. The agent calls query with domains and optional language/framework/pattern context. The MCP handler requires a nonempty domain array and bounds the result limit to 50. The Go client reads its local store, then requests remote units when configured. SQLite unions domain-index candidates and full-text candidates, ranks them by relevance times confidence and truncates. The server's ordinary SQL path selects approved, domain-matching units and ranks them by relevance times confidence with an ID tie-break. The Go client merges local first, deduplicates by ID with local winning and truncates without a global cross-store rerank. Local candidates can therefore displace every remote candidate at a small limit. The return is serialized knowledge-unit JSON as MCP text; the agent is requested to inspect action/detail and verify guidance before reliance. SRC-1: `cli/mcpserver/query.go`, `sdk/go/store_sqlite.go`, `sdk/go/scoring.go`, `sdk/go/client.go`, `server/backend/src/cq_server/repositories/knowledge.py`, `server/backend/src/cq_server/repositories/_queries.py`; [RT-RTE-knowledge-query](#rt-rte-knowledge-query).

The invocation terminates at a tool result, not a completed application task. Confirmation or supported flagging is another host-selected invocation that changes scores/flags, not proof of the earlier advice's correctness. Stale/incorrect flags can persist locally and remotely; Go-local duplicate flags can retain a reference. Python Client duplicate flags and server duplicate flags instead fail validation before the evidence update, so duplicate objection persistence is not universal. A stabilized insight takes the separate proposal route; the API creates retained content and a later query can reload it. Remote review adds another principal and invocation between creation and ordinary remote retrieval. SRC-1: `sdk/go/client.go`, `sdk/go/prompts/SKILL.md`, `server/backend/src/cq_server/services/knowledge.py`, `server/backend/src/cq_server/services/reviews.py`; [RT-RTE-knowledge-proposal](#rt-rte-knowledge-proposal), [RT-RTE-knowledge-feedback](#rt-rte-knowledge-feedback), [RT-RTE-remote-review](#rt-rte-remote-review).

### Alternate and forcing routes

Four source-level forcing cases challenge broad guarantees. None was executed.

1. **A proposal without a human approval token.** The skill requires interactive approval but the MCP handler accepts content fields directly and the Go/Python clients expose direct proposal APIs. The remote route checks an API key, not evidence of content approval or a VIBE√ result. Headless instructions explicitly permit clean or appropriately caveated proposals without a user. Human approval is consequently a prompt-level policy for interactive use, not a system-wide enforced prerequisite. SRC-1: `sdk/go/prompts/SKILL.md`, `cli/mcpserver/propose.go`, `sdk/go/client.go`, `sdk/python/src/cq/client.py`, `server/backend/src/cq_server/api/routes/knowledge.py`; [RT-CLM-proposal-approval](#rt-clm-proposal-approval).
2. **A remote outage or authentication rejection.** Go proposals fall back to local persistence for transport/server failures and 401/403; other client rejections do not persist. Python has that fallback for per-call HTTP failures after destination resolution, but its resolver turns exhausted transport/discovery-server failures into DiscoveryError. That exception propagates past propose's RemoteError/HTTPError catches and aborts before local insertion. Consequently an outage during Python discovery need not retain advice. SRC-1: `sdk/python/src/cq/discovery/_resolver.py`, `sdk/python/src/cq/client.py`; [RT-RTE-knowledge-proposal](#rt-rte-knowledge-proposal). A local proposal is queryable without remote review. MCP startup can later drain it automatically; successful posting deletes its local copy, although the remote replacement is still subject to review. The server assigns a new unit identity because the remote proposal payload carries no client ID. This is transfer-and-delete, not replication of one globally stable object. Lost acknowledgements can yield duplicate remote proposals; a 2xx response with malformed JSON is treated by Go as success to avoid resending. That fallback returns the client-side ID with server-assigned fields cleared, not a verified server identity. SRC-1: `sdk/go/client.go`, `sdk/go/remote.go`, `sdk/python/src/cq/client.py`, `cli/cmd/mcp.go`, `server/backend/src/cq_server/services/knowledge.py`; [RT-RTE-local-drain](#rt-rte-local-drain).
3. **Direct server calls versus a human browser review.** Public knowledge GET has no authentication dependency and filters by review status, not owner or tier. A PRIVATE unit becomes reachable through that path after approval. JWT-authenticated review endpoints require a current-user token, but the inspected dependency does not require a reviewer role. The shipped seed driver itself proposes, approves and adjusts confidence through APIs. Thus the SQL approved-only predicate does not establish private-tier isolation, human-only approval or independent validation. The service checks pending before writing, but its separate reads and unconditional status update do not establish an atomic single-winner transition under concurrent reviewers. SRC-1: `server/backend/src/cq_server/api/routes/knowledge.py`, `server/backend/src/cq_server/api/routes/review.py`, `server/backend/src/cq_server/api/deps.py`, `server/backend/src/cq_server/repositories/_queries.py`, `server/backend/src/cq_server/services/reviews.py`, `server/backend/src/cq_server/repositories/reviews.py`, `server/scripts/seed-kus.py`; [RT-CLM-approved-query](#rt-clm-approved-query).
4. **Optional semantic retrieval failure.** The semantic SQL also selects approved, domain-matching units, but limits nearest-vector candidates before relevance/confidence reranking. Its provider call sends query domain words or concatenated insight text to a configured `/predict` endpoint. `combined_query` wraps provider errors in generic RuntimeError, whereas the repository catches EmbeddingServiceError for SQL fallback. Therefore the apparent embedding-failure fallback is not established for errors wrapped by this route. Semantic insert/update needs an embedding before the combined database transaction; unavailable embeddings can prevent writes too. PostgreSQL with semantic search enabled is rejected at database construction. SRC-1: `server/backend/src/cq_server/semsearch/queries.py`, `server/backend/src/cq_server/semsearch/__init__.py`, `server/backend/src/cq_server/repositories/knowledge.py`, `server/backend/src/cq_server/core/db.py`; [RT-RTE-knowledge-query](#rt-rte-knowledge-query).

The shell alternate is shipped, not hypothetical: the Pi installer maps every CQ action to CLI invocations. CLI query preserves warnings on stderr; MCP query serializes only `result.Units`, dropping the client's nonfatal warning/source metadata. Remote failure may thus look like a successful local-only result to the MCP consumer, unlike the CLI consumer. Go's SourceRemote label also marks configuration rather than proving a successful remote response. Direct SDK calls return the richer result. Python query returns a source indicator and warnings but does not share Go's 50-result client clamp in its inspected query method; Python local confirmation and stale/incorrect flagging also attempt remote forwarding, whereas Go local feedback only updates local state. Python Client has no duplicate-reference argument, so duplicate flagging fails before its local update; remote duplicate flags fail in the server regardless of whether the Go caller sent a reference. Store injection changes candidate selection and storage under the Store interface contract. These alternatives prevent a blanket claim of identical behavior across all surfaces. SRC-1: `cli/internal/install/pi.go`, `cli/cmd/query.go`, `cli/mcpserver/query.go`, `sdk/go/client.go`, `sdk/go/store.go`, `sdk/python/src/cq/client.py`.

### Controls, change admission and limits

Capability surface is five MCP tools plus CLI/SDK operations, installer/hook wiring and remote review APIs. A configured API key grants server mutation access in the inspected routes; an actual deployed key/grant set is not supplied. API-key authentication uses active-key lookup and HMAC comparison; query is public. JWT is the review authentication channel. These checks authenticate a principal, not the truth of advice or whether a human made the call. Local operation uses the process's database/file access, with no equivalent server key requirement. SRC-1: `cli/mcpserver/server.go`, `server/backend/src/cq_server/api/deps.py`, `server/backend/src/cq_server/services/api_keys.py`, `server/backend/src/cq_server/repositories/_queries.py`, `sdk/go/client.go`.

The deployed isolation envelope remains unobserved. The supplied Compose file exposes a port and durable volume and mounts maintenance scripts read-only; it is deployment configuration, not proof of sandboxing or host tool confinement. External agent shell/model/provider paths are not mediated by CQ. CQ's `extensions` proposal field stores namespaced data, not executable plugin loading; its optional SQLite vector extension executes dependency code during database connection setup. Custom stores execute caller-supplied implementation code. No inspected control point restricts the external host's alternative tools. SRC-1: `docker-compose.yml`, `cli/mcpserver/propose.go`, `sdk/go/options.go`, `sdk/go/store.go`, `server/backend/src/cq_server/semsearch/__init__.py`.

Changes to retained knowledge pass through proposal, score feedback and server review routes below. The runtime leaves detailed memory lineage, revisions and curation to the memory member. Static instructions/capabilities change through operator installation of packaged prompts and host configuration, not an inspected model-written self-patching loop: [RT-RTE-host-installation](#rt-rte-host-installation). Production storage changes through shipped database migrations and operator maintenance scripts. The baseline supplies schema creation/downgrade; backup uses container SQLite `.backup` and copies the result outside the container. These are explicit operator/programmer mechanisms, not agent improvement admission. Source inspection supports their existence, not a successful backup, deployment, schema migration or rollback. SRC-1: `cli/internal/install/pi.go`, `cli/internal/install/files.go`, `server/backend/alembic/versions/0001_baseline.py`, `server/scripts/backup-db.sh`.

Working-context selection consists here of requested retrieval, a requested compact reflection summary and an automatic bounded Cursor failure reminder. Reflection says to omit routine edits and already documented events; it does not implement host compaction or remove old turns. The Cursor hook stores the latest bounded failure per conversation and surfaces then clears it at stop. A session-start sweep expires old failure files. This is selective external read-back, not isolation in a separate sub-agent frame. Host context windows, eviction and delegation stay opaque; no host execution evidence is supplied. SRC-1: `sdk/go/prompts/reflect.md`, `cli/internal/hook/cursor.go`; [RT-RTE-failure-reminder](#rt-rte-failure-reminder).

Correction coverage under SRC-1 additionally inspects Python discovery retry/error conversion and destination resolution, Python Flag construction and scoring, server FlagRequest/service admission, and Go local/remote flag payloads. These are implementation evidence, not observed successful or failed operations. Additional coverage under the existing SRC-1 register includes direct inspection of MCP query/propose handlers, CLI query, Go validation/scoring/store contracts and remote payloads, Python query/proposal/feedback, API dependencies/key authentication, review endpoints and repository writes, baseline migration, semantic query/index code, installer manifests/file ownership, and browser review/seed/backup drivers at the paths cited above. These add implementation evidence, not a new source. Prompts add doctrine/design. No tests, examples, model calls or target services were run. Operation, activation and benefit remain unobserved throughout. Uninspected host adapters, discovery/cache behavior beyond the inspected Python failure chain, other maintenance drivers and custom-store/provider internals prevent exhaustive route equivalence, deployment safety and performance conclusions; they do not erase the inspected shipped routes.

## Shared records

### Components

#### RT-CMP-host-model
Label: Consuming host model

Source-native identity: the agent using the CQ skill and reflection command. Its decision machinery is distributed-parametric, with parameters on an external opaque provider/runtime substrate. CQ supplies natural-language input; provider weights and session execution are outside the frozen repository. Parameter changes during operation are uninspected; no exact host model version is pinned by these prompts; whether its endpoint resolves to another model is uninspected because no host provider configuration was supplied. SRC-1: `sdk/go/prompts/SKILL.md`, `sdk/go/prompts/reflect.md`.

> Using your own reasoning, scan the session for insights worth sharing.
> --- `sdk/go/prompts/reflect.md`

This component owns candidate reasoning and advice interpretation, not CQ's SQL policy. Neither requested reflection nor this model's opacity proves exercised learning.

#### RT-CMP-token-embedding
Label: Token embedding service

Source-native identity: `_TOKEN_EMBEDDING_URL`, configured from TOKEN_EMBEDDING_URL. Distributed-parametric embedding production uses external opaque model parameters; its numeric outputs become float32 blobs in SQLite's knowledge_units_vec table. Whether parameters change during operation is uninspected. An exact model version is not pinned by the inspected request; the configurable endpoint can resolve to different external machinery. Provider implementation, initial embedding provenance, quality and model mutability are not supplied. SRC-1: `server/backend/src/cq_server/semsearch/__init__.py`, `server/backend/src/cq_server/semsearch/queries.py`.

> response = await client.post("/predict", json=request_data)
> --- `server/backend/src/cq_server/semsearch/queries.py`

Optional activation depends on URL and installed dependencies. Query words and combined insight text are model inputs; CQ computes an average vector and serializes it, but does not train this provider in the inspected path.

### Operative objects

#### RT-OBJ-skill
Label: CQ skill instructions

Source-native identity: SKILL.md embedded/distributed with the SDK and host installations. The operative body is natural-language guidance interpreted by the host agent; it is stored as shipped Markdown and installed files. YAML metadata supports host discovery but does not enforce the body's approval policy. SRC-1: `sdk/go/prompts/SKILL.md`, `cli/internal/install/pi.go`, `plugins/cq/.claude-plugin/plugin.json`.

> Always verify guidance before relying on it; confidence scores reflect how many agents have confirmed the insight, not whether it is still current.
> --- `sdk/go/prompts/SKILL.md`

#### RT-OBJ-failure-record
Label: Cursor failure record

Source-native identity: failureRecord, keyed by sanitized conversation ID or a session sentinel. Symbolic JSON fields are mechanically selected, rendered and deleted; their input/error string payloads are natural-language text for the later host reader. Substrate is a per-conversation `-failure.json` file. Input and error are each bounded to 200 runes plus an ellipsis; writes replace the previous record. This is auxiliary event state, not a proposed knowledge unit. SRC-1: `cli/internal/hook/cursor.go`.

> data, err := json.Marshal(failureRecord{
> ToolName: p.ToolName,
> Input: formatToolInput(p.ToolName, p.ToolInput),
> Error: truncate(p.ErrorMessage, maxSnippetLength),
> })
> --- `cli/internal/hook/cursor.go`

### Routes

#### RT-RTE-knowledge-query
Label: Knowledge query and delivery

Owner/endpoints: host agent or direct caller → MCP/CLI/SDK → local Store and optional remote knowledge API → caller. Fixed symbolic selectors/rankers operate on stored fields; the host interprets delivered natural-language insight text. Optional embeddings add the component above, not a new candidate-writing model. CQ owns retrieval and transport; the host owns application decisions. SRC-1: `cli/mcpserver/query.go`, `cli/cmd/query.go`, `sdk/go/client.go`, `sdk/go/store_sqlite.go`, `server/backend/src/cq_server/repositories/knowledge.py`, `server/backend/src/cq_server/semsearch/queries.py`.

- Immediate return: selected units; direct SDK additionally returns warnings/source, CLI emits warnings, MCP omits those nonfatal fields.
- Later read-back: persisted proposals and updated evidence fields reach subsequent queries; no persistence of the query itself is established here.
- Delegated visibility: configured remote service receives query tags/context; MCP/CLI returns selected units to the invoking host, not automatically to a separate worker.
- Selection predicate: local SQLite domain OR full-text candidates, then relevance × confidence; ordinary server domain overlap AND approved status, then relevance × confidence; optional semantic path preselects nearest vectors within approved domain matches, then reranks; Go merge gives local-first priority.
- Invalidation or expiry: no age predicate in inspected query selectors; review status filters remote visibility, confidence/flags alter ranking rather than proving invalidity.
- Activation or effect: wired result delivery; host use of advice and resulting behavior are uninspected.
- Evidence limits: no run trace; custom Store ranking and provider quality uninspected; wrapped semantic errors can bypass the intended SQL fallback.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision roles: foreground caller chooses tags and limit; code selects results; host decides reliance. Operating mode: open task requests, not a bounded curriculum. Answer oracle: inapplicable — retrieval has no expected correct answer/reference outcome in these code paths.

> data, err := json.Marshal(result.Units)
> --- `cli/mcpserver/query.go`

> return QueryResult{
> Units: mergeResults(localResults, remoteResults, limit),
> Source: SourceRemote,
> Warnings: warnings,
> }, nil
> --- `sdk/go/client.go`

#### RT-RTE-knowledge-proposal
Label: Knowledge proposal admission

Owner/endpoints: host/caller supplies content → handler/client validates → local Store or authenticated server service persists → caller receives a unit. The proposed change is new natural-language advice with symbolic tags and evidence defaults. Interactive guidance requests VIBE√, draft presentation and approval; software admission checks shape/bounds and authentication, not that requested reasoning occurred. SRC-1: `sdk/go/prompts/SKILL.md`, `cli/mcpserver/propose.go`, `sdk/go/validate.go`, `sdk/go/client.go`, `sdk/python/src/cq/client.py`, `server/backend/src/cq_server/services/knowledge.py`.

- Immediate return: created unit; Go MCP includes a warning plus local unit on FallbackError; ordinary remote return is PRIVATE but not thereby approved for query.
- Later read-back: local units can reach the next local query; remote persisted units reach ordinary query after review approval.
- Delegated visibility: configured remote receives proposal content on success; local fallback can later drain without another prompt approval step.
- Selection predicate: caller selects candidate; software validates fields, domains and extension keys; server creates its own identity and authenticated created_by.
- Invalidation or expiry: no knowledge TTL established by this admission path; rejected remote proposals stay outside approved-query selection; local content is separately removable through Store operations.
- Activation or effect: wired storage, not demonstrated future application of the action field.
- Evidence limits: no actual candidate, human approval, sanitization, retrieval benefit or deployed grant set supplied; Python discovery failures can propagate before fallback insertion, so not every outage retains a candidate.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Trigger/mode: open discoveries mid-task or candidates from retrospective reflection; human review is requested interactively, headless software/model judgment is permitted under prompt conditions. Proposer: agent or direct caller. Decider/veto: interactive user can approve/edit/skip under doctrine; headless agent applies requested safety gate; client/server can reject malformed input; server reviewer can reject later retrieval admission. Answer oracle: inapplicable — no expected answer supplied by the proposal API. Guidance persists as packaged skill; candidate summary/detail/action/context persists as a knowledge unit. Recovery: Go auth/transport/server failure stores locally. Python stores locally for caught per-call RemoteError (401/403/5xx) or HTTPError, but not for DiscoveryError raised during destination resolution; other 4xx rejects without storing; failed local insertion reports error. No content-level rollback is provided by MCP propose itself. Detailed content revision remains for the memory account.

> if err := validateProposeParams(params); err != nil {
> return KnowledgeUnit{}, err
> }
> --- `sdk/go/client.go`

> tier=Tier.PRIVATE,
> created_by=created_by,
> --- `server/backend/src/cq_server/services/knowledge.py`

Python resolves the destination inside `_remote_propose` before posting. Its resolver's exhausted transport/5xx retry chain raises DiscoveryError, distinct from HTTPError; propose catches only RemoteError and HTTPError before insertion. A cached or successfully resolved destination can still reach the supported per-call fallback. SRC-1: `sdk/python/src/cq/client.py`, `sdk/python/src/cq/discovery/_resolver.py`.

> return self._resolver.resolve(self._addr).api_base_url.rstrip("/")
> --- `sdk/python/src/cq/client.py`

> except httpx.HTTPError as err:
> raise DiscoveryError(f"discovery: probe failed after {_RETRY_ATTEMPTS} attempts: {err}") from err
> --- `sdk/python/src/cq/discovery/_resolver.py`

> except RemoteError as exc:
> if exc.status_code not in (401, 403) and not (500 <= exc.status_code < 600):
> raise
> remote_cause = exc
> except httpx.HTTPError as exc:
> remote_cause = exc
> --- `sdk/python/src/cq/client.py:286-291`

#### RT-RTE-remote-review
Label: Remote review admission

Owner/endpoints: browser human or JWT-bearing API caller → review endpoint/service → review repository → status metadata → future public queries. Frontend fetches pending units, presents one, accepts approve/reject/skip and recovers 409 by fetching again. Server execution updates status/reviewer/time, not insight text. SRC-1: `server/frontend/src/pages/ReviewPage.tsx`, `server/backend/src/cq_server/api/routes/review.py`, `server/backend/src/cq_server/services/reviews.py`, `server/backend/src/cq_server/repositories/reviews.py`.

- Immediate return: review decision status, reviewer and timestamp; browser proceeds to another card.
- Later read-back: approved status gates later remote knowledge query; review APIs can read units regardless of status.
- Delegated visibility: authenticated review consumers can see pending/rejected content; ordinary knowledge consumers see approved content even when tier is PRIVATE.
- Selection predicate: queue selects pending oldest-first; browser skips seen IDs in client state; decision API service requires a pending status at its pre-write check.
- Invalidation or expiry: reject prevents ordinary retrieval; already-reviewed decisions ordinarily raise 409; no reviewed-status reset path is exposed by these handlers.
- Activation or effect: wired status change enables retrieval; actual agent reliance remains uninspected.
- Evidence limits: no reviewed content or human decision trace supplied; check/update is not an atomic conditional transition; JWT identity does not establish human presence.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Trigger/proposed change: pending knowledge becomes approved or rejected. Proposer: original caller; decider/veto: JWT-bearing reviewer; frontend is a human affordance, seed script is an automated alternate using the same API. Answer oracle: inapplicable — no canonical expected judgment is required by endpoint/service. Operating mode: open review queue, with a separate demonstration-seeding mode. Recovery: browser retries/fetches after failures/conflicts; API offers no ordinary reversal of a completed decision. Retained rationale: status/reviewer/time, not a required textual reason. SRC-1: `server/scripts/seed-kus.py`, `server/backend/src/cq_server/services/reviews.py`.

> if existing_status != "pending":
> raise KnowledgeUnitAlreadyReviewedError(existing_status)
> await self._reviews.set_status(unit_id, status, reviewer)
> --- `server/backend/src/cq_server/services/reviews.py`

#### RT-RTE-knowledge-feedback
Label: Knowledge confirmation and flagging

Owner/endpoints: agent/direct caller → confirm or flag handler/client → local Store or authenticated remote approved-unit lookup → persisted evidence change. A confirmation boosts confidence and count; successful flagging reduces confidence and appends a reason. Stale/incorrect flags are supported locally and remotely. Go-local duplicate flags can retain duplicate_of; Python Client exposes no reference argument and its duplicate flags fail Flag validation before local update. Server FlagRequest admits only reason, so even a Go-sent duplicate_of is discarded and server duplicate flag construction fails before repository update. Go uses unit tier to route; Python supported local feedback additionally attempts remote forwarding. SRC-1: `sdk/go/client.go`, `sdk/go/scoring.go`, `sdk/python/src/cq/client.py`, `server/backend/src/cq_server/services/knowledge.py`, `server/backend/src/cq_server/api/routes/knowledge.py`.

- Immediate return: updated unit or operation error; local Go update does not wait for remote publication.
- Later read-back: later query reads successfully updated confirmation/stale/incorrect evidence and Go-local duplicate flags and ranks accordingly; failed Python Client/server duplicate flags yield no persisted update.
- Delegated visibility: remote callers update shared approved-unit evidence; local Go writes remain local, Python attempts forwarding when configured.
- Selection predicate: supplied ID/tier; server get requires approved status; code applies numerical boost/penalty without evaluating underlying task evidence; Python Flag requires duplicate_of for a duplicate reason, but Python Client and server service supply only reason.
- Invalidation or expiry: flags affect score and retained flags, not automatic deletion or review-status revocation in inspected service.
- Activation or effect: wired changes to ranking inputs; actual reliance or improved outcomes uninspected.
- Evidence limits: no verification trace; repeated feedback is not independently validated confirmation; duplicate success is limited to the Go-local path, not Python Client or server paths; no cross-language equivalence guarantee.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Trigger/proposed change: claimed success, independent verification, stale/incorrect/duplicate guidance. Host/caller proposes and decides the evidence judgment; software executes update and can reject missing/invalid units. Human approval is not required in these handlers. Answer oracle: uninspected — prompt asks for current docs/tool verification but no particular reference outcome is supplied. Mode: open experience-based feedback. Recovery/rollback: failed operations return errors; further flags/confirmations change scores, but are not exact inverses of metadata/history. Guidance persists in skill; successful feedback persists in evidence/flags, while Python Client/server duplicate validation prevents update. This is not by itself a content-directed revision of insight text.

The duplicate failure scope agrees with [MEM-OBJ-flags](memory.md#mem-obj-flags); that object supplies retained flag semantics rather than declaring this invocation route. SRC-1: `server/backend/src/cq_server/models/knowledge.py`, `server/backend/src/cq_server/services/knowledge.py`, `sdk/python/src/cq/client.py`, `sdk/python/src/cq/scoring.py`, `sdk/python/src/cq/models.py`, `sdk/go/remote.go`, `sdk/go/scoring.go`.

> flagged = apply_flag(unit, reason)
> await self._knowledge.update(flagged)
> --- `server/backend/src/cq_server/services/knowledge.py`

> if self.reason is FlagReason.DUPLICATE and not self.duplicate_of:
> raise ValueError("duplicate_of is required when reason is 'duplicate'")
> --- `sdk/python/src/cq/models.py`

> out.Flags = append(slices.Clone(ku.Flags), Flag{
> Reason: reason,
> Timestamp: &now,
> Detail: cfg.detail,
> DuplicateOf: cfg.duplicateOf,
> })
> --- `sdk/go/scoring.go`

> out.Evidence.Confidence = min(out.Evidence.Confidence+cqschema.ConfirmationBoost(), cqschema.ConfidenceCeiling())
> out.Evidence.Confirmations++
> --- `sdk/go/scoring.go`

#### RT-RTE-local-drain
Label: Local proposal drain

Owner/endpoints: explicit caller or MCP startup goroutine → Go client reads all local units → remote propose → local delete. The remote service owns its newly assigned fields and pending review state. SRC-1: `cli/cmd/mcp.go`, `sdk/go/client.go`, `sdk/go/remote.go`, `server/backend/src/cq_server/services/knowledge.py`.

- Immediate return: explicit drain gets pushed count/warnings; startup goroutine discards result/error and imposes a 30-second deadline.
- Later read-back: successfully deleted local content is no longer selected locally; its remote replacement becomes queryable only after remote approval.
- Delegated visibility: remote service receives each LOCAL unit's content; it does not receive client unit ID in the inspected proposal body.
- Selection predicate: Store.All then tier equals Local; successful remote proposal required before local deletion.
- Invalidation or expiry: successful transfer deletes local unit; failed post retains it; failed delete leaves a possible resend candidate.
- Activation or effect: wired transfer and deletion; no guarantee of continuous availability, exactly-once transfer or stable cross-store identity.
- Evidence limits: no executed drain or idempotency experiment; lost acknowledgement and delete failure can permit duplicates; startup hides warnings.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: reuses server proposal checks, without new per-content approval; later review can veto retrieval. Trigger is configured remote at startup or explicit drain. Operating mode: bounded transfer attempt, not learning evaluation. Answer oracle: inapplicable — HTTP/storage outcomes guide recovery, not correctness judgment. Recovery: warnings and retained failed units enable a later attempt; no rollback of an accepted remote post after local delete failure is shown. Persisted change is remote knowledge and removal of the local copy.

> _, err := c.remote.propose(ctx, ku)
> --- `sdk/go/client.go`

> if err := c.store.Delete(ctx, ku.ID); err != nil {
> --- `sdk/go/client.go`

#### RT-RTE-session-reflection
Label: Agent-led session reflection

Owner/endpoints: user/session-end command → foreground agent summarizes session and extracts candidates → user review → ordinary propose. It requests dense selective prose covering errors, fixes, tool failures and dead ends, omitting routine edits. No separate model call, isolated worker context or server extraction is wired by this command. Python DefaultReflector is a stub. SRC-1: `sdk/go/prompts/reflect.md`, `sdk/python/src/cq/reflect.py`.

- Immediate return: requested candidate list/summary from host agent; Python stub returns a guidance message, not candidates.
- Later read-back: only approved/proposed candidate content is wired to knowledge persistence through the proposal route; no durable session-summary store is established by the command.
- Delegated visibility: interactive user sees candidates; proposed content reaches local/remote storage; full session upload is not implemented by this reflection command.
- Selection predicate: requested generalizable, non-obvious, actionable and novel candidates; excludes already proposed/confirmed insights and unshareable content.
- Invalidation or expiry: user can edit/skip; no candidate storage/expiry subsystem established before propose.
- Activation or effect: requested reasoning and review; implementation supports subsequent proposal but does not establish successful mining.
- Evidence limits: no session/candidate trace; a conflicting skill subsection describes server-returned candidates, but the dedicated command, registered tools and stub do not support attributing that extraction to CQ server.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

Admission roles: agent drafts and safety-checks; user approves/edits/skips; subsequent software proposal admission is separate. Operating mode: open retrospective sessions, not bounded experimental curriculum. Answer oracle: uninspected — actual session outcomes could inform candidates but none was supplied. Guidance asks for why behavior exists/matters and recommended action; retained product is a knowledge unit, not necessarily a formulated theory. Theory-builder conditions 1–4: each uninspected for actual candidate reasoning and iteration; shipped requests establish neither a localized candidate theory nor exercised content-dependent criticism. Persistence of proposed guidance is supported separately from learning benefit. Reflection here is a source-native procedure name, not evidence satisfying every architectural reflection condition.

> The actual extraction is performed by the agent (via the cq skill),
> which analyzes its own session context and calls propose directly.
> --- `sdk/python/src/cq/reflect.py`

#### RT-RTE-failure-reminder
Label: Cursor failure reminder

Owner/endpoints: host failure hook → CQ writes failureRecord → host stop hook → CQ prints and clears record. Session-start hook sweeps stale state; successful post-tool-use is a no-op. SRC-1: `cli/internal/hook/cursor.go`.

- Immediate return: failure event records state with no guidance output; stop event emits previous failure/tool/input text.
- Later read-back: a later stop invocation reads the last stored per-conversation failure record before deleting it.
- Delegated visibility: hook stdout reaches the host under its external lifecycle contract; no automatic knowledge-store proposal is made.
- Selection predicate: non-interrupt failures with tool name or error; conversation-keyed latest record, bounded input/error, no success pairing.
- Invalidation or expiry: stop clears after rendering; corrupt records are discarded; session-start sweeps files older than 24 hours by modification time.
- Activation or effect: wired reminder emission; host attention or corrective action uninspected.
- Evidence limits: no host hook execution trace; record is a snippet, not complete task history or verified lesson.
- implementation conclusion status: wired
- operation conclusion status: uninspected

The mechanism mechanically curates context by clipping payloads and surfacing a selected failure. It does not diagnose the failure or admit a knowledge change. Sanitized IDs and a directory containment check limit file-path construction; these do not establish content secrecy or model compliance.

> if p.IsInterrupt {
> return nil
> }
> --- `cli/internal/hook/cursor.go`

#### RT-RTE-host-installation
Label: Host instruction installation

Owner/endpoints: operator installer call → packaged prompts/shared skill and host configuration → future host instruction load. Pi writes the skill, transformed reflect/status prompts and an AGENTS.md CLI-mapping block; uninstall removes owned prompt/config material but deliberately keeps the shared skill. SRC-1: `cli/internal/install/pi.go`, `cli/internal/install/files.go`, `cli/internal/install/manifest.go`.

- Immediate return: file change reports; dry-run can avoid writes.
- Later read-back: installed static instructions are future host configuration, not experience-derived memory; load itself depends on the host.
- Delegated visibility: configured host can discover skill/prompts; no agent-worker distribution is established by installation.
- Selection predicate: packaged prompt accessors and caller's target/binary settings; managed-file hashes identify owned unchanged content eligible for replacement/pruning.
- Invalidation or expiry: reinstall updates owned unchanged files; user-modified/unowned files are skipped; uninstall removes eligible owned files and Pi block, retains shared skill.
- Activation or effect: wired configuration changes; actual host loading and behavior uninspected.
- Evidence limits: no installation run; inspected Pi/file ownership path does not establish all host adapters' equivalent recovery.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Trigger/proposed change: operator chooses install/update/uninstall of packaged instruction/capability wiring. Computational decider applies ownership/hash checks; caller chooses operation and may avoid it via dry-run. Rejection: modified files stay intact. Guidance is supplied package text, not proposed by a runtime learning model. Recovery: uninstall/idempotent reinstall, not transactional restoration of an entire partially failed multi-file install. Mode: operator configuration. Answer oracle: inapplicable — no epistemic expected answer; file hashes are ownership/integrity comparisons. Persisted result is Markdown/host configuration and manifests.

> if prev, owned := prevHash[rel]; !owned || onDisk != prev {
> // The user or another tool owns this file; do not overwrite it.
> skipped = true
> continue
> }
> --- `cli/internal/install/files.go`

### Claims

#### RT-CLM-proposal-approval
Label: Interactive proposal approval

Claimed operation: every interactive direct proposal waits for user approval; headless use follows different conditions. Owner: consuming agent/user protocol. Enforcement point: natural-language skill, not proposal handlers. Guarantee strength: policy. Covered path: instructed interactive host behavior. Alternate paths: headless rules, direct MCP/CLI/SDK/server calls, startup drain. Required external contract: host follows skill and faithfully waits for the user's content decision. SRC-1: `sdk/go/prompts/SKILL.md`, `cli/mcpserver/propose.go`, `sdk/go/client.go`.

> presenting the candidate to the user and waiting for their approval is a precondition of every direct `propose` call, regardless of what the check finds.
> --- `sdk/go/prompts/SKILL.md`

- doctrine conclusion status: claimed
- implementation conclusion status: afforded
- operation conclusion status: uninspected

Software validates structure and credentials, not approval or VIBE√. The headless exception expressly states that VIBE√ is the only gate; no guarantee of secret removal, factual validity or human approval applies universally.

#### RT-CLM-approved-query
Label: Approved-only remote knowledge reads

Claimed operation: ordinary server knowledge query returns approved units. Owner: server repository. Enforcement point: SQL status predicate, also present in semantic selector. Guarantee strength: invariant, conditional on the inspected selectors/database content and query execution. Covered paths: ordinary SQL and optional semantic public knowledge query, approved-unit get used by feedback. Alternate paths: local stores have no corresponding review gate; authenticated review `get_any`/list/queue can expose non-approved units; direct database maintenance can change status. Required external contract: database/driver executes these selectors; approval identities/quality remain separate. SRC-1: `server/backend/src/cq_server/repositories/_queries.py`, `server/backend/src/cq_server/semsearch/__init__.py`, `server/backend/src/cq_server/repositories/knowledge.py`, `server/backend/src/cq_server/services/reviews.py`.

> SELECT_APPROVED_BY_ID: TextClause = text("SELECT data FROM knowledge_units WHERE id = :id AND status = 'approved'")
> --- `server/backend/src/cq_server/repositories/_queries.py`

> WHERE ku.status = 'approved'
> AND ku.id IN (
> SELECT DISTINCT unit_id
> FROM knowledge_unit_domains
> WHERE domain IN :domains
> )
> --- `server/backend/src/cq_server/semsearch/__init__.py`

- implementation conclusion status: wired
- operation conclusion status: uninspected

This invariant concerns status selection, not human-only approval, reviewer independence, tenancy or PRIVATE-tier confidentiality. The migration defaults new remote rows to pending; approving them does not promote their tier. SRC-1: `server/backend/alembic/versions/0001_baseline.py`, `server/backend/src/cq_server/repositories/_queries.py`.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-skill-protocol
Label: Skill protocol authority

Consumer: external foreground agent. Channel: loaded CQ skill and reflection instructions, or installed Pi AGENTS.md mapping to CLI. Force: natural-language request whose actual priority/compliance depends on host; not a local API authorization rule. Horizon: installed configuration can guide many sessions until edited/uninstalled; current session application remains unobserved. SRC-1: `sdk/go/prompts/SKILL.md`, `sdk/go/prompts/reflect.md`, `cli/internal/install/pi.go`.

> Before starting any implementation task, load the `cq` skill and follow its Core Protocol.
> --- `cli/internal/install/pi.go`

The quoted text occurs inside generated instruction string construction; its delivery is wired by installation, not evidence that a host obeyed it.

#### RT-BAP-knowledge-guidance
Label: Retrieved knowledge guidance authority

Consumer: querying host agent/human. Channel: selected unit JSON/tool text or CLI output containing insight action/detail. Force: advisory natural language interpreted under a skill instruction to verify first; code selection and confidence can influence which advice arrives but do not execute the action field. Horizon: persisted units can guide later tasks/sessions after applicable selection/admission; actual application and benefit unobserved. SRC-1: `cli/mcpserver/query.go`, `cli/cmd/query.go`, `sdk/go/prompts/SKILL.md`.

> When a query returns results, read the `insight.action` field for the recommended approach and `insight.detail` for the full explanation.
> --- `sdk/go/prompts/SKILL.md`

## Annotations

none
