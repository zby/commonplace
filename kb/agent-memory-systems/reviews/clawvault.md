---
description: "Deprecated OpenClaw-era markdown memory system with session ledgers, scored observations, fact stores, context profiles, hooks, and maintenance workers"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-05-16"
---

# ClawVault

ClawVault is Versatly's TypeScript memory system for AI agents, built around a local markdown vault plus CLI and legacy OpenClaw plugin integration. The repository now marks ClawVault as deprecated for new OpenClaw deployments because OpenClaw has first-party memory and QMD-backed retrieval, but the inspected code remains a useful reference for session lifecycle, trace compression, context injection, and file-backed maintenance loops ([README.md](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/README.md), [docs/openclaw-plugin-usage.md](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/docs/openclaw-plugin-usage.md)).

**Repository:** https://github.com/Versatly/clawvault

**Reviewed commit:** https://github.com/Versatly/clawvault/commit/bd702e9cce436bc3065827714cd576e8be20c375

**Source freshness caveat:** parent checkout refresh from GitHub failed due credential/access failure; this review uses the local clean checkout at the reviewed commit.

## Core Ideas

**A markdown vault is the primary user-visible substrate; `.clawvault/` is operational state.** `ClawVault.init()` creates category directories for rules, preferences, decisions, patterns, people, projects, goals, transcripts, inbox, lessons, agents, commitments, handoffs, research, tasks, and backlog, plus a `ledger/raw`, `ledger/observations`, and `ledger/reflections` tree. Markdown files with frontmatter are the durable knowledge surface, while `.clawvault.json`, `.clawvault/graph-index.json`, `.clawvault/facts.jsonl`, checkpoint files, cursors, embedding caches, and maintenance logs are system state or derived projections ([src/lib/vault.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/lib/vault.ts), [src/lib/ledger.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/lib/ledger.ts), [src/lib/fact-store.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/lib/fact-store.ts)).

**Session lifecycle is a first-class memory interface.** `checkpoint` writes `last-checkpoint.json`, checkpoint history, session metadata, and a dirty-death flag; `wake` clears recovery state, loads handoffs, projects, commitments, recent decisions/lessons, and recent scored observations; `sleep` writes a handoff and can process the session transcript into observations before optional reflection. This makes continuity an operational workflow, not just search over notes ([src/commands/checkpoint.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/commands/checkpoint.ts), [src/commands/wake.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/commands/wake.ts), [src/commands/sleep.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/commands/sleep.ts)).

**Observation ledgers separate raw traces from compressed memory.** The observer can persist raw transcript messages under `ledger/raw/{source}/YYYY/MM/DD.jsonl`, compress sanitized session messages into scored observation markdown under `ledger/observations/YYYY/MM/DD.md`, route high-importance observations into category notes, and archive old observation files after weekly reflection. The raw trace is evidence; the scored observation is a distilled knowledge artifact; routed notes and fact records are stronger retained surfaces ([src/observer/observer.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/observer/observer.ts), [src/observer/compressor.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/observer/compressor.ts), [src/observer/router.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/observer/router.ts), [src/observer/archive.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/observer/archive.ts)).

**The trace-derived path has multiple output forms.** The compressor uses configured LLM providers when available and deterministic regex fallback otherwise; the router maps observations to decisions, lessons, people, preferences, commitments, projects, and backlog items; fact extraction writes `(entity, relation, value)` records with confidence, source, valid-from, and supersession timestamps into `.clawvault/facts.jsonl`. Prose notes, scored observation lines, JSONL facts, and task/backlog records have different representational forms and authority, but they all derive from session or inbox material ([src/lib/fact-extractor.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/lib/fact-extractor.ts), [src/lib/fact-store.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/lib/fact-store.ts), [src/capture/service.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/capture/service.ts), [src/capture/extractor.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/capture/extractor.ts)).

**Retrieval blends search, graph, facts, observations, and profiles.** In-process search chunks markdown and runs BM25, optional hosted embeddings, reciprocal-rank fusion, and optional cross-encoder reranking; QMD remains a fallback/configurable backend. `context` adds daily notes, recent observations with importance decay, fact-store matches, search hits, and graph neighbors, then orders them by task profile (`default`, `planning`, `incident`, `handoff`, or `auto`) and token budget. This is more like a context scheduler than a bare memory lookup ([src/lib/in-process-search.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/lib/in-process-search.ts), [src/lib/search.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/lib/search.ts), [src/lib/context-profile.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/lib/context-profile.ts), [src/commands/context.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/commands/context.ts), [src/lib/memory-graph.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/lib/memory-graph.ts)).

**OpenClaw plugin hooks give memory behavioral authority.** The plugin registers `memory_search` and `memory_get`, prepends a recall mandate before prompt build, injects session recap and vault context, rewrites or cancels outbound questions when memory already has evidence, checkpoints before resets, observes on reset/compaction/heartbeat, and can run weekly reflection. These hooks move ClawVault artifacts from optional reference material toward system-definition artifacts consumed with instruction, routing, enforcement, and prompt-construction force ([src/openclaw-plugin.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/openclaw-plugin.ts), [src/plugin/hooks/before-prompt-build.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/plugin/hooks/before-prompt-build.ts), [src/plugin/hooks/message-sending.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/plugin/hooks/message-sending.ts), [src/plugin/hooks/session-lifecycle.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/plugin/hooks/session-lifecycle.ts), [openclaw.plugin.json](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/openclaw.plugin.json)).

**Maintenance workers create a workshop layer, but mostly around inbox.** `clawvault maintain` runs curator, janitor, distiller, and surveyor workers. The curator copies inbox captures into typed categories; janitor archives duplicates/stale items and writes merge reports; distiller emits facts, decisions, and lessons from long inbox captures; surveyor writes vault-health recommendations. State lives under `.clawvault/maintenance`, and workers degrade to heuristics when LLMs are unavailable ([src/commands/maintain.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/commands/maintain.ts), [src/lib/maintenance/curator-worker.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/lib/maintenance/curator-worker.ts), [src/lib/maintenance/janitor-worker.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/lib/maintenance/janitor-worker.ts), [src/lib/maintenance/distiller-worker.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/lib/maintenance/distiller-worker.ts), [src/lib/maintenance/surveyor-worker.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/lib/maintenance/surveyor-worker.ts)).

## Comparison with Our System

| Lens axis | ClawVault | Commonplace |
|---|---|---|
| Primary substrate | Local markdown vault plus `.clawvault/` JSON, JSONL, graph, cursor, and maintenance state | Repo KB with typed markdown artifacts under `kb/`, generated indexes, commands, and review gates |
| Trace handling | Raw transcripts -> scored observations -> routed category notes, facts, tasks, reflections | Work traces usually become workshop artifacts, source snapshots, reviews, notes, instructions, and validation outputs through explicit workflows |
| Artifact contracts | Category folders and frontmatter conventions; fact-store schema; OpenClaw plugin config | Path-valued type specs with collection contracts, link vocabulary, status, validation, and review semantics |
| Activation | `wake`, `context`, plugin `before_prompt_build`, `memory_search`, message-sending filter | AGENTS routing, skills, `rg`, indexes, type specs, validators, semantic review bundles |
| Authority gradient | Notes advise; facts/context entries rank and inject; hooks instruct, rewrite, checkpoint, and observe | Notes advise; instructions/skills/commands/validators enforce or route; review gates assess artifacts |
| Lifecycle | Checkpoints, handoffs, observation archive, observation-format migration, QMD migration, maintenance state | Explicit statuses, replaced reviews, generated indexes, relocation tools, validation, review/fix procedures |
| Current product status | Historical/legacy for OpenClaw; README points new users to OpenClaw native memory | Active methodology KB and shipped framework for operating KBs |

ClawVault is stronger than commonplace on live session instrumentation. It has a concrete answer to "what happens when the agent starts, resets, compacts, asks an unnecessary question, or ends a session?" Commonplace has stronger artifact contracts and review discipline, but ClawVault shows the runtime surface around those contracts: capture, score, route, inject, and maintain.

The biggest conceptual alignment is the workshop/library split. ClawVault's raw ledgers, inbox, maintenance workers, and observations are workshop-like: they are temporal, noisy, and consumed for later promotion. Decisions, lessons, facts, people notes, handoffs, and task files are library-like, though ClawVault lacks a strong type-spec and validation layer to distinguish evidence, claim, instruction, and derived view.

The biggest divergence is governance. ClawVault has many automatic writes and prompt hooks, but its quality gates are heuristic confidence, importance, dedup, category routing, and optional LLM judgment. Commonplace is slower and more manual because it treats artifact type and semantic review as the trust boundary. ClawVault is better at not losing signal; commonplace is better at saying what a retained artifact is allowed to mean.

## Borrowable Ideas

**Session lifecycle as a command family.** Ready to borrow in spirit. `wake`, `checkpoint`, and `sleep` make continuity concrete and user-visible. In commonplace this should map to workshop state and handoff reports, not necessarily a new permanent note type.

**Scored observation ledgers.** Useful, but needs a quality contract first. ClawVault's `[type|c=confidence|i=importance]` observation lines are compact enough for wake/context flows and concrete enough for later reflection. Commonplace could use a similar workshop-only trace ledger if it also defines invalidation, source citation, and promotion criteria.

**Context profiles.** Ready as a small design pattern. Planning, incident, and handoff tasks really do need different ordering of observations, facts, graph neighbors, and search hits. Commonplace currently relies on agent judgment and instructions; profile-shaped retrieval would be a clean future command surface.

**Separate raw, compressed, promoted, and enforced surfaces.** Ready as vocabulary. ClawVault accidentally demonstrates the artifact contract we want explicitly: raw transcript evidence, scored observation knowledge artifacts, fact JSONL records, promoted markdown notes, prompt-injected context, and hook-level system definitions should not be collapsed into "memory."

**Maintenance workers over inbox, not over the library.** Borrowable with care. The curator/janitor/distiller/surveyor split is a plausible workshop maintenance model because it acts on pending captures and reports. Commonplace should keep fully promoted notes behind stricter validation and review rather than letting background workers freely rewrite them.

**Prompt-time memory recall mandate plus evidence rewrite.** Needs a concrete OpenClaw-like integration point before borrowing. The before-prompt and message-sending hooks show a stronger authority path than passive retrieval, but importing that pattern into commonplace would require careful scoping so "memory says so" does not override source-grounded review.

## Trace-derived learning placement

**Trace source.** ClawVault consumes live agent/session traces through explicit transcript files, OpenClaw session JSONL, file watchers, `sleep --session-transcript`, active-session cursors, before-reset observation, compaction observation, heartbeat observation, and assistant-response capture. Raw traces are stored under `ledger/raw/{source}/YYYY/MM/DD.jsonl` when raw capture is enabled; cursor state lives in `.clawvault/observe-cursors.json` ([src/observer/active-session-observer.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/observer/active-session-observer.ts), [src/observer/watcher.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/observer/watcher.ts), [src/observer/session-parser.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/observer/session-parser.ts)).

**Extraction.** Extraction has three paths: observation compression from sanitized message batches, assistant-response memory capture from `<memory_note>` tags or sentence heuristics, and structured fact extraction from observation/event text. The oracle is mixed: LLM completion when configured, deterministic regex and scoring fallback otherwise, plus hand-coded thresholds such as observation importance `>= 0.4`, reflection promotion at high importance or repeated medium importance, and capture quality/dedup gates.

**Storage substrate.** Raw traces live in dated JSONL ledger files. Compressed observations live in dated markdown ledger files. Promoted notes live in category markdown folders. Facts live in `.clawvault/facts.jsonl`. Search indexes and graph indexes live as derived state in memory, `.clawvault/graph-index.json`, embedding cache files, or QMD indexes. Context profiles are code/config, not memory content. Hook outputs are injected into OpenClaw prompt construction and runtime state.

**Representational form.** Raw traces are mixed structured/text evidence. Observations and notes are prose with light symbolic tags (`type`, confidence, importance, frontmatter). Fact records are symbolic JSONL triples with temporal fields. Search embeddings are distributed-parametric derived indexes when hosted embeddings are configured. Context profiles and hook policies are symbolic system definitions encoded in TypeScript and plugin JSON.

**Lineage.** The strongest lineage chain is raw transcript -> observation line -> routed note/fact/task/reflection, with source/session metadata carried inconsistently. Backlog items generated from observations include session, transcript, source, approximate timestamp, observation type, and original observation text. Fact records carry `source` and `rawText`; reflections cite observation ledger paths. Category notes created by maintenance workers carry `inboxHash` and `inboxPath`. The weak point is regeneration: derived files are inspectable, but there is no universal "this note is derived from this trace and should be regenerated/invalidated when source changes" contract.

**Behavioral authority.** Raw transcripts and observations are knowledge artifacts: evidence and context for later review. Fact-store records become ranking/context artifacts when `context` injects them, and can approach system-definition authority when prompt hooks use them to change what the agent sees. Context profiles, memory recall mandates, message-sending rewrites, auto-checkpoint hooks, and plugin configuration are system-definition artifacts because they instruct, route, enforce, or schedule future behavior. Maintenance reports are advisory knowledge artifacts unless an operator acts on them.

**Scope and timing.** Scope is mostly per-vault and per-agent, with optional per-agent vault mapping in the OpenClaw plugin. Timing is online and staged: traces can be observed during sessions, flushed on reset/compaction/sleep, reflected weekly, archived after reflection, and maintained through explicit `maintain` runs.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), ClawVault belongs in the live session-mining / artifact-learning cluster. It strengthens the claim that trace-derived candidate generation is tractable in ordinary agent workflows, but it also splits the category into several authority layers: raw evidence, scored observation ledgers, symbolic fact stores, promoted prose notes, and hook-level system definitions. It is not weight-learning; any embeddings are retrieval indexes, not learned agent policy.

## Curiosity Pass

ClawVault's README architecture diagram says "Session -> Observe -> Score -> Route -> Store -> Reflect -> Promote," and the implementation mostly earns that sequence. The surprising part is how many mechanisms are real: dated ledgers, active-session cursors, scored observation parsing, fact supersession, context profiles, graph neighbors, plugin prompt hooks, and maintenance workers all exist in code.

The simpler alternative would be much smaller: a markdown vault with `wake`, `sleep`, `search`, and `handoff` only. ClawVault chose the broad surface instead, which makes it rich as a reference but also explains the deprecation note. It became a sidecar memory runtime at the same time OpenClaw was growing a first-party memory stack.

The fact store is more operational than semantic. It has confidence, temporal supersession, and simple indexes, but no source quotation contract, reviewer status, or validation of extracted relation quality. That is still useful for prompt-time recall, but it should not be mistaken for a reviewed knowledge graph.

The OpenClaw plugin is the most consequential part of the design because it changes authority. A note found by `search` advises; a before-prompt recall mandate and message-sending filter can alter behavior before the agent decides to search. That is powerful and risky: any noise in retrieval or fact extraction can be promoted from "maybe relevant" to "system context says this matters."

The legacy status matters. ClawVault is still worth reviewing because it shows a complete local-first memory runtime, but new design borrowing should treat it as mined experience, not a dependency target.

## What to Watch

- Whether OpenClaw's native memory keeps ClawVault's useful split between raw traces, observations, facts, notes, context profiles, and hooks, or collapses those into a simpler memory abstraction.
- Whether ClawVault's migration guidance becomes more concrete for existing vaults: especially mapping observations, fact stores, and handoffs into OpenClaw builtin/QMD memory.
- Whether fact extraction gains review states, citations, or invalidation semantics before being used as strong prompt-time context.
- Whether maintenance workers stay inbox-scoped or expand into library-note rewriting, which would raise the trust bar substantially.
- Whether context profiles become benchmarked against session-resumption or incident tasks, rather than remaining plausible hand-tuned ordering rules.

---

Relevant Notes:

- [a functioning KB needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) - exemplifies: ClawVault's raw ledgers, observations, inbox, maintenance reports, and handoffs are a concrete workshop-like layer around durable notes.
- [Retained artifact](../../notes/definitions/retained-artifact.md) - defined-in: ClawVault shows why stored objects should be classified by future behavioral consequence, not by being called "memory."
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) - defined-in: the distinction between observation evidence, prompt-injected context, and OpenClaw hook enforcement is the central comparison axis.
- [Representational form](../../notes/definitions/representational-form.md) - defined-in: ClawVault mixes prose observations, symbolic facts/config, and distributed-parametric retrieval indexes.
- [automating KB learning is an open problem](../../notes/automating-kb-learning-is-an-open-problem.md) - extends: ClawVault automates candidate generation and routing, but still leaves trust, review, and invalidation only partially specified.
