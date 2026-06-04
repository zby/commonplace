---
description: "Spacebot review: Rust multi-process agent harness with typed graph memory, working-memory synthesis, task autonomy, and engineered prompt activation"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-02"
tags: [trace-derived, push-activation]
---

# Spacebot

Spacebot, by Spacedrive, is a Rust agent harness for team and community agents. It is not just a memory database: it splits user-facing channels, thinking branches, workers, compaction, cortex synthesis, cron execution, tasks, skills, wiki pages, and messaging adapters into a single local service. The memory-relevant design is a typed SQLite/LanceDB graph plus several prompt-time context layers that make conversations, workers, and autonomous runs inherit distilled state from prior activity.

**Repository:** https://github.com/spacedriveapp/spacebot

**Reviewed commit:** [ac52277404d3813045aa053b78c95810ab85e7c5](https://github.com/spacedriveapp/spacebot/commit/ac52277404d3813045aa053b78c95810ab85e7c5)

**Last checked:** 2026-06-02

## Core Ideas

**Process roles are code-level isolation boundaries.** The README describes five process types: channels, branches, workers, compactor, and cortex. The implementation backs that up with separate structs, prompts, tool servers, hooks, routing, and lifecycle handling. Channels talk to users and delegate; branches clone channel history for short reasoning; workers get focused tasks and worker tools; the compactor watches context size; cortex synthesizes memory and supervises system state ([README.md](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/README.md), [AGENTS.md](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/AGENTS.md), [src/agent/branch.rs](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/agent/branch.rs), [src/agent/channel_dispatch.rs](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/agent/channel_dispatch.rs)).

**Long-term memory is a typed graph with hybrid recall.** Durable memories live in SQLite with type, importance, source, channel, access counters, soft-forget state, and graph associations; embeddings and full-text search live in LanceDB. Hybrid search merges LanceDB FTS, vector search, and graph traversal with Reciprocal Rank Fusion, while metadata modes support recent, important, and typed recall ([migrations/20260211000001_memories.sql](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/migrations/20260211000001_memories.sql), [src/memory/types.rs](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/memory/types.rs), [src/memory/store.rs](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/memory/store.rs), [src/memory/search.rs](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/memory/search.rs)).

**Memory write paths are guarded by tools and contracts.** `memory_save` validates type, importance, byte length, target associations, embeddings, LanceDB storage, and FTS indexing; if embedding generation or storage fails, it compensates by deleting the SQLite row and associations. Silent memory-persistence branches must end with `memory_persistence_complete`, whose contract rejects fabricated saved-memory IDs and can also emit extracted working-memory events ([src/tools/memory_save.rs](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/tools/memory_save.rs), [src/tools/memory_persistence_complete.rs](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/tools/memory_persistence_complete.rs), [src/agent/branch.rs](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/agent/branch.rs)).

**Working memory is a separate temporal layer, not the same store as graph memory.** Spacebot keeps append-only working-memory events, intra-day synthesis paragraphs, and daily summaries in their own tables. Channel prompt assembly renders a budgeted "today / yesterday / week" working-memory section, a channel activity map, participant context, memory bulletin, and knowledge synthesis into the channel prompt when memory mode permits it ([migrations/20260319000001_working_memory.sql](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/migrations/20260319000001_working_memory.sql), [src/memory/working.rs](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/memory/working.rs), [src/agent/channel.rs](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/agent/channel.rs), [src/prompts/engine.rs](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/prompts/engine.rs)).

**Context efficiency is handled by decomposition, budgets, and compaction.** Branches inherit channel history but preflight-compact on overflow risk; workers start from focused prompts rather than full conversation history; channel prompt layers have explicit token budgets; compactor thresholds trigger background summarization, aggressive summarization, or emergency truncation. The system still pushes a lot of context into channels, but its complexity is managed by process separation and rendered layers rather than a single RAG blob ([src/agent/branch.rs](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/agent/branch.rs), [src/agent/compactor.rs](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/agent/compactor.rs), [src/config/types.rs](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/config/types.rs), [src/agent/channel_dispatch.rs](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/agent/channel_dispatch.rs)).

**Adoption is native to chat and local infrastructure.** The code packages a single Rust binary with SQLite, LanceDB, redb, messaging adapters, browser/shell/file tools, MCP clients, OpenCode workers, task storage, wiki storage, secret isolation, and a dashboard API surface ([Cargo.toml](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/Cargo.toml), [src/messaging.rs](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/messaging.rs), [src/mcp.rs](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/mcp.rs), [src/opencode.rs](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/opencode.rs), [src/secrets.rs](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/secrets.rs), [src/wiki/store.rs](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/wiki/store.rs)).

## Artifact analysis

- **Storage substrate:** `sqlite` — SQLite `memories` and `associations` tables plus LanceDB embeddings/FTS rows
- **Representational form:** `prose` `symbolic` `parametric` — typed rows and graph edges carry symbolic structure, memory `content` is prose, and LanceDB vectors/FTS indexes are derived retrieval state
- **Lineage:** `authored` `imported` `trace-extracted` — retained state comes from user/agent authored rows, imported skill/wiki/ingestion inputs, and traces distilled from conversations, worker/process events, persistence branches, and cortex synthesis
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — memories, wiki pages, and transcripts provide knowledge; skills/prompts instruct; task/cron and contract rows constrain and route work; validation contracts check persistence; ranking, synthesis, and maintenance decide what is retained or shown

**Graph memories and associations.** Storage substrate: SQLite `memories` and `associations` tables plus LanceDB embeddings/FTS rows. Representational form: mixed symbolic/prose/distributed-parametric: typed rows and graph edges carry symbolic structure, memory `content` is prose, and LanceDB vectors/FTS indexes are derived retrieval state. Lineage: authored or trace-extracted through `memory_save`, ingestion, compaction-adjacent persistence, branch/cortex tools, or API calls; embeddings and indexes are derived and invalidated by memory content or embedding model changes. Behavioral authority: knowledge artifact when recalled as evidence/context; ranking authority when importance, access counters, graph relations, RRF scores, and type filters decide what is shown.

**Working-memory events, intra-day syntheses, and daily summaries.** Storage substrate: SQLite `working_memory_events`, `working_memory_intraday_syntheses`, and `working_memory_daily_summaries`. Representational form: symbolic event type/channel/user/importance metadata plus prose summaries. Lineage: raw events are emitted from branch completions, worker lifecycle, cron execution, memory saves, decisions extracted from replies, and persistence-branch extractions; syntheses and summaries are derived by cortex or rendering routines. Behavioral authority: prompt-time advisory context for channels and cortex, with stronger selection authority under token pressure because rendering budgets decide which events survive into context.

**Knowledge synthesis and memory bulletin.** Storage substrate: in-memory `RuntimeConfig` fields refreshed by cortex, backed indirectly by SQLite memories, tasks, and working-memory input sections. Representational form: prose synthesis. Lineage: LLM-derived from gathered memory/task sections and regenerated when memory changes bump the synthesis version; freshness and warmup state track whether the cached synthesis is usable. Behavioral authority: pushed system-prompt context for channels and cortex chat, not a canonical source of truth. It summarizes and activates other artifacts; it should be invalidated when the underlying memory/task graph changes ([src/agent/cortex.rs](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/agent/cortex.rs), [src/config/runtime.rs](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/config/runtime.rs)).

**Skills.** Storage substrate: built-in embedded skills, instance-level skill directories, and agent workspace `skills/` directories. Representational form: Markdown instruction packages with YAML frontmatter, rendered as summaries for channels and as readable full instructions for workers. Lineage: authored, installed from GitHub/skills.sh, or uploaded via API/CLI; in this checkout I found installation, loading, removal, prompt listing, and `read_skill`, but not a checked code path that automatically writes new skill files from post-conversation reflection. Behavioral authority: system-definition artifact when worker prompts list skills and `read_skill` supplies instructions; softer advisory context when channels see only skill names/descriptions ([src/skills.rs](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/skills.rs), [src/tools/read_skill.rs](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/tools/read_skill.rs), [src/tools/install_skill.rs](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/tools/install_skill.rs), [src/agent/channel_dispatch.rs](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/agent/channel_dispatch.rs)).

**Tasks, cron jobs, wiki pages, conversations, and worker transcripts.** Storage substrate: SQLite tables and per-feature stores. Representational form: symbolic status/type/priority/version fields plus prose descriptions, prompts, summaries, and transcript blobs. Lineage: user-authored, agent-created, imported, or generated during process execution; task approval and task status transitions are explicit. Behavioral authority: system-definition artifacts for scheduling and task selection, knowledge artifacts for wiki/conversation lookup, and audit/evidence artifacts for worker transcripts ([src/tasks/store.rs](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/tasks/store.rs), [src/cron/store.rs](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/cron/store.rs), [src/wiki/store.rs](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/wiki/store.rs), [src/conversation/history.rs](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/conversation/history.rs), [src/conversation/worker_transcript.rs](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/conversation/worker_transcript.rs)).

The main promotion path is trace -> event/memory row -> derived synthesis -> prompt injection. A weaker promotion path is memory maintenance: low-importance memories decay/prune, near duplicates merge, and successful prune/merge dirties knowledge synthesis so prompt-facing summaries can refresh ([src/memory/maintenance.rs](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/memory/maintenance.rs), [src/agent/maintenance.rs](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/agent/maintenance.rs)). I did not find a Commonplace-style governance promotion from evidence to reviewed note to enforced validator.

## Comparison with Our System

| Dimension | Spacebot | Commonplace |
|---|---|---|
| Primary purpose | Runtime harness for live chat agents, workers, autonomy, memory, tools, and messaging | Git-native methodology KB for durable agent-readable knowledge, instructions, validation, and review |
| Canonical artifacts | SQLite memory/task/wiki/event rows, LanceDB vectors, prompt syntheses, skill files, transcripts | Typed Markdown notes, collection/type contracts, source snapshots, generated indexes, review reports, scripts |
| Context strategy | Channels receive rendered context layers; branches clone then compact; workers get focused prompts and optional skills | Agents deliberately pull notes, indexes, links, skills, and review reports under collection/type contracts |
| Trace-derived learning | Conversation/process traces become memories, working-memory events, syntheses, task state, and sometimes maintenance updates | Trace-derived extraction is mostly explicit through review/workshop workflows and agent-authored notes |
| Activation | Engineered prompt push plus explicit memory/wiki/task pull tools | Mostly pull through `rg`, indexes, links, skills, and validation; occasional instructions are always-loaded |
| Governance | Type fields, associations, contracts, circuit breakers, soft forget, maintenance, task approval | Source citation, review gates, link vocabulary, type validation, lifecycle statuses, archive/replacement discipline |

Spacebot is stronger as a live runtime. It solves problems Commonplace mostly sidesteps: concurrent user channels, process isolation, status injection, background compaction, autonomous task wakeups, messaging adapters, tool containment, and local databases for high-write operational state. Its most useful memory lesson is that not every retained artifact should be a Markdown file; event logs, task rows, vector indexes, and prompt caches are useful when they have bounded authority and regeneration paths.

Commonplace is stronger as a durable knowledge system. Spacebot memories have types, importance, source, channel, and associations, but they do not carry review state, explicit source spans, semantic link labels, collection-local writing contracts, replacement archives, or validation gates. Spacebot optimizes for agent continuity and responsiveness; Commonplace optimizes for inspectable claims and long-term methodological structure.

**Read-back:** `both` — Agents can pull through memory/wiki/task/channel tools, while channels and workers receive engineered prompt-time push from retained memory layers: memory bulletins, knowledge synthesis, working memory, channel maps, participant context, and instance-installed skills

The context-efficiency contrast is useful. Commonplace keeps canonical artifacts human-readable and asks the acting agent to choose what to load. Spacebot centralizes more runtime choice in renderers, budgets, and the cortex synthesis loop. That reduces per-turn agent burden, but it also makes trust depend on prompt assembly code and synthesis freshness rather than on explicit human-readable navigation choices.

### Borrowable Ideas

**Separate event memory from durable knowledge.** Ready now as vocabulary. Commonplace should continue treating workshop logs, review bundles, and source snapshots as different from library notes; Spacebot makes that separation concrete with working-memory events versus graph memories versus syntheses.

**Use prompt-layer budgets as first-class contracts.** Ready for generated context. Spacebot's `WorkingMemoryConfig` gives concrete budgets and retention limits. Commonplace generated packs or review summaries should state token budgets and selection policy, not just produce "helpful context."

**Make memory persistence end with a terminal contract.** Ready for review tooling. `memory_persistence_complete` verifies that a persistence branch either saved exactly the memory IDs it produced or declares why nothing was saved. Commonplace could use the same pattern for trace-ingest or review-bundle agents that must close with explicit promoted artifacts or a no-promotion reason.

**Keep branch conclusions as summaries, not full traces.** Ready as a design rule. Spacebot branches return conclusions to the channel and are then deleted; Commonplace can borrow this for sub-agent review workflows where the parent needs findings and cited evidence, not a full scratch transcript.

**Treat generated synthesis as a cache, not an authority.** Ready now. Spacebot's bulletin/knowledge synthesis is prompt-effective but derived. Commonplace should keep that distinction for any future memory bulletin: the cache can activate canonical notes, but should not become the note.

**Do not borrow unreviewed auto-memory authority wholesale.** Spacebot is optimized for live interaction, so a memory row can shape future behavior quickly. Commonplace should keep higher-friction promotion for claims that enter the methodology library.

## Write-side placement

**Write agency:** `automatic` `manual` — the review identifies a trace-derived or rule-driven path that changes retained memory from execution/session evidence; manual surfaces are included where the reviewed prose describes user or operator authoring.

**Curation operations:** `consolidate` `dedup` `synthesize` `invalidate` `decay` `promote` — the existing review evidence identifies automatic store-changing operations matching these curation classes.

### Trace-derived learning
**Trace source:** `session-logs` `tool-traces` `event-streams` — channel conversations, worker transcripts, tool-mediated memory saves, branch/cortex completions, cron/task events, persistence-branch extractions, and ingestion chunks all feed retained memory or synthesis layers.

**Learning scope:** `per-project` `cross-task` — memory is service-owned per agent with channel/user metadata, multi-agent links, task state, wiki input, and synthesis layers that can affect later work across channels and tasks.

**Learning timing:** `online` `staged` — prompt assembly, event capture, persistence branches, compaction, cortex synthesis, cron runs, and maintenance run during service operation, with synthesis and maintenance staged by cadence, thresholds, or dirty-version state.

**Distilled form:** `prose` `symbolic` `parametric` — trace outputs include prose graph memories, working-memory syntheses, daily summaries, and knowledge synthesis; symbolic event/type/task/status/association rows; and LanceDB embedding state derived from memory content.

**Trace source.** Spacebot qualifies as trace-derived learning. Raw signals include channel conversations, branch conclusions, worker lifecycle/results, cron executions, memory saves, explicit decisions in replies, persistence-branch extractions, conversation logs, worker transcripts, task status changes, and ingestion chunks. Trigger boundaries are per turn, process completion, compaction threshold, persistence threshold, cortex synthesis cadence, maintenance pass, cron wake, and ingestion chunk ([src/agent/channel.rs](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/agent/channel.rs), [src/agent/channel_dispatch.rs](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/agent/channel_dispatch.rs), [src/tools/memory_persistence_complete.rs](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/tools/memory_persistence_complete.rs), [src/agent/ingestion.rs](https://github.com/spacedriveapp/spacebot/blob/ac52277404d3813045aa053b78c95810ab85e7c5/src/agent/ingestion.rs)).

**Extraction.** Extraction is split across deterministic emitters and LLM branches. Deterministic emitters record process and decision events; memory tools let branches/cortex save typed graph memories; persistence branches run silently after message, time, or event-density thresholds and must close through a terminal contract; cortex gathers memory/task sections and generates a compact knowledge synthesis. The primary oracles are tool/schema validation, ID matching in the completion contract, memory importance/type choices, maintenance thresholds, and LLM judgment inside branch/cortex prompts. Effective semantic quality is not verified from code.

**Scope and timing.** Scope is service-owned per agent, with channel/user metadata and multi-agent links layered in. Timing is online during normal operation: prompt assembly, working-memory rendering, persistence branches, compaction, cortex synthesis, cron runs, and maintenance all run as part of the deployed service rather than an offline benchmark-only pipeline.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), Spacebot belongs in the service-owned trace backend family, near systems that turn live agent activity into symbolic/prose artifacts and then push distilled context back into future sessions. It strengthens the survey's "raw trace plus derived working memory" axis: the raw event log, graph memories, working-memory syntheses, knowledge synthesis, and prompt renderers are distinct operative layers. It also weakens any simple equation of trace-derived learning with "skill writing"; at this commit the inspected code clearly implements trace-to-memory and trace-to-synthesis, while autonomous skill capture is claimed in README prose but not found as a concrete save-skill path.

## Read-back placement

**Read-back signal:** `coarse` `identifier` `inferred / lexical` `inferred / embedding` — prompt assembly pushes coarse service-level bulletins and synthesis caches, identifier-scoped channel/user/day/event/task layers, and graph-memory recall that combines FTS, vector search, keyword-seeded graph expansion, type filters, and top-k curation.

**Faithfulness tested:** `no` — the review found no read-back faithfulness test proving that injected working memory or knowledge synthesis changes downstream behavior.

**Direction.** Both. `memory_recall`, wiki tools, task tools, channel recall, and API surfaces are pull paths. Channel prompt assembly pushes retained memory through the memory bulletin, knowledge synthesis, working-memory rendering, channel activity maps, participant context, and, where installed for the instance, skills. Worker ambient memory likewise pushes knowledge synthesis and working memory into worker prompts. Static prompt fragments, built-in tool docs, adapter prompts, worker capabilities, and status scaffolding are baseline context surfaces, not memory read-back.

**Targeting and signal.** The strongest memory push is `instance` targeted, mostly by `identifier`: channel prompts pass the current `channel_id` into working-memory rendering, exclude that channel from the other-channel map, scope participant context by active participant keys, and use day/time, event type, channel, user, and config symbols to select what survives. The memory bulletin and knowledge synthesis are coarser service-level caches, refreshed by dirty-version/freshness logic and gathered memory/task sections, then pushed into each channel when memory mode is enabled. The explicit graph-memory pull path uses mixed inferred selection: LanceDB FTS (`inferred / lexical`), vector search (`inferred / embedding`), keyword-seeded graph expansion, RRF, optional type filters, and top-k curation. Precision, recall, and context dilution are not verified from code. This remains `push-activation` because before-action prompt assembly pushes retained memory with scope, freshness, and budget controls, not merely a manual search tool.

**Injection point.** Channel push happens before each channel LLM call. Worker skills and worker context are assembled before worker execution. Memory persistence and compaction run after activity and can affect later turns through new memory rows, working-memory events, or updated syntheses.

**Selection, scope, and complexity.** Selection is layered: graph memory recall has top-k/search mode/type filters; working memory has token budgets and event caps; channel maps cap channels and inactive windows; participant context has participant thresholds; synthesis caches summarize broader retained state. Complexity remains high because many layers can be present in one prompt. The code makes the complexity explicit, but quality of final prompt composition is runtime-dependent.

**Authority at consumption.** Most pushed memory is advisory context. Installed skills become stronger system-definition artifacts for workers when `read_skill` returns full instructions. Task rows and cron rows can schedule or constrain future work. The code does not include a read-back faithfulness test proving that injected memory changes behavior.

**Other consumers.** Humans consume the same retained state through dashboard/API/CLI views; cortex consumes it for synthesis and supervision; maintenance consumes graph memory for decay/prune/merge; cron/task schedulers consume task and cron rows for autonomous execution.

## Curiosity Pass

**The README is more ambitious than the code I found for skills.** The README says branches write skills from experience and post-conversation reflection saves skills. The inspected code clearly implements skill loading, installation, listing, worker injection, and `read_skill`; I did not find an automatic skill-file creation path comparable to `memory_save`.

**Memory is both operational state and agent knowledge.** Tasks, cron jobs, worker transcripts, wiki pages, prompt snapshots, and project metadata all shape future behavior, but only some are called "memory." Spacebot is a good example of why retained-artifact analysis needs storage, form, lineage, and authority rather than a single memory label.

**The channel is protected from doing too much, but still receives a lot.** Branch/worker decomposition prevents a monolithic LLM loop, yet channels can receive identity, bulletin, knowledge synthesis, skills summary, status, coalescing hint, available channels, org context, adapter prompt, project context, backfill transcript, working memory, channel activity map, and participant context. Spacebot's real context problem is not only volume; it is layer interaction.

**Graph traversal starts from high-importance memories with keyword overlap.** That is pragmatic and cheap, but it means graph recall is not a general symbolic reasoner over the memory graph. It is a retrieval expansion heuristic.

**Soft forgetting is not evidence deletion.** Forgotten memories are excluded from search/recall but remain in SQLite. That is good for audit/recovery, but it matters for privacy and retention claims.

## What to Watch

- Whether the claimed autonomous skill capture becomes a concrete, validated write path with source traces, previews, rollback, and prompt-injection tests.
- Whether memory rows gain source spans, confidence, review state, or contradiction resolution beyond typed associations and maintenance merging.
- Whether prompt-layer quality gets measured with WITH/WITHOUT activation tests, especially for working memory and knowledge synthesis.
- Whether knowledge synthesis records enough gathered-section metadata to explain why a later prompt contained a specific claim.
- Whether task/cron autonomy starts using stricter provenance and approval links from `source_memory_id` to generated tasks and autonomous runs.

## Bottom Line

Spacebot is one of the more complete live-agent memory runtimes in this survey: it owns conversations, background work, typed graph memory, working-memory events, synthesis, scheduling, tools, and messaging in one service. Its best lesson for Commonplace is not "replace Markdown with SQLite"; it is to separate trace capture, durable knowledge, derived prompt caches, and activation layers so each carries only the authority it can justify.

Relevant Notes:

- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) - exemplifies: Spacebot manages context through process isolation, rendered memory layers, budgets, and compaction.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Spacebot's memory surfaces require separating storage substrate, representational form, lineage, and behavioral authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: graph memories, wiki pages, transcripts, and working-memory events can serve as evidence/reference/context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: skills, tasks, cron rows, prompt renderers, and tool contracts can instruct, schedule, route, or constrain future behavior.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: Spacebot has both stored memory and engineered prompt activation layers.
- [Use Trace-Derived Extraction As Meta-Learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: Spacebot derives memory rows, working-memory events, and prompt syntheses from live conversation/process traces.
