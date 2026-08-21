# Runtime account — RUN-GBRAIN-20260820

Logical record 5 of the result. Mandatory step-4 baseline, owned by the orchestrator.
Scheduling, context assembly, and external state/action are treated as **causal responsibilities**,
not module boundaries; several GBrain facilities span more than one.

Anti-conflation rules held throughout: a filesystem is not a scheduler; retaining material is not
selecting it into context; a tool schema present in context is not tool execution.

## 4.1 Materiality of the recorded loops

Six loops are recorded as material — each alters the analysis question, a control path, evidence
strength, or a lens result:

| Loop | Why material |
|---|---|
| L1 Minion job loop | The only durable scheduler; owns retry, timeout, dead-letter, and concurrency for every background action |
| L2 Subagent turn loop | The only in-repo loop that issues model calls and executes tool actions in sequence |
| L3 Dream/maintenance cycle | The autonomous loop that produces most accumulated-from-use material (memory lens input) and most checking (epistemic lens input) |
| L4 Retrieval / context assembly | Determines what enters any consuming model's context; the read-back delivery point |
| L5 `think` synthesis | Produces the system's headline truth-apt artifact (answer + citations + gaps) |
| L6 MCP request loop | The boundary through which external agents act on the brain; carries the authority gates |
| L7 Doctor remediation loop | A goal-directed loop with a target, a plan, per-step re-evaluation, and a cost cap — the closest thing in the repo to autonomous goal pursuit, and it contains no model in the planning decision |

A seventh loop — the host agent's per-message "signal → search → respond" loop asserted by
`README.md:241` — is **outside the boundary**. Status: `claimed` (README, `templates/HEARTBEAT.md.template`).
No implementation of that loop exists in this checkout; it is executed by OpenClaw/Hermes/Claude Code
under skill instructions GBrain ships. This prevents any conclusion about end-to-end agent behavior.

**One partial exception, recorded because it crosses the boundary.** GBrain ships an OpenClaw plugin
entry (`src/openclaw-context-engine.ts`) that registers a **deterministic** context engine into the
host's per-turn context slot, injecting live temporal/spatial context on every turn to prevent the
"time warp" class of bug where a compacted session loses the user's current time, location, and
state. It is opt-in (`plugins.slots.contextEngine: "gbrain-context"` in `openclaw.json`), OpenClaw-
specific, and the core logic in `src/core/context-engine.ts` is SDK-free. Status: `implemented`
(plugin registration and engine factory are in the checkout); whether any deployment enables the slot
is `uninspected`. This is the only in-repo write into the host agent's per-turn context assembly;
every other host-side behavior is carried by advisory markdown (BAP-01, BAP-02).

## 4.2 L1 — Minion job loop (RTE-01)

| Field | Finding | Status | Anchor |
|---|---|---|---|
| Trigger/input | Row inserted into `minion_jobs` by CLI, MCP op, cron, autopilot, or a parent job | implemented | `src/core/minions/queue.ts` (`add`, cols at :249-270) |
| Next-step owner | `MinionWorker` poll loop, `pollInterval` default 5000 ms | implemented | `src/core/minions/worker.ts:204`, `:505` |
| Decision policy + form | **Symbolic, in SQL.** `ORDER BY priority ASC, created_at ASC … FOR UPDATE SKIP LOCKED LIMIT 1`, filtered to `queue` and `name = ANY(registeredNames)`. No model call in the scheduling decision. | implemented | `src/core/minions/queue.ts:601-628` |
| Context selection | None. The claim reads a row; the handler decides what context to assemble. Retention of `minion_jobs` rows is **not** context selection. | implemented | same |
| State reads/writes | Claim writes `status='active'`, `lock_token`, `lock_until`, `timeout_at`, `attempts_started`; via `executeRawDirect` (session-mode pool) so a transaction-mode pooler cannot recycle the lock-holding connection | implemented | `queue.ts:607-626` |
| Action executor + boundary | Registered handler by name. 37 built-in names registered in `src/commands/jobs.ts`: `autopilot-cycle, backlinks, consolidate, contextual_reindex_per_chunk, embed, embed-backfill, embed-catch-up, enrich, extract, extract-atoms-drain, extract-conversation-facts, extract_facts, extract-ner, extract-takes-from-pages, extract-timeline-from-meetings, import, ingest_capture, integrity, integrity-auto, lint, lint-fix, noop, orphans, patterns, purge, recompute_emotional_weight, reindex, repair-jsonb, resolve_symbol_edges, shell, skillopt, subagent, subagent_aggregator, sync, sync-retry-failed, synthesize, unify-types`. Third-party handlers arrive through `loadPluginsFromEnv`, validated against `validAgentToolNames`. `shell` is registered only under `--allow-shell-jobs`; `PROTECTED_JOB_NAMES` gates submission of privileged names. | implemented | `src/commands/jobs.ts:707-1731, 1980-1993`; `src/core/minions/{handlers/,protected-names.ts,plugin-loader.ts}`; `supervisor.ts:16` |
| Persistence | Postgres/PGLite `minion_jobs` (+ children, attachments via S3/Supabase) | implemented | `queue.ts`, `attachments.ts` |
| Coordination + return | Parent/child jobs (`parent_job_id`, `on_child_fail`), cascading timeouts, `child_done` events, `subagent-aggregator` | implemented | `queue.ts:640+`, `handlers/subagent-aggregator.ts` |
| Retry / cancel / recovery | Token-fenced lock with renewal tick; stall detector requeues (`handleStalled`), timeout detector dead-letters (`handleTimeouts`), wall-clock detector dead-letters; ordering is stall-before-timeout by design; `INFRASTRUCTURE_ABORT_REASONS` skips `failJob` so a pooler blip does not burn an attempt; `delay_until` promotion for delayed jobs; backoff with jitter; quiet-hours re-defer ~15 min evaluated **at claim time, not dispatch**; RSS watchdog drain; DB-liveness probe with `dbFailExitAfter`; supervisor respawn with exponential backoff and a 5-crash cap | implemented | `worker.ts:48-51, 297-319, 547-560`; `queue.ts:631-660, 1128-1146`; `supervisor.ts:22-26` |
| Output | Job row terminal state + handler result; audit JSONL | implemented | `queue.ts`, `src/core/audit/` |

**Ownership note:** the supervisor spawns `gbrain jobs work` as a *separate child process* so a
misbehaving handler cannot kill the supervisor (`supervisor.ts:17-21`). Postgres only; PGLite's
exclusive file lock makes a separate worker process impossible and the CLI refuses the combination
(`supervisor.ts:8-11`). This is a real deployment-shape constraint, not a preference.

## 4.3 L2 — Subagent turn loop (RTE-02)

Two implementations behind one feature flag, `agent.use_gateway_loop` (default OFF).

| Field | Finding | Status | Anchor |
|---|---|---|---|
| Trigger/input | `subagent` job with `data.prompt`; from `gbrain agent run` or a queue submission | implemented | `handlers/subagent.ts:175-180` |
| Next-step owner | The model. Loop continues while the assistant message contains `tool_use` blocks; terminates on zero tool calls (`end_turn`) or `assistantTurns >= maxTurns` (default 20) | implemented | `subagent.ts:60, 426-430, 570-583` |
| Decision policy + form | **Natural-language + model-resolved.** System prompt = caller's `data.system` (default: one generic line) plus a *deterministic* tool-usage preamble rendered from the actual `toolDefs` array, each tool's `usage_hint` spliced in. Determinism is load-bearing for the Anthropic prompt-cache marker. | implemented | `system-prompt.ts:11-30, 43-60`; `subagent.ts:254-259` |
| Context selection + framing | Full conversation replayed from `subagent_messages`; system block and the *last* tool definition carry `cache_control: {type:'ephemeral'}` (Anthropic semantics: cache everything up to and including this block); `max_tokens: 4096` | implemented | `subagent.ts:478-503` |
| State reads/writes | Two tables are the single source of truth for loop position: `subagent_messages` (per-turn content blocks + token counts) and `subagent_tool_executions` (two-phase `pending → complete/failed`) | implemented | `subagent.ts:1-12, 1106-1178` |
| Action executor + boundary | `BRAIN_TOOL_ALLOWLIST` — a **manually reviewed name-based** allow-list derived from `src/core/operations.ts`, not from `OperationContext.remote`. Read-only ops plus one conditional write: `put_page`, whose slug is namespace-restricted to `wiki/agents/<subagentId>/…` in *both* the tool schema and a server-side fail-closed check. Per-job narrowing via `data.allowed_tools` (`filterAllowedTools`) and `data.allowed_slug_prefixes`. | implemented | `tools/brain-allowlist.ts:1-60`; `subagent.ts:243-252` |
| Persistence / crash recovery | Assistant message persisted **before** tool dispatch. On resume: committed rows are trusted; `complete`/`failed` outcomes are replayed as synthesized `tool_result` blocks; `pending` rows are re-run only for tools marked `idempotent`, otherwise the job throws. A terminal assistant message with no `tool_use` returns immediately (Sonnet 4.6+ rejects assistant prefill). | implemented | `subagent.ts:321-420, 617-640` |
| Coordination + return | Rate leases around each LLM call: `acquire → call → release`, key `anthropic:messages`, cap from `GBRAIN_ANTHROPIC_MAX_INFLIGHT` (default 32, `"unlimited"`/`"none"` sentinel, anything else throws at startup), 120 s TTL. Lease exhaustion raises `RateLeaseUnavailableError`, which the worker treats as renewable, not terminal. Ordering is load-bearing: budget reserve runs **before** lease acquisition so a budget throw never consumes a pacer slot. | implemented | `subagent.ts:76-87, 436-467, 508-509` |
| Retry / cancel / recovery | Dual-signal abort (`ctx.signal` + `ctx.shutdownSignal`) merged via `AbortSignal.any`; `prompt is too long` 400s converted to `UnrecoverableError` → straight to `dead`, bypassing `max_stalled` retries | implemented | `subagent.ts:505-519, 1195-1256` |
| Output | `{result, turns_count, stop_reason, tokens}`; `stop_reason` ∈ `end_turn`/`max_turns`/`refusal`/`error` | implemented | `subagent.ts:705-711, 910-934` |

**Gateway variant.** `gateway.toolLoop()` is provider-agnostic (Vercel AI SDK bridge, recipes under
`src/core/ai/recipes/`), keyed on a stable `gbrain_tool_use_id` from migration v81 with a read-time
shim for pre-v81 rows. It adds a **guardrail seam** that classifies tool *input* before persistence
and execution — explicitly observe-only and fail-open, sending only tool name + input, never tool
output or conversation state (`gateway.ts:2950-2965`). Because the flag defaults OFF
(`subagent.ts:221-227`), the legacy Anthropic-direct path is the deployed default and the guardrail
seam does **not** run there. Status of guardrail coverage on the default path: `absent` within the
inspected boundary of `handlers/subagent.ts`.

**Not implemented in this loop (author-declared, `claimed`+`implemented`-consistent):** refusal
detection on the legacy path, `stop_reason=max_tokens` partial recovery, and parallel tool dispatch —
tools run serially (`subagent.ts:20-24`).

## 4.4 L3 — Dream / maintenance cycle (RTE-03)

| Field | Finding | Status | Anchor |
|---|---|---|---|
| Trigger/input | Three entry points converging on one primitive `runCycle()`: `gbrain dream` (one-shot, cron), `gbrain autopilot` (interval daemon), and the `autopilot-cycle` Minion handler (durable) | implemented | `src/core/cycle.ts:1-11`; `src/commands/dream.ts:1-23`; `src/commands/autopilot.ts:1-18` |
| Next-step owner | Fixed ordered phase list `ALL_PHASES`; no model chooses the order | implemented | `cycle.ts:101-175` |
| Decision policy + form | **Symbolic and semantically motivated**: fix files first, then index. lint → backlinks → sync → synthesize → extract → extract_facts → extract_atoms → resolve_symbol_edges → patterns → recompute_emotional_weight → consolidate → propose_takes → grade_takes → calibration_profile → embed → orphans → purge → schema-suggest → synthesize_concepts → conversation_facts_backfill → enrich_thin → skillopt. Several phases are default-OFF or pack-gated (`extract_atoms`, `synthesize_concepts` gated on the active schema pack's `phases:` declaration; `conversation_facts_backfill`, `enrich_thin`, `skillopt` opt-in). | implemented | `cycle.ts:13-30, 57-175` |
| Context selection | Per phase. Ordering constraints are stated as data dependencies: `patterns` must follow `extract` so graph state is fresh; `extract_facts` must follow `extract` and precede `patterns`; `extract_atoms` after `extract_facts` so the Haiku check has fact context. | implemented | `cycle.ts:20-23, 104-120` |
| State reads/writes | Filesystem writes (lint, backlinks), DB writes (sync, extract, embed, consolidate, takes phases), read-only report (orphans) | implemented | `cycle.ts:15-27` |
| Action executor + boundary | Phase functions in `src/core/cycle/`; LLM-calling phases (synthesize, propose_takes, grade_takes, calibration_profile, extract_atoms, synthesize_concepts, enrich_thin, skillopt, schema-suggest) go through the gateway under a `BudgetTracker` | implemented | `src/core/cycle/*`, `cycle/budget-meter.ts`, `cycle.ts:83-99` |
| Persistence | Brain git repo (system of record) + engine DB | implemented | `README.md:284` |
| Coordination | Postgres: TTL row in `gbrain_cycle_locks` (30 min), refreshed *between* phases via `yieldBetweenPhases` **and during** long phases via `buildYieldDuringPhase`. PGLite/engine-null: `~/.gbrain/cycle.lock` file holding PID + mtime, same TTL. Advisory locks were rejected because session-scoped `pg_try_advisory_lock` does not survive PgBouncer transaction pooling. Lock-skip: filesystem-only/read-only phase selections skip acquisition entirely. | implemented | `cycle.ts:30-43, 615-651` |
| Retry / cancel / recovery | Abort signal checked between phases; a fatal condition (timeout, cancel, lock-loss) bails between phases and returns a `failed` report rather than running the next phase; per-phase results roll into `clean`/`partial`/`failed` | implemented | `cycle.ts:323-334, 428-440, 695` |
| Output | `CycleReport` with per-phase results and typed counters (transcripts synthesized, pattern pages, code edges resolved/ambiguous, rows purged, facts promoted, takes created) | implemented | `cycle.ts:307-378` |

## 4.5 L4 — Retrieval and context assembly (RTE-04)

Recorded as a control path because it determines what any consuming model sees.

| Field | Finding | Status | Anchor |
|---|---|---|---|
| Trigger/input | `search`/`query` op, `think` gather, subagent tool call, or MCP client request | implemented | `src/core/search/hybrid.ts`, `operations.ts` |
| Decision policy + form | **Symbolic, layered, no model in the ranking decision** except optional query expansion and intent classification: vector (HNSW on pgvector) + BM25 keyword + reciprocal-rank fusion + source-tier boost + reranker, with per-query graph signals (adjacency boost, cross-source corroboration boost, session demote), title/alias match boost, recency decay, autocut, dedup, best-chunk-per-page pooling | implemented (mechanism inventory); efficacy `claimed` | `src/core/search/{hybrid,graph-signals,rerank,source-boost,title-match,recency-decay,autocut,dedup,two-pass}.ts`; `README.md:255` |
| Selection scope + budget | Three named modes bundling the knobs — `conservative` (~4K tokens, limit 10), `balanced` (default; ~12K, limit 25), `tokenmax` (budget off, limit 50, LLM multi-query expansion on). Resolution chain: per-call `SearchOpts` → per-key config → `MODE_BUNDLES[search.mode]` → `balanced`. Mode resolution deliberately lives in bare `hybridSearch`, not only the cached wrapper, so evals exercise the same mode-affected path as production. | implemented | `CLAUDE.md` "Search Mode"; `src/core/search/mode.ts`, `token-budget.ts` |
| Caching | `query_cache` with a `knobs_hash` column (migration v56, version 3) folding the knob set **plus the active embedding column name and provider** into the key, so a tokenmax write cannot be served to a conservative read and a Voyage-1024d row cannot be served to an OpenAI-1536d read. Similarity threshold 0.92, TTL 3600 s. | implemented | `CLAUDE.md` "Cache-key contamination hotfix"; `src/core/search/query-cache.ts`, `query-cache-gate.ts` |
| Interpretation aids returned | Each result carries an `evidence` tag (why it matched) and a `create_safety` hint (`exists`/`probable`/`unknown`) so a calling agent decides whether a page already exists rather than guessing from a raw score | implemented | `src/core/search/evidence.ts`; `README.md:255` |
| Observability | `search --explain` per-stage attribution; `search stats` fire counts and failure breakdowns; `search diagnose --target <slug>`; `doctor` check `graph_signals_coverage` | implemented | `README.md:255` |
| Schema-pack coupling | The active pack threads through every read and write path: `parseMarkdown` infers page type from pack prefixes; `whoknows` scopes expert routing to `expert_routing: true` types; `extract_facts` runs only on `extractable: true` types; the search cache folds pack name + version into its key | implemented (per doctrine); code sites `uninspected` in this run | `README.md:222` |

## 4.6 L5 — `think` synthesis (RTE-05)

Runtime-owned facts only; transformation, checking, warrant, and acceptance belong to the epistemic lens.

| Field | Finding | Status | Anchor |
|---|---|---|---|
| Pipeline | GATHER → MERGE → SYNTHESIZE | implemented | `src/core/think/prompt.ts:4` |
| Inputs assembled into context | `<pages>` (hybrid-search chunks), `<takes>` (typed/weighted/attributed claims), optional `<graph>` (anchor subgraph), optional `<calibration>` block, optional `<trajectory>` block | implemented | `think/prompt.ts:40-46, 155-226`; `think/gather.ts` |
| Message ordering | Two shapes only, and the code explicitly refuses a third: default = question → pages → takes → graph → trajectory → instruction; calibration mode = pages → takes → graph → calibration → trajectory → question → instruction | implemented | `think/prompt.ts:132-153, 172-225` |
| Output contract | Strict JSON: `answer` (markdown with inline `[slug#row]` / `[slug]` citations), `citations` (structured `{page_slug, row_num, citation_index}`), `gaps` (array). Structured citations exist so persistence is deterministic — "never trust the model to keep prose citations stable" — with a regex fallback recovering inline markers when the model omits the field. | implemented | `think/prompt.ts:9-17, 60-70`; `think/cite-render.ts` |
| Intent conditioning | Detected intent (`general`/`temporal`/`entity`/`event`) adjusts the prompt; `--anchor`, `--since`/`--until` narrow it | implemented | `think/prompt.ts:20-38, 72-98`; `think/intent.ts` |
| Multi-round | `--rounds N` uses the `gaps` field to drive follow-up | implemented (declared purpose) | `think/prompt.ts:13` |
| Injection posture | `<take>` contents declared DATA, never instructions; shared `INJECTION_PATTERNS` sanitizer is the single source of truth across takes/think/facts extraction | implemented | `think/prompt.ts:43-45`; `think/sanitize.ts`; `facts/extract.ts:25` |
| Durable variant | `gbrain agent run "…"` exposes the same surface to a subagent through the Minions queue with crash-safe two-phase persistence | claimed (README) + implemented (L2 machinery) | `README.md:171` |

## 4.7 L6 — MCP request loop (RTE-16)

| Field | Finding | Status | Anchor |
|---|---|---|---|
| Trigger/input | MCP tool call over stdio (`gbrain serve`) or HTTP (`gbrain serve --http`, OAuth 2.1 + DCR-style registration + rate limiting) | implemented | `src/mcp/{server,http-transport,rate-limit}.ts`; `README.md:143-151` |
| Contract source | Contract-first: `src/core/operations.ts` (~47 shared operations) is the single source; CLI and MCP tool defs are both generated from it | implemented | `CLAUDE.md` "Contract-first"; `src/mcp/tool-defs.ts` |
| Decision policy + form | **Symbolic, pre-handler.** Tool list filtered by `operations.filter(op => !op.localOnly)`; then `hasScope(authInfo.scopes, op.scope || 'read')` with `insufficient_scope` on failure; then `validateParams` against declared `params` | implemented | `src/commands/serve-http.ts:1394, 1490-1523`; `src/mcp/dispatch.ts:171-187, 228-248` |
| Trust boundary | `OperationContext.remote` is **required on the type** and fail-closed: anything not strictly `false` is untrusted. `src/cli.ts` sets `false`; `src/mcp/server.ts` sets `true`. `file_upload` tightens filesystem confinement when remote. | implemented | `CLAUDE.md` "Trust is fail-closed"; `dispatch.ts:31, 211` |
| Source isolation | Every read-side op routes through `sourceScopeOpts(ctx)`; precedence federated array (`ctx.auth.allowedSources`) > scalar (`ctx.sourceId`) > nothing. Hand-rolled filtering is called out as a cross-source data-leak class. `takesHoldersAllowList` is a second, orthogonal per-token filter on the takes holder field. | implemented | `CLAUDE.md` "Source isolation"; `dispatch.ts:36-50, 206-212` |
| Context assembly (server-side push) | After a successful op the dispatcher calls an optional `metaHook` and injects `_meta.brain_hot_memory`. Best-effort in its own try/catch: any failure degrades to no `_meta` rather than failing the call. Skipped for `recall`, `extract_facts`, `forget_fact`. | implemented | `dispatch.ts:16-27, 255-267`; `facts/meta-hook.ts:39-47` |
| Logging posture | `summarizeMcpParams` publishes only the request *shape* — declared param names intersected against the op's allow-list, unknown keys counted but not named, byte size bucketed up to 1 KB to close a size side channel. Full payloads only under an explicit `--log-full-params` with a loud startup warning. | implemented | `dispatch.ts:75-168` |
| Error shape | Every error path returns JSON-parseable content (`unknown_tool`, `invalid_params`, `OperationError.toJSON()`, `internal_error`) | implemented | `dispatch.ts:228-282` |

## 4.7b L7 — Doctor remediation loop (RTE-24, registered post-freeze)

Recorded because it is the only loop in the repository that pursues a numeric goal state, and
because what sits in its decision slot is a notable negative finding.

| Field | Finding | Status | Anchor |
|---|---|---|---|
| Trigger/input | `gbrain doctor --remediate --yes --target-score 90 --max-usd 5`; also reached from `gbrain onboard` and the MCP `run_onboard` op through the same library | implemented | `src/core/remediation/index.ts:1-16`; `AGENTS.md:75-85` |
| Goal | `targetScore` (default 90) on the brain health score | implemented | `remediation/run.ts:44` |
| Decision policy + **form** | **Symbolic. No model call in the planning decision.** `computeRemediationPlan` derives a dependency-ordered step list from `computeRecommendations(RecommendationContext)`; ordering constraints are hard-coded semantics (sync before extract, embed after consolidate) | implemented | `remediation/{plan,run,context}.ts`; `brain-score-recommendations.ts`; `AGENTS.md:76-79` |
| Pre-flight | Ceiling check: if `target_unreachable`, return `max_reachable_score` and bail rather than burn budget. Empty brains and unconfigured embedding keys hit that ceiling. | implemented | `remediation/run.ts:70-80`; `AGENTS.md:79-81` |
| Per-step re-evaluation | D7 scoped recheck — the plan is recomputed from fresh health between every step, so the loop reacts to what its own actions did | implemented | `remediation/run.ts:6-11` |
| Failure handling | D5 dependency cascade: a failed step aborts its dependents rather than proceeding on a broken precondition | implemented | `remediation/run.ts:9` |
| Budget | Wrapped in `withBudgetTracker`; `BudgetExhausted` is **never thrown out** — the exhaustion snapshot is returned on `result.budget_exhausted` so the caller decides. Other errors propagate. | implemented | `remediation/run.ts:31-37, 56-59` |
| Persistence / resume | Checkpoint keyed on `plan_hash`; resume only against a matching hash, so a changed plan cannot silently continue an old run | implemented | `remediation/run.ts:60-66`; `remediation-checkpoint.ts` |
| Execution substrate | Postgres: ordered Minion job submission (D3, sequential). PGLite: synchronous in-process execution, no durable queue. | implemented | `remediation/run.ts:29-32` |
| Library discipline | No `console.*`, no `process.exit`, no argv parsing inside the library; observability via injected `RemediationHooks`; callers decide exit codes | implemented | `remediation/run.ts:1-11, 38` |

**Negative finding worth stating plainly:** GBrain's autonomous-repair loop is a deterministic
planner over a scored checklist. Model calls occur *inside* individual steps (embed, extract,
synthesize), never in the choice of what to do next. Status: `implemented`. This prevents any
conclusion that GBrain performs model-directed goal pursuit over its own state.

## 4.8 Conditional surfaces inspected (step 4.4), with materiality stated

Each entry states why it alters the analysis question, a control path, evidence strength, or a lens
result. This is not a taxonomy and not a maturity ladder.

| Surface | Materiality | Finding | Status |
|---|---|---|---|
| Permissions / authority | Alters the action-execution control path in L2 and L6 | Three independent gates: `localOnly` (transport reachability), `scope` read/write/admin (OAuth), `remote` fail-closed trust; plus subagent-level name allow-list and slug namespace. `schema_apply_mutations` is deliberately admin-scope but **not** `localOnly`, so remote agents can author schema packs over HTTPS. | implemented |
| Governance / human gates | Determines whether machine output is accepted — directly bounds the epistemic lens | `propose_takes` writes to a review queue the user accepts/rejects; `grade_takes` auto-resolve is OFF by default; `schema review-candidates` is a human promote/rename/ignore gate; SkillOpt never auto-mutates bundled skills, emitting `proposed.md` instead | implemented |
| Budget / rate control | Constrains whether a loop can run at all; also the pacing mechanism the whole fleet shares | `BudgetTracker` via `AsyncLocalStorage` (`withBudgetTracker`/`getCurrentBudgetTracker`), reserve-before-lease ordering, per-skill \$0.50 and brain-wide \$2.00 SkillOpt caps, `BudgetExhausted` with a pricing-lookup fail-closed/warn-only/null policy per consumer | implemented |
| Observability | Determines what evidence a later observed-run analysis could even collect | Weekly-rotated JSONL audits under `~/.gbrain/audit/` (subagent submission + heartbeat, skillopt, batch-retry, db-disconnect, lock-renewal); `gbrain doctor` checks read them (`batch_retry_health`, `graph_signals_coverage`, `subagent-health`); progress events on stderr with machine-stable `snake_case.dot.path` phase names, stdout reserved for data | implemented |
| Providers | Changes which loops can run and the failure modes each carries | Gateway with recipes for Anthropic, OpenAI, OpenRouter, Voyage, ZeroEntropy (default embed + rerank), Gemini, Azure, MiniMax, DashScope, Zhipu, Ollama, llama.cpp, LiteLLM; capability classifier refuses models lacking native tool calling (`unusable:no_tools`) and unknown providers | implemented |
| Persistence engines | Determines which deployment shapes exist and which coordination primitives are available | `BrainEngine` contract, ~47 ops, two implementations moving in lockstep (parity pinned by `test/e2e/engine-parity.test.ts`). PGLite is single-writer: `gbrain serve` must be stopped before a large sync, and the supervisor cannot run at all. | implemented |
| Packaging / distribution | Determines the channel through which instruction artifacts reach a consuming model — a `BAP-*` input — and, here, the channel through which a remote file acquires shell authority | Skillpack bundler drops the shipped skills into the agent workspace; `openclaw.plugin.json` declares the OpenClaw mod. `INSTALL_FOR_AGENTS.md` is an install *protocol written for an agent to execute*: the documented entry point is pasting `Retrieve and follow the instructions at: https://raw.githubusercontent.com/garrytan/gbrain/master/INSTALL_FOR_AGENTS.md` into an agent, which then runs `curl -fsSL https://bun.sh/install \| bash` and `bun install -g github:garrytan/gbrain`. The force of that document is advisory-to-the-model but its **effect** is shell execution on the user's machine, mediated only by the agent's compliance. Recorded because it is a control path, not because it is a recommendation for or against. | implemented | `README.md:79-84, 112-117`; `INSTALL_FOR_AGENTS.md:1-30` |
| Performance | Only noted where it changes a control path | `knobs_hash` cache keying; best-chunk-per-page pooling; chunked backfills in 1000-row batches; `CREATE INDEX CONCURRENTLY` with `transaction:false` on Postgres, plain index on PGLite | implemented |

Surfaces deliberately **not** inspected: admin dashboard UX, release tooling, test discipline,
embedding-provider recipe internals, tutorial content. None of them change a recorded control path.
