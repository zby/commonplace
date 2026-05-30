---
description: "Phantom review: AI co-worker runtime with prompt-block assembly, Qdrant memory, file-backed evolved identity, scheduler, MCP/UI surfaces, and invariant-checked reflection"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-05-16"
---

# Phantom

Phantom is Ghostwright's AI co-worker runtime: a Bun/TypeScript service that runs an agent on its own VM, exposes Slack/web chat/email/webhook/MCP surfaces, gives the agent broad workstation authority, and retains memory through both vector stores and mutable identity/configuration files. For commonplace, the important shape is not just "persistent memory." Phantom separates raw chat/session records, Qdrant-backed episodic/semantic/procedural memories, agent-owned notes, evolution-managed config files, runtime indexes and tools, and operator-locked safety files into different authority bands.

**Repository:** https://github.com/ghostwright/phantom

**Reviewed commit:** [f8c7ab42d885936ee54abc785528000260f4acc5](https://github.com/ghostwright/phantom/commit/f8c7ab42d885936ee54abc785528000260f4acc5)

**Last checked:** 2026-05-16

## Core Ideas

**Prompt assembly is a layered authority stack.** `assemblePrompt(...)` builds the runtime system prompt from identity, tenant self-knowledge, optional persona overlay, environment, security, role template, onboarding prompt, evolved config, agent-memory instructions, fixed operating instructions, working memory, dynamic vector-memory context, and chat runtime context ([prompt-assembler.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/agent/prompt-assembler.ts)). The ordering matters. `phantom-config` files become system-definition artifacts when `buildEvolvedSections(...)` injects constitution, communication style, user profile, domain knowledge, and learned strategies into the prompt ([evolved.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/agent/prompt-blocks/evolved.ts)). Qdrant recall is added later as `# Your Memory`, so it has prompt-time influence but lower structural authority than identity, role, security, and evolved config.

**There are three file-backed memory authorities before vector memory is even considered.** `data/working-memory.md` is trusted personal notes, injected directly when present and truncated after 75 lines with a compaction warning ([working-memory.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/agent/prompt-blocks/working-memory.ts)). `phantom-config/memory/agent-notes.md` is agent-owned append-only memory taught through prompt instructions, but deliberately not auto-injected; the main agent must read it when needed ([agent-memory-instructions.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/agent/prompt-blocks/agent-memory-instructions.ts)). `phantom-config` evolved files are reflection-managed and auto-injected. This is a useful authority gradient: direct prompt state, optional self-authored notes, and curated/evolved system-definition files are not collapsed into one "memory" bucket.

**Vector memory is Qdrant plus Ollama, with separate episodic, semantic, and procedural collections.** `MemorySystem` wraps three stores and degrades to an empty memory surface if Qdrant or Ollama is unavailable ([system.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/memory/system.ts)). Episodes store session summaries/details, tools, files, outcomes, importance, access count, and decay metadata with dense summary/detail vectors plus sparse BM25 vectors ([episodic.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/memory/episodic.ts)). Semantic facts store subject/predicate/object natural-language facts with source episode ids, confidence, temporal validity, and supersession through `valid_until` ([semantic.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/memory/semantic.ts)). Procedures store triggerable step lists with source episode ids and success/failure counts ([procedural.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/memory/procedural.ts)). Retrieval uses Qdrant hybrid dense+sparse search with RRF fusion where both vectors exist ([qdrant-client.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/memory/qdrant-client.ts)).

**Session consolidation is implemented, but thinner than the docs imply.** The docs describe session-end extraction, semantic facts, and nightly promotion to procedures ([docs/memory.md](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/docs/memory.md)). The inspected implementation's consolidation path creates one episode from session metadata and extracts semantic facts only through correction/preference regex-style patterns; `proceduresDetected` is always zero, and the richer LLM consolidation path was removed ([consolidation.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/memory/consolidation.ts)). That still qualifies as trace-derived memory, but the Qdrant procedural tier is more of an available storage/retrieval surface than a fully wired session-to-procedure learner at this commit.

**The self-evolution loop is a staged trace-to-config learner.** After a session, `decideGate(...)` asks a Haiku judge whether durable learning signal exists; failures default to fire rather than silently drop signal ([gate.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/evolution/gate.ts)). Fired sessions are stored in SQLite `evolution_queue`, deduplicated by `session_key`, retried on invariant failures, and moved to `evolution_queue_poison` after three retry-count failures ([queue.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/evolution/queue.ts), [schema.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/db/schema.ts)). A cadence drains the queue every 180 minutes by default, or immediately when depth reaches five, with an in-flight guard so only one drain runs ([cadence.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/evolution/cadence.ts)).

**Reflection is delegated to a constrained subprocess, then checked deterministically.** `runReflectionSubprocess(...)` writes a staged JSONL batch, snapshots `phantom-config`, spawns the Claude Agent SDK at Haiku/Sonnet/Opus as needed, parses a final sentinel, and either commits a version or restores the snapshot ([reflection-subprocess.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/evolution/reflection-subprocess.ts)). The subprocess prompt teaches the memory-manager role, file taxonomy, skip default, compaction rules, promotion between files, and sentinel protocol ([subprocess-prompt.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/evolution/subprocess-prompt.ts)). The SDK allowlist is read-wide/write-narrow inside `phantom-config`: no Bash, Task, WebFetch, or arbitrary directories; writes are limited to persona, user profile, domain knowledge, strategies, corrections, and principles, while constitution, meta, agent notes, and session log are denied. The invariant check then re-enforces scope, constitution byte identity, canonical-file existence, size bounds, markdown/JSONL syntax, credential patterns, URL warnings, near-duplicate bullets, sentinel/diff agreement, and staging cleanup ([invariant-check.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/evolution/invariant-check.ts)).

**Runtime surfaces are broad and intentionally operational.** The main runtime wraps the Claude Agent SDK, persists SDK session ids, injects prompt layers, resumes conversations when possible, tracks files edited via hooks, records cost, and applies operator-configured permission modes and tool allow/deny lists ([runtime.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/agent/runtime.ts), [permission-options.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/agent/permission-options.ts)). The scheduler stores jobs in SQLite, executes them through a `scheduler:sched:<id>` runtime session, serializes executions, advances schedules, applies failure backoff, and delivery-reports results ([service.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/scheduler/service.ts), [executor.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/scheduler/executor.ts)). MCP exposes status, evolved config, metrics, sessions, memory search, ask, and task tools ([tools-universal.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/mcp/tools-universal.ts)). The dashboard memory API exposes read/search/detail/delete over episodes, facts, and procedures ([memory.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/ui/api/memory.ts)).

## Comparison with Our System

| Dimension | Phantom | Commonplace |
|---|---|---|
| Primary purpose | Always-on AI co-worker with its own VM, channels, tools, scheduler, and memory | Agent-operated methodology KB in a git repo |
| Raw trace substrate | SQLite sessions/chat tables, staged evolution batches, optional `session-log.jsonl`, Qdrant episode payloads | Source snapshots, notes, reviews, validation/review reports, git history |
| Durable knowledge artifacts | Qdrant episodes/facts/procedures, session records, agent notes, memory explorer records | Typed markdown notes, source snapshots, reports, generated indexes |
| System-definition artifacts | Prompt blocks, `phantom-config` identity/strategy files, role YAML, permissions, scheduler jobs, MCP dynamic tools | Instructions, type specs, schemas, validators, commands, skills, AGENTS.md |
| Learning loop | Trace-to-episode/fact heuristics plus gate/queue/reflection-to-config evolution | Mostly human/agent-authored curation, validation, review, and explicit promotion |
| Storage substrate | SQLite + Qdrant + Ollama + markdown/YAML files | Git-tracked markdown/YAML/Python with generated indexes |
| Activation | Automatic prompt assembly, scheduler wakeups, MCP/UI surfaces, memory context builder | Agent navigation, skill loading, `commonplace-*` commands, authored links, validation |
| Governance | Operator permissions, regex command blocker, reflection write allowlists, deterministic invariant rollback | Git review, validation, type contracts, instructions, review/fix workflows |

Phantom is stronger than commonplace at making memory operational inside a live agent runtime. A retained fact can be searched through MCP or the dashboard, injected before a query, or used by a scheduled job without a human explicitly navigating a repo. The runtime also distinguishes multiple consumers: the main agent consumes prompt blocks and memory context; the reflection subprocess consumes staged session summaries and memory files; operators consume dashboard/API surfaces; MCP clients consume memory/config/history tools.

Commonplace is stronger at inspectable lineage and durable knowledge governance. Phantom's Qdrant memories preserve some source episode ids, and evolution versions record file-level changes, but much of the trace-to-fact and trace-to-config lineage is operational rather than editorial. A future agent can see a fact's source episode id or an evolution log row, but not a reviewed claim with explicit source citations, link contracts, and collection-level type discipline.

The most interesting comparison is authority management. Phantom has a real authority gradient: raw sessions are evidence; Qdrant facts and episodes are knowledge artifacts; memory context advises the next prompt; evolved config is system-definition material; constitution is operator-locked; reflection-managed files are writeable only through a constrained subprocess; scheduler rows can wake the full agent later; MCP dynamic tools can become shared runtime capabilities. Commonplace has a richer vocabulary for this gradient, while Phantom has a richer running system that exercises it.

The docs still carry traces of an older, heavier evolution story: `docs/security.md` describes five gates and LLM judge voting, while the implementation says the six-judge pipeline was deleted and replaced with a reflection subprocess plus deterministic invariant checks ([security.md](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/docs/security.md), [engine.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/evolution/engine.ts), [invariant-check.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/evolution/invariant-check.ts)). The code-grounded review should follow the implementation.

## Borrowable Ideas

**Authority bands over one file tree.** Ready to borrow as vocabulary pressure on commonplace. Phantom's `phantom-config` tree demonstrates operator-locked files, evolution-managed files, agent-owned notes, read-only trace context, meta logs, and prompt-injected sections living near each other without equal authority. Commonplace can make this distinction sharper in workshop design and review reports.

**Reflection subprocess with deterministic rollback.** Worth borrowing when commonplace adds trace-derived learning. The useful part is not self-evolution branding; it is the combination of staged input, narrow tool surface, snapshot, final sentinel, deterministic invariant check, and restore-on-fail. That maps well to candidate instruction/skill updates from review traces.

**Skip-first memory management.** Ready to borrow as a prompt principle. Phantom explicitly teaches the reflection subprocess that most drains should skip. This is a strong antidote to memory systems that accrete marginal reflections because every session must produce something.

**Separate agent-owned scratch from promoted memory.** Ready now. `agent-notes.md` is append-only and not auto-injected, while evolved config is curated and prompt-loaded. Commonplace's workshop layer could use the same split: cheap agent scratch that future agents can grep, and promoted library/system-definition artifacts that carry stronger authority.

**Dashboard/API deletion over vector memories.** Useful if commonplace ever adopts an operational memory substrate. Phantom exposes memory deletion through authenticated UI/API routes. File-first KBs get deletion from git, but database/vector layers need explicit operator surfaces or stale records become invisible residue.

**Do not borrow broad default runtime authority without the deployment boundary.** Phantom's normal operating model assumes a dedicated VM and often broad Agent SDK permissions. In a KB repo, that would be the wrong default. The borrowable part is the explicit permission mapping and audit hooks, not bypass authority itself.

## Trace-derived learning placement

**Trace source.** Phantom qualifies as trace-derived learning in two implemented ways. First, session-end consolidation consumes session summaries: user messages, assistant messages, tools used, files touched, cost, duration, and outcome. Second, the evolution loop consumes queued session summaries selected by the Haiku gate. Raw traces also exist in chat/session SQLite tables, `chat_stream_events`, optional `phantom-config/memory/session-log.jsonl`, and the staged `.staging/batch-*.jsonl` files created for reflection.

**Extraction.** Vector-memory extraction is mostly heuristic at this commit: one episode is created per consolidated session, and semantic facts are extracted from correction/preference patterns in user messages. Procedure extraction is not wired; the result reports zero procedures. Evolution extraction is stronger and more agentic: a Haiku gate decides whether to fire, queued summaries are batched by cadence/depth, and a constrained SDK subprocess reads the batch plus current memory files to decide whether to edit, compact, promote, skip, or escalate model tier.

**Storage substrate.** Raw operational state persists in SQLite tables for sessions, chat sessions/messages/events, cost events, scheduler jobs, evolution queue, poison rows, and audit logs. Vector retained state persists in Qdrant collections for episodes, semantic facts, and procedures, with embeddings supplied by Ollama. File-backed retained state lives in `phantom-config/` markdown/YAML/JSON files and `data/working-memory.md`. Reflection staging is transient `.staging/*.jsonl`; version metadata and evolution logs persist under `phantom-config/meta/`.

**Representational form.** Raw sessions are mixed: structured SQLite/JSON plus natural-language messages and tool outputs. Episodes and semantic facts are mixed symbolic/prose records with distributed-parametric embeddings as retrieval indexes. Procedures are symbolic/prose step records. `phantom-config` memory files are prose system-definition artifacts; YAML/JSON config and SQLite rows are symbolic system-definition artifacts; prompt blocks are prose instructions assembled into the runtime context.

**Lineage.** Qdrant facts and procedures carry source episode ids, and episodes carry session ids. The evolution loop has stronger operational lineage: staged batch ids, queue rows, version numbers, file-level `VersionChange[]`, evolution log entries, and snapshot rollback. It is still weaker than citation-grade KB lineage because a final bullet in `user-profile.md` or `domain-knowledge.md` does not necessarily carry source message ids, extraction rationale, or review state inside the artifact.

**Behavioral authority.** Raw sessions, chat logs, episodes, and facts are knowledge artifacts when used as evidence, context, or recall. The Qdrant context builder gives selected facts/episodes/procedures prompt influence, but not enforcement. `phantom-config` evolved files become system-definition artifacts because they are injected as constitution, profile, domain knowledge, and strategy sections before the agent acts. Scheduler jobs are system-definition artifacts because they wake the full agent with self-contained task prompts. MCP dynamic tools and registered APIs become system-definition/runtime artifacts when future agents call them as capabilities. The constitution has operator-locked behavioral authority; the reflection subprocess can read it but is denied write access and checked by byte comparison.

**Scope.** The scope is per Phantom deployment: user, team, VM, channels, tools, and projects for one running co-worker. Learned config can generalize across future tasks within that deployment. It is not a cross-project public memory bank unless exported manually or exposed through MCP.

**Timing.** Episode/fact consolidation runs after sessions. Evolution is staged: gate at session end, persistent queue, periodic or depth-triggered batch drain, reflection subprocess, invariant check, version commit or rollback. Scheduler jobs later activate the full runtime with memory and prompt context, which turns prior retained artifacts into future action.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), Phantom splits the survey's trace-derived category in a useful way. Its Qdrant path is trace-to-episode/fact memory with light extraction. Its reflection path is trace-to-system-definition artifact learning: session summaries become edits to prompt-injected identity, profile, domain, strategy, correction, and principle files under deterministic invariant checks. It strengthens the survey claim that the most important distinction is raw trace retention versus promoted behavior-shaping artifacts.

## Curiosity Pass

Phantom's memory architecture is unusually honest about mixed substrates. It does not pretend Qdrant is the whole memory system. The file prompt stack, scheduler rows, MCP tools, dynamic tool registry, and agent notes all shape future behavior.

The implemented vector consolidation is much weaker than the documentation's full three-tier narrative. The code has a procedural store and context injection path, but the session consolidator does not yet mine procedures. The two-stage learning loop is therefore: lightweight trace-to-episode/fact storage plus heavier trace-to-config reflection.

The reflection subprocess is more compelling than the older judge-heavy story. Deterministic invariants are cheaper, inspectable, and closer to real enforcement. The tradeoff is that content quality is entrusted to the subprocess prompt and later operator observation, while the invariant layer mostly checks boundaries, syntax, size, duplicates, and sensitive patterns.

The main runtime's command blocker is explicitly defense-in-depth, not a sandbox. Phantom's real safety argument depends on deployment isolation, owner access control, permission options, evolution write constraints, secret handling, and audit logs. That is coherent for a dedicated VM; it would be too much ambient authority for a shared development machine.

The `agent-notes.md` design is a quiet but important alternative to over-automated memory. It gives the main agent a cheap place to leave durable scratch without immediately granting those notes automatic prompt authority.

## What to Watch

- Whether session consolidation grows beyond heuristics into LLM-derived semantic facts and real procedure promotion.
- Whether procedures become outcome-updated by actual task execution rather than only stored/retrieved.
- Whether evolved bullets gain source message ids or clickable lineage back to session/chat rows.
- Whether the documentation is updated to match the implemented reflection-subprocess/invariant architecture.
- Whether scheduler jobs, dynamic MCP tools, and generated pages get stronger lifecycle and rollback stories comparable to evolved config files.
- Whether the memory explorer deletion path grows audit/restore support for Qdrant records, not just immediate delete.

## Bottom Line

Phantom is the strongest reviewed example so far of an agent runtime where memory is not one store but a set of authority-bearing surfaces. Raw sessions and chat events are evidence; Qdrant episodes/facts/procedures are knowledge artifacts with retrieval influence; working memory and agent notes are file-backed continuity aids; evolved `phantom-config` files are prompt-injected system-definition artifacts; scheduler rows and MCP tools activate future behavior; and the reflection subprocess is a trace-derived promotion path bounded by write allowlists, invariant checks, and snapshot rollback.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Phantom combines trace-to-fact memory with trace-to-config system-definition learning.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: sessions, episodes, facts, and reports advise future action as evidence/context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: evolved config, scheduler jobs, prompt blocks, permissions, and tools shape or enforce future behavior.
- [Retained artifact](../../notes/definitions/retained-artifact.md) - exemplifies: Phantom has several retained surfaces whose behavioral consequence differs by consumer and channel.
- [Operative part](../../notes/definitions/operative-part.md) - exemplifies: Qdrant records bundle prose payloads, symbolic metadata, and distributed-parametric indexes with different operative roles.
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) - exemplifies: Phantom's design is best read by separating advice, instruction, runtime capability, write permission, and rollback authority.
- [A functioning KB needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) - compares-with: Phantom operationalizes a workshop-like layer through sessions, queues, scratch files, and promotion into stronger config artifacts.
