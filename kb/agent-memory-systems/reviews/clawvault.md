---
description: "ClawVault review: deprecated markdown vault memory with graph/search context, OpenClaw prompt hooks, observer compression, facts, and maintenance workers"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
status: current
last-checked: "2026-06-04"
---

# ClawVault

ClawVault, from Versatly, is a deprecated but source-visible memory system for AI agents. At the reviewed commit it stores Markdown notes in a local vault, indexes them for BM25/semantic retrieval, builds graph and fact sidecars under `.clawvault`, exposes CLI and Python SDK workflows, and includes an OpenClaw memory plugin with prompt hooks, memory tools, session checkpointing, observer compression, and optional background maintenance.

**Repository:** https://github.com/Versatly/clawvault

**Reviewed commit:** [bd702e9cce436bc3065827714cd576e8be20c375](https://github.com/Versatly/clawvault/commit/bd702e9cce436bc3065827714cd576e8be20c375)

**Last checked:** 2026-06-04

## Core Ideas

**The primary memory substrate is a human-readable Markdown vault.** The README describes ClawVault as local-first, Markdown-native, graph-aware memory, and the `ClawVault` class initializes category directories, templates, ledger directories, a config file, and a welcome note in a user-chosen vault path ([README.md](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/README.md), [src/lib/vault.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/lib/vault.ts)). That makes the durable knowledge store inspectable and git/Obsidian-friendly rather than a hidden vector database.

**Search is hybrid, with local lexical retrieval as the baseline.** The in-process search engine chunks documents, computes BM25 scores, optionally fuses semantic embedding ranks with reciprocal rank fusion, and can apply hosted cross-encoder reranking; `qmd` is now an optional fallback path rather than the only search dependency ([src/lib/in-process-search.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/lib/in-process-search.ts), [src/lib/search.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/lib/search.ts), [src/lib/embedding-store.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/lib/embedding-store.ts)). Context efficiency is therefore selection-based: queries, profiles, top-k limits, source caps, graph expansion, snippets, and optional token budgets determine what enters context.

**Context assembly mixes retrieval channels instead of returning a single search list.** `buildContext()` loads the vault, runs vector/hybrid search, adds today/yesterday daily notes, fact-store hits, recent observations, and graph neighbors, then orders them by profile before fitting a token budget ([src/commands/context.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/commands/context.ts)). The `inject` command separately targets rules, decisions, and preferences by triggers, keywords, graph neighbors, scope, and optional LLM intent matching ([src/lib/inject-utils.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/lib/inject-utils.ts), [src/commands/inject.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/commands/inject.ts)).

**OpenClaw integration turns the vault into an active prompt participant.** The plugin registers `memory_search` and `memory_get`, adds a before-prompt hook that can prepend a memory recall mandate, recovery notices, session recap, and prompt-selected vault context, and registers lifecycle hooks for startup recovery, session start, reset, compaction, and agent heartbeat ([src/openclaw-plugin.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/openclaw-plugin.ts), [src/plugin/hooks/before-prompt-build.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/plugin/hooks/before-prompt-build.ts), [src/plugin/vault-context-injector.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/plugin/vault-context-injector.ts), [openclaw.plugin.json](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/openclaw.plugin.json)). Many of those hook features are opt-in in the manifest.

**Trace-derived memory exists, but it is layered.** The observer raw-captures session messages, compresses buffered messages into daily observations, routes important observations into category notes and backlog items, and can extract structured facts with conflict resolution ([src/observer/observer.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/observer/observer.ts), [src/observer/compressor.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/observer/compressor.ts), [src/observer/router.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/observer/router.ts), [src/lib/fact-store.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/lib/fact-store.ts)). The durable outputs are not just logs; they can become notes, facts, graph state, and future retrieval material.

**The repository is historical for new OpenClaw deployments.** The README warns that ClawVault is deprecated for new OpenClaw deployments and points users to first-party OpenClaw memory instead ([README.md](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/README.md)). For Commonplace comparison, that matters: the code is still useful as a design reference, but not as a stable product target.

## Artifact analysis

- **Storage substrate:** `files` — The primary retained state is Markdown files in vault categories such as `decisions/`, `lessons/`, `people/`, `projects/`, `tasks/`, `backlog/`, `handoffs/`, and `inbox/`; secondary file substrates include `.clawvault` JSON/JSONL sidecars, `.clawvault-index.json`, embedding caches, ledger raw transcripts, observations, reflections, and maintenance state.
- **Representational form:** `prose` `symbolic` `parametric` — Markdown bodies and observations carry prose; frontmatter, route rules, graph indexes, fact tuples, checkpoints, templates, manifests, and command/plugin schemas carry symbolic state; hosted embeddings and optional rerankers add parametric retrieval signals.
- **Lineage:** `authored` `trace-extracted` — Users and agents author notes through CLI/SDK/plugin paths, while session transcripts, hook events, observations, facts, checkpoints, maintenance outputs, graph indexes, and embedding caches are derived from later use traces or generated views.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — Vault notes and observations advise as knowledge; OpenClaw prompt hooks and communication protocol text instruct; message-sending filters can cancel or rewrite; search/context/profile/graph paths route and rank; config schemas, safe path checks, fact conflict handling, and command guards validate; observer and maintenance paths learn from traces.

**Vault notes and templates.** Storage substrate: Markdown files under the vault root, initialized from templates and routed by type/category. Representational form: prose plus frontmatter symbols. Lineage: authored by `store`, `remember`, `capture`, `patch`, task/project commands, SDK calls, or routed observer/maintenance outputs. Behavioral authority: knowledge artifact when retrieved; instruction-like authority when a note lives under `rules/`, `decisions/`, or `preferences` and is injected.

**Search, graph, and embedding sidecars.** Storage substrate: `.clawvault-index.json`, `.clawvault/graph-index.json`, and `.clawvault/embeddings.bin.json`. Representational form: symbolic document/chunk/graph records plus parametric vectors. Lineage: derived from Markdown file contents, wiki links, tags, frontmatter relations, embedding provider/model signatures, and document hashes ([src/lib/memory-graph.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/lib/memory-graph.ts), [src/lib/embedding-store.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/lib/embedding-store.ts)). Behavioral authority: routing and ranking for `search`, `vsearch`, `context`, plugin memory tools, and graph-neighbor expansion.

**Observer ledger.** Storage substrate: `ledger/raw/<source>/<yyyy>/<mm>/<dd>.jsonl`, `ledger/observations/<yyyy>/<mm>/<dd>.md`, `ledger/reflections/`, and archive directories. Representational form: raw symbolic JSONL transcript records plus prose observations with typed importance/confidence markers. Lineage: trace-extracted from OpenClaw, ChatGPT, Claude, or opencode-style session messages, then compressed and deduplicated. Behavioral authority: knowledge and learning input; observations are later read by `wake`/`context` and routed into stronger stores.

**Fact store and entity graph.** Storage substrate: `.clawvault/facts.jsonl` and `.clawvault/entity-graph.json`. Representational form: symbolic `entity`, `relation`, `value`, confidence, validity interval, source, and raw-text records. Lineage: trace-extracted from observation or hook text by rule-based, LLM, or hybrid extraction; conflicts supersede previous active facts with `validUntil` ([src/lib/fact-extractor.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/lib/fact-extractor.ts), [src/plugin/fact-extractor.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/plugin/fact-extractor.ts)). Behavioral authority: knowledge and ranking/routing input when context queries pull matching facts.

**OpenClaw plugin surfaces.** Storage substrate: repository code and `openclaw.plugin.json` configuration, with runtime session state in memory. Representational form: symbolic hook registrations, tool schemas, config schema, and prose recall/protocol instructions. Lineage: authored integration surface. Behavioral authority: instruction, enforcement, routing, and push read-back; the plugin decides when memory context and recall mandates enter the model context.

**Resilience artifacts.** Storage substrate: `.clawvault/last-checkpoint.json`, `.clawvault/checkpoints/*.json`, `.clawvault/session-state.json`, `.clawvault/dirty-death.flag`, and `handoffs/*.md`. Representational form: symbolic state plus prose handoff summaries. Lineage: authored or automatically written around session lifecycle, reset, checkpoint, sleep, and wake workflows ([src/commands/checkpoint.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/commands/checkpoint.ts), [src/commands/recover.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/commands/recover.ts), [src/commands/sleep.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/commands/sleep.ts), [src/commands/wake.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/commands/wake.ts)). Behavioral authority: recovery context and session-continuity knowledge.

Promotion path: ClawVault has multiple ladders from low-authority traces toward stronger behavior-shaping artifacts: raw transcript JSONL to observations, observations to category notes/backlog items/facts, inbox items to curated or distilled notes, and authored rules/decisions/preferences to prompt injection. It has structural validation and dedup/conflict handling, but not a Commonplace-style semantic review gate before learned or routed memories affect later context.

## Comparison with Our System

| Dimension | ClawVault | Commonplace |
|---|---|---|
| Primary purpose | Operational memory for AI agents and OpenClaw sessions | Methodology KB for agent-operated knowledge bases |
| Canonical artifact | Markdown vault note plus sidecar indexes/facts/checkpoints | Typed Markdown artifact in a git repository |
| Source of truth | Local vault files; sidecars derived or internal | Repository files plus generated indexes/reports |
| Write path | CLI/SDK/plugin writes, observer routing, fact extraction, maintenance workers | Authored notes, snapshots, review workflows, validation, index refresh |
| Read-back | Pull CLI/tool reads plus optional OpenClaw prompt push | Mostly explicit pull through search, indexes, links, skills, and instructions |
| Governance | File/path guards, config schemas, fact conflicts, hook opt-ins, tests | Collection/type contracts, validation, semantic review, git diffs, archives |

ClawVault and Commonplace share the file-native premise: durable memory should remain inspectable by humans and agents. ClawVault aims that premise at live agent operation: prompt hooks, checkpoint/recover flows, context profiles, observations, facts, and task/backlog routing. Commonplace aims it at durable methodology: type contracts, source citations, review sections, validation, and semantic QA.

The major divergence is authority. ClawVault can push memory into OpenClaw prompt construction and can enforce outbound-message rewrites or cancellations through hooks. Commonplace mostly relies on agents deliberately loading repository artifacts or being governed by already-loaded instructions. That makes ClawVault more active but also more vulnerable to context pollution and unreviewed learned state.

### Borrowable Ideas

**Separate raw trace, compressed observation, and distilled artifact layers.** Ready as a design principle. Commonplace workshop logs could benefit from explicit raw/observation/distillation tiers rather than mixing everything into notes.

**Session-resilience artifacts as first-class memory.** Ready now. Checkpoints, dirty-death flags, and handoffs are useful because they name the operational state a future agent needs, not just the facts it might search.

**Context assembly profiles.** Needs a concrete use case. ClawVault's `planning`, `incident`, and `handoff` ordering policies show how retrieval can change by task mode; Commonplace could use this for workshop or review workflows before adopting it globally.

**Push read-back should stay opt-in and auditable.** Ready now as a constraint. ClawVault's manifest-level toggles are a good reminder that automatic prompt injection needs explicit operator control, narrow budgets, and visible provenance.

**Do not borrow semantic gates by implication.** ClawVault's tests and conflict handling prove structural behaviors, not truth or usefulness of learned memories. Commonplace should keep semantic review separate from extraction and indexing.

## Write side

**Write agency:** `manual` `automatic` — Manual writes come from CLI, SDK, plugin tools, and direct Markdown editing; automatic writes include search/index refreshes, graph/embedding caches, checkpoints, observer raw capture, compression, routing, fact extraction, background maintenance workers, and plugin lifecycle hooks.

**Curation operations:** `consolidate` `dedup` `synthesize` `invalidate` `decay` `promote` — Observer compression consolidates messages into observations; observation dedup and task dedup remove duplicates; maintenance distillation can synthesize fact/decision/lesson files from inbox items; fact conflicts invalidate previous active facts with `validUntil`; reflection drops older low-priority observations; context profiles, importance, confidence, recency, and ranking promote or demote what gets read back.

### Trace-derived learning

**Trace source:** `session-logs` `tool-traces` `event-streams` — The observer and plugin hooks consume session messages, reset/compaction/heartbeat events, prompt text, and hook payloads; raw transcript records and observed text become durable ledger, fact, note, and checkpoint artifacts.

**Learning scope:** `per-project` `cross-task` — A vault is selected per configured path or agent mapping, and its notes, facts, observations, handoffs, and indexes persist across sessions and later tasks.

**Learning timing:** `online` `staged` — Hook-time checkpointing, prompt context selection, fact extraction, and observer cursor updates can happen during operation; `sleep`, `wake`, `reflect`, `maintain`, embedding rebuilds, and QMD updates are staged workflows.

**Distilled form:** `prose` `symbolic` `parametric` — Session traces become prose observations and notes, symbolic facts/graphs/checkpoints/routes, and embedding/reranking state for retrieval.

**Trace source.** ClawVault qualifies as trace-derived because durable retained artifacts are derived from interaction traces, not merely user-authored notes. `Observer.processMessages()` optionally persists raw messages, buffers them until a token threshold, compresses them into observation Markdown, and routes the result; plugin lifecycle handlers call checkpointing, observer cron, and fact extraction on reset/compaction/heartbeat events ([src/observer/observer.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/observer/observer.ts), [src/plugin/hooks/session-lifecycle.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/plugin/hooks/session-lifecycle.ts), [src/plugin/hooks/observation.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/plugin/hooks/observation.ts)).

**Extraction.** Extraction is a mix of LLM compression, deterministic fallback heuristics, regex/rule facts, optional LLM fact extraction, routing rules, and maintenance worker heuristics/LLM calls. The oracle is therefore not one judge: it varies by provider availability, config, worker, and feature flag.

**Scope and timing.** The trace-derived layer is vault-scoped and agent-aware when OpenClaw agent vault mappings are configured. Online paths update raw logs, observations, facts, checkpoints, and prompt context; staged paths turn inbox or observations into curated/distilled notes and reflections.

**Survey fit.** ClawVault strengthens the trace-derived survey's raw-to-distilled split. Raw transcripts and hook payloads are weak knowledge artifacts; compressed observations, facts, handoffs, and injected rules have stronger downstream authority. The risky part is that some distilled outputs can enter prompt context without a semantic review step.

## Read-back

**Read-back:** `both` — Stored vault memory is available by pull through CLI commands, SDK calls, `memory_search`, `memory_get`, `context`, `inject`, `wake`, and direct Markdown browsing, while the OpenClaw plugin can push recall instructions, session recap, recovery notices, prompt-selected vault context, and communication protocol text before prompt construction.

**Read-back signal:** `coarse` `inferred / lexical` `inferred / embedding` — The recall mandate and protocol appendix are coarse always-load/setup pushes when enabled; vault-context push uses the current prompt as an inferred query over BM25/semantic search; `inject` uses deterministic trigger/keyword/entity/graph matching plus optional LLM intent matching when the user invokes it.

**Faithfulness tested:** `no` — The repository contains tests for command behavior, search, hooks, context formatting, observer routing, and plugin surfaces, but I did not find with/without ablations or post-action audits showing that pushed memory changes model behavior faithfully.

**Direction edge cases.** `memory_search`, `memory_get`, `search`, `vsearch`, `context`, and `inject` are pull when the agent or user asks for them. The before-prompt hook is push because it can insert memory and recall policy without the receiving model first choosing a retrieval call. The message-sending hook is another active consumer: when an outbound question appears answered by memory search, it rewrites or cancels the message ([src/plugin/hooks/message-sending.ts](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/plugin/hooks/message-sending.ts)).

**Targeting and signal.** Prompt-context push is instance-targeted by inferred relevance: `buildVaultContextInjection()` searches the vault with the current prompt and filters by score, while the `MEMORY_RECALL_MANDATE` and protocol appendix are coarse instructions. Pull context assembly uses profile ordering, source caps, graph expansion, fact matching, observations, daily notes, and token budgets.

**Injection point.** The implemented push happens pre-invocation in OpenClaw's `before_prompt_build` hook through `prependSystemContext` and `appendSystemContext`. Reset, compaction, heartbeat, observer flushes, checkpoint writes, and fact extraction are write-side maintenance for later reads, not read-back after an action completes.

**Selection, scope, and complexity.** The plugin caps pushed vault memories with `maxContextResults` and snippets; CLI `context` can apply a token budget. Complexity can still be high because a single assembly may combine recap, daily notes, observations, facts, search hits, graph neighbors, recovery notices, and protocol instructions. Effective context dilution is not verifiable from code.

**Authority at consumption.** Search results and context snippets are advisory knowledge. Recall mandates and protocol appendices are system-context instructions. Message-sending rewrites/cancellations are enforcement-like. Effective authority depends on OpenClaw host behavior, feature flags, and model compliance.

**Other consumers.** Humans consume the same vault through Markdown, Obsidian, CLI output, generated canvases, task/kanban views, dashboards, WebDAV/Tailscale sync, logs, and Python SDK calls. The system is deliberately mixed human/agent infrastructure.

## Curiosity Pass

**The README and local AGENTS guidance disagree about QMD's role.** The README says QMD is optional, while the checked-in agent instructions still say the CLI requires `qmd` for vault operations. The code supports in-process search as the default with QMD fallback, so the review follows the code path rather than the stale instruction file.

**Deprecation makes the code more useful as a pattern library than as a product recommendation.** ClawVault contains many implemented mechanisms, but the maintainers point new OpenClaw deployments to first-party memory.

**The strongest mechanism is the layered trace pipeline.** Raw logs, observations, facts, notes, and prompt injection are separate enough to analyze; that separation is more valuable than any single search command.

**Push read-back is powerful but broad.** The before-prompt hook can inject both selected context and general instructions. That is operationally useful, but it needs stronger budgets and faithfulness testing before it becomes a high-trust memory interface.

**Fact extraction is useful but semantically shallow.** The conflict model handles exclusive relations and supersession, but it cannot prove that an extracted fact is true, important, or still valid outside the relation heuristic.

## What to Watch

- Whether OpenClaw native memory fully absorbs ClawVault's observer, fact, checkpoint, and context-profile ideas; that would make ClawVault mainly historical evidence.
- Whether before-prompt context injection gains behavioral faithfulness tests; that would make the push path more defensible as memory rather than context stuffing.
- Whether learned facts and routed notes gain review state before injection; that would close the current gap between extraction and authority.
- Whether the Python SDK grows the same observer/plugin/trace-derived surface as the Node implementation; at this commit it is a narrower file/search/checkpoint interface.
- Whether the stale QMD requirement in local instructions is removed or the README's optional-QMD claim changes; that affects adoption and architecture interpretation.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: ClawVault stores many memories, but only plugin hooks and explicit commands decide whether they enter context.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: vault notes, facts, graph indexes, checkpoints, and hook instructions carry different lineage and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: Markdown notes, observations, facts, and retrieved snippets mostly advise as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: OpenClaw hook instructions, config schemas, message filters, and search/profile policies shape behavior with stronger force.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: ClawVault derives observations, facts, and distilled notes from sessions and hook events.
