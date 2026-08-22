# Evidence packet — RUN-GBRAIN-20260820

Prepared once by the orchestrator under step 2.4 of `analyse-agentic-system`.
Lens workers consume this packet plus targeted reads inside the frozen boundary.
**No source reacquisition, no boundary widening, no revision change, no parallel ID namespace.**

> **ERRATUM — added after lens return; the text below is left exactly as the workers received it.**
> The memory/context lens inspected the checkout and found three assertions in this packet to be
> wrong. They are corrected centrally in `result.md` §4.4, not here, so that this file remains a
> faithful record of what was frozen and dispatched. Do not rely on the following without reading
> that correction:
> 1. **"43 skills"** (§3 boundary table, SRC-16, CMP-16) — the tree holds **53 directories and 51
>    `SKILL.md` files**. Four incompatible counts exist across the repo; preserved as conflict C1.
> 2. **CMP-16's skillpack description** — `skills/manifest.json` declares 50 skills at
>    `version: 0.32.3.0` while `VERSION` is `0.42.25.0`; the manifest is stale relative to the tree.
> 3. **Table anchoring** — `facts`, `takes`, and `query_cache` are defined only inside the
>    `MIGRATIONS` array of `src/core/migrate.ts`, **not** in `src/schema.sql`. An inventory keyed on
>    `schema.sql` alone misses the three most memory-relevant tables in the system.

## 1. Run identity

- Run/result ID: `RUN-GBRAIN-20260820`
- Target system: GBrain (github.com/garrytan/gbrain)
- Staging identity: `kb/work/multistage/multistage-write-analyse-agentic-system-20260820/trials/gbrain/`
- Analysis cutoff: 2026-08-20 (inspection date); frozen revision below.

## 2. Frozen revision

- Checkout: `/home/zby/llm/commonplace/related-systems/gbrain`
- Revision: `9a0bae8d62cdd1e0dd6655e24e082fe6c69c5dac`
- Commit date: 2026-06-03
- Commit subject: `v0.42.25.0 fix(pricing): unify chat-model pricing into one canonical source; add Opus 4.8 (#1819) (#1827)`
- `VERSION` file: `0.42.25.0`
- Working tree: clean (`git status --porcelain` empty)
- Inspection mode: read-only. No fetch, pull, or refresh.

## 3. Declared boundary

Included by function — components whose scheduling, context selection, retained state,
action execution, checking, acceptance, or authority decisions produce or constrain
GBrain's deployed behavior:

| Function | Included material |
|---|---|
| Scheduling | `src/core/minions/{queue,worker,supervisor,child-worker-supervisor,rate-leases,quiet-hours,lock-renewal-tick}.ts`; `src/core/cycle.ts` phase orchestration |
| Model-call loop | `src/core/minions/handlers/subagent.ts`, `src/core/minions/system-prompt.ts`, `src/core/minions/tools/brain-allowlist.ts`, `src/core/ai/gateway.ts` |
| Context assembly | `src/core/search/*` (hybrid, mode, token-budget, query-cache, graph-signals, rerank, expansion), `src/core/think/{gather,prompt,index}.ts`, `src/core/context-engine.ts` |
| Retained state | `src/core/facts/*`, takes tables + `src/core/cycle/{propose-takes,grade-takes,calibration-profile}.ts`, `src/core/cycle/phases/consolidate.ts`, `src/schema.sql`, `src/core/migrate.ts`, brain git repo as system of record |
| Action execution / boundary | `src/core/operations.ts` (contract), `src/mcp/{dispatch,server,http-transport,rate-limit}.ts`, `OperationContext.remote` trust boundary, source isolation |
| Checking / acceptance | `src/core/eval-contradictions/*`, `src/core/cycle/grade-takes.ts`, `src/core/cycle/nightly-quality-probe.ts`, `src/core/skillopt/*` (validate-gate, score, held-out), `src/core/guardrails.ts` |
| Instruction artifacts | `skills/` (43 skills, `RESOLVER.md`, manifest), `templates/*.template`, `INSTALL_FOR_AGENTS.md`, `AGENTS.md`/`CLAUDE.md` for the GBrain repo itself |
| Doctrine | `README.md`, `DESIGN.md`, `docs/` (architecture, ethos, eval, takes-vs-facts, contradictions, guardrails) |

Excluded (named, not analysed): `admin/` dashboard UI; `test/` and `tests/` (1,244 files) except as
named pins; `scripts/` CI guards; release/versioning tooling; binary self-update; embedding-provider
recipe internals; `evals/` harness internals; docs tutorials as walkthrough narrative.

External dependencies (outside boundary, named): Anthropic Messages API and other model providers via
the gateway; ZeroEntropy embeddings + reranker (default); OpenAI/Voyage/etc. embedding providers;
Postgres/Supabase or PGLite (Postgres 17 WASM); the host agent platform (OpenClaw, Hermes, AlphaClaw,
Claude Code, Codex, Cursor, ChatGPT, Perplexity) that runs the outer conversational loop; git; S3/Supabase
storage for attachments; Twilio/OpenAI Realtime for the voice recipe.

**Boundary character:** whole-system for the GBrain repository, but *subsystem-only with respect to the
advertised agent loop.* README's "signal → search → respond → write → auto-link → sync" loop places the
signal detector and the respond step inside the **host agent platform**, which is not in this checkout.
Conclusions about the end-to-end agent loop are therefore bounded; conclusions about GBrain's own
scheduling, retrieval, retention, and synthesis machinery are not.

## 4. Overall evidence tier

`code-grounded`. Every material loop recorded in the runtime account rests on inspected TypeScript
implementation in this checkout. Doctrine sources are cited as `doctrine/design` and never upgraded.

No `observed run` and no `causal experiment` evidence exists in this run: nothing was executed.
Benchmark numbers in `README.md` (P@5 49.1%, R@5 97.9%, +31.4 P@5) and production counts
(146,646 pages; 100,720 takes) are `claimed` — the underlying runs live in the sibling
`gbrain-evals` repo, outside the boundary.

## 5. Source register

| ID | Kind | Identity / location | Revision / capture | Evidence layer | Inspected scope | Access gaps |
|---|---|---|---|---|---|---|
| SRC-01 | repo checkout | `related-systems/gbrain` (whole) | `9a0bae8` | implementation | tree listing, file inventory | none |
| SRC-02 | doc | `README.md` | `9a0bae8` | doctrine/design + reported operation | full (442 lines) | production numbers unverifiable here |
| SRC-03 | doc | `CLAUDE.md` | `9a0bae8` | doctrine/design | full (732 lines) | — |
| SRC-04 | code | `src/core/minions/handlers/subagent.ts` | `9a0bae8` | implementation | full (1,275 lines) | — |
| SRC-05 | code | `src/core/minions/worker.ts` | `9a0bae8` | implementation | lines 1–470 read; rest scanned by grep | tail of file not line-read |
| SRC-06 | code | `src/core/minions/queue.ts` | `9a0bae8` | implementation | `claim`, `handleTimeouts`, schedule columns | ~1,200 lines not line-read |
| SRC-07 | code | `src/core/cycle.ts` | `9a0bae8` | implementation | header + `CyclePhase` + `ALL_PHASES` + lock/scope commentary | body of phase dispatch not line-read |
| SRC-08 | code | `src/core/think/prompt.ts` | `9a0bae8` | implementation | full (227 lines) | — |
| SRC-09 | code | `src/mcp/dispatch.ts` | `9a0bae8` | implementation | full (284 lines) | — |
| SRC-10 | code | `src/core/facts/meta-hook.ts` | `9a0bae8` | implementation | full (133 lines) | — |
| SRC-11 | code | `src/core/facts/decay.ts` | `9a0bae8` | implementation | full (63 lines) | — |
| SRC-12 | code | `src/core/facts/extract.ts` | `9a0bae8` | implementation | header + config gates (lines 1–70) | body not line-read |
| SRC-13 | doc | `docs/takes-vs-facts.md` | `9a0bae8` | doctrine/design + reported operation | full (94 lines) | 2026-05-10 extraction run is reported, not observed here |
| SRC-14 | code | `src/core/skillopt/{apply-edits,audit}.ts` | `9a0bae8` | implementation | headers | rest of `skillopt/` not line-read |
| SRC-15 | file | `templates/{SOUL,HEARTBEAT,USER,ACCESS_POLICY}.md.template` | `9a0bae8` | doctrine/design | SOUL + HEARTBEAT heads | USER/ACCESS_POLICY not read |
| SRC-16 | dir | `skills/` (125 files incl. `RESOLVER.md`, `manifest.json`, `_brain-filing-rules.md`) | `9a0bae8` | implementation + doctrine | inventory only | individual SKILL.md bodies not read |
| SRC-17 | code | `src/core/search/*` (30 files) | `9a0bae8` | implementation | inventory only | `hybrid.ts` (1,870 lines) not line-read |
| SRC-18 | code | `src/core/operations.ts` | `9a0bae8` | implementation | referenced via `dispatch.ts` + `CLAUDE.md` invariants | 4,751 lines not line-read |

Targeted reads inside the frozen boundary are permitted, but they must be reported back to the
orchestrator for central registration; they invalidate affected downstream findings.

## 6. Canonical records registered so far

### Components (`CMP-*`)

| ID | Component | Substrate | Form |
|---|---|---|---|
| CMP-01 | Minions job queue (`minion_jobs` + `MinionQueue`) | Postgres/PGLite tables | symbolic (SQL + TS) |
| CMP-02 | MinionWorker (in-process concurrent poller) | Node/Bun process | symbolic (TS) |
| CMP-03 | Minion supervisor / child-worker supervisor | OS processes | symbolic (TS) |
| CMP-04 | Subagent LLM tool loop handler | Node/Bun process + provider API | mixed (TS + prompt) |
| CMP-05 | AI gateway (`src/core/ai/gateway.ts`) | in-process module | symbolic (TS) |
| CMP-06 | Brain tool registry / allowlist | in-process module | symbolic (TS + JSON schema) |
| CMP-07 | Dream/maintenance cycle orchestrator (`runCycle`) | in-process module | symbolic (TS) |
| CMP-08 | Hybrid retrieval stack (vector + BM25 + RRF + rerank + graph signals) | Postgres/pgvector + provider APIs | symbolic (TS + SQL) |
| CMP-09 | `think` synthesis pipeline | in-process module + provider API | mixed (TS + prompt) |
| CMP-10 | Facts hot-memory subsystem | `facts` table | symbolic + natural-language rows |
| CMP-11 | Takes cold-storage subsystem | `takes` table | symbolic + natural-language rows |
| CMP-12 | Brain repo (markdown, system of record) | git repo on disk | natural-language |
| CMP-13 | Engine layer (`BrainEngine`: PGLite / Postgres) | database | symbolic |
| CMP-14 | Operation contract + MCP dispatch | in-process module | symbolic (TS) |
| CMP-15 | Schema packs (`gbrain-base-v2` etc.) | config + files | symbolic (declarative pack) |
| CMP-16 | Skillpack (43 skills + RESOLVER) | markdown files in agent workspace | natural-language (prompt-consumed) |
| CMP-17 | SkillOpt optimizer | in-process module + provider API | mixed |
| CMP-18 | Contradiction eval (`eval-contradictions`) | in-process module + provider API | mixed |
| CMP-19 | Calibration profile builder | in-process module + provider API | mixed |
| CMP-20 | Audit/JSONL trail (`~/.gbrain/audit/*.jsonl`) | filesystem | symbolic |

### Operative objects (`OBJ-*`)

| ID | Object | Substrate | Form | Producer | Consumer |
|---|---|---|---|---|---|
| OBJ-01 | Page (markdown + frontmatter + timeline) | git repo + `pages` table | natural-language | user, agent, dream cycle | retrieval, think, sync |
| OBJ-02 | Chunk + embedding | `chunks` table / pgvector | distributed-parametric + text | chunker + embedding provider | vector search |
| OBJ-03 | Typed graph edge (`attended`, `works_at`, …) | `links` table | symbolic | auto-link on every page write (no LLM) | graph query, graph signals |
| OBJ-04 | Fact row (hot memory) | `facts` table | natural-language + typed fields | per-turn Haiku/Sonnet extractor | `recall`, MCP `_meta.brain_hot_memory` |
| OBJ-05 | Take row (cold, attributed claim) | `takes` table | natural-language + typed fields (`kind`, `holder`, `weight`, `since`) | LLM extraction from pages; consolidate bridge | `think`, takes CLI/MCP, grading |
| OBJ-06 | Synthesis answer (+ citations + gaps) | `think` output, optionally a saved page | natural-language | `think` LLM call | user / calling agent |
| OBJ-07 | Structured citation `(page_slug, row_num)` | `synthesis_evidence` | symbolic | `think` structured output | citation persistence, cite-render |
| OBJ-08 | Gap statement | `think` output field | natural-language | `think` LLM call | user; `--rounds N` follow-up |
| OBJ-09 | Take verdict (graded) | takes grading rows | symbolic + natural-language | judge model in `grade_takes` | calibration profile |
| OBJ-10 | Calibration profile (pattern statements + bias tags + Brier) | profile store | natural-language + symbolic | `calibration_profile` phase | `think` prompt (`<calibration>` block) |
| OBJ-11 | Suspected-contradiction record | contradictions cache | symbolic + natural-language | query-conditioned LLM judge | dream cycle report, agent |
| OBJ-12 | Subagent conversation turn | `subagent_messages` | natural-language blocks (JSONB) | subagent loop | crash replay |
| OBJ-13 | Tool execution record | `subagent_tool_executions` | symbolic | subagent loop | crash replay |
| OBJ-14 | SKILL.md | markdown file | natural-language (prompt) | maintainers; SkillOpt | host agent platform |
| OBJ-15 | SOUL.md / HEARTBEAT.md / USER.md / ACCESS_POLICY.md | markdown file | natural-language (prompt) | `soul-audit` skill | host agent platform |
| OBJ-16 | Schema pack | declarative pack file | symbolic | maintainers; `schema detect`/`suggest`/`review-candidates` | parse, extract, route, cache key |
| OBJ-17 | Job row | `minion_jobs` | symbolic | submitters | worker claim |
| OBJ-18 | Audit event (JSONL) | filesystem | symbolic | handlers, skillopt, batch-retry | `gbrain doctor` |
| OBJ-19 | Query cache row | `query_cache` | symbolic + vector | hybrid search | hybrid search |
| OBJ-20 | Atom / concept page (lens packs) | pages | natural-language | `extract_atoms`, `synthesize_concepts` phases | retrieval |

### Routes (`RTE-*`)

| ID | Route | Kind | Endpoints |
|---|---|---|---|
| RTE-01 | Job submit → claim → handler → complete/fail/dead | control | submitter → `minion_jobs` → MinionWorker → handler |
| RTE-02 | Subagent turn loop (LLM call → tool dispatch → persist → next turn) | control + action | handler → provider API → brain tools → DB |
| RTE-03 | Cron/daemon → dream cycle → ordered phases | control | cron/`autopilot`/`autopilot-cycle` job → `runCycle` → phase functions |
| RTE-04 | Query → hybrid retrieval → ranked chunks | context | caller → search stack → `pages`/`chunks`/`links` |
| RTE-05 | `think`: gather → merge → synthesize | context + truth-apt | question → pages/takes/graph/trajectory/calibration → LLM → answer+citations+gaps |
| RTE-06 | Conversation turn → fact extraction → `facts` table | state (write) | host agent turn → extractor → DB |
| RTE-07 | Any MCP tool call → `_meta.brain_hot_memory` injection | context (read-back, push) | dispatcher → `facts` → tool response |
| RTE-08 | `recall` op → facts | context (read-back, pull) | agent → `facts` |
| RTE-09 | Facts → dream `consolidate` → takes | state (promotion) | `facts` → LLM consolidation → `takes` |
| RTE-10 | Pages → `propose_takes` → review queue → accepted takes | truth-apt | markdown → LLM proposal → human gate → `takes` |
| RTE-11 | Unresolved takes → `grade_takes` (evidence retrieval + judge) → verdicts | checking | `takes` → retrieval → judge model → verdicts |
| RTE-12 | Verdicts → `calibration_profile` → profile → `think` prompt | state + context | verdicts → aggregation → `<calibration>` block |
| RTE-13 | Retrieval pairs → contradiction judge → conflict records | checking | `pages`/`takes` → date pre-filter → judge → cache |
| RTE-14 | Page write → auto-link (regex, no LLM) → typed edges | state (write) | `put_page` → link extraction → `links` |
| RTE-15 | Brain repo git → `sync` → DB (soft deletes) | state | git → import → `pages`/`chunks` |
| RTE-16 | MCP request → scope/localOnly/trust/source-isolation gate → op handler | authority | client → transport → dispatch → operations |
| RTE-17 | Skillpack install → host agent workspace → prompt context | context (static) | installer → `skills/` in workspace → host agent |
| RTE-18 | SkillOpt: benchmark → proposed edits → score → accept/reject → SKILL.md | checking + state | skill + benchmark → optimizer → validate-gate → version store |
| RTE-19 | Schema pack activation → parse/extract/route/cache-key behavior | control + state | pack → every read and write path |
| RTE-20 | Handler events → JSONL audit → `gbrain doctor` checks | observability | handlers → files → doctor |

### Behavioral-authority paths (`BAP-*`)

Definition in force: one consumption path's **consumer**, **channel**, and **force**, plus this run's
`horizon` field.

| ID | Consumer | Channel | Force | Horizon |
|---|---|---|---|---|
| BAP-01 | Host agent platform LLM (OpenClaw/Claude Code/Codex) | skillpack markdown loaded into workspace prompt | advisory instruction (model may deviate) | every session where the skillpack is installed |
| BAP-02 | Host agent platform LLM | `SOUL.md`/`HEARTBEAT.md` identity + cadence files | advisory instruction | persistent until regenerated by `soul-audit` |
| BAP-03 | Subagent loop model | `buildSystemPrompt(toolDefs, data.system)` system block | advisory instruction | one subagent job |
| BAP-04 | Subagent loop model | tool schemas (`input_schema`) in the API request | advisory shape; enforced server-side on execution | one subagent job |
| BAP-05 | Brain tool executor | `filterAllowedTools` / `allowed_slug_prefixes` / `PROTECTED_JOB_NAMES` | binding enforcement (code refuses) | one subagent job |
| BAP-06 | MCP operation dispatcher | `scope: read/write/admin` + `localOnly` + `OperationContext.remote` | binding enforcement (pre-handler) | every remote MCP call |
| BAP-07 | Read-side operations | `sourceScopeOpts(ctx)` source isolation, `takesHoldersAllowList` | binding enforcement (SQL predicate) | every read op |
| BAP-08 | `think` synthesis model | `THINK_SYSTEM_PROMPT_BASE` hard rules (cite everything, surface conflicts, name gaps, never instruct) | advisory instruction | one `think` call |
| BAP-09 | `think` synthesis model | `<take>` contents declared DATA, not instructions; `INJECTION_PATTERNS` sanitizer | advisory instruction + partial code enforcement | one call |
| BAP-10 | Human operator | `propose_takes` review queue; `schema review-candidates`; SkillOpt bundled-skill gate (`proposed.md`) | binding gate (no write without accept) | per proposal |
| BAP-11 | Worker scheduler | quiet hours, rate leases, budget tracker, RSS watchdog, lock fencing | binding enforcement | continuous |
| BAP-12 | Downstream agent | `_meta.brain_hot_memory` on tool responses | advisory context (client may ignore unknown `_meta`) | per tool call, 30s cache |

## 7. Vocabulary in force

- Conclusion statuses: `absent`, `inapplicable`, `uninspected`, `claimed`, `implemented`, `observed`, `causally supported`.
- Never upgrade: context presence → activation; implementation → observed operation; observation → causality; operational continuation → warrant.
- **Memory read-back** = material accumulated or changed through use returns to a later invocation or action. Static shipped material (skills, tool specs, docs) and ordinary current-run state are retained state, not read-back.
- **Activation** = evidence that delivered material changed behavior, not merely that it entered context.
- **Truth-apt** = capable of truth or falsity.
- Keep **behavioral**, **epistemic**, and **operational** authority separate.
