---
description: "Zikkaron review: local Claude Code memory engine with SQLite/vector retrieval, trace capture, hook-based context injection, and compaction replay"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived, push-activation]
status: current
last-checked: "2026-06-02"
---

# Zikkaron

Zikkaron, from amanhij, is a local Python MCP server and hook package for Claude Code memory. At the reviewed commit it stores memories, entities, relationships, checkpoints, action logs, rules, profiles, derived beliefs, and vector indexes in one SQLite database; exposes explicit MCP tools for remembering, recalling, seeding, checkpointing, restoring, rules, and diagnostics; and installs Claude hooks that capture tool actions and inject selected memory into future sessions and prompts.

**Repository:** https://github.com/amanhij/Zikkaron

**Reviewed commit:** [dda34a5d903d04ecb5517af214d437873c833302](https://github.com/amanhij/Zikkaron/commit/dda34a5d903d04ecb5517af214d437873c833302)

**Last checked:** 2026-06-02

## Core Ideas

**The durable substrate is a local SQLite memory database.** `StorageEngine` initializes `~/.zikkaron/memory.db` by default, enables WAL and foreign keys, loads `sqlite-vec`, and creates tables for episodes, memories, FTS, vectors, entities, relationships, profiles, derived beliefs, prospective triggers, rules, archives, transitions, causal edges, checkpoints, and an `action_log` ([storage.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/storage.py), [config.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/config.py)). The repository is not a git-native note system; git only carries the implementation.

**Memory writes are gated, enriched, and classified before later retrieval.** The `remember` MCP tool runs a predictive-coding write gate before storage, embeds content with an optional contextual prefix, computes thermodynamic scores, lets the curator merge/link/create memories, classifies each memory into episodic or semantic store, assigns astrocyte/engram/HDC metadata, auto-protects strong decision patterns, and may create a micro-checkpoint or return related context ([server.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/server.py), [predictive_coding.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/predictive_coding.py), [curation.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/curation.py), [cls_store.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/cls_store.py)).

**Retrieval is multi-signal fusion rather than one vector lookup.** `HippoRetriever.recall()` combines FTS5, vector search, graph PageRank, spreading activation, fractal clusters, Hopfield energy, HDC, successor-representation navigation, temporal matching, optional cross-encoder/NLI/multi-passage reranking, profile/belief search, neuro-symbolic rules, and metacognitive context management before returning a bounded result set ([retrieval.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/retrieval.py), [rules_engine.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/rules_engine.py), [metacognition.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/metacognition.py)). Context efficiency is implemented through `max_results`, candidate pools, hook-level character/result caps, cognitive-load limiting, heat thresholds, and compaction replay budgets; some explicit pull tools, especially `get_project_context`, still return all hot memories for a directory unless the caller or hook path limits them.

**Claude hooks turn stored memory into automatic read-back.** `install_hooks()` writes project `.claude/settings.json` entries for `PreCompact`, `SessionStart`, `PostToolUse`, and `UserPromptSubmit`, copying five hook scripts into `.claude/hooks/` ([server.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/server.py)). The `SessionStart` hook prints checkpoint, anchored facts, hot project memories, and recent actions to stdout; the `UserPromptSubmit` hook performs FTS/vector retrieval over the SQLite database and prints up to five memories within a 3,000-character budget, so memory reaches Claude's context without an explicit tool call ([session-start-context.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/hooks/session-start-context.py), [prompt-recall.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/hooks/prompt-recall.py)).

**Trace capture is split between a hot path and a consolidation path.** The `PostToolUse` hook writes lightweight tool-call rows directly to `action_log`, skipping Zikkaron tools to avoid loops; `AstrocyteEngine._process_action_log()` later groups unprocessed actions by directory and 30-minute bucket and creates low-heat `_action_stream` memories for groups of at least three actions ([post-tool-capture.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/hooks/post-tool-capture.py), [consolidation.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/consolidation.py)). That is the clearest code-grounded trace-derived learning path.

**Project seeding gives a cold-start import path.** `seed_project` scans a project tree, parses common config formats, reads documentation, CI files, entry points, and component boundaries, generates `_seed` memories with differentiated heat, and replaces prior seed memories for the same directory on rerun ([seed.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/seed.py), [server.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/server.py)). This is source-derived project memory, not trace-derived agent learning.

## Artifact analysis

- **Storage substrate:** `sqlite` — SQLite tables plus `sqlite-vec` virtual tables and FTS5
- **Representational form:** `prose` `symbolic` `parametric` — prose memory content, symbolic metadata/scores/graph edges/rules, and distributed-parametric embeddings/HDC vectors plus FTS tokens
- **Lineage:** `authored` `imported` `trace-extracted` — authored via `remember`, imported by seed scans of project files, and trace-extracted from action logs; consolidation abstracts derived views
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — recall returns knowledge/advisory context; policies instruct; hard rules enforce by filtering candidates; retrieval routes; classification validates; heat/embeddings/rerankers rank; consolidation learns schemas

**Memory rows and vector/FTS indexes.** Storage substrate: SQLite tables plus `sqlite-vec` virtual tables and FTS5. Representational form: mixed prose memory content, symbolic metadata and scores, distributed-parametric embeddings/HDC vectors, and FTS tokens. Lineage: authored via `remember`, generated from seed scans, derived from action logs, or abstracted by consolidation; file changes, model changes, compression, curation, and consolidation can invalidate or regenerate derived views. Behavioral authority: knowledge artifact when returned by recall; ranking artifact through heat, embeddings, graph signals, rules, rerankers, and metacognitive trimming; advisory context when hooks or tools print memories into Claude context.

**Action logs, checkpoints, and anchors.** Storage substrate: SQLite `action_log`, `checkpoints`, and protected memory rows. Representational form: symbolic event summaries plus prose checkpoint/anchor content. Lineage: `PostToolUse`, `PreCompact`, explicit `checkpoint`, `anchor`, and micro-checkpoint triggers. Behavioral authority: action logs begin as raw trace knowledge artifacts, then become summarized memories during consolidation; checkpoints and anchors have stronger advisory authority because restore/session-start paths explicitly select them for injection.

**Consolidation, compression, curation, and classification policies.** Storage substrate: Python source, regexes, settings, prompts/heuristics, thresholds, and scheduled daemon loops. Representational form: symbolic code and prose comments/configuration. Lineage: authored system-definition artifacts; changing thresholds, similarity cutoffs, compression ages, retrieval weights, or hook budgets changes what is stored, retained, compressed, promoted, or read back. Behavioral authority: instruction, extraction, validation, ranking, routing, compression, and scheduling.

**Graph, causal, profile, belief, rule, and prospective-memory stores.** Storage substrate: SQLite tables and authored engines. Representational form: mixed symbolic graph edges/rules/triggers, prose profile/belief content, embeddings, and confidence fields. Lineage: extracted from memory content, authored through MCP tools, derived by enrichment/profile/belief/consolidation engines, or triggered by future-oriented phrases. Behavioral authority: mostly ranking, filtering, route, and advisory context; hard rules can filter retrieval candidates, while prospective triggers surface matching future reminders.

**Claude Code integration files.** Storage substrate: repository hook scripts copied into project `.claude/hooks/` and JSON hook configuration written under `.claude/settings.json`. Representational form: executable Python/shell plus symbolic hook configuration. Lineage: installed by `install_hooks()` from package source; updates require reinstall or sync. Behavioral authority: system-definition artifact authority over capture and read-back timing because these hooks decide when memory is captured and when selected memory is printed into the host agent's context.

Promotion path: Zikkaron has several promotion-like routes: raw tool actions -> grouped action-stream memory; episodic memories -> semantic schemas in CLS consolidation; raw content -> protected decision memory; project files -> seed memories; and retrieved memories -> reconsolidated or compressed records. It does not have an explicit human review gate before advisory memories gain prompt-injection authority.

## Comparison with Our System

| Dimension | Zikkaron | Commonplace |
|---|---|---|
| Primary purpose | Runtime memory engine for Claude Code sessions | Git-native methodology KB for agent-operated knowledge systems |
| Canonical retained artifact | SQLite memory row, trace summary, checkpoint, rule, trigger, profile, belief | Typed Markdown note, instruction, source, review, ADR, index, report |
| Storage substrate | Local SQLite, FTS5, sqlite-vec, hook files, Python code | Repository files plus generated indexes and validation/review reports |
| Write path | MCP tools, hook capture, seed scans, consolidation daemons | Explicit file edits under collection/type contracts, source snapshots, review/validation |
| Read-back | Explicit MCP pull plus hook-based session/prompt/compaction push | Mostly deliberate pull through `rg`, indexes, links, skills, and loaded instructions |
| Governance | Gates, heat, rules, staleness, compression, tests, hook config | Type specs, collection contracts, citations, git diffs, validators, semantic gates |

Zikkaron is stronger than Commonplace as an always-on runtime memory layer. It can capture tool traces, inject context at session/prompt/compaction boundaries, run local retrieval over a large memory store, and manage heat, compression, and automatic recall without making the agent browse a repository.

Commonplace is stronger as a governed knowledge substrate. Its retained artifacts are inspectable Markdown files with collection contracts, type specs, citations, validation, semantic review, and git history. Zikkaron has many local control signals, but memories can become injected advisory context without the kind of explicit source review and authority promotion Commonplace requires.

**Read-back:** `both` — With engineered push activation. `recall`, `get_project_context`, `restore`, and other MCP tools are explicit pull surfaces; installed Claude hooks push selected memories, checkpoints, actions, and prompt-matched recall into context before the receiving agent acts.

### Borrowable Ideas

**Hook-level context budgets.** Ready for narrow experiments. Zikkaron's prompt hook caps result count and total injected characters, while session-start injects small sections for last task, anchors, project context, and recent actions. Commonplace could borrow that shape for active-workshop context without changing the library substrate.

**Action-log hot path plus delayed consolidation.** Ready for workshop traces, not for library authority. Capturing raw tool events cheaply and summarizing them later is a clean separation. In Commonplace, those summaries should land as work reports or draft notes until reviewed.

**Protected anchors for compaction recovery.** Ready as an instruction/workshop concept. A user- or agent-marked "must survive compaction" fact is useful, but Commonplace should label it as advisory retained context unless promoted into an instruction or validated artifact.

**Separate storage authority from activation authority.** Ready now as vocabulary. Zikkaron shows that the same memory row can be pulled by a tool, selected by a prompt hook, or restored after compaction. Commonplace should keep classifying where a retained artifact lives separately from how it enters context.

**Do not borrow automatic prompt injection without review boundaries.** Needs a use case and gates. Zikkaron's hooks are effective, but automatic read-back can give stale or weak memories practical authority. Commonplace should require trace lineage, budgets, and observable effect checks before broad push activation.

## Write-side placement

**Write agency:** `automatic` `manual` — the write gate, curator, consolidation daemons, and hook trace capture change the store without the user; `remember` and the other MCP tools are the manual authoring channel

**Curation operations:** `consolidate` `dedup` `evolve` `decay` `promote` — CLS consolidation abstracts episodic memories into semantic schemas and compresses by age; the curator merges/links near-duplicates; enrichment reconsolidates existing entries in place; heat decay and age compression evict cold memories; auto-protection and heat reweighting promote salience

### Trace-derived learning

- **Trace source:** `session-logs` `tool-traces` `event-streams` — `PostToolUse` action rows, compaction/session traces, and hook event streams
- **Learning scope:** `per-project` `cross-task` — directory/project-scoped action memories plus cross-task semantic schemas from consolidation
- **Learning timing:** `online` `staged` — the action hook captures online; consolidation is staged until idle or explicit `consolidate_now`
- **Distilled form:** `prose` `symbolic` `parametric` — compressed prose memories, symbolic schemas/rules, and embedding/HDC vectors

**Trace source.** Zikkaron qualifies as trace-derived. The clearest trace source is Claude Code `PostToolUse` input: tool name, selected input summary, current directory, session id, and timestamp are stored in `action_log`. Compaction/session traces are captured through checkpoints, pre-compact drain, restore, and session-start context. Manual `remember` calls can also store task outcomes, but the code-grounded automatic trace path is the hook action stream.

**Extraction.** The hot path records only compact event summaries. During consolidation, unprocessed actions are grouped by directory and 30-minute window; groups with at least three actions become low-heat memories tagged `_action_stream` and `_auto`. Other extraction paths derive entities, relationships, semantic schemas, profiles, beliefs, and compression summaries from memory content using regexes, embeddings, clustering, enrichment engines, and heuristics rather than a human review oracle.

**Four fields.** Raw trace stage: SQLite `action_log` and checkpoint rows, symbolic summaries, lineage from Claude hook events, behavioral authority as audit/source knowledge until processed or injected. Distilled stage: `_action_stream` memories, semantic memories, protected anchors/checkpoints, graph/profile/belief/rule-derived state, with mixed prose/symbolic/distributed forms and advisory/ranking/filtering/prompt-injection authority depending on the read path. System-definition stage: hook scripts, consolidation code, write gates, scoring policies, and settings determine what traces are captured, summarized, retained, and activated.

**Scope and timing.** Scope is per local database, directory, session id, time bucket, and hook-installation project. The action hook is online and cheap; consolidation is delayed until idle or explicit `consolidate_now`; session/prompt hooks read before action; compaction hooks drain before compaction and restore after compaction.

**Survey placement.** Zikkaron belongs in the trace-to-summary-memory and trace-to-runtime-context families. It strengthens the survey split between raw trace capture and distilled behavior-shaping artifacts: raw tool rows do little by themselves, while grouped action memories, checkpoints, anchors, and hook-selected memories can shape future agent behavior. It also shows the governance risk of trace-derived systems whose automatic summaries can be injected without a review step.

## Read-back placement

**Direction.** Zikkaron is both pull and push. MCP tools such as `recall`, `get_project_context`, `restore`, `memory_stats`, and `get_rules` are pull. Installed Claude hooks push retained memory on `SessionStart`, `UserPromptSubmit`, and post-compaction restore; `PreCompact` and `PostToolUse` capture memory for later read-back rather than themselves returning memory to the agent.

**Read-back signal:** `coarse` `identifier` `inferred / lexical` `inferred / embedding` — mixed push targeting: `SessionStart` and post-compaction restore carry `coarse` session/anchor state and `identifier` directory selection for hot project memories, while `UserPromptSubmit` adds `inferred / lexical` (FTS5 over prompt terms) and `inferred / embedding` (sqlite-vec over the prompt embedding) recall.

**Faithfulness tested:** `no` — the repo ships tests and benchmark scripts, but there is no code-grounded with/without ablation proving injected context changes downstream behavior.

**Targeting and signal.** Zikkaron has mixed push targeting. The `UserPromptSubmit` hook is `instance`-targeted: it extracts the current prompt, runs FTS5 over prompt terms (`inferred / lexical`) and optionally sqlite-vec over the prompt embedding (`inferred / embedding`), then boosts current-directory, non-action-stream, and high-heat memories within result, character, and time budgets. The `SessionStart` hook is mixed but mostly `instance`: it uses `cwd` as an `identifier` for hot project memories, always includes protected anchors globally, and includes the latest active checkpoint and recent actions as coarse session context. Post-compaction restore is also mixed: active checkpoint and recent/anchored memories are coarse or session-carried state, hot project memories are `identifier`-selected by directory, and SR prediction uses checkpoint task or directory text as an inferred query. Precision, recall, and context dilution are not verified from code.

**Injection point.** The read-back assembles before the receiving Claude turn acts: `UserPromptSubmit` and `SessionStart` print into context pre-invocation, and post-compact restoration reconstructs context for the resumed session. `PreCompact` and `PostToolUse` fire after the turn but are write-side capture/maintenance, not a second read (see Write-side placement).

**Selection, scope, and complexity.** Selection is bounded in hook code: prompt recall uses `MAX_RESULTS = 5`, `MAX_CONTEXT_CHARS = 3000`, and a 0.5 second time budget; session-start limits checkpoint, anchors, hot project memories, and recent actions. Full MCP recall has caller-provided `max_results`, many internal candidate/rerank stages, and metacognitive trimming. Complexity can still be high because the retrieval stack combines many signals and derived stores.

**Authority at consumption.** Hook output is advisory context, but it has practical prompt authority because it arrives in Claude's context before the next response. Rules can hard-filter retrieval candidates; anchors are always included in restoration; checkpoints define "what you were doing." Effective model faithfulness is not verified by code.

**Faithfulness.** The repository contains extensive tests and benchmark scripts, but I did not run the benchmark suite and did not find a code-grounded with/without hook ablation proving that injected context changes downstream Claude behavior reliably. The code proves activation and selection mechanics, not effective behavioral compliance.

**Other consumers.** Human operators and agents can inspect memory stats, hot/stale memories, narratives, rules, coverage, gaps, causal chains, and seed output through MCP resources and tools. These are pull-oriented observability and governance surfaces.

## Curiosity Pass

**The implementation is much broader than the core product need.** The strongest mechanism is local SQLite memory plus hooks. Many neuroscience-named modules are implemented, but the design value for Commonplace comes less from the labels and more from the concrete capture, ranking, compression, and injection paths.

**Some README claims require runtime or benchmark trust, not just code reading.** The repository includes benchmark scripts and advertised scores, but this review did not reproduce LoCoMo, BEAM, LongMemEval, or the 998-test claim. Treat those as product claims unless separately verified.

**Automatic context is a double-edged affordance.** Zikkaron solves "agent forgets to look" by pushing memories into context. That same mechanism can over-authorize unreviewed, stale, or weakly summarized memories unless selection and faithfulness are audited.

**Project seeding is simpler and more durable than many neural mechanisms.** The seed scanner's config/doc/CI/component extraction is an adoption-friendly cold-start path. It is source-derived, inspectable, and rerunnable.

**The pull/push boundary is unusually explicit.** The same database supports direct MCP calls, hook injection, and compaction restore. That makes Zikkaron a good example for separating retained artifact analysis from activation-path analysis.

## What to Watch

- Whether hook-injected memories gain source snippets, timestamps, or confidence markers in the emitted text; that would reduce over-authority when Claude consumes automatic context.
- Whether action-log consolidation adds review, correction, or deletion affordances before `_action_stream` memories become prompt-injectable.
- Whether benchmark evaluation is wired as reproducible commands with pinned data and models; without that, retrieval claims remain less useful for Commonplace design decisions.
- Whether `get_project_context` gains explicit result and token budgets like the hook paths, because unbounded hot-memory returns can become context dilution.
- Whether rules, derived beliefs, and profiles get stronger provenance and contradiction workflows before being used as high-authority read-back inputs.

## Bottom Line

Zikkaron is a code-grounded example of local runtime memory for Claude Code: SQLite-backed retained state, multi-signal retrieval, trace capture, automatic hook read-back, and compaction recovery. Its most borrowable parts are the activation architecture and hot-path trace capture, not the number of subsystems. For Commonplace, it is evidence that engineered push activation can solve lookup omission, but it also sharpens why review state, lineage, and authority labels matter before memory becomes automatic prompt context.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: Zikkaron explicitly adds hook-based activation paths on top of stored memories.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Zikkaron's memory rows, action logs, hook scripts, rules, and retrieval policies differ by substrate, form, lineage, and authority.
- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Zikkaron converts Claude tool/action traces into durable summary memories and hook-selected context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: hooks, rules, gates, scoring policies, and consolidation code carry instruction, routing, ranking, and activation authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: stored memories and seed-derived project facts are evidence/advice until a read path gives them stronger prompt authority.
