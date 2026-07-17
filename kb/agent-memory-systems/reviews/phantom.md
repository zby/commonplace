---
description: "Phantom review: VM co-worker with Qdrant memory, heuristic session extraction, and queued self-evolution over config files"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-04"
tags: [trace-learning]
---

# Phantom

Phantom, from `ghostwright/phantom`, is a Bun/TypeScript AI co-worker that runs on its own VM and exposes Slack, web chat, email, webhook, CLI, scheduler, MCP, memory, dynamic tools, and self-evolution in one process. Its durable behavior-shaping state is split between Qdrant vector memory, SQLite queues/session state, `phantom-config/` files, dynamic tool rows, role YAML, schedules, and operator-visible UI/API surfaces.

**Repository:** https://github.com/ghostwright/phantom

**Reviewed commit:** [f8c7ab42d885936ee54abc785528000260f4acc5](https://github.com/ghostwright/phantom/commit/f8c7ab42d885936ee54abc785528000260f4acc5)

**Source directory:** `related-systems/ghostwright--phantom`

## Core Ideas

**The agent is an always-on machine resident, not only a chat surface.** The README and architecture docs frame Phantom as a single Bun process on a VM with channels, agent runtime, prompt assembler, memory, evolution, MCP, dynamic tools, scheduler, and public UI endpoints ([README.md](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/README.md), [docs/architecture.md](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/docs/architecture.md), [src/index.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/index.ts)). That matters for memory because future action is not limited to answering; retained state can alter scheduled work, tool registration, page creation, email behavior, MCP exposure, and VM-side infrastructure work.

**The vector memory has three stores with different intended authority.** `MemorySystem` wires episodic, semantic, and procedural Qdrant stores behind one interface; each store has its own collection schema, sparse BM25 vector, payload indexes, and recall API ([src/memory/system.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/memory/system.ts), [src/memory/episodic.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/memory/episodic.ts), [src/memory/semantic.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/memory/semantic.ts), [src/memory/procedural.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/memory/procedural.ts)). Episodic memory stores session summaries, tools, files, outcomes, importance, access counts, and decay metadata; semantic memory stores facts with source episode ids, confidence, validity intervals, and contradiction supersession; procedural memory stores workflow steps and success/failure counters.

**Context efficiency is engineered by ranked pre-call assembly, not by making the store small.** `MemoryContextBuilder.build()` searches facts, episodes, and one procedure from the current query, prioritizes known facts, filters episodes through durability/recency thresholds, formats only compact summaries, and respects a configured token budget ([src/memory/context-builder.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/memory/context-builder.ts), [src/memory/ranking.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/memory/ranking.ts), [config/memory.yaml](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/config/memory.yaml)). The default budget is large at 50,000 estimated tokens, so the design is "select and budget" rather than minimal context.

**The self-evolution loop is file-based and trace-fed.** After sessions, `EvolutionEngine` gates learning signal, enqueues worthy session summaries in SQLite, drains by cadence/depth, spawns a constrained Agent SDK subprocess over `phantom-config/`, validates the diff with deterministic invariants, and either commits a version or restores a snapshot ([docs/self-evolution.md](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/docs/self-evolution.md), [src/evolution/gate.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/evolution/gate.ts), [src/evolution/queue.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/evolution/queue.ts), [src/evolution/reflection-subprocess.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/evolution/reflection-subprocess.ts), [src/evolution/invariant-check.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/evolution/invariant-check.ts)). This is stronger than ordinary chat history: the distilled outputs become prompt sections such as user profile, domain knowledge, and learned strategies.

**There are several memory surfaces, and their trust levels differ.** Vector memory is automatically extracted and ranked; evolved config is agent-written but sandboxed, invariant-checked, versioned, and injected into the prompt; `agent-notes.md` is instructed as append-only but must be pulled by the agent later; dynamic MCP tools are persisted in SQLite and registered on future MCP sessions; UI memory APIs let operators inspect and delete Qdrant entries ([src/agent/prompt-assembler.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/agent/prompt-assembler.ts), [src/agent/prompt-blocks/agent-memory-instructions.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/agent/prompt-blocks/agent-memory-instructions.ts), [src/mcp/dynamic-tools.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/mcp/dynamic-tools.ts), [src/mcp/tools-dynamic.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/mcp/tools-dynamic.ts), [src/memory/system.ts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/memory/system.ts)).

## Artifact analysis

- **Storage substrate:** `vector` `sqlite` `files` `repo` `service-object` — Qdrant stores episodes, semantic facts, and procedures; SQLite stores sessions, evolution queues, metrics, dynamic tools, MCP audit, scheduler, and other process state; `phantom-config/` stores evolved Markdown and JSONL memory files; role/config/source files live in the repo; channels, scheduler jobs, MCP factories, and Agent SDK subprocesses are service objects.
- **Representational form:** `prose` `symbolic` `parametric` — prompt sections, memory summaries, facts, procedures, config files, and notes are prose; YAML/Zod schemas, SQLite rows, Qdrant payloads, schedules, permission rules, sentinel JSON, invariants, and tool definitions are symbolic; dense embeddings and BM25 sparse vectors are parametric access structures.
- **Lineage:** `authored` `imported` `trace-extracted` — operator config, role templates, schedules, tool definitions, and manual memory edits are authored; external messages, uploaded files, email/web/chat content, and API results are imported; sessions, transcripts, tool/file traces, outcomes, user corrections, preferences, and reflection batches are trace-extracted into Qdrant entries or evolved config.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — vector memories and session transcripts advise as knowledge; evolved config, role prompts, working memory, agent memory instructions, and learned strategies instruct; security blocks, permission rules, scope checks, and invariant failures enforce; prompt assembly, roles, MCP factories, schedules, and dynamic tool registration route behavior; tests, health checks, preview validation, and invariant checks validate; Qdrant ranking and episode durability steer attention; consolidation and self-evolution learn from traces.

**Vector memory entries.** Storage substrate: Qdrant collections named from `config/memory.yaml`. Representational form: prose payloads plus symbolic metadata and dense/sparse vectors. Lineage: session-end heuristic extraction in `src/memory/consolidation.ts` and explicit store calls. Behavioral authority: advisory knowledge when formatted into `# Your Memory`, ranking input through vector/BM25 search, and weak learning input when source episode ids back semantic facts.

**Evolved config files.** Storage substrate: `phantom-config/` files and meta logs. Representational form: prose Markdown plus symbolic version/sentinel/diff metadata. Lineage: trace-extracted batches of session summaries that pass the gate and are rewritten by the reflection subprocess. Behavioral authority: strong instruction when injected as Constitution, Communication Style, User Profile, Domain Knowledge, and Learned Strategies before the model call.

**Evolution queue and logs.** Storage substrate: SQLite queue rows plus `meta/evolution-log.jsonl` and `metrics.json`. Representational form: symbolic JSON/SQL rows with prose reasons and summaries. Lineage: session summaries and gate decisions. Behavioral authority: learning and validation infrastructure; queue rows decide what the memory-manager subprocess sees, while logs make accepted changes auditable.

**Working memory and agent notes.** Storage substrate: `data/working-memory.md` and `phantom-config/memory/agent-notes.md`. Representational form: prose. Lineage: authored or agent-authored. Behavioral authority: working memory is pushed into the prompt when present, bounded to 75 lines; agent notes are intentionally not injected and must be retrieved by the agent with file tools, making them pull-side memory.

**Dynamic tools.** Storage substrate: SQLite `dynamic_tools` rows. Representational form: symbolic tool schema/handler metadata plus prose descriptions and optional shell/script handler text. Lineage: authored by the agent/operator through `phantom_register_tool`. Behavioral authority: routing and capability definition because persisted rows are registered on future MCP server instances and can become tools available to later agents.

Promotion path: raw channel/session traces become compact episodes and heuristic semantic facts; repeated access increases episode salience; contradictions can supersede older facts; queued session summaries can become prompt-level files after reflection and invariants; dynamic tool registrations turn built infrastructure into future callable capability. The strongest promotion is trace summary to evolved config, because it moves from memory-as-evidence into instruction-bearing prompt material.

## Comparison with Our System

Phantom is closer to a continuously operating agent appliance than Commonplace. Commonplace stores reviewed, git-readable knowledge artifacts and asks agents to navigate them deliberately; Phantom pushes selected memory and evolved prompt sections into a VM-resident agent loop that also owns channels, scheduler, dynamic tools, and infrastructure.

The strongest alignment is the split between raw evidence, distilled memory, and governance. Phantom keeps session traces, Qdrant entries, evolved files, version logs, and invariants distinct. Commonplace similarly separates sources, notes, indexes, type contracts, review runs, and validation. The difference is authority speed: Phantom is willing to let a reflected session modify future instructions after deterministic scope checks, while Commonplace usually requires source-grounded review before new methodology becomes durable guidance.

The main divergence is reviewability. Commonplace's durable artifacts are ordinary Markdown and generated indexes in git. Phantom's behavior can depend on Qdrant payloads, SQLite queue rows, scheduler state, MCP registrations, local `phantom-config/` files, environment variables, and live service availability. That makes Phantom operationally powerful but harder to audit from one file tree.

Phantom also exposes a useful warning about context scale. A 50,000-token memory budget can preserve continuity, but it still risks context dilution if ranking quality is weak. Commonplace's slower, file-native approach trades less automatic recall for more explicit navigation and review.

### Borrowable Ideas

**Diff-checked memory-manager subprocess.** Commonplace could use a constrained agent to propose edits to mutable profile or operator-preference files, then deterministic invariants and review gates would decide what lands. Ready only for a narrow, low-authority memory surface.

**Trace batches before reflection.** Phantom queues and dedups sessions before asking an agent to learn from them. Commonplace could batch recurring review findings before proposing a synthesis note, but should keep source links and operator review mandatory.

**Separate injected memory from searchable memory.** Phantom's `agent-notes.md` deliberately stays out of the prompt until read, while evolved config and selected vector context are injected. Commonplace already has this principle in indexes versus full notes; Phantom is a good operational example.

**Invariant checks around agent-written memory.** The concrete checks for file scope, immutable files, size bounds, syntax, credential patterns, and sentinel/diff agreement are directly portable to any Commonplace workflow that lets an agent write semi-automatically.

**Do not borrow large automatic recall without measurement.** Phantom's design assumes ranked memory helps continuity, but the code does not prove downstream faithfulness. Commonplace should require ablations or post-action audits before granting pushed memory high authority.

## Write side

**Write agency:** `manual` `automatic` — Operators and agents can manually edit config files, memory files, dynamic tools, schedules, and dashboard memory entries; automatic paths consolidate sessions into Qdrant, increment access counts on recall, supersede contradictory facts, enqueue and drain evolution batches, rewrite evolved config files through a subprocess, and commit or roll back versioned changes.

**Curation operations:** `consolidate` `evolve` `invalidate` `decay` `promote` — The reflection subprocess can compact existing memory files; evolved config and semantic facts are modified in place; semantic contradictions mark older facts with `valid_until`; episode ranking down-weights stale memories through recency/decay; access-count reinforcement and repeated/session-derived reflection can raise salience or authority without changing the original trace.

### Trace-learning

**Trace source:** `session-logs` `tool-traces` `event-streams` — Session summaries include user and assistant messages, tools, files tracked, outcome, cost, and timestamps; web chat also stores event-log and transcript surfaces; the memory system extracts episodes/facts from completed sessions, and the evolution queue batches session summaries.

**Extraction:** Vector-memory extraction is heuristic at this commit: it always creates an episode from session metadata and extracts semantic facts only from correction/preference patterns in user messages. Self-evolution uses a Haiku gate or failsafe to decide whether a session carries durable learning signal, then an Agent SDK subprocess reads the batch and current memory files and decides what to edit, compact, skip, or escalate.

**Learning scope:** `per-project` `cross-task` — A Phantom's memory applies across channels and sessions for its VM/workspace, and the evolved config is meant to affect many future tasks for that owner or role.

**Learning timing:** `online` `staged` — Qdrant consolidation runs non-blocking after a session; self-evolution is staged through a persistent queue drained on cadence or demand depth.

**Distilled form:** `prose` `symbolic` `parametric` — Episodes, facts, procedures, evolved Markdown, corrections, principles, and learned strategies are prose; queue rows, version changes, sentinels, metrics, validity intervals, and dynamic tool definitions are symbolic; embeddings and sparse vectors are parametric.

Survey position: Phantom is a strong trace-learning example because runtime traces can become both knowledge artifacts and prompt-level system-definition artifacts. Its differentiator is not only extraction, but the rollback/invariant envelope around agent-authored memory edits. The weak point is semantic faithfulness: the deterministic invariants protect scope, syntax, and obvious safety, not whether a learned principle is true.

## Read-back

**Read-back:** `both` — Pull paths include explicit reflective tools, memory dashboard/API reads, file reads of agent notes, Qdrant scroll/get/search endpoints, and dynamic tool listing. Push paths include pre-call `MemoryContextBuilder` output, evolved config sections, working memory injection, scheduled runs that wake the agent with retained state, and dynamic tools registered on new MCP sessions.

**Read-back signal:** `coarse` `inferred / lexical` `inferred / embedding` — Evolved config and working memory are coarse prompt additions when present; vector memory is selected from the current query using dense embeddings and BM25 sparse vectors; procedure/fact/episode filters and ranking are applied before injection.

**Faithfulness tested:** `no` — The repo has many unit/e2e tests and deterministic invariants, but I did not find a with/without ablation or post-action audit proving that injected memories, evolved config, or retrieved procedures change agent behavior as intended.

**Direction edge cases.** Agent notes are explicitly not injected, so they are pull even though the main agent writes them. Evolved config is push because `assemblePrompt()` includes it before calls. Dynamic tools are not memory text in the prompt, but they are behavior-shaping retained state because persisted registrations become available tools for later MCP sessions.

**Targeting and signal.** The main pre-call memory path is instance-conditioned on the current user text. It embeds the query, computes sparse BM25 terms, searches configured Qdrant collections, then budgets formatted facts, episodes, and a single procedure into the system prompt. Evolved config and working memory are coarser: if loaded, they appear without query-specific retrieval.

**Injection point.** Memory read-back happens before Agent SDK invocation, in `AgentRuntime.runQuery()` and `executeChatQuery()`, when `memoryContextBuilder.build(text)` runs and `assemblePrompt()` appends memory/evolved/working-memory sections. Scheduler activation is also pre-invocation: the scheduled prompt starts a normal run with the same runtime memory surfaces.

**Selection, scope, and complexity.** Defaults are top 10 episodes, top 20 facts, one procedure, and 50,000 estimated memory tokens. Episodic results are reranked by search score, importance, access reinforcement, last access, recency, and decay; semantic facts default to currently valid facts; procedural lookup requires a minimum score. Complexity is high because prompt context can combine evolved files, working memory, vector memory, role instructions, runtime channel context, and tool surfaces.

**Authority at consumption.** Facts and episodes are advisory under `# Your Memory`; procedures are closer to soft instructions because they provide named steps and success counts; evolved config is stronger instruction; invariant checks and permission rules are enforcement; dynamic tools extend the action surface. Effective authority is not separately measured from source code.

**Other consumers.** Humans can inspect dashboard memory, chat transcripts, pages, logs, metrics, and config files. The evolution engine consumes queued sessions and config files. External MCP clients consume dynamic tools and universal tools. Schedulers consume retained job definitions to initiate future agent runs.

## Curiosity Pass

**The docs promise richer consolidation than the current vector code shows.** `docs/memory.md` describes semantic extraction with heuristic or LLM extraction, procedural promotion, and nightly consolidation; `src/memory/consolidation.ts` says the LLM judge path is gone and currently creates one episode plus heuristic correction/preference facts. The stronger learning loop is the reflection subprocess, not Qdrant consolidation.

**Phantom has two long-term memories with different activation semantics.** The evolved config is automatically injected and trusted enough to shape behavior; `agent-notes.md` is agent-owned but explicitly not injected. This is a useful design split because not every durable note deserves context budget or instruction authority.

**The invariant envelope checks shape, not truth.** It can prevent constitution edits, credential leaks, oversized diffs, malformed Markdown, and scope violations. It cannot prove that a new user-profile bullet faithfully summarizes the session that produced it.

**Access-count updates make read-back mutate the store.** Episode recall increments access counts in the background, so read-side use feeds future ranking. This is a salience feedback loop, not just passive retrieval.

**The VM premise expands memory authority.** A learned preference can change future shell work, scheduled reports, email, public pages, and MCP-exposed tools. That gives continuity more leverage than in a chat-only system.

## What to Watch

- Whether Qdrant consolidation gains the documented nightly compression, procedural promotion, and pruning paths; that would broaden automatic curation beyond the current heuristic extractor.
- Whether semantic extraction records richer evidence spans, source message ids, or review state so evolved facts can be audited back to exact turns.
- Whether Phantom adds behavioral tests that compare actions with and without injected memory/evolved config; that would change the faithfulness verdict.
- Whether dynamic tool registration gains provenance and review gates before tools become available to other clients.
- Whether large memory budgets produce context dilution in real deployments and whether the ranking thresholds are tuned from observed failures.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - applies: Phantom separates searchable notes, automatically injected memory, and always-loaded evolved config.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Phantom's retained behavior is split across files, Qdrant, SQLite, service objects, embeddings, prompts, and invariants.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: episodes, facts, transcripts, memory search results, and dashboard memory advise future work.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: evolved config, permission rules, dynamic tools, schedules, invariants, and prompt assembly configure future behavior.
- [Context engineering](../../notes/definitions/context-engineering.md) - frames: Phantom is a context-routing and activation system around a persistent VM-based agent.
- [Agent memory needs discoverable, composable, trusted knowledge under bounded context](../../notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md) - compares: Phantom is strong on composition and activation but still needs stronger trust checks for learned memory.
