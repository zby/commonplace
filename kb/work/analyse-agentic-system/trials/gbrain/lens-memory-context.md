# Memory/context lens — RUN-GBRAIN-20260820

> **Provenance note (trial apparatus, not part of the lens result).** The memory/context lens worker
> completed this analysis and returned it to the orchestrator, but both the worker and the
> orchestrator were terminated by a usage limit before the file was written to disk. This file was
> recovered verbatim from the worker's returned report. No content was added, and no finding was
> altered. Formatting may differ in trivial ways from the worker's original file layout.

Lens worker output. Boundary, revision, and IDs as given in the evidence packet. No system execution; no reads outside the frozen checkout except the packet.

---

## 0. Scope note and one packet correction

Two packet facts did not survive targeted inspection and should be corrected centrally before publication:

| Packet claim | Inspected reality | Status | Anchor |
|---|---|---|---|
| SRC-16: `skills/` "(43 skills…)"; boundary table "43 skills" | 53 directories, **51** `SKILL.md` files, 125 files total | `implemented` | `skills/` tree listing |
| CMP-16 "Skillpack (43 skills + RESOLVER)" | `skills/manifest.json` declares `version: 0.32.3.0` and lists **50** skills, while `VERSION` is `0.42.25.0` — the manifest is stale relative to the tree | `implemented` | `skills/manifest.json:1-5`; `VERSION` |

Also note: `src/schema.sql` does **not** define `facts`, `takes`, or `query_cache` — `facts` (migration v40), `takes` (v37), and `query_cache` (v55/v56) are defined only inside the `MIGRATIONS` array in `src/core/migrate.ts`. Any inventory keyed on `schema.sql` alone will miss the three most memory-relevant tables.

---

## 1. Inventory of retained operative parts

Split by content / form / producer / consumer / checks / authority path. `RB` column: **read-back** = accumulated or changed through use AND returns to a later invocation or action; **retained** = state that persists but does not return as input to a later model invocation or action; **static** = shipped material.

### 1.1 Facts subsystem (CMP-10 / OBJ-04)

| Part | Substrate | Form | Persistence | Lineage | Producer | Consumer | Invalidation / regeneration | Promotion path | RB | Status / anchor |
|---|---|---|---|---|---|---|---|---|---|---|
| `facts` row (hot memory) | Postgres/PGLite `facts` table | natural-language `fact` + typed fields (`kind`, `notability`, `visibility`, `confidence`, `valid_from/until`, `claim_metric/value/unit/period`) | durable, never deleted by consolidation | extracted from one conversation turn / page body | `extractFactsFromTurn` (Sonnet by default, `facts.extraction_model`) | `recall` op, `_meta.brain_hot_memory`, consolidate, trajectory | `expired_at`, `valid_until`, `superseded_by`; `forget` rewrites the markdown fence | → take via `consolidate` | **RB** | `implemented` — `src/core/migrate.ts:2288-2356`; `src/core/facts/extract.ts:149-254` |
| Facts **markdown fence** (`## Facts` block on the entity page) | git repo file | natural-language table rows | durable; system of record | same extraction, written to disk first | `writeFactsToFence` | `parseFactsFence` → DB reconcile on `extract_facts` / `rebuild` | fence is canonical; DB is an index rebuilt from it | — | **RB** (survives rebuild; the DB row does not) | `implemented` — `src/core/facts/fence-write.ts:1-46` |
| Decayed effective confidence | computed, not stored | numeric | per-call | derived from `kind` + age | `effectiveConfidence` | `recall`, `_meta` sort, supersession audit, `facts_health` | pure function; recomputed every read | — | **RB** (changes ordering of what returns) | `implemented` — `src/core/facts/decay.ts:25-56` (halflives: event 7d, commitment/preference 90d, belief/fact 365d) |
| Facts extraction eligibility predicate | in-process module | symbolic | n/a | n/a | `isFactsBackstopEligible` | `put_page`, sync, `file_upload`, `code_import`, `extract_facts` | type/slug/length gates; anti-loop `dream_generated` skip | — | static | `implemented` — `src/core/facts/eligibility.ts:70-98` |
| Facts extraction queue (bounded, in-memory) | process memory | symbolic | ephemeral | n/a | `getFactsQueue().enqueue` | extraction pipeline | cap 100, drop-oldest; drops on shutdown | — | retained (ephemeral) | `implemented` — `src/core/facts/queue.ts:1-40` |
| Facts absorb log | `ingest_log` table | symbolic reason codes | durable | failure events | `writeFactsAbsorbLog` | `gbrain doctor`, admin dashboard | none | — | retained (operator-facing) | `implemented` — `src/core/facts/absorb-log.ts:1-40` |
| Phantom-audit / stub-guard JSONL | `~/.gbrain/audit/*.jsonl` | symbolic | ISO-week rotated | guard fires | `logStubGuardEvent`, phantom pass | `gbrain doctor` | none; best-effort writes | — | retained | `implemented` — `src/core/facts/stub-guard-audit.ts:1-31` |
| `forget` state | fence strikethrough + `valid_until` | natural-language + symbolic | durable | user act | `forget_fact` op / CLI | fence parser → DB `expired_at` | legacy pre-v51 rows fall back to DB-only expire and **do not survive rebuild** | — | **RB** (suppresses later return) | `implemented` — `src/core/facts/forget.ts:1-33` |

### 1.2 Takes / calibration (CMP-11, CMP-19; OBJ-05, OBJ-09, OBJ-10)

| Part | Substrate | Form | Persistence | Lineage | Producer | Consumer | Invalidation | Promotion | RB | Status / anchor |
|---|---|---|---|---|---|---|---|---|---|---|
| `takes` row | `takes` table (+ page fence) | NL `claim` + `kind`/`holder`/`weight`/`since_date` | durable | (a) LLM extraction from pages, (b) `consolidate` bridge from facts | `consolidate`, `takes propose --accept`, `take add` | `think` gather (kw + vector), takes CLI/MCP, grading, emotional weight | `active=false`, `superseded_by`, `resolved_*` | facts → take (`kind='fact'`, `holder='self'`) | **RB** | `implemented` — `src/core/migrate.ts:1253-1289`; `src/core/cycle/phases/consolidate.ts:128-207` |
| `take_proposals` queue | `take_proposals` table | symbolic + NL | durable | LLM scan of markdown prose | `propose_takes` phase | **human** via `gbrain takes propose --accept` | idempotency key `(source_id, page_slug, content_hash, prompt_version)` | queue → canonical fence only on human accept | retained (gated) | `implemented` — `src/core/cycle/propose-takes.ts:1-37` |
| `take_grade_cache` verdict | `take_grade_cache` table | symbolic + NL | durable | judge model over retrieved evidence | `grade_takes` phase | calibration scorecard; auto-apply when opted in | prompt-version keyed | verdict → `takes.resolved_*` only when `cycle.grade_takes.auto_resolve.enabled` **and** confidence ≥ 0.95 | retained → RB via profile | `implemented`, **evidence stage is a declared stub** — `src/core/cycle/grade-takes.ts:1-35, 299-305` |
| `calibration_profiles` row | `calibration_profiles` table | NL pattern statements + kebab bias tags + Brier/accuracy/`domain_scorecards` JSONB | durable, append-only per run | aggregation over resolved takes | `calibration_profile` phase (Sonnet + voice gate, 2 retries → hand-written template) | `think` `<calibration>` block; cross-brain mounts | superseded by newer `generated_at` (latest wins; `published` is **not** filtered locally) | `published=true` gates cross-brain mount visibility only | **RB** (CLI path only — see §3) | `implemented` — `src/core/cycle/calibration-profile.ts:350-381`; `src/commands/calibration.ts:47-71` |
| `think_ab_results` | table | symbolic | durable | A/B of baseline vs calibration answer | `think-ab.ts` | eval reporting | — | — | retained | `implemented` — `src/schema.sql:1260-1273` |

Note the version strings: `GRADE_TAKES_PROMPT_VERSION = 'v0.36.1.0-stub'` and `CALIBRATION_PROFILE_PROMPT_VERSION = 'v0.36.1.0-stub'`. The judge prompt and the profile prompt both self-declare stub status at this revision (`src/core/cycle/grade-takes.ts:50`; `src/core/cycle/calibration-profile.ts:41`).

### 1.3 Pages and derived page classes (OBJ-01, OBJ-20)

Split by producer/authority, because they differ materially:

| Page class | Producer | Marker | Re-consumed by retrieval? | Anti-loop treatment | RB | Status / anchor |
|---|---|---|---|---|---|---|
| User-authored page | human, via git repo | none | yes | eligible for facts extraction | **RB** (acquired material) | `implemented` — `src/schema.sql:85-195` |
| Dream-generated page (synthesize phase) | Sonnet subagent under `allowed_slug_prefixes` | frontmatter `dream_generated: true` | yes (chunked, indexed) | **excluded** from facts extraction, atom extraction, and transcript discovery | **RB** | `implemented` — `src/core/cycle/synthesize.ts:1-27`; `src/core/facts/eligibility.ts:86-88`; `src/core/cycle/extract-atoms.ts:182,254,267`; `src/core/cycle/transcript-discovery.ts:57-72` |
| Synthesis-saved page (`think --save`) | `persistSynthesis` | citations in `synthesis_evidence` | yes | remote MCP callers **cannot** persist (`safeSave = remote ? false : …`) | **RB** | `implemented` — `src/core/operations.ts` `think` handler (`safeSave`/`safeTake`) |
| Atom page | `extract_atoms` phase (Haiku, 1-3 atoms per item) | `frontmatter.source_hash` (16-char sha256) | yes | idempotency by `source_hash`; `dream_generated` excluded | **RB** | `implemented` — `src/core/cycle/extract-atoms.ts:1-46` |
| Concept page | `synthesize_concepts` phase; tiers T1 ≥10 / T2 ≥5 / T3 ≥2 / T4 ≥1 atoms; Sonnet narrative for T1/T2, deterministic stub for T3/T4 | `type: concept` | yes | excludes `imported_from`-marked atoms | **RB** | `implemented` — `src/core/cycle/synthesize-concepts.ts:1-21` |
| Pattern page | `patterns` phase, single Sonnet subagent over recent reflections | topic slug from the model | yes | skipped below `min_evidence` | **RB** | `implemented` — `src/core/cycle/patterns.ts:1-19` |
| Stub / thin page | user or import | thin body | yes | `enrich_thin` develops ≤3 per source per tick; **default OFF** | **RB** | `implemented` — `src/core/cycle/enrich-thin.ts:1-30` |
| Phantom page (unprefixed root slug) | accidental writes | unprefixed slug | until redirected | redirect pass migrates fact rows + fence, soft-deletes, bounded 50/cycle | retained → removed | `implemented` — `src/core/cycle/phantom-redirect.ts:1-37` |
| `page_versions` snapshot | page write path | NL + JSONB | durable | — | **no consumer found in inspected surface** | `uninspected` (consumer) | retained | `implemented` (table) — `src/schema.sql:512-520`; consumer `uninspected` |

### 1.4 Index and graph state (OBJ-02, OBJ-03, OBJ-19)

| Part | Substrate | Form | Producer | Consumer | Invalidation | RB | Status / anchor |
|---|---|---|---|---|---|---|---|
| `content_chunks` + `embedding` (HNSW) | pgvector | distributed-parametric + text | chunker + embedding provider | vector search, `think` gather | `embedded_at` reset on content change; `content_chunks_stale_idx` | **RB** | `implemented` — `src/schema.sql:279-334` |
| `links` typed edge | `links` table | symbolic | auto-link on every page write, regex, no LLM | graph traversal (`think --anchor`), graph signals | recomputed on write; `pages_links_extracted_at_idx` | **RB** | `implemented` — `src/schema.sql:424-460` |
| `code_edges_chunk` / `code_edges_symbol` | tables | symbolic | `resolve_symbol_edges` phase (two-pass) | code retrieval | staleness columns | **RB** | `implemented` — `src/schema.sql:370-404` |
| Graph signals (adjacency 1.05×, cross-source 1.10×, session demote 0.95×) | computed at query time | numeric | `runPostFusionStages` | hybrid ranking | fail-open; floor-gated | **RB** (past use reshapes present ranking) | `implemented` — `src/core/search/graph-signals.ts:1-67` |
| `query_cache` row | `query_cache` table + embedding | symbolic + vector | `hybridSearch` write-back | `hybridSearch` lookup (cosine ≥ 0.92) | TTL 3600s; `knobs_hash` v3 folds mode + embedding column/provider; `hit_count`/`last_hit_at` bumped | **RB** — a prior search's *output* is returned verbatim to a later query | `implemented` — `src/core/migrate.ts:2873-2900` + v56 knobs_hash; `src/core/search/query-cache.ts:1-30, 76-80` |
| `page_aliases` / `slug_aliases` | tables | symbolic | ingest projection of frontmatter `aliases:` | query-side alias match | shared normalizer both sides (NFKC + lowercase + whitespace collapse) | **RB** | `implemented` — `src/core/migrate.ts:4803-5005`; `src/core/search/alias-normalize.ts:1-33` |
| `timeline_entries` | table | symbolic + NL | auto-timeline on write / meeting extraction | temporal retrieval, `think` time-window prompt | dedup key widened to `(page_id, date, summary, source)` | **RB** | `implemented` — `src/schema.sql:492-507` |
| `pages.emotional_weight` (salience) | `pages` column | numeric 0..1 | `recompute_emotional_weight` phase, deterministic formula over tags + active takes | salience ranking (`get_recent_salience`, `salience` sort, query-intent boost) | recomputed per cycle; `emotional_weight.high_tags` config override | **RB** | `implemented` — `src/core/cycle/emotional-weight.ts:96-135`; `src/core/types.ts:495`; `src/core/engine.ts:1247-1251, 2043` |
| `pages.last_retrieved_at` | `pages` column | timestamp | op-layer fire-and-forget write-back on `search`/`query`/`get_page` **only** (internal callers bypass) | LSD stale-page selection (`staleBias`), not ranking | 5-min throttle; default-on with `search.track_retrieval` escape hatch | **RB** (to a maintenance selection, not to a model's context) | `implemented` — `src/core/last-retrieved.ts:1-34, 173-204`; `src/core/engine.ts:885-886`; `src/core/postgres-engine.ts:1318-1385` |
| Trajectory points (derived over `facts` typed claims) | computed from `facts` rows with `claim_metric/value` + embeddings | symbolic + NL | `findTrajectory` engine query + `computeTrajectoryStats` | `think` `<trajectory>` block; `find_trajectory` op; `gbrain eval trajectory` | regression threshold 10% (env-tunable); drift score null under 3 embedded points | **RB** | `implemented` — `src/core/trajectory.ts:26-170`; `src/core/think/index.ts:315-398` |
| Recall cursor state | `~/.gbrain/recall-cursors/<source>[.watch].json` | symbolic | `recall --since-last-run` / `--watch` tick | next `recall` window selection | corrupt / future-shifted → null → 24h default; atomic tmp+rename | **RB** | `implemented` — `src/core/recall-cursor-state.ts:1-113` |

### 1.5 Execution / control state

| Part | Substrate | Form | Producer | Consumer | RB | Status / anchor |
|---|---|---|---|---|---|---|
| `subagent_messages` | table, JSONB `content_blocks`, `schema_version` 1/2 | NL blocks | subagent loop, persisted **before** tool dispatch | crash-replay of the *same job* | retained (replay of one job identity, not cross-task memory) | `implemented` — `src/schema.sql:914-936`; `src/core/minions/handlers/subagent.ts:554, 734, 768, 832-876, 1067, 1108` |
| `subagent_tool_executions` | table, two-phase ledger (`pending`→`complete`/`failed`) | symbolic | subagent loop | crash-replay; **also** queried by `synthesize` to learn which slugs children wrote | retained + **RB** for the synthesize orchestrator's write-back step | `implemented` — `src/schema.sql:941-967`; `src/core/cycle/synthesize.ts:6-11` |
| `minion_jobs` row | table | symbolic | submitters | worker claim, timeouts, `pg_notify` trigger | retained | `implemented` — `src/schema.sql:776-832, 1276-1289` |
| `minion_inbox` | table (`child_done` payloads) | symbolic | child workers | parent supervisor | retained | `implemented` — `src/schema.sql:835-844` |
| `dream_verdicts` | table, keyed `(file_path, content_hash)` | symbolic | Haiku "worth processing?" judge | `synthesize` transcript gate | **RB** (a past cheap verdict decides a later run's work) | `implemented` — `src/core/migrate.ts` v30; `src/core/cycle/synthesize.ts:4-6` |
| Audit JSONL family | `${GBRAIN_AUDIT_DIR:-~/.gbrain/audit}/<prefix>-YYYY-Www.jsonl` | symbolic | 16 call sites incl. graph-signals, skillopt, shell, supervisor, phantom, batch-retry | `gbrain doctor`, `search stats` (reads current + previous ISO week) | retained (operator/tool-facing, not model-facing) | `implemented` — `src/core/audit/audit-writer.ts:1-46` |
| `mcp_request_log` | table, redacted param **shape** only | symbolic | MCP dispatch | admin SSE, doctor | retained | `implemented` — `src/mcp/dispatch.ts:75-168` |
| `eval_contradictions_cache` | table, PK `(chunk_a_hash, chunk_b_hash, model_id, prompt_version, truncation_policy)` | symbolic verdict JSONB | query-conditioned contradiction judge | later probe runs (cost avoidance); dream report | **RB** (verdict reuse), plus report → agent | `implemented` — `src/schema.sql:1101-1112`; `src/core/pglite-engine.ts:3964-4011` |
| `eval_contradictions_runs` | table incl. full `report_json` | symbolic | probe runner | trend subcommand, doctor | retained | `implemented` — `src/schema.sql:1118-1135` |
| `op_checkpoints`, `import-checkpoint` | tables/files | symbolic | bulk ops | resumption | retained | `implemented` — `src/schema.sql:662-669` |

### 1.6 Instruction artifacts (CMP-16, OBJ-14, OBJ-15) — split by mutation authority

| Part | Substrate | Producer | Consumer | Mutation path | RB | Status / anchor |
|---|---|---|---|---|---|---|
| Shipped `skills/*/SKILL.md` (51 files) | markdown in agent workspace | maintainers | host agent platform prompt | none at runtime | **static** | `implemented` — `skills/` tree |
| `skills/RESOLVER.md` router | markdown | maintainers | host agent (dispatch table) | none at runtime | **static** | `implemented` — `skills/RESOLVER.md:1-40` |
| `skills/manifest.json` | JSON | maintainers | installer/skillpack tooling | none at runtime | **static** (stale vs tree, §0) | `implemented` |
| `skills/_brain-filing-rules.json` | JSON | maintainers | `synthesize` phase's `allowed_slug_prefixes` (single source of truth) | none at runtime | **static, but load-bearing for enforcement** | `implemented` — `src/core/cycle/synthesize.ts:14-17` |
| **SkillOpt-mutated `SKILL.md`** | same file, rewritten in place | SkillOpt optimizer after validation gate | host agent platform prompt on **every subsequent session** | accepted only when `selScore > bestScore + 0.05` on median-of-3 judged rollouts | **RB — instruction-level self-modification** | `implemented`, default OFF (`cycle.skillopt.enabled`) — `src/core/skillopt/validate-gate.ts:55-128`; `src/core/skillopt/version-store.ts:126-171`; `src/core/cycle.ts` `'skillopt'` phase |
| SkillOpt `versions/vNNNN_eE_sS.md` + `best.md` + `history.json` | files under `skills/<name>/skillopt/` | version store, 5-step ordered write | crash-resume; rollback source | `revertAllPending` on crash | retained | `implemented` — `src/core/skillopt/version-store.ts:1-30, 201-247` |
| SkillOpt `proposed.md` | file | optimizer under `--no-mutate` or bundled-without-flag | **human review** | never touches `SKILL.md` | retained (gated) | `implemented` — `src/core/skillopt/bundled-skill-gate.ts:53-100` |
| `SOUL.md` / `HEARTBEAT.md` / `USER.md` / `ACCESS_POLICY.md` | markdown templates instantiated in workspace | `soul-audit` skill (agent-run, human-triggered) | host agent platform prompt, persistent until regenerated | regenerate by re-running `soul-audit` | **RB** (generated from prior sessions, returns to all later sessions) | `implemented` — `templates/SOUL.md.template:1-40`; `templates/HEARTBEAT.md.template:1-30` |
| Schema pack (`gbrain-base`, `gbrain-base-v2`, …) | declarative pack file + config | maintainers | parse, extract, route, cache key, `calibration_domains` | `gbrain schema use <name>` | **static/config** | `implemented` — `src/core/schema-pack/loader.ts`, `load-active.ts`; consumed at `src/core/cycle/calibration-profile.ts:327-339` |
| Detected schema candidate (`schema detect`) | computed from `pages.source_path` prefixes + frontmatter type distribution | SQL heuristic, no LLM | `schema suggest`, `review-candidates` | recomputed on demand from disk | **RB** (brain shape reshapes its own type system proposal) | `implemented` — `src/core/schema-pack/detect.ts:1-40` |
| Suggested schema change (`schema suggest`) | LLM refinement over `runDetect` | Sonnet-class or heuristic fallback (confidence 0.5) | `review-candidates` → **human** | confidence < 0.6 must not auto-apply | retained (gated) | `implemented` — `src/core/schema-pack/suggest.ts:1-59` |
| `schema-suggest` cycle phase | wraps `runSuggest` | dream cycle | same queue | late-cycle | retained (gated) | `implemented` — `src/core/cycle.ts` `'schema-suggest'` |

### 1.7 Host-workspace live-context files (not in the packet's registers)

| Part | Substrate | Producer | Consumer | RB | Status / anchor |
|---|---|---|---|---|---|
| `memory/heartbeat-state.json` (awake flag, current location, `lastChecks`, `blockers`) | workspace JSON | heartbeat cron / other producers, **outside this checkout** | `generateLiveContext` → `systemPromptAddition` on **every** `assemble()` | **RB (push)** | `implemented` — `src/core/context-engine.ts:183-197, 413` |
| `memory/upcoming-flights.json` | workspace JSON | external producer | same | **RB (push)** | `implemented` — `src/core/context-engine.ts:199-207, 414` |
| `memory/calendar-cache.json` (+ `lastUpdated` staleness) | workspace JSON | external producer | same; >6h emits an explicit staleness warning line | **RB (push)** | `implemented` — `src/core/context-engine.ts:218-221, 334-341, 541-543` |
| `ops/tasks.md` `## Today` unchecked items | workspace markdown | human/agent | same; capped at 5 items, 1MB file guard | **RB (push)** | `implemented` — `src/core/context-engine.ts:381-407` |

`ingest()` on this engine is an explicit no-op (`src/core/context-engine.ts:566-569`) and `ownsCompaction: false` — so this engine reads workspace state but writes none of it, and delegates compaction to the OpenClaw runtime (outside the boundary).

### 1.8 Marked `uninspected`

- `page_versions` consumers — table exists, no reader found in the surface inspected.
- Full `src/core/search/hybrid.ts` (1,870 lines): the graph-signals and query-cache seams and the mode/knobs contract were read, not the fusion body. Ranking-stage ordering beyond the four stages named in `graph-signals.ts:27-33` is `uninspected`.
- `src/core/operations.ts` (4,751 lines): `think`, `recall`, `forget_fact`, `extract_facts` headers read. Other ops' read-back behavior is `uninspected`.
- Skillpack install/projection mechanics (RTE-17 endpoint side) — the installer path was not read.
- Everything under `test/`, `evals/`, `admin/` — excluded by boundary.

---

## 2. Write side vs read-back, separated

### 2.1 Write agency

| Write path | Agency | Trigger | Gate |
|---|---|---|---|
| Fact extraction from a turn / page write | **automatic** | `put_page`, sync import, `file_upload`, `code_import` (mode `queue`, fire-and-forget) | `facts.extraction_enabled` kill switch (default ON); eligibility predicate; anti-loop `dream_generated` |
| `extract_facts` MCP op | **manual** (agent-invoked) | explicit tool call | mode `inline`, returns truthful counts |
| Fact fence write | automatic, follows extraction | — | FS page-lock (`~/.gbrain/page-locks/<sha256>.lock`, PID-liveness + 5-min TTL, 5s timeout); atomic tmp + re-parse + rename |
| `forget_fact` | **manual** | user/agent | fence rewrite, falls back to DB-only for legacy rows |
| `consolidate` facts→takes | **automatic** | dream cycle phase | ≥3 unconsolidated facts per `(source_id, entity_slug)`; oldest ≥24h; cosine cluster ≥0.85; cluster size ≥2; entity page must exist |
| `propose_takes` | automatic proposal, **manual acceptance** | dream cycle | writes only to `take_proposals`; BAP-10 |
| `grade_takes` auto-apply | **manual opt-in** | `cycle.grade_takes.auto_resolve.enabled` = true AND confidence ≥ 0.95 | config tightening is free; loosening requires `--allow-loosen-confidence` |
| `calibration_profile` | automatic | dream cycle, after grade | ≥5 resolved takes; budget gate ($0.50 default); voice gate |
| Page write → auto-link, auto-timeline | automatic, regex, **no LLM** | every `put_page` | trusted-workspace branch re-enables these for subagent writes |
| `last_retrieved_at` bump | automatic, fire-and-forget, op-layer only | `search`/`query`/`get_page` | 5-min throttle; `search.track_retrieval` off-switch; internal callers bypass entirely |
| `query_cache` write | automatic | after a real hybrid search | keyed by `(source_id, query_text, knobs_hash)` |
| SkillOpt `SKILL.md` mutation | **automatic within an opt-in phase, human-gated for bundled skills** | `cycle.skillopt.enabled` (default OFF); benchmark stale AND `last_run_at` > 7d | bundled skills require `--allow-mutate-bundled` **and** a held-out set ≥ `MIN_HELD_OUT_SIZE`, else hard refusal |
| `SOUL.md`/`HEARTBEAT.md` | **manual** | operator runs `soul-audit` | none in code (skill-level) |
| Schema candidate promotion | **manual** | `schema review-candidates --apply` | confidence < 0.6 must not auto-apply |

### 2.2 Acquisition and index maintenance vs curation

**Acquisition / index maintenance** (no epistemic transformation claimed): git `sync` → `pages`/`chunks` import with soft deletes (RTE-15); chunking + embedding (`embed` phase, `embedded_at` staleness); auto-link regex edge extraction (RTE-14); alias projection; timeline materialization; `resolve_symbol_edges`; `query_cache` population; `last_retrieved_at`.

**Curation** (a model or a human decides what is worth keeping, at what strength): notability filter in the extractor prompt (`high` extract now / `medium` wait for batch / `low` skip entirely — `src/core/facts/extract.ts:124-131`); sync's `high-only` notability filter (`backstop.ts` D4); consolidate's cluster-representative selection (highest-confidence fact's text, *verbatim*, no LLM synthesis at this revision — `consolidate.ts:130-133`); `propose_takes` proposal set; `grade_takes` verdicts; calibration pattern statements; atom/concept tiering.

The consolidate step is worth naming precisely: the take's `claim` is a **copy of the best fact's text**, not a synthesis. The header itself flags "v0.31 ships without LLM synthesis to keep the cycle deterministic" (`consolidate.ts:9-12`). So the facts→takes edge is a **selection + re-typing + re-attribution** operation (`kind='fact'`, `holder='self'`, `weight = mean(confidence)`), not a semantic distillation. The label `consolidate` does not establish semantic preservation — it establishes a copy with a new authority attribution (`holder='self'`) and a new confidence number computed by averaging.

### 2.3 Named mechanisms

| Mechanism | Present? | How | Anchor |
|---|---|---|---|
| **Consolidation** | yes | greedy cosine clustering (threshold 0.85, first-member-as-centroid), ≥2 per cluster → one take; contributing facts marked `consolidated_at` + `consolidated_into`, **never deleted** | `consolidate.ts:128-290` |
| **Deduplication** | yes, several distinct kinds | (a) fact insert dedup at cosine 0.95 with supersede support (`backstop.ts:1-25`); (b) `takes` semantic upsert on `(page_id, claim, since_date)` to survive `extract_facts`'s delete-and-reinsert (`consolidate.ts:150-175`); (c) `take_proposals` idempotency on `(source_id, page_slug, content_hash, prompt_version)`; (d) atom idempotency on `frontmatter.source_hash`; (e) timeline `(page_id,date,summary,source)` unique index | multiple |
| **Evolution** | yes | bitemporal writeback: consolidate sorts each cluster chronologically and stamps each older fact's `valid_until = next_newer.valid_from`; newest keeps NULL | `consolidate.ts:209-238` |
| **Synthesis** | partial | present in `think`, `patterns`, `synthesize_concepts` (T1/T2 only), `calibration_profile`; **absent** in `consolidate` at this revision | `consolidate.ts:9-12` |
| **Invalidation** | yes | `expired_at`, `valid_until`, `superseded_by`, `active=false`, `deleted_at` soft delete + 72h purge, `query_cache` TTL + `knobs_hash` version bump, `eval_contradictions_cache.expires_at`, prompt-version cache-key bumps | multiple |
| **Decay** | yes, read-time only | `effectiveConfidence` exponential half-life per kind; nothing is written back | `decay.ts:44-56` |
| **Promotion** | yes, four ladders | facts→takes (automatic, thresholded); proposals→takes (human); verdicts→resolved takes (opt-in + 0.95); atoms→concepts (count tiers); candidate skill→`SKILL.md` (gated) or →`proposed.md` (human) | multiple |
| **Salience weighting** | yes | `emotional_weight` = tag boost 0.5 + take density 0.3 + avg weight 0.1 + user-holder ratio 0.1, capped at 1.0; deterministic, no LLM | `emotional-weight.ts:96-135` |

### 2.4 Raw traces vs distilled retained artifacts

| Raw trace | Distilled artifact | Is the raw kept? |
|---|---|---|
| Conversation turn text | `facts` row (≤500 chars, sanitized in and out) | No — the turn is not stored by this subsystem |
| Transcript file | dream verdict → synthesized page(s) + summary index; atoms | Yes, on disk in the corpus dir |
| `facts` rows | `takes` row | **Yes** — "NEVER DELETE"; facts stay as audit trail |
| Resolved takes | `calibration_profiles` narrative | Yes |
| Rollout trajectories | SkillOpt `selScore`, `history.json` edits | Trajectories scored then discarded from the version store; audit JSONL keeps per-task medians |
| Subagent turns | none | Yes, `subagent_messages` (until job row cascade-deletes) |

---

## 3. Annotation of runtime-owned context routes carrying read-back

Read-back direction is stated **from the receiving agent's perspective**. Per instruction, post-turn capture / consolidation is counted as write-side maintenance, not a second read-back point.

### RTE-07 — `_meta.brain_hot_memory` injection on every MCP tool response

| Field | Value | Status / anchor |
|---|---|---|
| Direction | **push** — the receiving agent does not ask; the dispatcher attaches it to whatever tool result it already requested | `implemented` — `src/mcp/dispatch.ts:255-267` |
| Selection signal | session-scoped facts first (`listFactsBySession`); if empty, source-wide facts from the last 24h (`listFactsSince`) | `implemented` — `meta-hook.ts:69-79` |
| Targeting | `(source_id, session_id)`; **not** query- or task-conditioned. Self-exclusion: skipped for `recall`, `extract_facts`, `forget_fact` | `implemented` — `meta-hook.ts:47, 49-53` |
| Selection scope + budget | top-K default 10, hard cap 25; sorted by **decayed** effective confidence before truncation | `implemented` — `meta-hook.ts:56, 85-88` |
| Delivery + consumption point | `ToolResult._meta` on a *successful* op; `content` shape unchanged. Cache key `(source_id, session_id, sorted takesHoldersAllowList)`, TTL 30s, invalidated by `bumpHotMemoryCache` after extraction | `implemented` — `meta-hook.ts:21-29, 107-120` |
| Visibility | remote → `['world']` only; local (`ctx.remote === false`) → all rows | `implemented` — `meta-hook.ts:66` |
| Behavioral-faithfulness test | **none found.** Failure degrades silently to no-`_meta`; the client may ignore unknown `_meta` entirely | `absent` (test), `implemented` (degradation) — `dispatch.ts:259-267` |

### RTE-08 — `recall` op → facts

| Field | Value | Status / anchor |
|---|---|---|
| Direction | **pull** — the agent issues the tool call | `implemented` — `src/core/operations.ts:3545-3655` |
| Selection signal | five mutually exclusive branches in priority order: `supersessions` → `entity` (via `resolveEntitySlug`) → `session_id` → `since` → unfiltered recent | `implemented` |
| Targeting | agent-supplied entity slug / session / time window; `grep` substring applied **client-side after** the DB query | `implemented` — recall handler, `if (grep) rows = rows.filter(...)` |
| Scope + budget | `limit` default 50, documented cap 100; `activeOnly` unless `include_expired` | `implemented` |
| Delivery | full JSON row projection incl. `confidence`, `notability`, `superseded_by`, `consolidated_into`; optional `pending_consolidation_count` piggy-back | `implemented` |
| Cursor coupling | `recall --since-last-run` reads/writes a per-source file cursor, `briefing` and `watch` variants kept separate so quitting a watch doesn't lose the briefing position | `implemented` — `recall-cursor-state.ts:1-35` |
| Behavioral-faithfulness test | **none found** | `absent` |

### RTE-04 — query → hybrid retrieval → ranked chunks

| Field | Value | Status / anchor |
|---|---|---|
| Direction | **pull**, with one push-shaped shortcut: a semantic cache hit returns a *prior call's* results without running retrieval | `implemented` — `query-cache.ts:1-30` |
| Selection signal | vector + BM25 + RRF + rerank, then four post-fusion stages including graph signals; alias match; recency decay; source boost; intent weighting; `emotional_weight` salience boost | `implemented` (seams read), fusion body `uninspected` |
| Targeting | free-text query, `source_id`-scoped; `sourceScopeOpts(ctx)` federated-array > scalar precedence | `implemented` — BAP-07 |
| Scope + budget | search mode bundle: `conservative` 4K tokens / limit 10, `balanced` 12K / 25, `tokenmax` off / 50 + LLM expansion. Resolution chain: per-call → per-key config → `MODE_BUNDLES[search.mode]` → `balanced` | `implemented` — `src/core/search/mode.ts`; described `CLAUDE.md` "Search Mode" |
| Cache correctness | `knobs_hash` (v3) folds mode bundle + active embedding column + provider, so a tokenmax write can't serve a conservative read and a Voyage-1024d row can't serve an OpenAI-1536d read; similarity ≥ 0.92; TTL 3600s | `implemented` — migration v56; `mode.ts:KNOBS_HASH_VERSION` |
| Read-back write-side coupling | `last_retrieved_at` bump (5-min throttled, fire-and-forget) — **write-side maintenance**, feeds LSD selection, not this call's context | `implemented` — `last-retrieved.ts:173-204` |
| Behavioral-faithfulness test | benchmark numbers exist (P@5 49.1%, R@5 97.9%, +31.4 P@5) but the runs live in the sibling `gbrain-evals` repo, outside the boundary | `claimed` — packet §4 |

### RTE-05 — `think`: gather → merge → synthesize

Three separately-wired read-back injections converge here; they must not be collapsed.

| Sub-route | Direction | Selection signal | Targeting | Scope / budget | Delivery point | Status |
|---|---|---|---|---|---|---|
| Pages stream | pull | hybrid search, `expansion: false` (think supplies its own anchor/graph context) | question text | `gatherLimit` 40; excerpt 600 chars each | `<pages>` block | `implemented` — `gather.ts:110-116, 184-195` |
| Takes streams | pull | keyword + vector over active takes, RRF-fused (k=60) on `(page_slug, row_num)` | question text (+ embedding when supplied) | `takesLimit` 30 | `<takes>` block, declared **DATA not instructions** | `implemented` — `gather.ts:118-163`; `prompt.ts:43-45` |
| Graph stream | pull | `traversePaths(anchor, depth 2, both)` | requires explicit `--anchor` | first 30 slugs | `<graph>` block | `implemented` — `gather.ts:139-153`; `think/index.ts:282-284` |
| **Calibration profile** | push into the call, **opt-in** | latest `calibration_profiles` row for holder, ordered `generated_at DESC LIMIT 1`; `published` is **not** filtered on the local path | `--with-calibration` flag; holder default `'garry'` | pattern statements + bias tags + Brier | `<calibration>` block, placed **after** retrieval and **before** the question; system prompt gains anti-bias instructions | `implemented` on the CLI path; **`absent` on the MCP path** — `think/index.ts:286-313`; `commands/think.ts:80,119`; the `think` op handler in `operations.ts` never sets `withCalibration` |
| **Trajectory** | push into the call, **default-on** | `classifyIntent(question)` must be `temporal` or `knowledge_update`; entity candidates extracted from question + retrieved slugs; `fallback_slugify` resolutions rejected | per-candidate, concurrency 3, 5s timeout each, `limit: 100` points | rendered `<trajectory>` block(s), joined | between retrieval/calibration and the question in both prompt shapes; emits `TRAJECTORY_INJECTED_N_POINTS` warning | `implemented` — `think/index.ts:315-398`; kill switch `think.trajectory_enabled` |

Behavioral-faithfulness tests on RTE-05: the system prompt carries four hard rules (cite everything, mark weight<0.5 or `kind=hunch` explicitly, surface both sides of a conflict, name gaps, never instruct) — these are *instructions*, not tests. The one code-side check is deterministic citation persistence: the model must emit a structured `citations` array, with a regex fallback in `cite-render.ts` recovering inline `[slug#row]` markers when it doesn't. Compliance with the four hard rules is `uninspected`.

### RTE-12 — verdicts → calibration profile → think prompt

Direction: push (write-side aggregation), then push at the `think` consumption point. **The chain's evidence stage is a declared placeholder at this revision**: `defaultEvidenceRetriever` returns a literal `[evidence retrieval not yet wired — v0.36.1.0 ship-state]` string containing only the take's own claim text (`grade-takes.ts:299-305`). The module header states most stub-judge verdicts will therefore be `unresolvable`. Combined with `auto_resolve` default-OFF, the takes reaching `resolved_*` in a default deployment arrive through some path other than this phase — which path is `uninspected`.

### PROPOSED-RTE-A — workspace live-context → host agent system prompt (every turn)

| Field | Value | Status / anchor |
|---|---|---|
| Direction | **push** — injected on every `assemble()`; the receiving agent never asks | `implemented` — `context-engine.ts:571-600` |
| Selection signal | file presence + freshness only; no query conditioning, no LLM, no ranking | `implemented` — `context-engine.ts:409-475` |
| Targeting | fixed paths under `workspaceDir`: `memory/heartbeat-state.json`, `memory/upcoming-flights.json`, `memory/calendar-cache.json`, `ops/tasks.md` | `implemented` |
| Scope + budget | ≤3 upcoming events (4h lookahead), ≤5 open tasks, attendee lists truncated at 3, every string sanitized to ≤100 chars with control chars stripped, tasks file capped at 1MB | `implemented` — `context-engine.ts:150-152, 371-378, 403, 383` |
| Delivery point | `AssembleResult.systemPromptAddition`, concatenated with the memory plugin's addition | `implemented` |
| Behavioral-faithfulness test | **partial and unusual**: the engine refuses to emit a concrete local time when the timezone is unmapped (`UNKNOWN_TZ` sentinel), rendering an explicit "Local time NOT computed" warning instead of a confidently-wrong value; it also emits a staleness warning when the calendar cache is >6h old. These are *honesty guards on the injected content*, not tests that the model acted on it | `implemented` — `context-engine.ts:171-179, 500-509, 541-543` |
| Note | the block ends with `> This block is computed on every turn. Trust it over compaction summaries…` — an explicit instruction to prefer this channel over the host's own memory | `implemented` — `context-engine.ts:546` |

---

## 4. Four separate findings per main read-back path

Statuses are never upgraded. "Deployed wiring" = the material actually reaches a live consumption point in a default configuration. "Activation" = evidence that delivered material changed behavior. "Causal effect" = evidence the change is attributable to the material.

### 4.1 Facts → `_meta.brain_hot_memory` (RTE-07)

| Finding | Status | Evidence | What the status blocks |
|---|---|---|---|
| **Context presence** | `implemented` | `meta-hook.ts:90-108` constructs a payload of up to 10 fact objects with id/text/kind/notability/entity/valid_from/decayed-confidence | — |
| **Deployed wiring** | `implemented` | Both transports pass the hook: `src/mcp/server.ts:46` and `src/commands/serve-http.ts:1576` | — |
| **Activation** | `uninspected` | Nothing executed. `_meta` is by design ignorable by clients (`dispatch.ts:20-26`), so presence in the response is not presence in the model's attended context | Blocks: "the downstream agent's answers reflect hot memory." Cannot be asserted. |
| **Causal effect** | `uninspected` | No experiment; no A/B; the README production counts are `claimed` and their runs are outside the boundary | Blocks: "hot-memory injection improves agent behavior." Cannot be asserted at any strength. |

### 4.2 Facts → `recall` op (RTE-08)

| Finding | Status | Evidence | What the status blocks |
|---|---|---|---|
| **Context presence** | `implemented` | Full row projection returned by the handler | — |
| **Deployed wiring** | `implemented` | `recall` is a registered `scope: 'read'` operation, generated into both CLI and MCP surfaces by the contract-first pattern; `_meta` self-exclusion at `meta-hook.ts:47` confirms it is expected to be called by agents | — |
| **Activation** | `uninspected` | No trace of an agent choosing `recall` over `search` in any inspected artifact | Blocks: "agents actually pull hot memory rather than relying on the push channel." |
| **Causal effect** | `uninspected` | — | Blocks any claim that pull-based recall outperforms or complements push injection. |

### 4.3 Takes + graph → `think` synthesis (RTE-05, core streams)

| Finding | Status | Evidence | What the status blocks |
|---|---|---|---|
| **Context presence** | `implemented` | `<pages>`/`<takes>`/`<graph>` blocks assembled in both prompt shapes (`prompt.ts:155-226`) | — |
| **Deployed wiring** | `implemented` | `think` op registered `scope: 'write'`, `mutating: true`; handler forwards source scope, allow-list, remote flag | — |
| **Activation** | `uninspected` | The prompt *asks* for citation of every claim and explicit hunch-marking; whether output complies is not inspected. One partial code-side signal exists: `cite-render.ts` implements a regex fallback for models that omit the structured `citations` field — the existence of that fallback is evidence the authors expected non-compliance, but it is not evidence of behavior | Blocks: "`think` output is faithfully grounded in the retrieved takes." |
| **Causal effect** | `uninspected` | — | Blocks: "typed/weighted takes improve synthesis over plain page retrieval." |

### 4.4 Calibration profile → `think` prompt (RTE-12 consumption point)

| Finding | Status | Evidence | What the status blocks |
|---|---|---|---|
| **Context presence** | `implemented` | `buildCalibrationBlock` renders Brier + patterns + bias tags; `buildThinkSystemPrompt` adds four anti-bias instructions (`prompt.ts:88-96, 113-130`) | — |
| **Deployed wiring** | **split**: `implemented` on the CLI path (`gbrain think --with-calibration`, `commands/think.ts:80,119`); **`absent` on the agent-facing MCP path** — the `think` op handler never passes `withCalibration`, and `think`'s declared `params` do not include a calibration flag | This is the sharpest structural finding in the lens. Blocks: "calibration is part of GBrain's agent-facing memory read-back." It is a human-CLI feature at this revision. |
| **Activation** | `uninspected` | — | Blocks: "surfacing prior + counter-prior changes the answer." |
| **Causal effect** | `uninspected`; and the upstream evidence stage is `implemented`-as-stub | `grade-takes.ts:299-305` returns a placeholder string as "evidence"; `auto_resolve` default OFF; both prompt versions self-label `-stub` | Blocks any claim that GBrain's calibration reflects a real forecasting track record. The pipeline shape exists; the evidence input does not. |

### 4.5 Trajectory → `think` prompt

| Finding | Status | Evidence | What the status blocks |
|---|---|---|---|
| **Context presence** | `implemented` | `formatTrajectoryBlock` output spliced into both prompt shapes at a single defined slot (`prompt.ts:132-154`) | — |
| **Deployed wiring** | `implemented`, **default ON**, but narrowly gated: only for `temporal` / `knowledge_update` intent, only for entities that resolve by a means other than `fallback_slugify`, only when typed-claim facts with `claim_metric`/`claim_value` exist | Blocks: "trajectory is generally available." It requires the extractor to have emitted metric-shaped claims. |
| **Activation** | `uninspected` | The code emits a `TRAJECTORY_INJECTED_N_POINTS` warning string — an *instrumentation* signal that injection happened, not that it mattered | Blocks: "the model's temporal claims are grounded in trajectory." |
| **Causal effect** | `uninspected` | `gbrain eval trajectory` exists as a CLI surface; no results in the boundary | Blocks any claim of regression-detection or drift-score utility. |

### 4.6 SkillOpt → `SKILL.md` → host agent (RTE-18 → RTE-17)

| Finding | Status | Evidence | What the status blocks |
|---|---|---|---|
| **Context presence** | `implemented` | Accepted candidate text is written verbatim to `SKILL.md`, the file the host platform loads into its prompt (`version-store.ts:159-160`) | — |
| **Deployed wiring** | `implemented`, **default OFF** and multiply gated | `cycle.skillopt.enabled` default false; bundled skills → `proposed.md` unless `--allow-mutate-bundled`; bundled in-place mutation hard-refuses without a held-out set ≥ `MIN_HELD_OUT_SIZE` (`bundled-skill-gate.ts:86-100`) | Blocks: "GBrain self-modifies its instructions in a default install." It does not. |
| **Activation** | `uninspected` | The acceptance rule is itself a *measurement*: median-of-3 judged rollouts per sel-task, accept only if `selScore > bestScore + 0.05` (`validate-gate.ts:118-121`). That is evidence the *candidate scored higher on a judged benchmark*, not evidence that a later live session behaved differently | Blocks: "an optimized skill changes downstream agent behavior in production." |
| **Causal effect** | `uninspected` | The related functional-area-resolver A/B (+13 to +17pp at 48% size) is a *different* artifact (`evals/functional-area-resolver/`, deliberately outside `skills/`) and its runs are outside the boundary | Blocks attributing any behavioral gain to the SkillOpt loop specifically. |

### 4.7 Workspace live context → host system prompt (PROPOSED-RTE-A)

| Finding | Status | Evidence | What the status blocks |
|---|---|---|---|
| **Context presence** | `implemented` | `formatContextBlock` output returned as `systemPromptAddition` (`context-engine.ts:495-549, 598`) | — |
| **Deployed wiring** | `implemented`, **conditional on host configuration** — requires `plugins.slots.contextEngine: "gbrain-context"` in `openclaw.json`; outside OpenClaw the SDK import fails and the fallbacks return `undefined` memory addition (`context-engine.ts:90-94`) | Blocks: "GBrain injects live context for all host platforms." It is OpenClaw-specific and opt-in. |
| **Activation** | `uninspected` | The block instructs the model to trust it over compaction summaries; compliance not inspected | Blocks: "the time-warp bug class is fixed." The doctrine claims the motivation; the code shows the mechanism. |
| **Causal effect** | `uninspected` | — | Blocks any claim about compaction-loss mitigation. |

### 4.8 Query cache → search results

| Finding | Status | Evidence | What the status blocks |
|---|---|---|---|
| **Context presence** | `implemented` | A hit returns the stored `results` JSONB directly with no keyword search, vector search, expansion, RRF, or dedup (`query-cache.ts:4-11`) | — |
| **Deployed wiring** | `implemented`, on in all three shipped modes (`cache.enabled: true`, threshold 0.92, TTL 3600s) | — |
| **Activation** | `implemented`-as-mechanism, `uninspected`-as-behavior | The cache *is* the delivered context on a hit — there is no separate activation question for the retrieval stage. What is `uninspected` is whether the downstream model's answer differs | Blocks: "cache hits are behaviorally equivalent to fresh retrieval." Note the design history: two prior contamination bugs (mode cross-serving, embedding-provider cross-serving) were fixed by widening the key, which is evidence that equivalence was **not** initially true. |
| **Causal effect** | `claimed` only | "Cache hits cut all numbers ~50%" is a cost claim in `CLAUDE.md`, not an inspected measurement | Blocks quantitative cost or quality claims. |

---

## 5. Authority

Referencing the packet's BAP records, with consumer / channel / force / horizon kept explicit rather than substituted by a family label.

| BAP | Consumer | Channel | Force | Horizon | Lens annotation |
|---|---|---|---|---|---|
| BAP-01 | host platform LLM | skillpack markdown in workspace prompt | advisory instruction | every session where installed | 51 `SKILL.md` files; `RESOLVER.md` is a routing table, not enforcement. `_brain-filing-rules.json` is the one skillpack file that becomes **binding** downstream — `synthesize` reads it as the subagent `allowed_slug_prefixes` source, where BAP-05 enforces it in code. Same artifact, two force levels depending on channel. |
| BAP-02 | host platform LLM | `SOUL.md`/`HEARTBEAT.md` | advisory instruction | persistent until `soul-audit` regenerates | Templates ship with unresolved `<!-- Fill in via soul-audit -->` slots (`templates/SOUL.md.template:20-23`). An un-audited install carries literal placeholder text into the prompt. |
| BAP-03 | subagent loop model | `buildSystemPrompt(toolDefs, data.system)` | advisory instruction | one subagent job | Determinism is a hard requirement here *for cache-hit reasons*, not epistemic ones (`system-prompt.ts:14-21`). Caller can bypass the preamble entirely with `system_no_tool_preamble`. |
| BAP-05 | brain tool executor | `filterAllowedTools` / `allowed_slug_prefixes` / `PROTECTED_JOB_NAMES` | binding enforcement (code refuses) | one subagent job | The `synthesize` header states the allow-list is trusted **because** `PROTECTED_JOB_NAMES` prevents MCP from submitting `subagent` jobs — the binding force depends on a second, separate gate holding. |
| BAP-06 | MCP operation dispatcher | `scope` + `localOnly` + `OperationContext.remote` | binding enforcement, pre-handler | every remote MCP call | Fail-closed by type: `remote` is required and anything not strictly `false` is untrusted (`CLAUDE.md` cross-cutting invariants). Materialized in `dispatch.ts:205` (`remote: opts.remote ?? true`). |
| BAP-07 | read-side operations | `sourceScopeOpts(ctx)`, `takesHoldersAllowList` | binding enforcement (SQL predicate) | every read op | Token default is `{"takes_holders":["world"]}` — non-world takes hidden until explicitly granted (`migrate.ts` v38). The `_meta` hot-memory cache key includes the sorted allow-list hash so cached payloads cannot bleed across token tiers (`meta-hook.ts:8-9, 52-53`). |
| BAP-08 | `think` synthesis model | `THINK_SYSTEM_PROMPT_BASE` hard rules | advisory instruction | one `think` call | Four rules: cite everything, mark low-weight/hunch, surface both sides of conflicts, name gaps, never instruct. All advisory. Only the citation rule has a code-side recovery path. |
| BAP-09 | `think` synthesis model | `<take>` declared DATA + `INJECTION_PATTERNS` | advisory + partial code enforcement | one call | The sanitizer is reused as the single source of truth across takes, think, **and** fact extraction — applied to turn text on the way in *and* to each extracted fact on the way out (`extract.ts:155, 207`). Emits `SANITIZED_N_TAKE_CLAIMS` warnings. |
| BAP-10 | human operator | `propose_takes` queue; `schema review-candidates`; SkillOpt `proposed.md` | binding gate (no write without accept) | per proposal | Three independent human gates with different shapes: a DB queue, a disk-derived candidate list, and a file. The SkillOpt one is doubly bound — `assertBundledMutationHeldOut` *throws* rather than degrading (`bundled-skill-gate.ts:92-99`). |
| BAP-12 | downstream agent | `_meta.brain_hot_memory` | advisory context (client may ignore unknown `_meta`) | per tool call, 30s cache | The weakest authority in the system and the most-injected content. Correctly labeled advisory: there is no channel by which GBrain learns whether the payload was read. |

**Lineage/curation labels do not carry epistemic force.** Three cases where a label could be misread:

1. `consolidate` promotes facts to takes and stamps `holder='self'`. That is an **attribution assignment**, not an inference that the user holds the claim — the underlying fact may have been extracted from a third party's statement in a meeting transcript. The label does not establish that the take is warranted or that its meaning is preserved (the claim text is copied verbatim; only `weight` is newly computed, as a mean of confidences).
2. `sync` imports git markdown into `pages`/`chunks`. That is acquisition. Nothing in the import path evaluates the content.
3. `grade_takes` writes a "verdict". At this revision the verdict is produced against placeholder evidence. `verdict` names the row's role in the schema, not its epistemic standing.

`published` on a calibration profile is likewise an **exposure flag** for cross-brain mounts, not an acceptance mark: the local `think` path reads the newest profile regardless of `published` (`commands/calibration.ts:51-71` has no `published` predicate), while `cross-brain.ts:117-120` filters on it. Same field, two meanings; only the mount-side one is a gate.

---

## 6. Proposed new records for central registration

Proposed only — the orchestrator owns registration. None of these rename or re-inventory an existing record.

### Components

| Proposed ID | Component | Substrate | Form | Why it needs its own record |
|---|---|---|---|---|
| PROPOSED-CMP-01 | GBrain Context Engine (OpenClaw plugin, `createGBrainContextEngine`) | in-process module + host workspace files | mixed (TS + rendered NL block) | Carries a per-turn push read-back route into the host system prompt; no existing CMP covers it. Zero LLM calls, `ownsCompaction: false`. |
| PROPOSED-CMP-02 | Facts markdown-fence writer / parser (`fence-write.ts`, `facts-fence.ts`, `extract-from-fence.ts`) | git repo files + FS page-locks | natural-language table | CMP-10 covers the `facts` *table*; the fence is the declared system of record and has different persistence, different concurrency control, and different rebuild survival. |
| PROPOSED-CMP-03 | Trajectory subsystem (`trajectory.ts`, `trajectory-format.ts`, `findTrajectory`) | derived over `facts` typed-claim columns | symbolic + NL | Feeds a default-ON `think` injection slot; no existing CMP. |
| PROPOSED-CMP-04 | Shared audit-writer primitive + 16 consumers | filesystem JSONL, ISO-week rotated | symbolic | CMP-20 names the trail; this names the shared primitive and its `GBRAIN_AUDIT_DIR` override, current+previous-week read window, and best-effort posture. |

### Operative objects

| Proposed ID | Object | Substrate | Producer | Consumer |
|---|---|---|---|---|
| PROPOSED-OBJ-01 | Facts fence row (markdown table row on an entity page) | git repo file | `writeFactsToFence` | fence parser → DB reconcile; survives `rebuild` |
| PROPOSED-OBJ-02 | Trajectory point / `TrajectoryStats` (regressions + `drift_score`) | derived | `findTrajectory` + `computeTrajectoryStats` | `think` `<trajectory>` block, `find_trajectory` op |
| PROPOSED-OBJ-03 | `emotional_weight` salience score | `pages` column | `recompute_emotional_weight` phase | salience sort, `get_recent_salience`, query-intent boost |
| PROPOSED-OBJ-04 | `last_retrieved_at` retrieval-recency stamp | `pages` column | op-layer fire-and-forget write-back | LSD `staleBias` selection |
| PROPOSED-OBJ-05 | Recall cursor record (`{schema_version:1, last_run_iso}`) | `~/.gbrain/recall-cursors/*.json` | `recall --since-last-run` / `--watch` | next `recall` window |
| PROPOSED-OBJ-06 | Take proposal (queued, unaccepted) | `take_proposals` | `propose_takes` | human accept gate |
| PROPOSED-OBJ-07 | SkillOpt version snapshot + `history.json` row + `best.md`/`proposed.md` | files under `skills/<name>/skillopt/` | version store 5-step commit | crash-resume, rollback, human review |
| PROPOSED-OBJ-08 | Dream verdict (`is this transcript worth processing?`) | `dream_verdicts`, keyed `(file_path, content_hash)` | Haiku judge | `synthesize` gate on later runs |
| PROPOSED-OBJ-09 | Live-context block (`## Live Context (deterministic…)`) | rendered string | `formatContextBlock` | host system prompt, every turn |
| PROPOSED-OBJ-10 | Pattern page | `pages` | `patterns` phase Sonnet subagent | retrieval; distinct from OBJ-20 atoms/concepts |
| PROPOSED-OBJ-11 | Detected/suggested schema candidate | computed from disk + optional LLM | `runDetect` / `runSuggest` | `review-candidates` → human |

### Routes

| Proposed ID | Route | Kind | Endpoints |
|---|---|---|---|
| PROPOSED-RTE-A | Workspace state files → `assemble()` → `systemPromptAddition` | context (read-back, push), every turn | heartbeat/flights/calendar/tasks → context engine → host LLM |
| PROPOSED-RTE-B | Query → semantic query-cache hit → prior call's results | context (read-back, pull, bypasses retrieval) | query embedding → `query_cache` → caller |
| PROPOSED-RTE-C | Facts typed claims → `findTrajectory` → `<trajectory>` block | context (read-back, push into `think`) | `facts` → engine → `think` prompt |
| PROPOSED-RTE-D | Tags + active takes → `recompute_emotional_weight` → salience ranking | state → context | `tags`/`takes` → `pages.emotional_weight` → search ordering |
| PROPOSED-RTE-E | Retrieval op → `last_retrieved_at` → LSD stale-page selection | state (write) → maintenance selection | ops → `pages` column → `staleBias` query |
| PROPOSED-RTE-F | Transcript hash → `dream_verdicts` → later `synthesize` gate | checking + state | transcript → Haiku → cache → gate |
| PROPOSED-RTE-G | Unprefixed phantom page → redirect pass → canonical slug + migrated facts | state (repair) | `pages` → resolver → fence + DB migration |
| PROPOSED-RTE-H | Page write → fact fence → DB reconcile on `extract_facts`/`rebuild` | state (write, markdown-first) | write path → fence → `facts` |

### Behavioral-authority paths

| Proposed ID | Consumer | Channel | Force | Horizon |
|---|---|---|---|---|
| PROPOSED-BAP-A | Host platform LLM | `systemPromptAddition` from the context engine, incl. the explicit "trust it over compaction summaries" line | advisory instruction + advisory context | every turn, while the OpenClaw slot is configured |
| PROPOSED-BAP-B | SkillOpt acceptance | `runValidationGate` strict `> bestScore + 0.05` on median-of-3 judged rollouts | binding enforcement (candidate rejected in code) | one optimization step |
| PROPOSED-BAP-C | SkillOpt bundled-mutation | `assertBundledMutationHeldOut` (throws when held-out < `MIN_HELD_OUT_SIZE`) | binding enforcement (hard refusal, every entry point) | per run |
| PROPOSED-BAP-D | `grade_takes` auto-apply | `cycle.grade_takes.auto_resolve.enabled` + confidence ≥ 0.95 + tighten-only config ratchet | binding enforcement, default-closed | per verdict |
| PROPOSED-BAP-E | Facts extraction | `facts.extraction_enabled` kill switch + `isFactsBackstopEligible` + `dream_generated` anti-loop | binding enforcement (code refuses to extract) | every write surface |
| PROPOSED-BAP-F | Fence write path | FS page-lock (`~/.gbrain/page-locks/<sha256>.lock`, PID-liveness + 5-min TTL, 5s timeout) + atomic tmp/re-parse/rename | binding enforcement (multi-process serialization; DB not written when fence invalid) | per page write |

---

## 7. Files read inside the frozen checkout

All at `9a0bae8`, under `related-systems/gbrain/`. Read-only; nothing executed.

| File | Extent | What was taken |
|---|---|---|
| `CLAUDE.md` | full (auto-surfaced) | search-mode bundles + knobs_hash v3 contract, cost anchors, trust/source-isolation invariants, skills count claim (29), functional-area-resolver A/B numbers |
| `src/schema.sql` | index-grep + lines 279-334, 370-404, 424-460, 492-530, 662-669, 776-844, 905-980, 1101-1145, 1260-1344 | table inventory; chunks/links/timeline/page_versions/minion/subagent/contradiction schemas; RLS block; **confirmed `facts`/`takes`/`query_cache` are absent here** |
| `src/core/migrate.ts` | lines 1240-1330, 2280-2400, 2601-2640, 2865-2930, 4803-5005 (grep) | `facts` DDL v40 (incl. `row_num`/`source_markdown_slug` fence round-trip), `takes` DDL v37 + `synthesis_evidence`, `access_tokens.permissions` default v38, `query_cache` v55 + `knobs_hash` v56, alias tables |
| `src/core/facts/meta-hook.ts` | full (133) | RTE-07 payload shape, top-K/TTL, cache key incl. allow-list hash, visibility tiering, self-exclusion list |
| `src/core/facts/decay.ts` | full (63) | half-life table, read-time-only decay formula |
| `src/core/facts/extract.ts` | full (332) | extractor system prompt (kinds, notability tiers, typed-claim fields), sanitization in/out, Sonnet default, kill switch, 4-strategy JSON parse |
| `src/core/facts/eligibility.ts` | full (98) | eligible types union, rescue slug prefixes, `dream_generated` and `wiki/agents/` exclusions, 80-char floor |
| `src/core/facts/fence-write.ts` | header (60) | markdown-first invariant, page-lock, atomic write + quarantine |
| `src/core/facts/backstop.ts` | header (70) | five-surface choke point, queue vs inline modes, notability filter policy, provenance source enum |
| `src/core/facts/forget.ts` | header (45) | fence-rewrite forget, strikethrough parse contract, legacy DB-only fallback that does not survive rebuild |
| `src/core/facts/queue.ts` | header (40) | cap 100, per-session in-flight 1, shutdown drop semantics |
| `src/core/facts/absorb-log.ts` | header (45) | failure reason codes into `ingest_log` |
| `src/core/facts/stub-guard-audit.ts` | header (35) | ISO-week JSONL, two-file read window rationale |
| `src/core/cycle.ts` | lines 57-230 | `CyclePhase` union, full `ALL_PHASES` ordering + rationale comments, `PHASE_SCOPE` taxonomy, which phases are default-OFF |
| `src/core/cycle/phases/consolidate.ts` | full (297) | thresholds (3 facts / 24h / cosine 0.85 / cluster ≥2), verbatim-claim selection, semantic upsert key, chronological `valid_until` writeback, never-delete rule |
| `src/core/cycle/calibration-profile.ts` | full (406) | pattern/bias-tag prompts, voice gate + template fallback, ≥5-resolved floor, budget gate, `published: false` on insert, `domain_scorecards` pack resolution, `-stub` prompt version |
| `src/core/cycle/propose-takes.ts` | header (55) | queue-only posture, idempotency key, fence dedup, tuned prompt version + reported F1 |
| `src/core/cycle/grade-takes.ts` | header (60) + `defaultEvidenceRetriever` | **evidence-retrieval placeholder**, auto-resolve default-OFF, 0.95 threshold, tighten-only ratchet, `-stub` prompt version |
| `src/core/cycle/emotional-weight.ts` | full (142) | deterministic 0..1 formula and its four components; default high-emotion tag set |
| `src/core/cycle/synthesize.ts` | header (60) | dream verdict cache, subagent fan-out, allow-list source of truth, `subagent_tool_executions` slug harvest, cooldown key |
| `src/core/cycle/patterns.ts` | header (40) | reflection lookback, single-subagent design, trusted-workspace branch |
| `src/core/cycle/extract-atoms.ts` | header (60) | `source_hash` idempotency, budget, pack gating, known partial-write limitation |
| `src/core/cycle/synthesize-concepts.ts` | header (50) | tier thresholds, T1/T2 Sonnet vs T3/T4 stub narrative |
| `src/core/cycle/enrich-thin.ts` | header (50) | default-OFF, per-tick caps, budget/walltime structure |
| `src/core/cycle/auto-think.ts` | header (35) | default-disabled, cooldown key, **not wired into the main dispatcher** at this revision |
| `src/core/cycle/phantom-redirect.ts` | header (50) | phantom migration, 50/cycle bound, lock contract, idempotency |
| `src/core/think/gather.ts` | full (213) | four-stream gather, RRF k=60, limits 40/30, depth 2, per-stream failure isolation, block rendering |
| `src/core/think/prompt.ts` | full (226) | system prompt hard rules, output schema, calibration block, trajectory slot placement in both message shapes |
| `src/core/think/index.ts` | lines 250-428 + greps | gather wiring, calibration fetch + `NO_CALIBRATION_PROFILE` warning, trajectory gating/timeouts/concurrency, prompt assembly |
| `src/core/trajectory.ts` | full (170) | regression threshold + env override, drift score definition and null condition |
| `src/core/last-retrieved.ts` | full (204) | op-layer-only scope, 5-min throttle, config escape hatch, drain machinery |
| `src/core/recall-cursor-state.ts` | full (121) | two cursor variants, atomic write, null-return conditions |
| `src/core/context-engine.ts` | lines 1-611 (three reads) | live-context file set, sanitization, unknown-TZ refusal, staleness warning, `ingest` no-op, `assemble` output, "trust it over compaction" line |
| `src/openclaw-context-engine.ts` | full (66) | plugin registration shape, `plugins.slots.contextEngine` requirement |
| `src/mcp/dispatch.ts` | full (284) | `metaHook` invocation point and its isolation, param redaction + byte bucketing, `remote ?? true` default |
| `src/core/operations.ts` | `think` op block, `recall` op block (~3540-3660), `forget_fact` header | remote persist blocking, source-scope threading, absence of a calibration flag, recall branch order and caps |
| `src/commands/calibration.ts` | `getLatestProfile` + `formatProfileText` + op entry (~47-246) | no `published` predicate on local reads |
| `src/core/calibration/cross-brain.ts` | grep, lines ~6-120 | `published=true` mount-side filter |
| `src/core/search/query-cache.ts` | lines 1-120 | cache semantics, threshold/TTL defaults, row-id derivation with `knobs_hash` |
| `src/core/search/graph-signals.ts` | lines 1-90 | three signal magnitudes, floor gate, fail-open, audit-writer use |
| `src/core/search/alias-normalize.ts` | lines 1-56 | shared read/write normalizer |
| `src/core/skillopt/version-store.ts` | full (247) | 5-step commit ordering, crash-resume, `writeProposed` |
| `src/core/skillopt/validate-gate.ts` | full (176) | median-of-3, epsilon 0.05, must-abort handling |
| `src/core/skillopt/bundled-skill-gate.ts` | full (100) | bundled detection, mutate policy, hard-refusal on missing held-out |
| `src/core/schema-pack/detect.ts` | header (40) | SQL-only heuristic, privacy posture |
| `src/core/schema-pack/suggest.ts` | header (60) | LLM refinement, heuristic fallback confidence 0.5, <0.6 no-auto-apply rule |
| `src/core/schema-pack/review.ts` | header (50) | disk-derived candidates vs redacted audit |
| `src/core/audit/audit-writer.ts` | header (50) | ISO-week filenames, `GBRAIN_AUDIT_DIR`, best-effort, two-week read window, remote-deploy blind spot |
| `src/core/minions/system-prompt.ts` | header (60) | determinism-for-cache requirement, override paths |
| `src/core/minions/handlers/subagent.ts` | grep only (replay call sites) | replay ordering, persist-before-dispatch, stable-id shim |
| `skills/` | tree listing, `RESOLVER.md` lines 1-40, `manifest.json` head + counts | 53 dirs / 51 SKILL.md / 125 files; manifest version 0.32.3.0 listing 50 skills |
| `templates/SOUL.md.template`, `templates/HEARTBEAT.md.template` | heads (40 / 30) | placeholder slots, cadence beats referencing skill files and `gbrain` commands |
| `VERSION` | full | 0.42.25.0 |

Grep-only sweeps (no file substantively read): `emotional_weight` consumers across `src/`; `last_retrieved_at` readers; `dream_generated` call sites; `withCalibration` call sites; `metaHook` wiring; `createAuditWriter` consumers; `eval_contradictions_cache` engine methods.

---

## 8. Limitations, each paired with the conclusion it prevents

| # | Limitation | Exact conclusion it prevents |
|---|---|---|
| 1 | Nothing was executed (cold trial, read-only checkout). | Prevents any `observed` or `causally supported` status anywhere in this lens. Every activation and causal-effect finding in §4 is `uninspected` for this reason alone. |
| 2 | `src/core/search/hybrid.ts` (1,870 lines) was not line-read; only the graph-signals, query-cache, and mode seams. | Prevents "the ranking pipeline's full stage ordering and its interaction with `emotional_weight`, recency decay, autocut, and two-pass is as described." Only the four post-fusion stages named in `graph-signals.ts:27-33` are grounded. |
| 3 | `src/core/operations.ts` (4,751 lines) was read only at `think`, `recall`, `forget_fact`, `extract_facts`. | Prevents "the inventory of agent-facing read-back surfaces is complete." Other ops among the ~47 may carry read-back not seen — `get_recent_salience`, `find_anomalies`, `get_recent_transcripts`, `find_trajectory`, `whoknows` are all named in doctrine but their handlers are `uninspected`. |
| 4 | The host agent platform (OpenClaw, Claude Code, Codex, …) is outside the checkout. | Prevents "the injected `_meta`, skillpack, SOUL/HEARTBEAT, or live-context block reaches the model's attended context." Everything ends at GBrain's output boundary; the consumption side is unobservable here. This is the packet's own declared boundary character and it bites hardest on the push routes (RTE-07, RTE-17, PROPOSED-RTE-A). |
| 5 | `gbrain-evals` and `evals/functional-area-resolver/` runs are outside the boundary. | Prevents upgrading any benchmark number (P@5 49.1%, R@5 97.9%, +31.4 P@5, propose_takes 0.952/0.922 F1, resolver +13–17pp) above `claimed`. |
| 6 | `defaultEvidenceRetriever` is a declared placeholder and both calibration-wave prompt versions self-label `-stub`; whether any production path injects a real retriever was not traced. | Prevents "GBrain's calibration profile reflects a graded forecasting track record." Also prevents concluding the reverse — that no real retriever exists — since injection is a supported opt (`opts.evidenceRetriever`) and callers were not exhaustively traced. |
| 7 | Skillpack install / projection (RTE-17 producer side) was not read. | Prevents "the 51 shipped `SKILL.md` files are what a given install actually loads." The manifest's staleness (50 skills, version 0.32.3.0 vs VERSION 0.42.25.0) makes this gap load-bearing rather than cosmetic. |
| 8 | `page_versions` has a schema definition but no reader was found in the inspected surface. | Prevents both "page version history is read back" and "page version history is dead state." The consumer is `uninspected`, not `absent`. |
| 9 | Config defaults were read from code comments and header docs, not from a running config. Several read-back routes are gated by config keys (`think.trajectory_enabled`, `search.track_retrieval`, `cycle.skillopt.enabled`, `cycle.enrich_thin.enabled`, `cycle.grade_takes.auto_resolve.enabled`, `facts.extraction_enabled`, `search.mode`). | Prevents any claim about what a *particular deployment* has switched on. Every "default ON/OFF" in this report is a code-declared default, not an observed setting. |
| 10 | `src/core/minions/handlers/subagent.ts` was grep-read, not line-read (1,275 lines). | Prevents "crash replay is the only consumer of `subagent_messages`" — one additional consumer of `subagent_tool_executions` (the `synthesize` orchestrator) surfaced from a different file, which suggests there may be others not surfaced. |
| 11 | Only two of four `templates/*.md.template` files were read (`USER.md.template`, `ACCESS_POLICY.md.template` not read). | Prevents completing the OBJ-15 split — `USER.md` and `ACCESS_POLICY.md` remain `uninspected` as to producer, content shape, and whether either carries binding rather than advisory force. |
