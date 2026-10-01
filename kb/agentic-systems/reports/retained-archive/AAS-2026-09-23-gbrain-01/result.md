---
type: types/agentic-system-analysis-result.md
description: "Complete code-grounded analysis of GBrain v0.54.1.0 (memory, context delivery, skill distribution and self-maintenance layer around host harnesses) at 6040075c, complete-artifact partial-loop boundary"
run-id: AAS-2026-09-23-gbrain-01
system: "GBrain"
run-date: "2026-09-23"
result-disposition: complete
target-class: "memory/knowledge/context-engineering system"
boundary-kind: "complete artifact, partial loop"
reviewed-boundary: "6040075c6cb95be5881cc2e1b76ef7d71f4e5d29"
analysis-cutoff: "2026-09-23"
evidence-tier: code-grounded
memory-comparison:
  scope: 'Retained objects GBrain accumulates or changes through use: brain pages (Markdown files plus DB rows, chunks, embeddings), facts rows and `## Facts` fences, fact withdrawals, takes/take proposals/grade cache/calibration profiles, link and timeline edges, session_context_state, the raw transcript corpus (session-end, compaction-segment and writeback-turn files) and Stop live buffer, dream/think-generated pages, the bootstrap agent-workspace memory files (MEMORY.md, memory/ daily logs, USER.md, SOUL.md) as edited by the agent, brain-resident shared skill revisions, SkillOpt versions/best/proposed/history/rejected buffers and the SKILL.md files SkillOpt commits; plus access metadata (last_retrieved_at, context_volunteer_events). Routes: explicit remember/put_page/Markdown sync/workspace file edits, ambient Stop-hook writeback, compaction checkpoint harvest, session-end corpus plus serve sweep extraction, page-write facts backstop, dream-cycle phases, SkillOpt, shared-skill publish; maintenance by dedup, supersession, TTL, forget/withdrawal, decay-ranking, consolidation, purge; read-back through requested recall/search/query/entity/context_pack/delta/think/synthesize/get_skill and automatic hook push, MCP _meta hot memory, harness file imports and compile-context files. Statically shipped bundled skills, plugin trees and bootstrap templates are delivery artifacts and excluded; the Memorable procedure-extraction implementation is excluded.'
  axes:
    storage_substrate:
      assessment: known
      basis: wired
      values:
      - files
      - graph
      - rdbms
      - repo
      - vector
      records:
      - OBJ-1
      - OBJ-2
      - OBJ-4
      - OBJ-10
      - OBJ-16
      - OBJ-14
      - OBJ-17
      note: Pages and entity fact fences are Markdown files in a source content root (optionally Git) mirrored into PGLite/Postgres rows; facts, takes, session state and edges are relational rows; pgvector embeddings on chunks/facts/takes; typed link/timeline edges are traversed as a graph (stored in relational tables); the bootstrap workspace is a Git repo the hooks push; corpus files, SkillOpt stores and workspace memory are plain files. The 30s in-process hot-memory cache is a cache, not a store.
    representational_form:
      assessment: known
      basis: wired
      values:
      - natural-language
      - symbolic
      records:
      - OBJ-1
      - OBJ-2
      - OBJ-3
      - OBJ-4
      - OBJ-16
      - OBJ-14
      - OBJ-10
      note: 'Content consumed by later model calls is natural language (page bodies, fact claims, take claims, MEMORY.md, SKILL.md). Symbolic parts: typed edges, fact kind/entity/validity/metric fields, session cursors and banked entity lists, checkpoint link manifests, calibration scorecards/bias tags, grade verdicts. Embeddings are derived access structures (index vectors), not a distributed-parametric memory payload, so parametric is not assigned.'
    lineage:
      assessment: known
      basis: wired
      values:
      - authored
      - imported
      - other-compiled
      - trace-extracted
      records:
      - RTE-1
      - RTE-2
      - RTE-19
      - RTE-25
      - RTE-16
      - RTE-6
      - RTE-24
      - RTE-8
      - RTE-11
      - RTE-9
      - RTE-10
      - RTE-20
      note: 'authored: remember, put_page, workspace file edits, shared-skill publish. imported: Markdown repo sync and transcript/connector ingest. trace-extracted: facts from compaction segments, Stop-hook writeback turns and session-end transcripts; dream synthesize pages from the session corpus; SkillOpt versions from its own rollout trajectories. other-compiled: consolidate takes from facts, fence-to-DB fact reconciliation, page-write backstop facts, patterns from reflections, take proposals and grades from pages, calibration profiles from graded takes, auto-links, compile-context files.'
    behavioral_authority:
      assessment: known
      basis: wired
      values:
      - enforcement
      - instruction
      - knowledge
      - ranking
      - validation
      records:
      - OBJ-1
      - OBJ-2
      - RTE-5
      - BAP-8
      - BAP-4
      - BAP-5
      - OBJ-18
      - OBJ-19
      - RTE-11
      note: 'knowledge: pushed and pulled pages/facts arrive wrapped as ''data, not instructions''. instruction: MEMORY.md standing rules loaded by harness import each main session, SkillOpt-committed SKILL.md and followed shared skill revisions, and the calibration block that instructs think''s framing. ranking: decayed confidence orders hot facts; emotional weight/take count and backlinks boost search; last_retrieved_at breaks entity-card ties. enforcement: fact_withdrawals rows make later remember/extraction of the same claim fail. validation: retained SkillOpt benchmark and held-out sets gate acceptance of skill edits.'
    write_agency:
      assessment: known
      basis: wired
      values:
      - automatic
      - manual
      records:
      - RTE-1
      - RTE-2
      - RTE-25
      - RTE-16
      - RTE-6
      - RTE-24
      - RTE-9
      - RTE-8
      - RTE-11
      note: 'Manual: agent or operator calls remember/put_page/put_skill, edits workspace files, accepts take proposals. Automatic: Stop-hook writeback extraction, compaction checkpoint harvest, serve sweep corpus extraction, page-write facts backstop, dream phases, SkillOpt (including operator-triggered CLI runs, which remain automatic extraction).'
    curation_operations:
      assessment: known
      basis: wired
      values:
      - consolidate
      - decay
      - dedup
      - evolve
      - invalidate
      - promote
      - synthesize
      records:
      - RTE-1
      - RTE-7
      - RTE-8
      - RTE-9
      - RTE-11
      - RTE-4
      - CLM-7
      note: 'dedup: fingerprint and cosine>=0.95 candidate matching on every fact write. evolve: remember replaces a same-kind near-identical fact (supersede), pattern pages update in place, SkillOpt revises SKILL.md. consolidate: dream consolidate clusters >=2 facts and keeps the highest-confidence existing text. promote: that cluster becomes a take (hot facts to cold takes tier). synthesize: dream synthesize/patterns pages, think --save, calibration pattern statements. invalidate: forget/withdrawal, supersession expiry, TTL valid_until excluded at read time. decay: per-kind half-life downweights hot-memory ranking; GC of Stop buffer (7d) and corpus (30d), purge of soft-deleted pages. The LLM contradiction classifier is not wired (CLM-7).'
    read_back_direction:
      assessment: known
      basis: wired
      values:
      - pull
      - push
      records:
      - RTE-3
      - RTE-4
      - RTE-26
      - RTE-5
      - RTE-20
      note: 'Pull: recall/search/query/entity/context_pack/delta/synthesize/think/get_skill requested by the host agent or operator. Push: UserPromptSubmit and SessionStart hooks inject assembled context without a request; MCP responses carry _meta.brain_hot_memory; harness @imports load MEMORY.md and compiled context files each session.'
    read_back_signal:
      assessment: known
      basis: wired
      values:
      - coarse
      - identifier
      - inferred-lexical
      records:
      - RTE-5
      - RTE-20
      note: 'identifier: the session id selects that session''s facts for hot memory and that session''s banked standing entities and checkpoint links for the post-compaction pack. inferred-lexical: per-turn entity candidates from the last 4 turns resolved by alias/title/surname/slug-suffix match select pointers and volunteered pages. coarse: 24h recency fallback for hot facts, delta since the wake cursor, whole-file MEMORY.md import and allowlisted-section digest, compile-context prefix/tag/recency selection. No embedding or LLM judgment selects pushed parts.'
    trace_learning:
      assessment: known
      basis: wired
      values:
      - 'yes'
      records:
      - RTE-6
      - RTE-24
      - RTE-8
      - RTE-11
      note: 'Automatic trace-fed writes produce retained artifacts that later consumers receive: facts extracted from compaction segments, writeback turns and session-end transcripts reach later sessions through hot-memory push, entity cards, packs and recall; dream synthesize writes pages from session transcripts (opt-in by corpus-dir config); SkillOpt reflects over its own rollout trajectories and commits SKILL.md versions (CLI/MCP) or proposed.md (cycle).'
    trace_source:
      assessment: known
      basis: wired
      values:
      - session-logs
      - trajectories
      records:
      - RTE-6
      - RTE-24
      - RTE-8
      - RTE-11
      note: 'session-logs: harness transcript JSONL windows, gated user turns and session-end transcripts banked as corpus text. trajectories: SkillOpt rollout trajectories (final text plus tool calls) scored by a judge; optional captured production rollouts feed only the held-out gate.'
    learning_scope:
      assessment: known
      basis: wired
      values:
      - cross-task
      - per-task
      records:
      - RTE-6
      - RTE-24
      - RTE-5
      - RTE-8
      - RTE-11
      note: 'per-task: the PreCompact harvest feeds the same conversation''s post-compaction SessionStart re-entry (checkpoint links, banked standing entities, session-keyed hot facts), a continuation route rather than a session-id inference. cross-task: extracted facts, synthesized pages and optimized skills are read by any later session through recall, cards, packs, search and skill loading.'
    learning_timing:
      assessment: known
      basis: wired
      values:
      - offline
      - online
      - staged
      records:
      - RTE-6
      - RTE-24
      - RTE-8
      - RTE-11
      note: 'online: checkpoint harvest and Stop-hook writeback extraction run in the serve process during the session. offline: serve sweep corpus extraction, dream synthesize, operator-run SkillOpt. staged: dream-cycle SkillOpt always runs no-mutate and leaves proposed.md for review.'
    distilled_form:
      assessment: known
      basis: wired
      values:
      - natural-language
      - symbolic
      records:
      - RTE-6
      - RTE-24
      - RTE-8
      - RTE-11
      - OBJ-16
      note: 'natural-language: fact claims, synthesized pages, SKILL.md bodies. symbolic: structured fact fields (kind, entity_slug, validity, metric/value) and the checkpoint link manifest of verified page slugs banked in session_context_state.'
    faithfulness_tested:
      assessment: known
      basis: wired
      values:
      - 'no'
      records:
      - ABS-7
      - RTE-11
      - RTE-10
      note: No retained execution evidence in the frozen source tests whether later behavior depends on recalled content. Wired mechanisms could produce such evidence in a deployment (SkillOpt validation/held-out gates, the think calibration A/B table, volunteer-context usage stats), and retrieval benchmarks measure ranking, but none is retained here as a dependence test; a yes would need observed evidence.
---

# GBrain agentic-system analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-23-gbrain-01/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/gbrain-garrytan.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-23-gbrain-01/memory-report.md`

**Memory analysis report SHA-256:** 0051622a58b2fc0961f072803d7f78cd3b758f6ff3e78af198b4bf3e6b6e14a1

The caller asked for a refresh of `kb/agentic-systems/reviews/gbrain.md`. Destination inspection rejected that path as not a generated review of the same source (it is a legacy review), so this run publishes under the qualified slug above. The legacy review's prose was not read.

## Boundary and evidence

Intended use: a current, code-grounded account of GBrain as a whole system, including how it delivers its agent-facing parts (plugins, generated skill trees, scaffolded and stub skills, shared brain skills, bootstrap writes, upgrade handling) to host harnesses and projects.

Target class: memory/knowledge/context-engineering system that also ships an agent operating layer: a skill set with a resolver, harness hooks, a durable background job queue with an LLM sub-agent, a nightly maintenance cycle, and a skill optimizer. Boundary kind: `complete artifact, partial loop`. GBrain supplies memory, retrieval, context delivery, skills and background maintenance. The host harness (Claude Code, Codex, OpenClaw, Hermes, opencode and others) owns the main agent loop, the host model's decisions, skill activation and tool approval.

Functional inclusions: the `gbrain` CLI and operation contract; stdio and HTTP MCP servers and their dispatcher; persistence coordinator and both engines (PGLite, Postgres); retrieval, `think` synthesis, and push-context paths; fact, take and page write/curation routes; the dream cycle, autopilot and Minions queue; SkillOpt; the plugin generator, committed plugin trees, release publication of the `codex-plugin` branch; skillpack scaffold, harness bridge, stub skills and skill serving; shared brain skills and native router; bootstrap and in-agent install writers; self-upgrade, migrations and post-upgrade sweep.

Exclusions and the conclusions they prevent:

- Host harness internals (skill loading, hook execution, context assembly, permission prompts): prevent any claim that a delivered skill, hook output or instruction block was activated or changed host behavior.
- Model providers (Anthropic, Voyage, OpenAI and others): prevent claims about model internals, provider-side versioning of undated aliases, and output quality.
- The closed-source Memorable CLI and its remote extraction API: prevents any claim about procedure extraction, revision scoring or recall quality beyond GBrain's own capture hook and documentation.
- Claude and Codex marketplace services: prevent claims about how and when installed plugins refresh.
- The separate `gbrain-evals` repository and the author's production deployment: prevent verification of reported benchmark and scale figures.
- Deployed operation: no system was executed; all findings are implementation or doctrine, not observed runs.

Frozen revision: `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29` (v0.54.1.0, commit date 2026-09-23). Analysis cutoff: 2026-09-23. Evidence tier: code-grounded.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | Git | `https://github.com/garrytan/gbrain`; access root `/home/zby/llm/commonplace/related-systems/gbrain` | `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29` | Implementation: TypeScript under `src/`, `scripts/`, `.github/workflows/`, plugin manifests. Doctrine/design: `README.md`, `AGENTS.md`, `CLAUDE.md`, `docs/`, `skills/`. No observed-run or causal evidence. | Operation contract and MCP dispatch; persistence, facts, search, think, context and hook code; cycle, Minions, SkillOpt; skillpack, shared-skills, bootstrap, agent-install, upgrade; plugin generation and release workflow; memory-boundary, shared-skills, skillopt and memorable docs | Full commit-relative paths on the canonical records below, all at this revision | Worktree and current HEAD are never evidence. Large parts of `src/core` (company-brain, connectors, code-intel, google, schema-pack internals, admin SPA) were not read; they are not load-bearing here except where named. No dynamic execution, so no observed operation. |

## Shared records

### Components

CMP-1 — `gbrain` CLI, `src/cli.ts`. Implementation conclusion status: wired. Builds CLI commands from operation `cliHints` plus CLI-only commands, and runs every operation with `remote: false`, the trusted-local lane. First tries to delegate to a running `gbrain serve` over a local socket. Writes still require a verified local writer registration (see RTE-22). Source: SRC-1, `src/cli.ts:63-85,697-740,1569-1665`.

> // Local CLI invocation — the user owns the machine; do not apply remote-caller
> // confinement (e.g., cwd-locked file_upload).
> remote: false,
> --- `src/cli.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

CMP-2 — MCP servers and shared dispatcher: stdio `src/mcp/server.ts`, OAuth HTTP `src/commands/serve-http.ts`, legacy bearer HTTP `src/mcp/http-transport.ts`, all through `src/mcp/dispatch.ts`. Implementation conclusion status: wired. Every MCP call runs with `remote: true`. Surfaces (`verbs`, `starter`, `full`) filter the visible operation set; HTTP checks OAuth scopes at list and call time; `localOnly` operations dispatch only on stdio; `--source-guard` blocks writes without an explicit source binding. Source: SRC-1, `src/mcp/dispatch.ts:499-720`, `src/mcp/surface.ts:88-156`, `src/commands/serve-http.ts:2474-2604`.

> if (op.localOnly && opts.transport !== 'stdio') {
> return unknownToolEnvelope(name, opts.allowedOps);
> }
> --- `src/mcp/dispatch.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

CMP-3 — Operation contract, `src/core/operations.ts` and `src/core/ops/contract.ts`. Implementation conclusion status: wired. One registry of 100+ operations with `scope`, `requiredScopes`, `localOnly`, `mutating`, `verb` and a handler; CLI, MCP and `--tools-json` are generated from it. `OperationContext.remote` is required. Source: SRC-1, `src/core/operations.ts:1-4,126-221`, `src/core/ops/contract.ts:277-530`.

> * True when the caller is remote/untrusted (MCP over stdio/HTTP, or any agent-facing entry point).
> * False for local CLI invocations by the owner of the machine.
> --- `src/core/ops/contract.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

CMP-4 — Brain engine and persistence coordinator: PGLite (embedded Postgres via WASM) or Postgres with pgvector, behind `BrainEngine`; `src/core/persistence/*` admits page, fact and skill mutations through a write-request queue, write-through to Markdown files, and a trigger guard for legacy writers. Implementation conclusion status: wired. Symbolic code over an RDBMS plus Markdown files. Source: SRC-1, `src/core/persistence/memory-mutations.ts:47-148`, `src/core/persistence/page-prepare.ts:97-245`, `src/core/persistence/authority.ts:25-37`, `src/core/persistence/writer-guard-schema.ts:1`.

CMP-5 — AI gateway and distributed-parametric model components, `src/core/ai/gateway.ts`, `src/core/ai/defaults.ts`, `src/core/model-config.ts`. Roles: chat/synthesis (default `anthropic:claude-sonnet-4-6`; `think` resolves tier `deep` with fallback alias `opus` = `anthropic:claude-opus-4-7`), query expansion (`anthropic:claude-haiku-4-5-20251001`), embeddings (`voyage:voyage-4` at 1024 dimensions for new installs; legacy `zeroentropyai:zembed-1`), reranking (`voyage:rerank-2.5`), fact extraction, LLM judges, SkillOpt optimizer/target/judge tiers. Existence and call wiring: wired. Parameter changes during operation: absent within the searched boundary (ABS-6); GBrain issues inference calls only. Identity pinning: configurable defaults, none hard-pinned; the Haiku default names a dated snapshot, while the Sonnet, Opus, Voyage defaults are provider model names whose resolution is provider-controlled (uninspected). Provider internals: uninspected. Source: SRC-1, `src/core/ai/gateway.ts:128-129`, `src/core/ai/defaults.ts:44-60`, `src/core/model-config.ts:60-70`, `src/core/think/index.ts:488-493`.

> const DEFAULT_EXPANSION_MODEL = 'anthropic:claude-haiku-4-5-20251001';
> const DEFAULT_CHAT_MODEL = 'anthropic:claude-sonnet-4-6';
> --- `src/core/ai/gateway.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

> const modelUsed = await resolveModel(engine, {
> cliFlag: opts.model,
> configKey: 'models.think',
> tier: 'deep',
> fallback: 'opus',  // think is the high-stakes synthesis op; opus is the right default
> });
> --- `src/core/think/index.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

CMP-6 — Dream cycle, autopilot and Minions queue: `src/core/cycle.ts` and `src/core/cycle/*` run an ordered phase list (lint, backlinks, sync, synthesize, extract, extract_facts, extract_atoms, patterns, synthesize_concepts, consolidate, propose_takes, grade_takes, calibration_profile, drift, enrich_thin, skillopt, embed, orphans, schema-suggest, purge and others); `gbrain dream` runs one cycle; `gbrain autopilot` submits a cycle job per interval; `src/core/minions/*` provides a durable job queue whose `subagent` handler is crash-resumable. Implementation conclusion status: wired. Many LLM phases are off by default or gated by config. Source: SRC-1, `src/core/cycle.ts:61-202`, `src/commands/dream.ts:1-24`, `src/commands/autopilot.ts:1-17`, `src/core/minions/handlers/subagent.ts:1-24`.

> * crash-resumable: subagent_messages + subagent_tool_executions together
> * are the single source of truth about where the conversation is. On
> * resume after a worker kill, we load all committed rows, trust any tool
> * execution marked 'complete' or 'failed', and re-run 'pending' ones only
> --- `src/core/minions/handlers/subagent.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

CMP-7 — SkillOpt optimizer, `src/core/skillopt/*`. Implementation conclusion status: wired. Treats a `SKILL.md` body as the optimized artifact: target-model rollouts on benchmark tasks, two optimizer reflect calls (failures, successes), a judge-scored validation gate, versioned commit. See RTE-11. Source: SRC-1, `src/core/skillopt/orchestrator.ts:40-80,540-745`.

CMP-8 — Plugin generator and published plugin lanes: `scripts/generate-plugin-tree.ts` builds the committed `plugin/` and `plugin-variants/` trees; `scripts/check-plugin-tree.sh` gates drift; `.claude-plugin/`, `.codex-plugin/`, `.agents/plugins/marketplace.json`, `openclaw.plugin.json` and the shell launcher `.agents/gbrain-launcher` declare the lanes; `.github/workflows/release.yml` force-publishes a history-less `codex-plugin` branch. Implementation conclusion status: wired. Source: SRC-1, `scripts/generate-plugin-tree.ts:17-30,96-318`, `scripts/check-plugin-tree.sh:36-60`, `.github/workflows/release.yml:285-354`.

CMP-9 — Skillpack scaffold and harness bridge, `src/core/skillpack/*`, `src/commands/skillpack/*`. Implementation conclusion status: wired. Copies bundled skills into a workspace or into a harness's native skills directory, optionally as stubs, records install-time hashes for harness installs, and offers a read-only reference lens. Source: SRC-1, `src/core/skillpack/scaffold.ts:1-26,97-151`, `src/core/skillpack/harness-bridge.ts:1-31,283-313,604-730`, `src/core/skillpack/bridge-state.ts:1-64`.

CMP-10 — Shared brain skills: brain-resident skill packs with immutable revisions, publication policy and membership (`src/core/shared-skills/*`), the harness-side adapter that syncs authorized revisions into a local cache and renders a router skill, and `src/core/harness/native-router.ts`, which installs that router into the harness skills directory. Implementation conclusion status: wired. Source: SRC-1, `src/core/shared-skills/adapter.ts:48-200`, `src/core/harness/native-router.ts:27-78`, `src/core/shared-skills/publication.ts:28-32`.

CMP-11 — Bootstrap and in-agent install writers, `src/core/bootstrap/*`, `src/core/agent-install/*`, `templates/bootstrap/*`. Implementation conclusion status: wired. Write identity/instruction templates, harness hooks, MCP registrations and a marker-delimited instruction block, each with ownership receipts. Source: SRC-1, `src/core/bootstrap/render.ts:1-39`, `src/core/bootstrap/hooks.ts:1-25`, `src/core/bootstrap/host-specs.ts:184-239`, `src/core/bootstrap/instructions-block.ts:1-108`, `src/core/agent-install/setup.ts:120-298`.

CMP-12 — Upgrade machinery: `maybeEmitUpdateMarker` in `src/cli.ts`, `src/commands/check-update.ts`, `src/commands/upgrade.ts` (binary swap, `post-upgrade`, migrations, skill reference sweep), `src/commands/apply-migrations.ts`, `src/core/upgrade-checkpoint.ts`, and host-agent migration manuals in `skills/migrations/`. Implementation conclusion status: wired. Source: SRC-1, `src/cli.ts:351-412`, `src/commands/upgrade.ts:198-219,336-468,800-915`, `src/commands/migrations/index.ts:1-11`.

CMP-13 — Host harness and host model (excluded participant). Claude Code, Codex, OpenClaw, Hermes, opencode and others load GBrain skills, call MCP tools, run hooks and own the main loop. Conclusion status for activation of anything GBrain delivers: uninspected. Named so that routes can state where GBrain's responsibility ends.

### Operative objects

OBJ-1 — Pages. Markdown files in brain repositories plus DB page rows, chunks and embeddings; frontmatter typed by a schema pack. `put_page` stamps provenance fields (`source_kind`, `ingested_via`, `ingested_at`). Natural-language content with symbolic metadata; storage: files and RDBMS (with vector columns). Consumers: search, recall, think, context push, dream phases. Source: SRC-1, `src/core/persistence/page-prepare.ts:176-236`, `gbrain.yml`.

OBJ-2 — Facts. `facts` rows plus a page's `## Facts` fence; each carries provenance (`source`), `valid_from`, optional `valid_until` (TTL), visibility (`world` default, or `private`), embedding, `expired_at`, `superseded_by`, and withdrawal state. Natural-language claims with symbolic metadata. Source: SRC-1, `src/core/verbs.ts:106-162`, `src/core/persistence/memory-prepare.ts:28-90`, `src/core/facts/withdrawal.ts:11-86`.

> const visibility = typeof p.visibility === 'string' ? p.visibility : 'world';
> --- `src/core/verbs.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

Amendment (memory lens): the fence is canonical and the cycle reconciles DB rows from it (RTE-9). `source_session` is not stored in the fence, so a rebuilt row loses its session, and session-keyed hot-memory selection falls back to 24-hour recency (CLM-10). Source: SRC-1, `src/core/ops/facts.ts:46`, `src/core/cycle/extract-facts.ts:1-25`.

OBJ-3 — Takes, take proposals, grade cache and calibration profiles. Takes are held positions with conviction; `take_proposals` hold LLM-proposed takes pending human acceptance; `take_grade_cache` holds LLM verdicts; `calibration_profiles` hold Brier/accuracy scorecards plus voice-gated narrative statements and bias tags. Natural language plus numeric scores in RDBMS. Source: SRC-1, `src/core/cycle/propose-takes.ts:1-37`, `src/core/cycle/grade-takes.ts:1-33`, `src/core/cycle/calibration-profile.ts:1-24`.

OBJ-4 — Link and timeline edges. Typed graph edges and timeline entries extracted deterministically from page references on trusted writes, or added through `add_link`. Symbolic, RDBMS. Source: SRC-1, `src/core/persistence/page-prepare.ts:214`, `docs/guides/memory-boundaries.md`.

OBJ-5 — Bundled skill set (static, shipped). `skills/*/SKILL.md` with frontmatter `triggers:`, `skills/RESOLVER.md`, `skills/conventions/`, `skills/manifest.json`. Natural-language instructions; files in the repository and the installed package. Not memory: changed only by releases or by local editing of copies. Source: SRC-1, `skills/RESOLVER.md`, `skills/_AGENT_README.md:121-131`.

OBJ-6 — Generated plugin trees and manifests: `plugin/skills/`, `plugin-variants/gbrain-coding`, `plugin-variants/gbrain-daily`, each with a generated README version stamp and its own manifests and launcher; lane membership recorded with a reason per addition or exclusion in `skills/plugin-lanes.json`. Files; natural-language skills plus JSON manifests. Source: SRC-1, `scripts/generate-plugin-tree.ts:204-318`, `skills/plugin-lanes.json`, `.claude-plugin/plugin.json`.

OBJ-7 — Installed skill copies and their receipts. Workspace scaffold copies (no receipt); harness-bridge copies in `~/.claude/skills`, `~/.agents/skills` or opencode skills, full or stub, with per-file SHA-256 install receipts in `~/.gbrain/skillpack-bridge-state.json` (schema `gbrain-skillpack-bridge-v1`); third-party pack receipts in `~/.gbrain/skillpack-state.json` (pinned commit or tarball digest, no per-file hashes). Source: SRC-1, `src/core/skillpack/bridge-state.ts:1-64`, `src/core/skillpack/state.ts:1-57`.

> * reference lens can run a true three-way comparison: installed-hash vs
> * current-file vs current-source separates a LOCAL EDIT (file no longer
> * matches what we wrote) from UPSTREAM DRIFT (file untouched, source moved).
> --- `src/core/skillpack/bridge-state.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

OBJ-8 — Shared brain skill packs and the harness-side cache. Brain-resident `skillpack.json` and `skills/` in a source's content root, published as immutable revisions with sealed file hashes and a policy epoch; on the harness side, `revisions/` cache files, `router/SKILL.md`, `active.json`, `receipt.json` with `owned_files` and `pending_files` hashes, and a native router skill named `gbrain-shared-<hash24>`. Natural-language skills plus symbolic manifests. Source: SRC-1, `src/core/shared-skills/adapter.ts:48-130`, `src/core/harness/native-router.ts:27-78`, `docs/guides/shared-brain-skills.md`.

OBJ-9 — Host configuration written by bootstrap and in-agent install: workspace identity templates (`CLAUDE.md`, `AGENTS.md`, `SOUL.md`), `agent.json`, a marker-delimited instruction block in `~/.claude/CLAUDE.md` or `$CODEX_HOME/AGENTS.md`, hook entries keyed by `_gbrain` markers in Claude settings, MCP registrations, and receipts (`bootstrap/receipt.json`, `harness.json`, in-agent `owned_files`). Natural-language instructions plus JSON/TOML configuration. Source: SRC-1, `src/core/bootstrap/instructions-block.ts:32-33`, `src/core/bootstrap/host-specs.ts:184-239`, `src/core/bootstrap/format.ts:119-200`, `src/core/agent-install/setup.ts:120-153`.

> export const AMBIENT_WRITEBACK_BLOCK_BEGIN = '<!-- gbrain:ambient-writeback:begin -->';
> export const AMBIENT_WRITEBACK_BLOCK_END = '<!-- gbrain:ambient-writeback:end -->';
> --- `src/core/bootstrap/instructions-block.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

OBJ-10 — SkillOpt artifacts under `skills/<name>/skillopt/`: `history.json` (pending/committed rows with the applied edits, selection score and delta), `versions/vNNNN_eE_sS.md`, `best.md`, `proposed.md`, and `rejected.json` (bounded LRU of rejected edits with reasons, keyed to the skill text they were proposed against); plus the author-supplied benchmark (`skillopt-benchmark.jsonl`) and optional held-out set. Natural-language skill text; symbolic judges. Source: SRC-1, `src/core/skillopt/version-store.ts:1-60`, `src/core/skillopt/rejected-buffer.ts:1-40`, `src/core/skillopt/types.ts:36-83,240-262`.

> export type Judge =
> | { kind: 'rule'; checks: RuleCheck[] }
> | { kind: 'llm'; rubric: string; model?: string }
> | { kind: 'qrels'; expected_slugs: string[]; k: number };
> --- `src/core/skillopt/types.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

OBJ-11 — Superseded. This record combined derived session state with raw transcript files, which differ in lineage and consumers. It is split into OBJ-16 (session context state) and OBJ-17 (raw transcript corpus). OBJ-11 denotes no current object; see Reconciliation.

OBJ-12 — Derived pages: dream `synthesize` pages from transcripts, `patterns` pages, `enrich_thin` enrichments, and `think --save` synthesis pages with a `## Gaps` section. Natural language; files and RDBMS. Source: SRC-1, `src/core/cycle/synthesize.ts:1-48`, `src/core/cycle/patterns.ts:1-21`, `src/core/think/index.ts:966-1000`.

OBJ-13 — Upgrade state: update-check cache, `~/.gbrain/migrations/completed.jsonl`, `~/.gbrain/upgrade-checkpoint.json` bound to a database-URL hash, `pending-host-work.jsonl`, and the natural-language migration manuals in `skills/migrations/vX.md` addressed to the host agent. Source: SRC-1, `src/commands/migrations/index.ts:1-11`, `src/core/upgrade-checkpoint.ts:1-45`.

OBJ-14 — Bootstrap agent-workspace memory files: `MEMORY.md` (standing rules, open commitments, active context), `memory/YYYY-MM-DD.md` daily logs, `memory/reference/`, `USER.md`, `SOUL.md`, `HEARTBEAT.md`, in a workspace Git repository that hooks push to a private remote. The host agent writes them by editing files, as the workspace `AGENTS.md` instructs; Claude Code loads `MEMORY.md` through an `@MEMORY.md` import, and the SessionStart hook pushes a digest of three sections (RTE-5). Natural language; files and repo. The templates are shipped doctrine; the file contents change through use. Implementation conclusion status for loading and digest: wired; for agent writing: claimed (doctrine the host agent follows). Source: SRC-1, `templates/bootstrap/AGENTS.md.template:28-44,100-124`, `templates/bootstrap/CLAUDE.md.template:8-11`, `templates/bootstrap/memory-README.md.template:1-21`, `src/commands/hook.ts:118,486-490,603-631`.

> - Operational state (open commitments, corrections, active context) → `MEMORY.md`
> --- `templates/bootstrap/AGENTS.md.template` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

OBJ-15 — Stop-hook live buffer, `~/.gbrain/transcripts/live/<session>.txt`: one JSON line per turn with a 400-character excerpt of the last assistant message, collected after 7 days. Raw trace. Read back only as the "Last session activity" line at the next SessionStart, from the newest file of any session. Source: SRC-1, `src/commands/hook.ts:633-663,1431-1450`.

> ...(exchange ? { exchange: exchange.slice(0, 400) } : {}),
> --- `src/commands/hook.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

OBJ-16 — Session context state: `session_context_state` rows keyed `(source_id, client_id, session_id)` holding banked standing entities, the `delta` wake cursor and a checkpoint link manifest of verified page slugs. Symbolic; RDBMS. Idle cursors are collected after 7 days. Consumers: post-compaction SessionStart re-entry and `delta` (RTE-5, RTE-26). Source: SRC-1, `src/core/context/session-state.ts:1-55`, `src/core/ops/facts.ts:682-715`.

OBJ-17 — Raw transcript corpus, in `dream.synthesize.session_corpus_dir` or else `<config>/transcripts/corpus`: session-end transcripts, compaction segments, writeback turn files, a per-session ledger, harvest receipts and claim sidecars, secret-scanned before write and retained 30 days. Raw trace. Inputs to RTE-6, RTE-24 and the synthesize branch of RTE-8. Source: SRC-1, `src/commands/hook.ts:1320-1430,1630-1810`, `src/core/sweep.ts:26-35,582-586`.

OBJ-18 — Fact withdrawal ledger, `fact_withdrawals`, rows keyed `(source_id, visibility, fact fingerprint)` written by `forget`. A later `remember` or extraction of the same normalized claim is refused. Symbolic; RDBMS. Force: enforcement over future writes. Source: SRC-1, `src/core/facts/withdrawal.ts:11-40`, `src/core/facts/single-prepare.ts:19-24`.

> const inserted = await tx.executeRaw(`INSERT INTO fact_withdrawals(source_id,visibility,fact_hash)
> --- `src/core/facts/withdrawal.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

OBJ-19 — Access and feedback metadata: `pages.last_retrieved_at`, updated by `recall` and used to break entity-card ties, and `context_volunteer_events`, a log of delivered push items read only by operator statistics and doctor, pruned after 90 days. Symbolic access metadata, not content. Source: SRC-1, `src/core/ops/facts.ts:395-420`, `src/core/verbs/entity-card.ts:10-14`, `docs/guides/push-context.md`.

### Routes

RTE-1 — Explicit fact write (`remember` verb over MCP, `gbrain remember` locally). Implementation conclusion status: wired. The caller supplies a fact, required provenance, kind, optional TTL and visibility (default `world`). The coordinator resolves the entity page (or `memory/unattributed`), queues a write request, rejects a claim previously withdrawn, embeds the fact when a provider exists, and classifies it: exact fingerprint match is `duplicate`; cosine ≥ 0.95 against a same-entity, same-visibility, unexpired candidate is `superseded` (same kind) or `duplicate`; otherwise `inserted`. It appends to the page's `## Facts` fence, re-renders the page and inserts or expires `facts` rows. Return: status and ID. Revision admission: the caller proposes, the similarity rule decides supersession; no truth check applies. Rollback: withdrawal (RTE-7); an expired row keeps its history. Source: SRC-1, `src/core/verbs.ts:60-162`, `src/core/persistence/memory-mutations.ts:47-94`, `src/core/persistence/memory-prepare.ts:28-90`, `src/core/facts/single-prepare.ts:13-55`.

> if (candidate && score >= 0.95) return {
> status: candidate.kind === input.kind ? 'superseded' : 'duplicate', candidate,
> };
> --- `src/core/facts/single-prepare.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

> 'provenance is REQUIRED (free text, e.g. "conversation 2026-06-12", "user said in chat", "import: notes.md"). ' +
> --- `src/core/verbs.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

Amendment (memory lens): supersession is near-duplicate replacement, not contradiction handling. A contradicting fact below cosine 0.95 is inserted beside the old one; correcting it depends on an explicit `forget` or a near-identical restatement. Without an embedding provider, deduplication degrades to fingerprint matching. Affects the curation and epistemic readings of RTE-1 and RTE-9.

RTE-2 — Page write (`put_page`, `capture`). Implementation conclusion status: wired. Parses, chunks, stamps provenance, prepares timeline, fact and tag projections, writes the file through write-through, and embeds as a later persistence effect. Graph links are extracted only for trusted callers; a remote MCP `put_page` stores references as text and reports `auto_links.skipped: remote`. The fact backstop queues extraction of facts from the written page (RTE-9). Source: SRC-1, `src/core/ops/pages.ts:275-304`, `src/core/persistence/page-prepare.ts:97-245`, `src/core/persistence/effects.ts:12-17`.

> const links = !noop && !targetDeleted && ordinaryPage && (row.authority.autoLinkTrusted ?? !row.authority.remote) && await isAutoLinkEnabled(engine)
> --- `src/core/persistence/page-prepare.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

RTE-3 — Requested retrieval (`recall`, `search`, `query`, graph and entity reads). Implementation conclusion status: wired. `recall` gathers facts by entity, time window, session and supersession chains, optionally adds a page-search arm, updates `last_retrieved_at`, and packs facts first into a token budget. Remote callers see only world-visible facts and non-private pages. `search` runs keyword plus vector arms with reciprocal-rank fusion (k=60), post-fusion boosts (backlinks, salience, recency, compiled truth, source prefix, supersede down-rank) and a reranker in `balanced` and `tokenmax` modes; without an embedding provider it is keyword-only. `query` additionally expands the question with a model call. Next-step owner: the requesting agent. Source: SRC-1, `src/core/ops/facts.ts:180-510`, `src/core/ops/search.ts:226-400`, `src/core/search/hybrid.ts:1-10,1226`, `src/core/search/mode.ts:441-619`.

> const visibility =
> ctx.remote === false
> ? undefined
> : ['world'] as ('private' | 'world')[];
> --- `src/core/ops/facts.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

> * Pipeline: keyword + vector → RRF fusion → normalize → boost → cosine re-score → dedup
> *
> * RRF score = sum(1 / (60 + rank_in_list))
> --- `src/core/search/hybrid.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

RTE-4 — Cited synthesis (`think` op, `synthesize` verb, `gbrain think`). Implementation conclusion status: wired. Gathers pages by hybrid search, takes by keyword and vector search, and graph neighbours of an anchor; asks the resolved model for JSON `{answer, citations, gaps}`; flags citations absent from the gathered set as `CITATION_NOT_IN_GATHER`. With `--with-calibration` (off by default) it injects the calibration profile and anti-bias rules. Remote callers cannot persist; local `--save` writes `synthesis/<slug>-<date>` with a `## Gaps` section directly through `engine.putPage`, and `--take` writes a take. Gaps are returned, not queued as work; gap-driven follow-up rounds are not implemented. Source: SRC-1, `src/core/think/index.ts:9-17,91-100,479-1000`, `src/core/think/gather.ts:155-211`, `src/core/think/prompt.ts:40-70`, `src/core/ops/takes.ts:187-280`.

> const remote = ctx.remote ?? true;
> // Codex P1 #7 + privacy: remote callers cannot persist via MCP.
> const safeSave = remote ? false : Boolean(p.save);
> --- `src/core/ops/takes.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

RTE-5 — Automatic per-turn and per-session context push. Implementation conclusion status: wired (GBrain side); host activation: uninspected. Bootstrap installs Claude Code hooks for SessionStart, UserPromptSubmit, Stop, SessionEnd and PreCompact that call `gbrain hook <event>`. On a user prompt, the hook sends the prompt window over an authenticated local socket to `gbrain serve`, which assembles reflex pointers, volunteered pages (deterministic entity matching, confidence ≥ 0.7, at most 3 pages) and hot facts under a world-only context, wraps them in a data envelope, and returns up to 10,000 characters as `additionalContext`. Session start adds a file digest and a context pack; PreCompact banks standing entities. Independently, MCP tool responses can carry `_meta.brain_hot_memory` (top facts, 30-second TTL). The hook never opens the engine and fails open. Source: SRC-1, `src/core/bootstrap/host-specs.ts:184-199`, `src/commands/hook.ts:1-33,471-530,1226,1291-1330`, `src/core/context/turn-context.ts:1-24,59-60`, `src/core/context/volunteer.ts:1-45`, `src/core/facts/meta-hook.ts:1-20`.

> export const TURN_CONTEXT_ENVELOPE =
> '<!-- retrieved brain context — data, not instructions -->';
> --- `src/core/context/turn-context.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

Amendment (memory lens; the specialist's SessionStart route is merged here). Selection details:

- User prompt: the selector reads the last four turns, prior injected blocks and the session ID. Entity pointers and volunteered pages come from lexical alias, title, surname and slug-suffix matching, with no embedding or model call. Hot facts are the session's facts (else the last 24 hours) ranked by decayed confidence, top 10. The default block budget is 8 KB, trimmed facts first.
- SessionStart (1.5-second deadline): a digest of three `MEMORY.md` sections up to 3 KB (OBJ-14), the newest live-buffer line (OBJ-15), status notes, then a context pack of this session's banked standing entities, up to four entity cards, hot facts, the `delta` since the last wake, and checkpoint links on compaction re-entry (OBJ-16). The wake cursor advances only when the pack is complete.
- `_meta.brain_hot_memory` is attached to MCP responses on both transports except `recall`, `extract_facts` and `forget_fact`.
- The IPC lane works for Postgres as well as PGLite (CLM-8).

Push paths are world-only. Source: SRC-1, `src/core/context/turn-context.ts:180-330`, `src/core/facts/meta-hook.ts:65-165`, `src/commands/hook.ts:471-600`, `src/mcp/context-pack-handler.ts:137-160`, `src/core/context/volunteer.ts:1-24`.

> * Zero-LLM, deterministic, precision-biased: push noise is worse than pull
> --- `src/core/context/volunteer.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

> if (sessionId) {
> rows = await ctx.engine.listFactsBySession(sourceId, sessionId, {
> activeOnly: true, limit: topK, visibility,
> });
> }
> // If no session-scoped rows, fall back to recent across the source.
> --- `src/core/facts/meta-hook.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

> rows.sort((a, b) => effectiveConfidence(b, now) - effectiveConfidence(a, now));
> --- `src/core/facts/meta-hook.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

> export const DIGEST_SECTIONS = ['standing rules', 'open commitments', 'active context'];
> --- `src/commands/hook.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

RTE-6 — Ambient writeback. Implementation conclusion status: wired; default off. With `memory.auto_writeback` set to `salient` or `all`, the Stop hook parses the transcript tail, applies a deterministic gate to the last user turn, banks it as a corpus file, and asks the server to schedule a checkpoint flush. The serve-side harvest queue (8 jobs, 60-second abort) runs the LLM fact-extraction pipeline with `remote: false`, deduplicates and writes facts; the maintenance sweep is the backstop when serve is down. Source: SRC-1, `src/commands/hook.ts:1452-1535`, `src/core/context/checkpoint-harvest.ts:1-27,299-307,437-446`, `src/core/facts/extract.ts:519-577`.

> if (!wb.enabled) return 'wb_off';
> --- `src/commands/hook.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

Amendment (memory lens): the route has two lanes. Writeback is opt-in and, in `salient` mode, filters to medium-and-up notability. Compaction harvest is separate: PreCompact banks the window as a secret-scanned segment (OBJ-17), and the harvest is gated only by `facts.extraction_enabled`, default on. Extracted facts carry `source` `hook:writeback` or `hook:compact` and the session ID. The compaction lane also banks the checkpoint link manifest (OBJ-16), which the same conversation receives on post-compaction re-entry. Extraction runs as trusted local, outside the MCP dispatcher. Source: SRC-1, `src/core/context/checkpoint-harvest.ts:40-130,284-360,379-465`.

> r = await runFactsPipeline(raw, {
> engine: job.engine,
> sourceId: job.sourceId,
> sessionId: job.sessionId,
> source: 'hook:compact',
> mode: 'inline',
> remote: false,
> --- `src/core/context/checkpoint-harvest.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

RTE-7 — Withdrawal, supersession, TTL and page deletion. Implementation conclusion status: wired. `forget`/`forget_fact` strike the fence row, mark the fact withdrawn with a reason and keep history; a later `remember` of the identical claim fails with `fact_withdrawn`. Supersession sets `expired_at` and `superseded_by` and search down-ranks superseded content. TTL becomes `valid_until` and reads filter on it. `delete_page` is a 72-hour soft delete restorable by `restore_page`; autopilot purge then hard-deletes. Doctrine states that withdrawal is not erasure. Source: SRC-1, `src/core/verbs.ts:343-383`, `src/core/persistence/memory-mutations.ts:96-148`, `src/core/facts/withdrawal.ts:11-86`, `src/core/ops/pages.ts:352-410`, `docs/guides/memory-boundaries.md`.

> if (decision.status === 'superseded') await tx.executeRaw(`UPDATE facts SET expired_at=now(),superseded_by=$3
> --- `src/core/persistence/memory-prepare.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

RTE-8 — Dream-cycle page generation (synthesize, patterns, enrich_thin). Implementation conclusion status: wired; `enrich_thin` off by default. Trigger: `gbrain dream` or autopilot. Synthesize: a cheap-model triage selects transcripts; each passing transcript gets an LLM sub-agent (default Sonnet) whose `put_page` writes the orchestrator holds; the orchestrator then repairs quotes mechanically (exact, normalized or near match to a verbatim transcript span, otherwise strip the quotation marks) and stamps provenance. Patterns: one sub-agent writes or updates a pattern page per theme from recent reflections. Enrich_thin: grounded LLM synthesis from brain context, skipped when context is too thin, written with `expected_revision` and `enriched_by`. Admission: auto-applied; no review queue. Rejection: triage and the thin-context gate. Rollback: none general (ABS-3); the synthesize mode dial and page soft delete. Guidance shaping the proposal: fixed prompts in code, not revised by this route. Source: SRC-1, `src/core/cycle/synthesize.ts:1-48`, `src/core/cycle/synthesize-verify.ts:1-30`, `src/core/cycle/patterns.ts:1-21`, `src/core/enrich/thin.ts:1-40`, `src/commands/enrich.ts:438-462`.

> * Ladder invariant: NEVER fabricate — every replacement is a verbatim slice of
> * the source transcript; when nothing grounds, the span loses its quotation
> * marks but keeps its text.
> --- `src/core/cycle/synthesize-verify.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

Amendment (memory lens): the branches differ in lineage and gate. Synthesize is trace-fed from the transcript corpus (OBJ-17) and enabled by default only when `dream.synthesize.session_corpus_dir` is configured, which bootstrap does not do. Its pages carry `dream_generated` and `raw_source`, and are excluded from fact re-extraction. Patterns is compiled from reflection pages, not traces. Enrich_thin is off by default. Once enabled, all three are applied without review. Source: SRC-1, `src/core/cycle/synthesize.ts:1519-1525,2935-2941`.

> // v2: enabled defaults to true when corpus dir is configured, false otherwise.
> --- `src/core/cycle/synthesize.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

RTE-9 — Page-write fact extraction, fence reconciliation and consolidation (amended after the memory lens; the specialist's page-write backstop route is merged here). Implementation conclusion status: wired. The fact backstop is the single choke point for `put_page`, sync, file upload and code import. It queues LLM extraction over the page body, using the configured extraction model with Sonnet as fallback. Sync admits only high-notability facts. Dream-generated pages are ineligible (anti-loop guard). In the extraction lanes any matched candidate is treated as a duplicate, so extraction never supersedes. The LLM classifier in `src/core/facts/classify.ts` (duplicate, supersede or independent) has no non-test importer at this revision (CLM-7). The cycle's `extract_facts` phase runs no model: it reconciles DB rows from each page's `## Facts` fence, which is canonical. `consolidate` is also deterministic. It takes buckets of at least three facts whose oldest is at least 24 hours old, clusters them greedily at cosine 0.85, and turns each cluster of two or more into a `takes(kind='fact')` row using the highest-confidence fact's text. The contributing facts are marked, never deleted. Confidence decays by a kind-specific half-life at read time; the decay ranks facts and deletes nothing. Source: SRC-1, `src/core/facts/backstop.ts:1-40,261`, `src/core/facts/extract.ts:1-66`, `src/core/persistence/facts-prepare.ts:83-120`, `src/core/cycle/extract-facts.ts:1-25`, `src/core/cycle/phases/consolidate.ts:1-22,150-260`, `src/core/facts/decay.ts:1-33`.

> if (decision.candidate) { entries.push({ fact, duplicateId: decision.candidate.id }); continue; }
> --- `src/core/persistence/facts-prepare.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

> * Reconciles the facts DB index from the `## Facts` fence on each
> * entity page.
> --- `src/core/cycle/extract-facts.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

> *     3. For each cluster ≥ 2: pick the highest-confidence fact's text as
> *        the take claim (v0.31 ships without LLM synthesis to keep the
> --- `src/core/cycle/phases/consolidate.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

> * Formula: confidence × exp(-age_days / halflife_days). Clamped to [0, 1].
> --- `src/core/facts/decay.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

RTE-10 — Takes: proposal, grading and calibration. Implementation conclusion status: wired. `propose_takes` has an LLM write rows to a review queue only; a human accepts with `gbrain takes propose --accept N`. `grade_takes` collects evidence by hybrid search and asks an LLM judge for a verdict, cached with `applied=false`; auto-resolution is off by default and, when enabled, applies at confidence ≥ 0.95 with a three-model ensemble for the 0.6–0.95 band. `calibration_profile` computes Brier and accuracy scorecards plus narrative statements gated by a Haiku voice judge. Later consumers: `think --with-calibration` (off by default), stderr nudges on take commit, the brainstorm orchestrator. An undo removes auto-applied resolutions by `wave_version`. Source: SRC-1, `src/core/cycle/propose-takes.ts:1-37`, `src/core/cycle/grade-takes.ts:1-33,513-533,772-785`, `src/core/cycle/calibration-profile.ts:1-24`, `src/core/think/index.ts:91-100,557-576`, `src/core/calibration/undo-wave.ts:1-30`, `src/core/calibration/nudge.ts:1-27`.

> * propose_takes only WRITES proposals to the queue. Nothing here mutates
> --- `src/core/cycle/propose-takes.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

> * On a fresh install, grade_takes runs and writes verdicts to the cache,
> * but `applied=false` on every row. Operator reviews the queue, then flips
> --- `src/core/cycle/grade-takes.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

RTE-11 — SkillOpt skill revision. Implementation conclusion status: wired. Trigger: `gbrain skillopt <skill>` (human-invoked), the admin-scoped MCP operation `run_skillopt` (requires a remote skill allowlist), or the dream-cycle `skillopt` phase (off by default; weekly per skill; $0.50 per-skill cap; no-mutate for every skill, bundled or not, despite a `cycle.ts` comment that limits this to bundled skills, CLM-9). Proposal: the target model runs the skill on training tasks; two optimizer calls read the current skill body, failure or success trajectories, the plain-English scoring criteria and the rejected-edit buffer, and propose at most eight surgical `add`/`replace`/`delete` edits, each with a one-sentence reason and each required to address a specific observed failure; frontmatter edits are refused. Decision: a judge scores each selection task three times; the candidate is accepted only if the median selection score exceeds the current best by more than 0.05; an optional held-out set refuses candidates that regress. Answer oracle: the benchmark, supplied by the skill author (or bootstrapped by the optimizer model and marked `BOOTSTRAP_PENDING_REVIEW` until a human removes the marker); judges are rule checks, LLM rubrics, or `qrels` expected page slugs. Admission: accepted text is committed in five ordered steps ending with `SKILL.md`; with `--no-mutate`, in the dream path, or for a bundled skill without `--allow-mutate-bundled` plus a held-out set, the candidate goes to `proposed.md` for human review. For a shared brain skill the accepted text is published through `put_skill` against the approved revision, after an editor authorization check. Rejection: rejected edits enter `rejected.json` with the gate reason and are withheld from later proposals against the same skill text. Rollback: crash recovery of a pending version only; no rollback command (ABS-2); older versions remain on disk. Rollouts run with brain read tools only. Source: SRC-1, `src/core/skillopt/reflect.ts:1-120`, `src/core/skillopt/validate-gate.ts:160-190`, `src/core/skillopt/version-store.ts:1-60,207-245`, `src/core/skillopt/cycle-phase.ts:1-20,145-170`, `src/core/skillopt/rejected-buffer.ts:1-40`, `src/core/skillopt/rollout.ts:36-37`, `src/core/skillopt/benchmark.ts:79-85`, `src/core/shared-skills/optimizer.ts:1-158`.

> // D12 accept rule: strict > best + epsilon. Ties/sub-epsilon-gains are
> // rejected (paper-faithful — protects against noise-as-improvement).
> const threshold = opts.bestScore + VALIDATION_EPSILON;
> const accepted = selScore > threshold;
> --- `src/core/skillopt/validate-gate.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

> - Each edit MUST address a SPECIFIC failure pattern you observed.
> - anchor / target MUST be uniquely identifiable in the skill body (exact match).
> - Do NOT propose edits already in the rejected-edit history — those were tried and didn't help.
> --- `src/core/skillopt/reflect.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

> noMutate: true, // ALL dream-cycle runs are no-mutate by default
> --- `src/core/skillopt/cycle-phase.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

> const publication = await submitSharedSkillMutation(ctx, 'put_skill', { ...target, name: opts.skillName, files: input,
> --- `src/core/shared-skills/optimizer.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

Retained reasons: each edit's one-sentence reason is kept in `history.json` with its selection score and delta, which only crash recovery reads later; `SKILL.md` itself carries no reasons. Rejected edits and their gate reasons are read by the next reflect call. Source: SRC-1, `src/core/skillopt/types.ts:69-72,240-249`, `src/core/ops/skillopt.ts:127-130`.

> description: 'Run SkillOpt against a single skill. Admin scope and remote skill allowlist required.
> --- `src/core/ops/skillopt.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

RTE-12 — Durable sub-agent (`gbrain agent run`, Minions `subagent` jobs). Implementation conclusion status: wired. Local trusted submission only: `shell`, `subagent`, `subagent_aggregator` and the synthesize, patterns and consolidate jobs are protected names MCP cannot submit. The sub-agent receives brain read tools plus `put_page` and `add_timeline_entry` fenced to `wiki/agents/<subagentId>/` or a trusted-workspace allow-list, and each tool call runs with `remote: true`. Messages and tool executions persist in two phases so a killed worker resumes. Source: SRC-1, `src/commands/agent.ts:1-13`, `src/core/minions/protected-names.ts:15-30`, `src/core/minions/tools/brain-allowlist.ts:14-18,51-78,242`.

> remote: true,                // match MCP trust boundary for auto-link skip
> --- `src/core/minions/tools/brain-allowlist.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

RTE-13 — Plugin build, publication and host install. Implementation conclusion status: wired (repository side); marketplace refresh and host loading: uninspected. The generator computes each lane as the OpenClaw skill list minus recorded base exclusions plus recorded additions, snapshots skills whose declared MCP operations exceed the starter surface, copies skills and shared dependencies, writes a stamped README, and emits self-contained persona variants with their own manifests and launcher. `check-plugin-tree.sh` regenerates into a temporary directory and fails on any byte difference; it runs in `bun run verify` and before release publication. The release job copies the manifests, launcher and plugin trees into a fresh repository and force-pushes one history-less commit to the `codex-plugin` branch. The Claude plugin's MCP server runs the launcher as `serve --surface starter --source-guard`; the launcher resolves an already installed `gbrain` binary and never installs one. Neither plugin manifest declares hooks (ABS-5). No code compares an installed plugin tree's stamp with the binary (ABS-1); freshness depends on the host marketplace refresh. Source: SRC-1, `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `.codex-plugin/plugin.json:21-22`, `.codex-plugin/mcp.json`, `.agents/gbrain-launcher:18-51`, `scripts/generate-plugin-tree.ts:17-30,96-318`, `scripts/check-plugin-tree.sh:36-60`, `.github/workflows/release.yml:285-354`.

> "skills": "./plugin/skills/",
> "mcpServers": {
> "gbrain": {
> "command": "${CLAUDE_PLUGIN_ROOT}/.agents/gbrain-launcher",
> "args": [
> "serve",
> "--surface",
> "starter",
> "--source-guard"
> ],
> --- `.claude-plugin/plugin.json` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

> if ! diff -r "$TMP/plugin" "$ROOT/plugin" >/dev/null 2>&1; then
> echo "check-plugin-tree: FAILED — committed plugin/ tree is stale." >&2
> --- `scripts/check-plugin-tree.sh` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

> git init -q -b codex-plugin
> --- `.github/workflows/release.yml` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

RTE-14 — Workspace skillpack scaffold and reference lens. Implementation conclusion status: wired. `gbrain skillpack scaffold` copies selected skills, paired source files and shared dependencies into a workspace, never overwriting an existing file and recording no receipt. `skillpack reference` is read-only and reports identical, differs or missing with unified diffs; `--apply-clean-hunks` applies only hunks that apply cleanly; `skillpack sync` scaffolds only new skills and reports drifted ones. Without install hashes this lane cannot separate a local edit from upstream drift. The legacy managed AGENTS.md block installer and `skillpack install`/`uninstall` were retired. Third-party packs (`skillpack.json`, `api_version: gbrain-skillpack-v1`) pass a trust prompt and record a pinned commit or tarball digest. Source: SRC-1, `src/core/skillpack/scaffold.ts:1-26,97-151`, `src/core/skillpack/reference.ts:1-14`, `src/commands/skillpack.ts:103-191,362-387`, `src/core/skillpack/skill-currency.ts:1-36`, `src/core/skillpack/scaffold-third-party.ts:1-16`, `src/core/skillpack/state.ts:1-57`.

> *   2. **Refuses to overwrite existing files.** Once a file lands, the
> *      user owns it. To update, run `gbrain skillpack reference <name>`
> *      and decide.
> --- `src/core/skillpack/scaffold.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

RTE-15 — Harness bridge install, three-way update lens, and stub skills. Implementation conclusion status: wired; host loading of the copies: uninspected. `scaffold --harness claude-code|codex|opencode|openclaw` copies a persona's skills plus their shared-dependency closure into the harness's native skills directory after a frontmatter gate and target confinement, refusing to overwrite, and records a SHA-256 for every file it wrote. The reference lens compares installed hash, current file and current source: a file still matching its install hash is `upstream_drift`, anything else `local_edit`, and a file without a recorded hash `unknown`. Applying updates is permitted only for proven upstream drift and refreshes the stored hash; stubs, local edits and unknown files are refused. Removal deletes only ledger-recorded files. In `--stub` mode the frontmatter (name, description, triggers) is kept verbatim for discovery and the body is replaced by a marker line and an instruction to call the MCP `get_skill` operation, with `gbrain skill <slug>` as a local fallback; preflight refuses stub mode when skill publication is disabled or the skill cannot be served. `get_skill` is gated by `mcp.publish_skills` and serves from the brain host's configured or autodetected skills directory (remote callers never fall back to the binary's bundled skills), from a brain-resident pack, or from the shared catalog when active. The stub body is therefore as current as the serving host's skill source, not necessarily the upstream release. Source: SRC-1, `src/commands/skillpack/harness.ts:1-16,271-348`, `src/core/skillpack/harness-bridge.ts:1-31,78,283-313,604-730,897-930`, `src/core/ops/skills-catalog.ts:23-99`, `src/core/skill-catalog.ts:155-210`, `src/mcp/skill-resources.ts:11-81`.

> export const STUB_MARKER = '<!-- gbrain-skill-stub v1 -->';
> --- `src/core/skillpack/harness-bridge.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

> `This is a cold-pull stub installed by \`gbrain skillpack scaffold\`. The full\n` +
> `skill body is served by your gbrain brain, so it is always current.\n\n` +
> `To use this skill: call the gbrain MCP tool \`get_skill\` with\n` +
> --- `src/core/skillpack/harness-bridge.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

> const installedHash = stateEntry?.written[slug ?? SHARED_DEP_LEDGER_KEY]?.files[rel];
> const differsKind: HarnessRefDiffersKind = installedHash
> ? sha256Hex(actual) === installedHash
> ? 'upstream_drift'
> : 'local_edit'
> : 'unknown';
> --- `src/core/skillpack/harness-bridge.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

> * REMOTE callers use `autoDetectSkillsDir` (no install_path tier — a hosted
> * gbrain must never serve its own bundled dev skills); LOCAL callers
> --- `src/core/skill-catalog.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

RTE-16 — Shared brain skills: publication, following and native router. Implementation conclusion status: wired (brain and adapter); native activation: uninspected and declared unverified by the source. Canonical skills live in a brain source's content root. An authorized editor (`skill_editor` scope plus explicit `put_skill` access) publishes a complete file set against `expected_revision` with a request ID; a race returns a conflict. Human or Git edits to canonical files are proposals published through the local-only `import_skill_proposal` with expected hashes. Publication policy, audiences and following are separate `skill_publisher` grants; ordinary revisions within an approved policy can follow without per-install consent, while new permissions, file classes or requirements cannot. On the harness side the adapter calls `sync_brain_skills`, fetches each immutable revision and asset, checks hashes against the manifest, caches them, renders a router skill that instructs the agent to sync and fetch before using a shared skill, and refuses to overwrite any locally edited managed file (`local_conflict`). The native router installs as `gbrain-shared-<hash24>/SKILL.md` and refuses unowned or edited routers. A staged migration (`inventory`, `ownership`, `projection`, `policy`, `members`) moves existing installs; old harness scaffolds over an active shared brain return a pending plan instead of copying bodies. Source: SRC-1, `src/core/shared-skills/adapter.ts:48-200`, `src/core/harness/native-router.ts:27-78`, `src/core/shared-skills/knowledge-guard.ts:27`, `src/core/shared-skills/migration.ts:12-40`, `src/core/skillpack/shared-brain-bridge.ts:87-105`, `docs/guides/shared-brain-skills.md`.

> if (current !== null && current !== receipt.owned_files[path] && current !== pending?.before && current !== pending?.after) fail('local_conflict', 'A managed artifact was edited; preserve it and resolve the native shadow copy before following updates.');
> --- `src/core/shared-skills/adapter.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

> This paragraph is advisory, not an enforced invocation hook. Start a fresh session after updates; native activation is unverified.\n`;
> --- `src/core/shared-skills/adapter.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

> The publisher validates policy and file hashes, publishes the canonical bundle,
> and seals its catalog projection. A race returns a conflict instead of
> last-write-wins.
> --- `docs/guides/shared-brain-skills.md` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

RTE-17 — Bootstrap and in-agent install writes. Implementation conclusion status: wired; host activation: uninspected. `gbrain bootstrap` renders identity and instruction templates into a new workspace without overwriting (`--force` backs up), writes `agent.json`, and records `created_paths` and `registrations` in a machine-local receipt that uninstall reverses; a newer-version receipt refuses the run. Claude hooks are merged into settings by `_gbrain` marker keys (`bootstrap-v1`, `bootstrap-harness-v1`), atomically with a backup, aborting on unparsable settings. `gbrain bootstrap harness` registers an HTTP MCP server with a bearer token (Claude), a managed TOML block (Codex) or a managed JSONC entry (opencode), with a write-ahead receipt and mint-before-revoke token rotation. A marker-delimited ambient-writeback instruction block is spliced into the user-global `CLAUDE.md` or `AGENTS.md`; reruns replace only its interior and damaged markers throw. In-agent installs (Grok Bot, Muse) write a launcher, setup script, embedded router instruction and maintenance instructions through hash-receipted ownership; a modified owned file stops the rerun, and a different version requires `--upgrade`. Source: SRC-1, `src/core/bootstrap/render.ts:1-39`, `src/core/bootstrap/format.ts:1-200`, `src/core/bootstrap/hooks.ts:1-25`, `src/core/bootstrap/host-specs.ts:184-239,441-443`, `src/core/bootstrap/harness.ts:1-41`, `src/core/bootstrap/instructions-block.ts:1-108`, `src/core/agent-install/setup.ts:120-298`.

> if (actual !== receipt.owned_files[path] && actual !== pending?.before && actual !== pending?.after) {
> throw new AgentInstallError('modified_owned_file', `Preserve your changes at ${target} before rerunning setup; it will not be overwritten.`);
> --- `src/core/agent-install/setup.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

RTE-18 — Upgrade. Implementation conclusion status: wired. Every CLI call reads a cached latest version (the `VERSION` file on master) and, when newer than the running binary and stderr is not a TTY, prints a machine marker `UPGRADE_AVAILABLE <cur> <latest>` for the `gbrain-upgrade` skill; a stale cache triggers a detached refresh. `gbrain upgrade` swaps the binary and runs `post-upgrade`, which always applies pending migrations (TypeScript registry, resumable ledger, upgrade checkpoint bound to the database URL hash), prints feature notes, and sweeps the detected workspace's scaffolded skills, listing new and drifted skills without overwriting. Natural-language migration manuals in `skills/migrations/` are read by the host agent when host work is pending. Scaffolded copies change only when the user or agent acts; stubs read current text from the serving host; shared-skill copies follow through RTE-16. Source: SRC-1, `src/cli.ts:351-412`, `src/commands/check-update.ts:48-50`, `src/commands/upgrade.ts:198-219,336-468,800-915`, `src/commands/migrations/index.ts:1-11`, `src/commands/apply-migrations.ts:1-13`, `src/core/upgrade-checkpoint.ts:1-45`, `skills/_AGENT_README.md:121-131`.

> process.stderr.write(`UPGRADE_AVAILABLE ${VERSION} ${latest}\n`);
> --- `src/cli.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

> 'New skills → `gbrain skillpack sync`. Drifted skills → `gbrain skillpack reference <slug>` (local edits are yours; nothing is overwritten).\nSee `skills/_AGENT_README.md` for what your agent should do on update.\nSkip this sweep: `GBRAIN_SKIP_REFERENCE_SWEEP=1`.',
> --- `src/commands/upgrade.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

> For independent scaffolded copies, the user runs `gbrain upgrade`. Those skill
> files DO NOT change automatically.
> --- `skills/_AGENT_README.md` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

RTE-19 — Markdown repository sync. Implementation conclusion status: wired. `gbrain sync` admits changed repository files page by page through managed sync with per-page source authority and `remote: false`; git deletions become soft deletes. Edits to repository files therefore enter the brain without MCP scope, surface or visibility checks, while `remember`, `put_page` and `delete_page` write through to the files. Source: SRC-1, `src/commands/sync.ts:653-660,1383`, `src/core/persistence/sync-run.ts:143-160`.

RTE-20 — `compile-context` files. Implementation conclusion status: wired. Deterministic selection of pages by pinned prefixes, tags and recency within a source, scored with source boosts, filtered by a sensitivity scan and world visibility, written to `.claude/gbrain-context.md`, an `AGENTS.md` block or an OpenClaw file. No model call. Later consumer: the host harness loading those files (uninspected). Source: SRC-1, `src/commands/compile-context.ts:1-27`, `src/core/context/compile-view.ts:1-25,262`.

RTE-21 — Proposal-only maintenance: contradiction probe, advisor, schema suggestion, drift. Implementation conclusion status: wired. The suspected-contradiction probe pairs pages by hybrid search, asks an LLM judge, stores a run row and prints paste-ready supersession commands that it never runs. The advisor runs deterministic collectors and applies a finding only on `--apply <id>` with a TTY confirmation and a `gbrain` argv free of shell metacharacters. Schema suggestion writes candidates to an audit file; `review-candidates --apply` writes a delta the user must merge. Drift is report-only. Decider in all four: a human. Source: SRC-1, `src/core/eval-contradictions/runner.ts:1-25`, `src/core/eval-contradictions/auto-supersession.ts:5-6`, `src/core/advisor/apply.ts:1-40`, `src/commands/advisor.ts:122`, `src/core/cycle/schema-suggest.ts:9`, `src/core/schema-pack/review.ts:66-90`, `src/core/cycle.ts:71-74`.

> * a paste-ready CLI command. The probe NEVER auto-applies; the user runs
> * the command themselves. The proposal is descriptive, not directive.
> --- `src/core/eval-contradictions/auto-supersession.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

RTE-22 — Operation authorization and trust lanes. Implementation conclusion status: wired. Remote MCP callers pass surface filtering, `localOnly` denial off stdio, source guard, parameter validation, a missing-source refusal, and required-scope and bound-client checks (HTTP: OAuth scopes at list and call time). Writes from local lanes require a verified local writer whose lane (`cli` or `stdio`) matches the transport. A database trigger guard covers inventoried legacy writers when enabled; manual SQL is outside the protocol. `gbrain call` dispatches any operation with `remote: false`. Guarantee strength: protocol, for the MCP and CLI paths it covers; alternate paths are direct DB access, Markdown sync and trusted local calls. Source: SRC-1, `src/mcp/dispatch.ts:499-720`, `src/core/persistence/authority.ts:25-37`, `src/core/persistence/writer-guard-schema.ts:1`, `src/commands/call.ts:10-18`, `src/mcp/server.ts:455-468`.

> const verified = currentVerifiedLocalWriter() ?? await verifyLocalWriter(ctx.engine,
> await readLocalWriter(ctx.engine, ctx.remote === false ? 'cli' : 'stdio'));
> if (verified.remote !== (ctx.remote !== false)) deny('The local trust lane does not match this transport.');
> --- `src/core/persistence/authority.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

> /** Defense in depth for inventoried legacy writers. Manual SQL is outside the protocol. */
> --- `src/core/persistence/writer-guard-schema.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

RTE-23 — Brain health remediation. Implementation conclusion status: wired. `gbrain doctor --remediate` turns health recommendations into a dependency-ordered plan of queued jobs with a cost cap and a recheck of the health score after each step; autopilot forces a full cycle under stated thresholds (time since last run, plan size, estimated duration, score below 70). Checks are deterministic; the synthesize, patterns and consolidate phase handlers are protected from MCP submission. Source: SRC-1, `src/core/remediation/run.ts:1-40`, `src/commands/autopilot-remediation-policy.ts:1-35`, `AGENTS.md`.

RTE-24 — Session-end capture and sweep extraction. Implementation conclusion status: wired. The SessionEnd hook (and Codex session-end capture) writes the redacted transcript remainder to the corpus (OBJ-17). Pass 3 of the serve maintenance sweep runs the LLM fact pipeline over unprocessed corpus files, spend-gated and exactly once through sidecar files. The resulting facts reach later sessions through recall, entity cards, packs and push. This lane is also the fallback for compaction segments when serve is down. Source: SRC-1, `src/core/sweep.ts:1-45,582-586,733`, `src/commands/hook.ts:1630-1810`.

> *   3. CORPUS INGEST [CX-P0.1] — LLM-backed, spend-gated. Unprocessed
> --- `src/core/sweep.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

RTE-25 — Agent-authored workspace memory writes. The host agent edits `MEMORY.md` and the daily logs (OBJ-14) in the same turn, as the bootstrap `AGENTS.md` instructs; corrections become standing rules with the incident attached. GBrain supplies the doctrine and the loading, not a writer. Conclusion status for the writing: claimed (doctrine); for the loading: wired. Source: SRC-1, `templates/bootstrap/AGENTS.md.template:28-44`, `templates/bootstrap/memory-README.md.template:1-21`.

> 3. Corrections become standing rules in `MEMORY.md`, same turn, with the incident
> attached.
> --- `templates/bootstrap/memory-README.md.template` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

RTE-26 — Requested `context_pack` and `delta`. Implementation conclusion status: wired. These are two of the seven memory verbs, which the harness calls at session start, after compaction or on a heartbeat. `context_pack` packs requested entities to a token budget. `delta` returns changes since a per-(source, client, session) cursor with at-least-once delivery. `include_private` is honoured only for trusted local callers. No model call. Source: SRC-1, `src/core/ops/facts.ts:512-715`, `src/core/context/session-state.ts:1-20`.

### Claims

CLM-1 — Autonomous overnight improvement. The README claims the author's deployment ingests, enriches, fixes its own citations and consolidates memory overnight, so that "I wake up smarter than when I went to bed". Layer: doctrine and reported operation; production scale figures (155,795 pages, 66 cron jobs) are reported, not inspectable. Supporting routes: RTE-8, RTE-9, RTE-10, RTE-23 (wired). The claimed effect on the user or agent: uninspected. Source: SRC-1, `README.md`.

> It fixes its own citations and consolidates memory overnight. I wake up smarter than when I went to bed — and so will you.
> --- `README.md` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

CLM-2 — SkillOpt keeps only edits that measurably score higher. Layer: doctrine. Supporting route RTE-11 implements the rule against the benchmark oracle (wired); no run in this boundary shows a measured gain.

> watch the optimizer propose edits and keep only the ones that measurably score higher.
> --- `README.md` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

CLM-3 — Graph retrieval benchmark. A 240-page BrainBench run reported P@5 49.1%, R@5 97.9% and +31.4 points P@5 over a graph-disabled variant, explicitly scoped. Layer: reported operation; scorecards live in a separate repository (excluded). Conclusion status: claimed.

CLM-4 — Stub skills are "always current". Layer: implementation string in the stub body (RTE-15). Supported reading: the body is fetched at use time from the serving brain host's skill source; currency relative to upstream releases depends on that host's skills directory or shared catalog. Conclusion status: afforded, with that qualification.

CLM-5 — Memorable revisions: a new procedure revision gets a trial window and "the one with the better track record wins". Layer: doctrine about a closed-source external component. Conclusion status: claimed; scoring uninspected.

> surfaces whichever revision the evidence favours — a new one gets a short trial
> window, then the one with the better track record wins.
> --- `docs/memorable-agents.md` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

CLM-6 — Sharing boundary. The README states that remote clients are constrained by source and operation grants plus visibility filters, that local files and shared database credentials are a different trust boundary, and that tests exercise specific paths, not a universal no-leak guarantee. Layer: doctrine, consistent with RTE-22 and RTE-19.

> The authorization tests exercise specific access paths, not a universal no-leak guarantee.
> --- `README.md` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

CLM-7 — The `extract_facts` operation description advertises a "cosine fast-path + classifier dedup pipeline". Layer: implementation string (operation description). A commit-wide `git grep` for `classifyAgainstCandidates` finds only its definition in `src/core/facts/classify.ts` and `test/facts-classify.test.ts`. Classifier conclusion status: absent from runtime routes; the description overstates the pipeline. Consequence: contradictions below the 0.95 threshold accumulate (RTE-1, RTE-9).

> calls the configured extraction model (key-aware: any servable provider — OpenAI or Anthropic key both work), runs the cosine fast-path + classifier dedup pipeline, INSERTs into facts.
> --- `src/core/ops/facts.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

CLM-8 — The push-context guide says the hook lane is quiet on Postgres, but the code keys an IPC socket for Postgres from a hash of the database URL. Layer: doctrine versus implementation; the guide is stale. Implementation conclusion status for Postgres hook IPC: wired.

> The hook lane rides the PGLite serve's IPC socket: on a Postgres brain or a
> --- `docs/guides/push-context.md` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

> if (cfg.engine === 'postgres' && cfg.database_url) {
> return localIpcSocketPath(join(ipcRunDir(), `${kind}-${hash12(cfg.database_url)}.sock`));
> --- `src/core/context/resolve-ipc.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

CLM-9 — A comment says the dream cycle never auto-mutates bundled skills; the implementation passes `noMutate: true` for every skill (RTE-11). Layer: implementation comment versus code. The comment's scope is narrower than the behavior.

> // Bundled-skill safety: dream-cycle NEVER auto-mutates bundled skills.
> // For bundled skills we set --no-mutate; the user reviews proposed.md
> // at their own cadence.
> --- `src/core/skillopt/cycle-phase.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

CLM-10 — Session targeting of hot memory silently degrades for fence-backed facts: a rebuilt fence row has no `source_session`, so selection falls back to 24-hour recency (OBJ-2, RTE-5). Layer: implementation inference from the fence schema and the selector. Conclusion status: wired.

### Evidenced absences

ABS-1 — No runtime freshness check for installed plugin trees. Conclusion status: absent. Searched: `git grep -n 'plugin-tree-stamp'` over `src/` at the reviewed commit; no match. Supports: the stamp is written only into generated READMEs and checked in CI; an installed plugin's currency depends on the host marketplace. Does not exclude a host-side check.

ABS-2 — No SkillOpt rollback command. Conclusion status: absent. Searched: `git grep -n -iE 'rollback|restore|revert'` in `src/commands/skillopt.ts`; no match. Supports: reverting an accepted skill version is manual (old versions stay in `versions/`); crash recovery covers only a pending write.

ABS-3 — No general dream-cycle rollback. Conclusion status: absent. Searched: `git grep -n -iE 'rollback|undo|revert'` in `src/core/cycle.ts`, `src/commands/dream.ts`, `src/commands/autopilot.ts`; no match. Supports: auto-applied phase writes (RTE-8) are undone only through ordinary page operations; `src/core/calibration/undo-wave.ts` is a narrower undo for auto-applied take resolutions.

ABS-4 — `auto_think` is not a cycle phase. Conclusion status: absent. Searched: `git grep -n "auto_think\|'auto-think'\|auto-think"` in `src/core/cycle.ts`; no match. Supports: configured recurring `think` questions do not run in the cycle at this revision. The memory lens independently reached the same finding from the phase's own "not yet wired" comment (`src/core/cycle/auto-think.ts:24-28`).

ABS-5 — No hooks in plugin manifests. Conclusion status: absent. Searched: `git grep -n -E '"hooks"|hooks'` in `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`, `.codex-plugin/mcp.json`; no match. Supports: plugin installs deliver skills and an MCP server only; per-turn push (RTE-5) requires bootstrap.

ABS-6 — No model-weight updates issued by GBrain. Conclusion status: absent. Searched: `git grep -n -iE 'fine[-_ ]?tun|finetun|training_file|lora'` over `src/`; the only implementation hit is a comment naming the provider's fine-tune identifier format in `src/core/ai/recipes/openai.ts`. Supports: CMP-5 parameter fixity at GBrain's boundary; does not exclude provider-side model changes.

ABS-7 — No retained test of dependence on recalled memory. Conclusion status: absent. Searched (memory lens): the `evals/` directory listing, and `docs/` and `CHANGELOG.md` for ablation and A/B evidence. Retrieval benchmarks (BrainBench P@5 and R@5, `docs/architecture/RETRIEVAL.md`) measure ranking, not dependence. The `think` A/B table, SkillOpt receipts and volunteer statistics would be deployment-local and are not in the source. Supports: `faithfulness_tested` is `no` within this boundary. Does not exclude evidence held in a deployment.

### Behavioral-authority paths

BAP-1 — Delivered skills and resolver to the host agent. Consumer: host model (CMP-13). Channel: harness skill loading from plugin, scaffolded, bridge or stub copies (OBJ-5, OBJ-6, OBJ-7), or on-demand `get_skill` text. Force: instruction (advisory to the host; the resolver says the frontmatter `triggers:` are the authoritative routing signal). Horizon: every session in which the host loads the skill, until the copy changes. Activation: uninspected.

BAP-2 — Pushed per-turn context. Consumer: host model. Channel: hook `additionalContext` and MCP `_meta.brain_hot_memory` (RTE-5). Force: knowledge (the envelope labels it data, not instructions). Horizon: the current turn.

BAP-3 — User-global instruction block and bootstrap identity files. Consumer: host agent in every session reading the user-global `CLAUDE.md`/`AGENTS.md` or the workspace files (OBJ-9). Channel: always-loaded instruction files. Force: instruction. Horizon: persistent until removed.

BAP-4 — SkillOpt-accepted skill versions. Consumer: later executions of that skill, locally or, for shared skills, by every following installation through RTE-16 (OBJ-10, OBJ-8). Channel: `SKILL.md`. Force: instruction. Horizon: until the next accepted version or manual revert. Also covers followed shared-skill revisions from manual publication. The reasons for each edit stay in `history.json`, which no later consumer reads; `SKILL.md` does not carry them.

BAP-5 — Calibration profile in synthesis. Consumer: `think --with-calibration` and take-commit nudges (OBJ-3). Channel: prompt injection and stderr. Force: instruction on the framing of the question, with the scorecard (Brier score, per-domain accuracy) delivered as the reason. Horizon: per call; off by default, and reachable only through the CLI flag; the MCP `think` operation exposes no such flag.

> `\nCalibration-aware mode (v0.36.1.0): the user's calibration profile is included as <calibration> below the retrieval blocks. Apply it to the QUESTION FRAMING, not the evidence:`,
> --- `src/core/think/prompt.ts` @ `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`

BAP-6 — Operation grants and surfaces. Consumer: remote MCP callers. Channel: dispatcher checks (RTE-22). Force: enforcement. Horizon: per call, within the covered paths.

BAP-7 — Supersession, withdrawal, TTL and decay flags. Consumer: recall, search and push selection (OBJ-2). Channel: eligibility filters and ranking. Force: ranking and eligibility. Horizon: until the fact is re-asserted or history is purged. The withdrawal ledger (OBJ-18) additionally refuses re-assertion of a withdrawn claim (enforcement).

BAP-8 — `MEMORY.md` standing rules. Consumer: host model in every main Claude Code session of a bootstrapped workspace. Channel: `@MEMORY.md` import plus the SessionStart digest (OBJ-14, RTE-5). Force: instruction. Horizon: until the agent or user edits the rule. The incident that motivated a rule is attached by doctrine and delivered with it.

## Runtime account

**Ordinary invocation (plugin lane, Claude Code).** The user installs the `gbrain` plugin from the repository marketplace. The host loads skills from `plugin/skills/` and starts the launcher, which execs an already installed `gbrain serve --surface starter --source-guard` over stdio (RTE-13). A user message triggers the host model (principal: the user; next-step owner: the host model). The host may select a GBrain skill by its triggers and call MCP tools. A `remember` call enters CMP-2 with `remote: true`; the dispatcher filters by surface, blocks writes when the source is ambiguous under `--source-guard`, validates parameters and builds the context; the persistence coordinator admits the write, embeds when a provider exists, decides insert, duplicate or supersede by similarity, writes the fence, file and rows, and returns a status (RTE-1, RTE-22). A later `recall` or `search` returns world-visible facts and pages ranked by the hybrid pipeline (RTE-3). State persists in the database and Markdown files; the host's own context is lost at session end unless the host or GBrain hooks write it back. Terminal output is the host's reply. Stdio serve also runs best-effort startup and idle maintenance sweeps; HTTP serve does not.

**Material alternate paths.**

- Bootstrap lane: hooks push context every turn and at session start (RTE-5); compaction harvest and session-end capture extract facts from transcripts, and ambient writeback does so per turn when opted in (RTE-6, RTE-24). Plugin installs have no hooks (ABS-5).
- Trusted local lane: the CLI, `gbrain call`, serve-side harvest and Markdown sync run with `remote: false`, so world-only filters, save refusals and auto-link skipping do not apply (RTE-19, RTE-22). The MCP guarantees cover only remote MCP calls.
- Direct database access: outside the protocol by the source's own statement.
- Thin client: forwards operations to a remote server, which enforces its own grants; not a bypass.
- Background lane: dream cycle and autopilot (RTE-8, RTE-9, RTE-10, RTE-23) and durable sub-agents (RTE-12) act without a user turn.
- Provider-native tools and host shell access belong to the host and are outside GBrain's enforcement.

**Forcing cases traced.**

1. *Remote write into a multi-source brain from a plugin serve.* The source guard refuses the write with `source_binding_required` unless `GBRAIN_SOURCE` binds a source; reads continue. Guarantee owner: CMP-2 dispatcher; enforcement point: before validation; strength: protocol; covered path: MCP served with `--source-guard`; alternate paths: CLI and sync. Implementation conclusion status: wired. Source: SRC-1, `src/mcp/dispatch.ts:550-590`.
2. *Upstream release changes a skill that a user edited locally.* Workspace copies: reference reports `differs` without distinguishing the edit (RTE-14). Harness copies: install hashes classify `local_edit`, and apply refuses it (RTE-15). Shared-skill cache: the adapter raises `local_conflict` and stops following (RTE-16). Plugin copies: replaced by the host marketplace refresh (uninspected). Implementation conclusion status for the three GBrain-side cases: wired.
3. *Nightly SkillOpt on a skill with a benchmark.* The phase runs one epoch under a cost cap with `noMutate: true`; an accepted candidate lands in `proposed.md`, not `SKILL.md`, and a human decides. Implementation conclusion status: wired (RTE-11).
4. *Stub skill used where the MCP surface is too narrow.* The stub instructs the host to ask for a wider surface or use `gbrain skill <slug>`; the scaffold preflight refuses stub mode when publication is disabled. Implementation conclusion status: wired (RTE-15); host behavior: uninspected.

**Decision roles on admitting routes.** Explicit memory writes: the caller proposes; a similarity rule decides supersession; the user can withdraw (RTE-1, RTE-7). Dream page generation: an LLM sub-agent proposes, code repairs quotes and auto-admits; no human veto before admission (RTE-8). Takes: an LLM proposes, a human accepts; grade auto-resolution is opt-in (RTE-10). SkillOpt: the optimizer model proposes; the judge and the numeric gate decide; a human triggers the run and, on the nightly and bundled paths, decides adoption; for shared skills an authorized editor's grant is required (RTE-11, RTE-16). Maintenance proposals: humans decide (RTE-21). Remediation: deterministic checks decide; autopilot executes (RTE-23).

**Answer oracle.** Only SkillOpt uses one at runtime: the author-supplied benchmark (rule checks, rubric, or expected slugs), in the bounded-experiment mode of a SkillOpt run. `propose_takes` reports prompt tuning against a labelled corpus offline (doctrine in the source comment), with no runtime oracle. Take grading, contradiction probing and takes-quality evaluation use model judges without expected answers.

**Improvement triggers and operating modes.** Open requests (ordinary agent use) change memory. Scheduled cycles and autopilot run maintenance and derivation. SkillOpt runs are bounded experiments over a benchmark, human-triggered or scheduled as proposal-only.

**Execution preflight.** No dynamic check planned. Checks considered: running `gbrain skillopt` on a bundled skill (would need API keys and spend, and a single run would not establish improvement); running the plugin generator to compare trees (CI already encodes that check, and static reading of the script and workflow was sufficient for the delivery findings); exercising `scaffold --harness --stub` in a scratch home (would show file writes already legible from the code, while host activation, the unresolved question, would remain uninspected). Static evidence was sufficient for every conclusion drawn; the unresolved questions concern host activation and measured benefit, which none of these checks would settle.

## Lens scoping

### Memory/context scope

Trigger evidence: OBJ-1, OBJ-2, OBJ-3, OBJ-16, OBJ-17, OBJ-12, RTE-1, RTE-3, RTE-5, RTE-6. Inspected boundary: retained material accumulated or changed through use and its write, curation and read-back routes at SRC-1, including brain-resident shared skills and SkillOpt versions; statically shipped skills and plugin trees are delivery artifacts. Pointed-to records: CMP-4, CMP-5, CMP-6, CMP-7, OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-8, OBJ-10, OBJ-11, OBJ-12, RTE-1, RTE-2, RTE-3, RTE-4, RTE-5, RTE-6, RTE-7, RTE-8, RTE-9, RTE-10, RTE-11, RTE-16, RTE-19, RTE-20. Depth: full. Rationale: memory is GBrain's primary claimed work, with several automatic write and push routes. Executed by a fresh specialist from the frozen input.

### Epistemic scope

Trigger evidence: CLM-1, CLM-2, RTE-8, RTE-10, RTE-11, RTE-21. Inspected boundary: routes that produce or change truth-apt content, check or dispose candidates, or adapt behavior from evaluation at SRC-1. Pointed-to records: OBJ-2, OBJ-3, OBJ-10, OBJ-12, RTE-1, RTE-4, RTE-7, RTE-8, RTE-9, RTE-10, RTE-11, RTE-21. Classify-only: RTE-3, RTE-5, RTE-13, RTE-14, RTE-15, RTE-16, RTE-17, RTE-18 (transport, delivery and retrieval without content change). Depth: full, compact. Rationale: GBrain makes synthesis, consolidation and self-improvement claims, and has several admission rules with different evaluators. Executed locally in overlay mode.

## Lens outputs

### Memory/context lens

Executed by a fresh specialist from the frozen input `memory-input.md` (SHA-256 `26c2ad92635b4da79478f177aa1c085436ebe6e2274a01010a0118410e046402`), under method SHA-256 `7e86ed242caadc095d7f20ccd7fcbcb837b9d62e94fca50656b782c65cb0d675`. The report records `report-status: complete` and worker model `claude-opus-5-5[1m]`. The integrated findings below use canonical IDs, and their supporting quotes sit on those records.

**Inventoried.** Pages (OBJ-1), facts and their fences (OBJ-2), takes and calibration (OBJ-3), graph edges (OBJ-4), shared skill revisions (OBJ-8), SkillOpt stores (OBJ-10), derived pages (OBJ-12), workspace memory files (OBJ-14), the Stop live buffer (OBJ-15), session context state (OBJ-16), the transcript corpus (OBJ-17), the withdrawal ledger (OBJ-18) and access metadata (OBJ-19). Routes: explicit writes (RTE-1, RTE-2, RTE-19, RTE-25), trace-fed writes (RTE-6, RTE-24, the synthesize branch of RTE-8, RTE-11), automatic operations over retained material (RTE-9, RTE-10, patterns and enrich_thin in RTE-8), maintenance (RTE-7), pull (RTE-3, RTE-4, RTE-26) and push (RTE-5, RTE-20). Static bundled skills, plugin trees and bootstrap templates are excluded as delivery artifacts. Memorable's procedure extraction is excluded.

**Findings.**

1. *Facts are the unit most memory routes produce and push, and the Markdown fence is canonical.* Every fact lane runs one pipeline that ends in a fence row plus a DB row. Provenance is required but is free text that nothing verifies (RTE-1, RTE-9).
2. *Curation handles near duplicates, not contradictions.* `remember` supersedes only a same-entity, same-visibility, same-kind candidate at cosine ≥ 0.95. Extraction lanes treat any match as a duplicate. The LLM contradiction classifier is not wired (CLM-7). Consolidation copies the highest-confidence text of a cluster into a take and makes no model call (RTE-9).
3. *Push is deterministic and labelled as data.* Per-turn and session-start context is chosen by lexical entity matching, session identity and recency, never by an embedding or model call. It is world-visible only and wrapped as "data, not instructions" (RTE-5).
4. *Compaction is a memory boundary.* PreCompact banks the window. The serve process extracts facts from it as trusted local and banks link manifests and standing entities. The same conversation receives them on re-entry (RTE-6, OBJ-16, OBJ-17). This is the only route whose task horizon is established as within-task.
5. *A second, agent-maintained tier lives outside the database.* In a bootstrapped workspace the host agent is told to keep standing rules, commitments and active context in `MEMORY.md`, which the harness imports every session and the SessionStart hook digests (OBJ-14, RTE-25, BAP-8). GBrain supplies only the doctrine and the loading.
6. *Trace learning is wired.* Automatic trace-fed writes produce retained artifacts that later sessions receive. Facts come from compaction segments, writeback turns and session-end transcripts (RTE-6, RTE-24). Dream synthesize writes pages from transcripts, opt-in by corpus configuration (RTE-8). SkillOpt writes skill versions from rollout trajectories (RTE-11).
7. *Instruction authority reaches the host model through three retained paths only:* `MEMORY.md` standing rules (BAP-8), SkillOpt and shared skill revisions (BAP-4), and the calibration block (BAP-5). Everything else arrives as knowledge.

**Retained reasons.** `MEMORY.md` rules carry their incident, which is delivered every session. Facts carry provenance and context, which are delivered in packs. SkillOpt keeps per-edit reasons in `history.json`, which no later route reads. Rejected-edit reasons are read by the next reflection. Dream pages keep a pointer to the source transcript, not a rationale.

**Comparison profile.** The frontmatter `memory-comparison` block is the specialist's proposed profile with records mapped to canonical IDs; every axis is `known` at basis `wired`. `faithfulness_tested` is `"no"` (ABS-7). `read_back_signal` is coarse, identifier and inferred-lexical; `inferred-embedding` is excluded because the push selectors make no vector call.

**Conclusions prevented.**

- Activation: whether host harnesses honour `additionalContext`, `_meta` and `@` imports.
- Any observed or causal status.
- Whether the OpenClaw context-engine lane (`src/core/context-engine.ts`, read only up to its facts call) selects by embedding. If it does, `read_back_signal` would gain `inferred-embedding` for that branch.
- The details of emotional-weight derivation, the pack-gated `extract_atoms` and `synthesize_concepts` phases, and connector ingestion.

### Epistemic lens

#### 1. Source-and-claim boundary

GBrain at SRC-1 (`6040075c6cb95be5881cc2e1b76ef7d71f4e5d29`); declared scope as in Boundary and evidence, excluding host harnesses, providers, Memorable and the evals repository. Question: which routes produce, check, accept, retain and use truth-apt content or adapt behavior. Assessed route families: explicit memory writes, fact extraction and curation, derived-page generation, synthesis, takes, contradiction probing, SkillOpt. Unassessed: company-brain, connectors, code-intel, Google open-loop extraction, schema-pack typing internals; these prevent any whole-system completeness claim about knowledge production. Missing evidence: no observed runs, so every observed candidate state is `no instance observed`. Claims: CLM-1, CLM-2, CLM-3, CLM-5.

#### 2. Epistemic-object inventory

| Object | Candidate truth-apt content | Producer → consumer | Evidence | Gap |
|---|---|---|---|---|
| OBJ-2 facts | Claims about entities, with provenance string | caller or LLM extractor → recall, push, think | SRC-1 `src/core/persistence/memory-prepare.ts` | Provenance is caller-supplied text; not verified against a source |
| OBJ-12 derived pages | LLM synthesis over transcripts, reflections, brain context | dream sub-agents, `think --save` → search, think | SRC-1 `src/core/cycle/synthesize.ts` | Quote repair checks quoted spans, not the synthesis claims |
| OBJ-3 takes, grades, profiles | Held positions with conviction; verdicts; accuracy statistics | LLM proposer and judge, human → think, nudges | SRC-1 `src/core/cycle/grade-takes.ts` | Grade verdicts rest on retrieved brain evidence only |
| OBJ-10 skill versions | Non-truth-apt procedure text; benchmark judges carry expected outputs | optimizer model → skill executions | SRC-1 `src/core/skillopt/types.ts` | Benchmark representativeness uninspected |

#### 3. Authority-route ledger

| Route | Function | Architectural status | Content/update relation | Check target → evaluator | Result and force | Epistemic authority | Operational authority | Behavioral-authority path |
|---|---|---|---|---|---|---|---|---|
| RTE-1 | retention and disposition | implemented | truth-apt transformation: acquisition/import | new fact vs same-entity facts → embedding similarity ≥ 0.95 | insert, duplicate or supersede; enforcing on recall eligibility | none beyond caller's assertion; supersession is similarity, not truth | changes which fact recall returns | BAP-7 |
| RTE-9 | content transformation and dedup | implemented | truth-apt transformation: indeterminate (LLM extraction may paraphrase or infer) | turn or page → LLM extractor; duplicates by fingerprint and cosine (the LLM classifier is unwired, CLM-7) | automatic retention | preserved source link, unverified extraction | changes recall and push | BAP-7 |
| RTE-8 | content transformation | implemented | ampliative conjecture | quoted spans → verbatim transcript match | auto-admitted pages; quotes repaired or unquoted | quote fidelity only | pages enter retrieval | BAP-2 via push, requested reads |
| RTE-4 | content transformation, check | implemented | ampliative conjecture | citations → membership in gathered set | answer returned; persisted only on local save | citation presence, not support | none unless saved | requested read |
| RTE-10 (propose) | disposition/acceptance | implemented | ampliative conjecture | proposed take → human | accept or leave queued | human judgment, criterion unspecified | take becomes active | BAP-5 |
| RTE-10 (grade) | check/evidence production | implemented | no content change until applied | take → LLM judge over retrieved evidence | cached verdict; resolution only when opted in | verdict relative to brain evidence | none by default | BAP-5 |
| RTE-21 | check/evidence production | implemented | no content change | page pairs → LLM judge; health → collectors | report and paste-ready commands | suspected contradiction only | none; human applies | none automatic |
| RTE-11 | behavior/policy adaptation | implemented | non-truth-apt policy/content update: SKILL.md procedure revision | candidate skill → judge against author benchmark on selection tasks | accept if median > best + 0.05; instruction force on later runs | benchmark performance within its tasks | replaces or proposes skill text | BAP-4 |

#### 4. Per-object lifecycle disposition

OBJ-12 (RTE-8, RTE-4): ampliative conjecture. Observation: transcripts and reflections as input, implemented, no instance observed. Conjecture: LLM sub-agent synthesis, implemented, no instance observed. Derived consequence: no route found within boundary. Test/evidence: quote-span verification against the source transcript, implemented, no instance observed; it tests quotation fidelity, not the synthesized claims. Acceptance: no evidence-consuming acceptance transition; pages are admitted on write (no route found within boundary). Lifecycle integration: not reached as post-acceptance integration; retention and retrieval use happen before any acceptance.

OBJ-3 takes (RTE-10): ampliative conjecture. Conjecture: LLM proposal, implemented, no instance observed. Acceptance: human accept, implemented; evaluator human, criterion unspecified, intended use later reasoning and calibration; no instance observed. Test/evidence: grade_takes judges against retrieved evidence, implemented, no instance observed; auto-applied only when enabled. Integration: calibration profile and `think --with-calibration`, implemented, no instance observed.

OBJ-2 facts (RTE-1, RTE-9): explicit facts are acquisition/import, discovery lifecycle not applicable; warrant is the caller's provenance string, preserved as text and unverified. LLM-extracted facts are indeterminate: classifications still possible are non-ampliative reshaping or ampliative inference; lineage to the source page or turn is preserved; evidence needed is a fidelity check between extracted fact and source text, not found.

No lifecycle record for OBJ-10: no candidate truth-apt output for this object; relevant direct-adaptation routes: RTE-11.

#### 5. System-claim versus route comparison

| Claim | Layer | Implemented routes | Observed or causal support | Supported conclusion |
|---|---|---|---|---|
| CLM-1 | doctrine, reported operation | RTE-8, RTE-9, RTE-10, RTE-23 | none in boundary | Overnight citation repair, consolidation and enrichment routes exist; "smarter" is unsupported at this boundary |
| CLM-2 | doctrine | RTE-11 | none in boundary | The acceptance rule matches the claim within the benchmark; measured gains are not observed |
| CLM-3 | reported operation | RTE-3 | external repository excluded | Claimed only |
| CLM-5 | doctrine about external component | none inspectable | none | Claimed only |

#### 6. Bounded conclusion

GBrain retains, retrieves and reshapes large volumes of content and generates ampliative content automatically (RTE-8, RTE-9) and on request (RTE-4). Its checks are fidelity and membership checks: quote spans against transcripts, citations against the gathered set, and similarity thresholds for duplicates and near-duplicate supersession. Contradiction detection between facts is not wired (CLM-7), and consolidation is deterministic. None of them tests the truth of the synthesized claims. The only human acceptance gates on truth-apt content are take proposals and the proposal-only maintenance routes. The one route with an external expected-answer oracle is SkillOpt, and it adapts procedure text rather than producing truth-apt claims. Imported facts keep caller-supplied provenance as unverified text. The overnight "smarter" claim remains unsupported at this boundary for lack of observed or causal evidence.

## Reconciliation

**Specialist proposal-ID mappings.**

| Proposal | Disposition | Canonical ID |
|---|---|---|
| MEM-OBJ-1 | registered | OBJ-14 |
| MEM-OBJ-2 | registered | OBJ-15 |
| MEM-OBJ-3 | registered as one part of the OBJ-11 split | OBJ-17 |
| MEM-OBJ-4 | registered | OBJ-18 |
| MEM-OBJ-5 | registered | OBJ-19 |
| MEM-RTE-1 | merged: SessionStart push was already part of RTE-5 | RTE-5 |
| MEM-RTE-2 | registered | RTE-24 |
| MEM-RTE-3 | merged: the page-write backstop was already part of RTE-9 | RTE-9 |
| MEM-RTE-4 | registered | RTE-25 |
| MEM-RTE-5 | registered | RTE-26 |
| MEM-CLM-1 | registered | CLM-7 |
| MEM-CLM-2 | registered | CLM-8 |
| MEM-CLM-3 | registered | CLM-9 |
| MEM-CLM-4 | registered | CLM-10 |
| MEM-ABS-1 | merged, independent convergence | ABS-4 |
| MEM-ABS-2 | registered | ABS-7 |
| MEM-BAP-1 | registered | BAP-8 |
| MEM-BAP-2 | merged | BAP-4 |
| MEM-BAP-3 | merged | BAP-5 |

Profile references to OBJ-11 in the report denote session context state and were mapped to OBJ-16.

**Amendments.**

- OBJ-11 split. Superseded value: one record for session state and corpus files. Replacement: OBJ-16 (session context state) and OBJ-17 (raw transcript corpus); OBJ-11 is marked superseded. Evidence: `src/core/context/session-state.ts`, `src/core/sweep.ts`. Affected findings: storage and lineage axes, RTE-6.
- RTE-9. Superseded value: "a Haiku classifier decides duplicate, supersede or independent" and a cycle `extract_facts` that extracts. Replacement: the classifier has no non-test importer, extraction lanes never supersede, and the cycle phase reconciles DB rows from fences without a model. Evidence: the coordinator ran `git grep classifyAgainstCandidates`, which finds only `src/core/facts/classify.ts` and `test/facts-classify.test.ts`, and read `src/core/cycle/extract-facts.ts`. Affected findings: the epistemic ledger row for RTE-9, CLM-7, the curation axis, and the Synthesis mechanism (a).
- RTE-1. Superseded value: supersession described without its limits. Replacement: near-duplicate replacement only, with contradictions inserted beside existing facts. Evidence: `src/core/facts/single-prepare.ts`. Affected findings: epistemic bounded conclusion.
- RTE-8. Superseded value: synthesize treated as generally active. Replacement: synthesize is opt-in through corpus configuration, and branches are distinguished by lineage. Evidence: the coordinator confirmed `src/core/cycle/synthesize.ts:1522` (`session_corpus_dir`). Affected findings: the lineage and trace-learning axes, Synthesis.
- RTE-11. Superseded value: nightly no-mutate stated without the MCP trigger. Replacement: adds the admin-scoped `run_skillopt` (the coordinator confirmed `src/core/ops/skillopt.ts:127-128`) and CLM-9. Affected findings: decision roles.
- RTE-5. Superseded value: session-start contents summarized. Replacement: detailed selector inputs and the Postgres IPC lane (CLM-8). Affected findings: the read-back signal axis.
- OBJ-2 amended with the session loss on fence rebuild (CLM-10).
- BAP-4 amended for shared-skill revisions and reason retention.
- BAP-5 amended from knowledge to instruction on question framing, reachable only through the CLI flag.

**Independent convergence.** ABS-4 (auto_think not wired) was found by the coordinator's grep of `src/core/cycle.ts` and separately by the specialist from the phase's own comment. The no-mutate behavior of the nightly SkillOpt path was found by both, from the same line.

**Integration-issue dispositions.** The specialist listed twelve issues. Items 1–8 were adopted as the amendments above. Items 9–11 were adopted through the mappings above. Item 12 (activation of `_meta`, `@` imports and `additionalContext`) was retained as the Limitations row on the host harness. No conflict required return to the specialist.

**Ownership check.** RTE-5 and RTE-9 now carry merged specialist routes and keep their generic runtime identity. Shared routes RTE-11 and RTE-16 are owned by the runtime account, with memory classifications only in the profile.

Cross-lens ownership: RTE-11 appears in both lenses. The epistemic lens classifies it as a behavior/policy adaptation; the memory lens owns its trace-learning classification. Neither lens changes the canonical route record. RTE-16 is a delivery route in the runtime account; the memory lens treats shared skills as retained material only because use (editor publication, optimization) changes them.

Scout reports used during the runtime baseline were source-only locators; every load-bearing finding above was re-read or quote-checked against SRC-1 by the coordinator. One scout excerpt of `src/mcp/surface.ts` contained a scout-inserted ellipsis and was not quoted.

## Bounded synthesis

**Evidence basis and boundary.** Static reading of the GBrain repository at `6040075c6cb95be5881cc2e1b76ef7d71f4e5d29` (v0.54.1.0), cutoff 2026-09-23. The boundary is a complete artifact inside a partial loop: GBrain does not own the agent loop, so every claim about what a host does with delivered skills, hooks or context stays uninspected.

**Architectural characterization and claimed work.** GBrain is a memory and context service for agents that already exist. It stores pages and provenance-carrying facts in PGLite or Postgres with Markdown files as the canonical form for file-backed pages, exposes one operation contract through a CLI and MCP servers, and adds three layers around that core: retrieval and cited synthesis, automatic context push through harness hooks, and background maintenance through a nightly cycle and a durable job queue. It also ships a large skill set and treats the distribution of that skill set as a product surface in its own right.

**Runtime map.** Explicit writes (RTE-1, RTE-2) and trusted imports (RTE-19) fill the store; requested reads (RTE-3, RTE-4) and pushed context (RTE-5, RTE-20) return it. Compaction harvest (on by default in the bootstrap lane), opt-in ambient writeback (RTE-6), session-end sweep extraction (RTE-24) and the page-write backstop (RTE-9) extract facts automatically. The dream cycle derives pages and takes (RTE-8, RTE-10) and curates facts (RTE-9). Authorization (RTE-22) separates remote MCP callers from trusted local lanes; the local lanes, Markdown sync and direct SQL fall outside the remote-caller guarantees, which the source documents.

**Delivery mechanisms (the caller's focus).** GBrain ships its agent-facing parts through six mechanisms with different update semantics:

1. *Plugins* (RTE-13): one generated skill tree per lane, persona variants as self-contained plugin roots, byte-exact drift gating in CI, and a history-less `codex-plugin` branch rebuilt on every release. Every lane addition or exclusion carries a written reason. The plugin supplies skills and a launcher-started MCP server, but no hooks, and nothing checks an installed plugin's version at runtime.
2. *Workspace scaffold* (RTE-14): copy once, never overwrite, then compare. Without install hashes the lens reports differences but cannot tell an edit from upstream change.
3. *Harness bridge* (RTE-15): the same copy with per-file install hashes, giving a three-way classification that allows safe application of upstream drift and refuses local edits.
4. *Stub skills* (RTE-15): frontmatter stays local for discovery; the body is fetched at use time through `get_skill` or `gbrain skill`. Currency is relative to the serving host's skill source.
5. *Shared brain skills* (RTE-16): skills become versioned brain content with compare-and-set publication, separate editor and publisher grants, hash-checked delivery into a harness cache, and a router skill that tells the agent to sync before selecting. The source itself labels router activation as advisory and unverified.
6. *Bootstrap and in-agent installs* (RTE-17): marker-delimited instruction blocks, marker-keyed hook entries, and receipts recording owned files and hashes so that reinstall, upgrade and uninstall touch only what GBrain wrote.

Upgrade (RTE-18) connects them: a machine marker announces new versions to an upgrade skill, `post-upgrade` applies migrations, and a sweep lists new and drifted scaffolded skills without overwriting. Across all six, the consistent rules are: never overwrite a file the user may have edited, record ownership by hash where GBrain wrote the file, and treat activation in the host as unverified.

**Memory.** Facts with required but unverified provenance are the main retained unit. The Markdown fence is canonical and the database mirrors it. Automatic fact capture runs from compaction segments, opt-in writeback turns, session-end transcripts and page writes (RTE-6, RTE-24, RTE-9). These are wired trace-learning routes whose extracted facts reach later sessions through requested reads and deterministic push. A bootstrapped workspace adds an agent-edited `MEMORY.md` tier that the harness loads as instructions every session (OBJ-14, BAP-8).

**Discriminating mechanisms.** (a) Supersession by embedding similarity rather than any truth check. It covers only near duplicates: contradicting facts below cosine 0.95 accumulate side by side, because the LLM contradiction classifier is not wired (RTE-1, RTE-9, CLM-7). (b) Automatic ampliative page generation, admitted after quote-span repair, with no acceptance step (RTE-8). (c) A world-only view for remote callers across recall, push and synthesis (RTE-3, RTE-4, RTE-5). (d) SkillOpt's benchmark-gated revision of instruction text, which can propagate through shared-skill publication to every following installation (RTE-11, RTE-16).

**Scenario-relative assessment.** For a single user adding memory to an existing coding agent, the plugin or MCP path gives requested memory with provenance, correction and withdrawal, and requires no model API for keyword recall. Push context and automatic capture need the bootstrap lane and opt-in configuration. For a team brain, remote grants and visibility filters constrain MCP clients; shared local files and credentials do not isolate agents, as the source states. For skill distribution across many harnesses, shared brain skills provide versioned, authorized and hash-checked delivery; the plugin lane provides the simplest install but no GBrain-side currency check.

**Learning, reflection and self-improvement.** The strongest supported contribution is SkillOpt (RTE-11), and its components hold at different strengths:

- *Formulated theory.* A skill's text states a procedure for a task. Formulation status: wired.
- *Operative use.* The target model runs that text on benchmark tasks. Operative-use status: wired.
- *Content-directed criticism.* The optimizer reads the text, failure trajectories and the stated scoring criteria, and must tie each edit to an observed failure with a stated reason. Criticism status: wired, though the optimizer's reasoning itself is inaccessible model processing. The benchmark tests stated consequences of the skill.
- *Revision.* Edits are accepted only when they clear a numeric margin over the current best on selection tasks. Revision status: wired.
- *Retention.* Rejected edits and their gate reasons persist and are read by later reflection against the same skill text. Accepted edits persist with their reasons in `history.json`, which no later route reads except crash recovery.
- *Improved capacity.* Attributable improvement is what the gate tests, but no run within this boundary shows a gain, so the improved-capacity claim is `uninspected`. Addressability is high over one skill body: edits target exact anchors and frontmatter is fixed.

Whether criticism of the operative skill text improved the system's future capacity therefore remains unestablished for want of run evidence.

Reflection holds at two selected aspects, each wired:

- Doctor and remediation represent brain health; the represented state changes with the brain, and plans mediated by that representation change later state (RTE-23).
- SkillOpt represents a skill's performance as benchmark scores, and those scores gate the text that governs later runs (RTE-11).

No route was found that revises GBrain's own theory-building organization; the reflective-builder claim is not established.

Self-improvement at the declared boundary is wired but gated by humans:

- Local SkillOpt runs commit accepted versions.
- The nightly path only proposes.
- Bundled skills need a held-out set and an explicit flag.
- Shared-skill publication needs editor authority.

The dream cycle's automatic page generation and fact curation change the knowledge the system serves; it does not revise the procedures that produce it. Wired trace learning (facts from session traces) is a memory property; it does not establish conjectural learning. The extracted facts are not theories whose criticism is recorded, and no route tests whether recalling them improves later work (ABS-7).

**What would change this assessment.** Retained SkillOpt run records with selection and held-out scores would move improved capacity from uninspected toward observed. Host-side traces of skill selection and hook context would settle activation. A check of synthesized claims against sources, rather than of quoted spans, would change the epistemic reading of RTE-8. A runtime comparison of installed plugin versions would close ABS-1.

## Limitations

| Limitation | Affected IDs | Inspected boundary | Conclusion prevented | Evidence that would resolve it |
|---|---|---|---|---|
| No dynamic execution | SRC-1, all RTE-* | Static source at the reviewed commit | Any observed or causally supported status | Instrumented runs of the named routes |
| Host harness excluded | CMP-13, BAP-1, BAP-2, BAP-3, RTE-5, RTE-13, RTE-15, RTE-16, RTE-17 | GBrain side of delivery and hooks | Activation of skills, hooks and instruction blocks | Host transcripts showing skill selection and injected context |
| Provider internals excluded | CMP-5 | Gateway call sites and defaults | Model version resolution for undated aliases; output quality | Provider version logs per call |
| Memorable implementation not in repository | CLM-5 | GBrain hook, consent gate and docs | Procedure extraction and revision scoring | Memorable source or run records |
| Evals repository and production deployment excluded | CLM-1, CLM-3 | README claims | Benchmark and scale verification | `gbrain-evals` scorecards at a pinned revision |
| Unread subsystems | SRC-1 | company-brain, connectors, code-intel, Google loops, schema-pack internals, admin SPA not read | Completeness of the write-route and epistemic inventories | Targeted reading of those subsystems |
| SkillOpt outcomes not observed | RTE-11, CLM-2, OBJ-10 | Implementation and docs | Whether any skill improved | Retained `history.json`, receipts and held-out scores from real runs |
| Marketplace refresh behavior external | RTE-13, ABS-1 | Release workflow and manifests | How quickly installed plugins track releases | Host marketplace documentation or observation |

## Verification and blockers

### Semantic verification

Checked after reconciliation against the result type's comparison rules:

- **Profile scope versus records.** The profile scope names the same objects and routes as OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-8, OBJ-10, OBJ-12, OBJ-14, OBJ-15, OBJ-16, OBJ-17, OBJ-18, OBJ-19 and the listed routes. Static skills, plugin trees and templates (OBJ-5, OBJ-6, OBJ-9) are excluded explicitly. Every axis record resolves to a declared canonical ID. Superseded OBJ-11 is not referenced by any axis.
- **Trace-fed writes against the learning criterion.** Compaction harvest and writeback (RTE-6), session-end sweep (RTE-24), the synthesize branch of RTE-8, and SkillOpt (RTE-11) each have automatic trace-fed production, retention and a named later consumer. Their source, scope, timing and form are carried into the trace-learning axes. RTE-9 backstop extraction works over retained pages, not traces, and is excluded from trace learning.
- **Push signals.** Each push signal has its trigger, selector input and selected part named on RTE-5 and RTE-20. The identifier signal rests on session-ID selection of facts, banked entities and checkpoint links; a catalog entry alone is not counted. Requested reads (RTE-3, RTE-4, RTE-26) are counted as pull only.
- **Amendments.** Every amendment stays attached to its original canonical ID and referent. The OBJ-11 split uses new IDs.
- **Overlays.** The epistemic overlay cites canonical IDs without redefining them.
- **Specialist corrections.** The coordinator independently verified four: the unwired classifier (grep), synthesize gating, the cycle `extract_facts` phase, and `run_skillopt`.
- **Load-bearing guarantees.** Each names owner, enforcement point, strength and alternate paths (RTE-22, forcing case 1).
- **Quote occurrence.** Every quote block was checked for whitespace-normalized occurrence in its pinned blob with a local script before publication.
- **Assessment.** No known assessment is unsupported by its records. Remaining uncertainty is scoped in Limitations.

### Deterministic validation

`commonplace-validate --full kb/reports/state/agentic-system-analysis/AAS-2026-09-23-gbrain-01/result.md` was run on the final bytes before publication and passed.

### Blockers

none
