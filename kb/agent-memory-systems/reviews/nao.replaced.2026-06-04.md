---
description: "nao review: analytics-agent project context folder, CLI sync/deploy lifecycle, chat-derived user memories, MCP tools, stories, tests"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: []
status: outdated
last-checked: "2026-06-02"
---

# nao

> Replaced 2026-06-04. See [nao](./nao.md) for the current review.

nao, from nao Labs' `getnao/nao` repository, is an open-source analytics agent system. Its main retained state is not a single memory database: it combines a CLI-built project context folder, backend chat/story/memory tables, MCP and built-in tool surfaces, deployable Docker/git context lifecycles, and a frontend for configuring projects, memories, MCP access, and tests. The code distinguishes durable analytics context files from chat-derived user memories: project files guide analytic work, while extracted memories describe persistent user facts and global behavior preferences.

**Repository:** https://github.com/getnao/nao

**Reviewed commit:** [f996d94a0063d3313015fa6bf08205f24c97c7ac](https://github.com/getnao/nao/commit/f996d94a0063d3313015fa6bf08205f24c97c7ac)

**Last checked:** 2026-06-02

## Core Ideas

**The project folder is the primary analytics context substrate.** `nao init` creates `nao_config.yaml`, `.naoignore`, `RULES.md`, `databases/`, `queries/`, `docs/`, `semantics/`, `repos/`, `agent/tools`, `agent/mcps`, `agent/skills`, and `tests` ([init.py](https://github.com/getnao/nao/blob/f996d94a0063d3313015fa6bf08205f24c97c7ac/cli/nao_core/commands/init.py), [CLI README](https://github.com/getnao/nao/blob/f996d94a0063d3313015fa6bf08205f24c97c7ac/cli/README.md)). The backend system prompt then tells the agent that all user context is stored as files in the project folder, with database context represented by table folders and markdown files rather than by loading warehouse data directly ([system-prompt.tsx](https://github.com/getnao/nao/blob/f996d94a0063d3313015fa6bf08205f24c97c7ac/apps/backend/src/components/ai/system-prompt.tsx)).

**`nao sync` turns external analytics sources into inspectable files.** Database sync renders configured templates such as columns, preview, description, profiling, indexes, and how-to-use into `databases/type=.../database=.../schema=.../table=.../` paths; it can compute table profiling and query-history-derived usage stats where configured ([provider.py](https://github.com/getnao/nao/blob/f996d94a0063d3313015fa6bf08205f24c97c7ac/cli/nao_core/commands/sync/providers/databases/provider.py), [context.py](https://github.com/getnao/nao/blob/f996d94a0063d3313015fa6bf08205f24c97c7ac/cli/nao_core/config/databases/context.py)). Repository sync clones or copies configured repos under `repos/`, strips `.git` from cloned repositories so files become ordinary context, and supports include/exclude filters for local paths ([repository provider](https://github.com/getnao/nao/blob/f996d94a0063d3313015fa6bf08205f24c97c7ac/cli/nao_core/commands/sync/providers/repositories/provider.py)). Notion and template rendering round out the same file-first context model.

**Context efficiency is file navigation plus small prompt pushes, not full-context loading.** The system prompt always includes compact global instructions, `RULES.md` when present, database connection names, available skill summaries, and bounded user memories. It does not load every database file, repository file, or document into the prompt. The agent uses `list`, `search`, `grep`, and `read` tools against the project folder, plus `@` table mentions that append selected `columns.md` content to the last user message ([agent.ts](https://github.com/getnao/nao/blob/f996d94a0063d3313015fa6bf08205f24c97c7ac/apps/backend/src/services/agent.ts), [user-rules.ts](https://github.com/getnao/nao/blob/f996d94a0063d3313015fa6bf08205f24c97c7ac/apps/backend/src/agents/user-rules.ts), [file tools](https://github.com/getnao/nao/tree/f996d94a0063d3313015fa6bf08205f24c97c7ac/apps/backend/src/agents/tools)). User memories have an explicit `MEMORY_TOKEN_LIMIT` of 1000 estimated tokens and are selected in category priority order before entering the prompt ([system-prompt.tsx](https://github.com/getnao/nao/blob/f996d94a0063d3313015fa6bf08205f24c97c7ac/apps/backend/src/components/ai/system-prompt.tsx)).

**Chat-derived user memories are a separate trace-learning loop.** After an agent request is sent, Nao schedules memory extraction from the current chat messages. The extractor reads the recent conversation, truncates older message text, includes existing memories, and asks an LLM for structured `user_instructions` and `user_profile` outputs with optional `supersedes_id` fields ([agent.ts](https://github.com/getnao/nao/blob/f996d94a0063d3313015fa6bf08205f24c97c7ac/apps/backend/src/services/agent.ts), [memory-extractor-llm.ts](https://github.com/getnao/nao/blob/f996d94a0063d3313015fa6bf08205f24c97c7ac/apps/backend/src/agents/memory/memory-extractor-llm.ts), [memory prompts](https://github.com/getnao/nao/tree/f996d94a0063d3313015fa6bf08205f24c97c7ac/apps/backend/src/components/ai)). These memories persist in the backend DB, not in the project folder, and are user-scoped with project and user toggles ([memory service](https://github.com/getnao/nao/blob/f996d94a0063d3313015fa6bf08205f24c97c7ac/apps/backend/src/services/memory.ts), [memory queries](https://github.com/getnao/nao/blob/f996d94a0063d3313015fa6bf08205f24c97c7ac/apps/backend/src/queries/memory.ts), [settings UI](https://github.com/getnao/nao/tree/f996d94a0063d3313015fa6bf08205f24c97c7ac/apps/frontend/src/components/settings)).

**Skills are both product affordance and prompt routing surface.** The repository ships a root `skills/` pack for the analytics-context lifecycle: setup, rule writing, test creation, audit, semantic-layer addition, and deploy ([skills README](https://github.com/getnao/nao/blob/f996d94a0063d3313015fa6bf08205f24c97c7ac/skills/README.md)). Runtime project skills live in `agent/skills/*.md`; the backend parses their frontmatter, includes names/descriptions/locations in the system prompt, watches the folder for changes, and replaces the user's last message with full skill content when the user invokes a `/` skill mention ([skill service](https://github.com/getnao/nao/blob/f996d94a0063d3313015fa6bf08205f24c97c7ac/apps/backend/src/services/skill.ts), [agent.ts](https://github.com/getnao/nao/blob/f996d94a0063d3313015fa6bf08205f24c97c7ac/apps/backend/src/services/agent.ts)).

**Stories, compaction, and test artifacts are separate retained surfaces.** Chat messages and message parts persist tool calls, reasoning/text parts, images, feedback, source channels, and token usage. Stories persist versioned markdown-like report code, query data caches, sharing state, live refresh state, and scheduled jobs ([sqlite schema](https://github.com/getnao/nao/blob/f996d94a0063d3313015fa6bf08205f24c97c7ac/apps/backend/src/db/sqlite-schema.ts), [story tool](https://github.com/getnao/nao/blob/f996d94a0063d3313015fa6bf08205f24c97c7ac/apps/backend/src/agents/tools/story.ts)). Compaction has schemas, prompts, a threshold service, and tests, but the live agent's threshold-triggered compaction call is commented out in the reviewed commit; only rehydrating a previously stored compaction marker is active in message assembly ([agent.ts](https://github.com/getnao/nao/blob/f996d94a0063d3313015fa6bf08205f24c97c7ac/apps/backend/src/services/agent.ts), [compaction service](https://github.com/getnao/nao/blob/f996d94a0063d3313015fa6bf08205f24c97c7ac/apps/backend/src/services/compaction.ts), [compaction tests](https://github.com/getnao/nao/tree/f996d94a0063d3313015fa6bf08205f24c97c7ac/apps/backend/tests)).

**MCP exposes Nao as both a context layer and a sub-agent.** Project `agent/mcps/mcp.json` config is loaded, environment variables are substituted, tools are prefixed by server, newly discovered server tools are enabled by default, and the config file is watched for changes ([mcp service](https://github.com/getnao/nao/blob/f996d94a0063d3313015fa6bf08205f24c97c7ac/apps/backend/src/services/mcp.ts)). Nao's own MCP endpoint can expose `ask_nao` sub-agent mode, context-layer tools (`ls_nao_context`, `grep_nao_context`, `read_nao_context`, `execute_sql`, stories), asset tools, and embedded UI resources, controlled by project settings in the frontend ([MCP server](https://github.com/getnao/nao/blob/f996d94a0063d3313015fa6bf08205f24c97c7ac/apps/backend/src/mcp/server.ts), [context-layer tools](https://github.com/getnao/nao/blob/f996d94a0063d3313015fa6bf08205f24c97c7ac/apps/backend/src/mcp/tools/context-layer.ts), [sub-agent tool](https://github.com/getnao/nao/blob/f996d94a0063d3313015fa6bf08205f24c97c7ac/apps/backend/src/mcp/tools/sub-agent.ts), [MCP settings UI](https://github.com/getnao/nao/blob/f996d94a0063d3313015fa6bf08205f24c97c7ac/apps/frontend/src/components/settings/mcp-endpoint.tsx)).

**Deployment treats context as a replaceable project artifact.** The Docker entrypoint supports local volume context, git-cloned context with HTTPS token or SSH deploy key, sparse checkout, shallow fetch/reset, and API mode for deployed projects ([entrypoint.sh](https://github.com/getnao/nao/blob/f996d94a0063d3313015fa6bf08205f24c97c7ac/docker/entrypoint.sh), [Dockerfile](https://github.com/getnao/nao/blob/f996d94a0063d3313015fa6bf08205f24c97c7ac/Dockerfile)). The CLI `nao deploy` packages a project tarball while excluding `.git`, `.env`, `repos`, `node_modules`, tests, and `.naoignore` patterns; the backend `/deploy` route validates `nao_config.yaml`, creates or updates the project row, and fully replaces the stored project directory on update ([deploy CLI](https://github.com/getnao/nao/blob/f996d94a0063d3313015fa6bf08205f24c97c7ac/cli/nao_core/commands/deploy.py), [deploy route](https://github.com/getnao/nao/blob/f996d94a0063d3313015fa6bf08205f24c97c7ac/apps/backend/src/routes/deploy.ts)).

**Evaluation is natural-language-to-SQL result comparison.** `nao test` discovers YAML test cases with a prompt and expected SQL, runs the agent against a selected provider/model, executes and compares actual and expected result data, and writes timestamped JSON outputs with cost, tokens, duration, tool calls, and detailed comparison data ([test runner](https://github.com/getnao/nao/blob/f996d94a0063d3313015fa6bf08205f24c97c7ac/cli/nao_core/commands/test/runner.py), [test case](https://github.com/getnao/nao/blob/f996d94a0063d3313015fa6bf08205f24c97c7ac/cli/nao_core/commands/test/case.py)). The bundled example project demonstrates a DuckDB jaffle-shop context, `RULES.md`, an MCP config, a project skill, Notion docs, synced database markdown, and one test ([example](https://github.com/getnao/nao/tree/f996d94a0063d3313015fa6bf08205f24c97c7ac/example)).

## Artifact analysis

- **Storage substrate:** `repo` — Local filesystem project directory, Docker volume, git checkout, or API-deployed project directory recorded in the `project.path` DB field
- **Representational form:** `prose` `symbolic` — Prose rules, docs, table descriptions, user memories, stories, and compaction summaries combine with symbolic YAML, semantic files, MCP config, DB records, schemas, test cases, and generated metadata
- **Lineage:** `authored` `imported` `trace-extracted` — Project context is authored by data teams and agents, imported from warehouses/repos/Notion, generated by sync/deploy lifecycles, and supplemented by chat-derived memories
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — Files and chat traces provide knowledge; rules, skills, semantic files, MCP config, deploy filters, tests, memory prompts, category priority, and extraction schemas instruct, enforce, route, validate, rank, and learn

**Project context folder.** Storage substrate: local filesystem project directory, Docker volume, git checkout, or API-deployed project directory recorded in the `project.path` DB field. Representational form: mixed prose (`RULES.md`, docs, table descriptions), symbolic YAML (`nao_config.yaml`, semantic files, MCP config), generated markdown table metadata, copied repo files, and optional templates. Lineage: authored by data teams and agents, imported from warehouses/repos/Notion, or generated by sync templates; source changes require rerunning `nao sync`, git refresh, or `nao deploy`. Behavioral authority: knowledge artifacts when read as evidence and context; `RULES.md`, `nao_config.yaml`, skills, MCP config, semantic-layer files, `.naoignore`, and deploy packaging rules are system-definition artifacts because they instruct, route, filter, or configure future work.

**Database table context files.** Storage substrate: project folder paths under `databases/type=.../database=.../schema=.../table=.../`. Representational form: generated markdown/prose plus symbolic schema fields, profiling stats, previews, indexes, and sometimes query-history-derived usage notes. Lineage: derived from a specific configured warehouse connection and template set at sync time; freshness depends on sync cadence and profiling refresh policy. Behavioral authority: mostly knowledge artifacts for table selection and SQL writing; they gain routing authority when `RULES.md`, `@` mentions, or MCP/tool descriptions tell the agent to inspect them before querying.

**Runtime user memories.** Storage substrate: backend `memories` table in SQLite or Postgres, keyed by user with category, chat id, supersession pointer, and timestamps ([schema](https://github.com/getnao/nao/blob/f996d94a0063d3313015fa6bf08205f24c97c7ac/apps/backend/src/db/sqlite-schema.ts)). Representational form: concise prose statements, categorized symbolically as `global_rule` or `personal_fact`. Lineage: LLM-extracted from recent chat messages plus existing memory state; each new memory stores the chat id but not exact source spans, prompt version, or model output audit trail. Behavioral authority: `personal_fact` memories are knowledge artifacts; `global_rule` memories become prose system-definition artifacts when pushed into the system prompt as "Global User Rules." Supersession is recorded by `supersededBy`, and the frontend lets users edit or delete memories.

**Memory extraction prompts and schema.** Storage substrate: backend source files and schema definitions. Representational form: prose extraction policy plus Zod output schema. Lineage: authored system-definition artifacts; changes alter what future traces produce. Behavioral authority: learning and validation authority over chat-derived memories, including a conservative default-not-extract rule, permanence requirements for instructions, `user_profile` extraction, and `supersedes_id` replacement semantics ([memory-system-prompt.tsx](https://github.com/getnao/nao/blob/f996d94a0063d3313015fa6bf08205f24c97c7ac/apps/backend/src/components/ai/memory-system-prompt.tsx), [types/memory.ts](https://github.com/getnao/nao/blob/f996d94a0063d3313015fa6bf08205f24c97c7ac/apps/backend/src/types/memory.ts)).

**Chat messages, message parts, and inference records.** Storage substrate: backend chat/message/message-part/llm-inference tables. Representational form: symbolic DB records plus prose message text, tool inputs/outputs, reasoning text, files/images, citations, feedback, and token/cost metadata. Lineage: direct interaction traces from web, Slack, Teams, Telegram, WhatsApp, or MCP sources. Behavioral authority: knowledge artifacts for replay, forks, testing, trace inspection, and memory extraction; chat history also becomes prompt context in subsequent turns until pruned or compacted.

**Stories and story query caches.** Storage substrate: `story`, `story_version`, `story_data_cache`, `mcp_query_data`, and `mcp_chart_embed` tables. Representational form: prose/markdown-like story code, embedded chart/table/grid tags, symbolic version/action/source metadata, cached query rows, and chart config JSON. Lineage: assistant-created, user-edited, MCP-created, or scheduled/live refreshed; each version records source and action but not a full source-span derivation. Behavioral authority: knowledge artifacts as reports and dashboards; system-definition artifacts when story code and cached query data drive rendered charts, live refresh, sharing, or downstream MCP app display.

**Skills and MCP tools.** Storage substrate: root repository skill pack, project `agent/skills/*.md`, project `agent/mcps/mcp.json`, backend DB enabled-tool state, and MCP endpoint settings. Representational form: prose instructions, YAML frontmatter, JSON server config, tool schemas, and backend tool definitions. Lineage: authored or installed, then parsed and watched by runtime services. Behavioral authority: skills are system-definition artifacts when invoked or summarized in the prompt; MCP tools have routing and action authority over context reads, SQL execution, story creation, and sub-agent delegation.

**Compaction summaries.** Storage substrate: message data parts when produced, plus service code and prompts. Representational form: prose summary wrapped as an assistant message or `<conversation-summary>`. Lineage: LLM-derived from earlier chat messages selected under token budget. Behavioral authority: knowledge artifact for continuity and context efficiency. In the inspected commit, threshold-triggered generation is not wired into the active agent path, so this is implemented support rather than an active automatic promotion path.

The main promotion path is file/project context becoming higher-authority runtime guidance: synced metadata and copied repo files are evidence; `RULES.md`, skills, semantic-layer pointers, MCP config, and deployment settings convert selected evidence into instructions and routing. The chat-derived path is separate: raw conversations become extracted memory rows; only global-rule memories gain instruction-like authority when injected into future system prompts.

## Comparison with Our System

| Dimension | nao | Commonplace |
|---|---|---|
| Primary purpose | Build and deploy analytics agents over a local/project context folder | Build and maintain an agent-operated methodology KB |
| Canonical project context | `nao_config.yaml`, `RULES.md`, generated database files, repos, docs, semantics, skills, MCP config | Typed Markdown collections, source snapshots, indexes, instructions, schemas, review artifacts |
| Chat memory | DB-stored per-user facts and global rules extracted from chats | No equivalent automatic user-profile store in the KB core |
| Context activation | Push for `RULES.md`, skill summaries, connections, bounded user memories; pull for file search/read/grep, table mentions, MCP context tools | Pull through `rg`, indexes, links, skills; push through agent instructions and selected loaded artifacts |
| Governance | User/project toggles, frontend memory edit/delete, test suite, deploy replacement, code schemas | Git history, type specs, validation, semantic review gates, collection contracts, archived replacements |
| Evaluation | Natural-language prompt to expected-SQL result comparison | Deterministic validation and semantic review bundles over KB artifacts |

Nao is closer to an analytics-agent runtime plus context builder than to a general memory framework. Its project folder resembles a domain-specific KB: it has source routing, templates, generated indexes-by-directory, rules, skills, tests, and deploy packaging. Commonplace is broader and more explicit about artifact typing and review, while Nao is more productized around the analytics workflow.

The strongest parallel is the separation between a library layer and runtime context. Nao's `databases/`, `repos/`, `docs/`, `semantics/`, and `RULES.md` are a project-local library that the agent navigates with file tools. Commonplace's notes, instructions, reviews, indexes, and sources fill a similar role, but with stronger type contracts, backlink/search conventions, and validation. Nao's advantage is adoption: the context folder maps directly to warehouse metadata, SQL testing, MCP, Docker, and a chat UI.

The main divergence is authority control. In Nao, `RULES.md`, skills, memory rows, MCP config, and project settings can all affect future agent behavior, but only some are git-visible. Chat-derived user memories live in the app database and are editable in the frontend; they are not naturally reviewed as repository artifacts. Commonplace keeps durable behavior-shaping artifacts in git and validates them, but does not yet have Nao's integrated user-facing memory controls or result-based analytics eval loop.

**Read-back:** `both` — Most project context is pull through file/MCP tools and explicit `@`/`/` mentions; pushed retained memory is coarse, with `RULES.md`, project connection names, project skill summaries, and active user memories loaded when present/enabled rather than selected by an instance signal. Shipped baseline instructions and root skill-pack docs are baseline context surfaces, not read-back.

**Read-back signal:** `coarse` — Pushed retained memory is loaded when present/enabled rather than selected by an instance signal.

**Faithfulness tested:** `no` — The review describes analytics evals and tests, but no with/without read-back ablation showing that pushed memory changes downstream behavior.

### Borrowable Ideas

**Treat a project folder as a deployable context artifact.** Ready to borrow conceptually. Commonplace already lives in git, but Nao's `nao deploy` model is a useful reminder that a context bundle can be packaged, uploaded, and fully replaced as one unit when the source-of-truth is clear.

**Keep synced source context outside the prompt until requested.** Ready now. Nao's database markdown and repo files are available through tools, while only lightweight rules and summaries are pushed. Commonplace should keep favoring cheap lexical/file navigation over eager context loading.

**Expose context through both native agent tools and MCP.** Needs a concrete Commonplace product surface. Nao's MCP split between context-layer tools and `ask_nao` sub-agent mode is a clean interface distinction: external clients can either drive the workflow step by step or delegate to the domain agent.

**Make memory controls visible to users and admins.** Ready as a design requirement. Nao's per-user and per-project memory toggles, edit/delete UI, and project memory settings are practical governance surfaces for trace-derived personal memory. Commonplace trace-learning experiments should not grant hidden persistence without comparable controls.

**Use executable evals for context quality.** Ready for analytics-like domains; needs adaptation for methodology KBs. Nao's prompt-to-expected-SQL tests measure whether context supports a task, not just whether files validate. Commonplace could borrow the result-comparison framing for selected operational tasks.

**Do not borrow DB-only memory as the durable methodology source.** Nao's DB memory is appropriate for personal assistant preferences. For shared methodology, Commonplace should keep behavior-shaping rules, schemas, validators, and reviews in git with lineage and review status.

## Write-side placement

**Write agency:** `automatic` `manual` — the review identifies a trace-derived or rule-driven path that changes retained memory from execution/session evidence; manual surfaces are included where the reviewed prose describes user or operator authoring.

**Curation operations:** `consolidate` `synthesize` `invalidate` `decay` `promote` — the existing review evidence identifies automatic store-changing operations matching these curation classes.

### Trace-derived learning
**Trace source:** `session-logs` — Recent chat messages are the durable conversation trace consumed by the memory extractor.

**Learning scope:** `cross-task` — Extracted user instructions and profile facts persist per user for reuse across future agent requests when memory is enabled.

**Learning timing:** `online` — Extraction is scheduled asynchronously immediately after an agent request is sent.

**Distilled form:** `prose` `symbolic` — Distilled memories are prose statements with symbolic category and supersession metadata.

**Trace source.** Nao qualifies as trace-derived learning because it derives durable `memories` rows from chat traces. The extractor receives recent UI messages from the chat, including user and assistant messages, after each request is sent to the agent. It does not derive these memories from project context files or database metadata.

**Extraction.** Extraction is LLM-mediated and schema-constrained. `MemoryExtractorLLM` keeps the last 17 user/assistant messages, truncates ordinary messages to 1,250 characters and the last user message to 2,000 characters, appends existing memories in a `<memories>` block, and asks for structured `user_instructions` and `user_profile` output. The prompt is conservative: instructions need permanence signals, profile facts do not, and both outputs may be `null`.

**Four fields.** The raw stage is chat/message/message-part DB state: mixed prose/tool trace records, direct lineage from a user interaction, and knowledge-artifact authority for replay, extraction, and audit. The distilled stage is `memories` rows: DB substrate, prose plus symbolic category/supersession metadata, LLM-derived lineage from recent chat, and either knowledge-artifact authority (`personal_fact`) or instruction authority (`global_rule`) when read into the system prompt.

**Scope and timing.** Scope is per-user and gated by both user-level and project-level memory settings. Timing is online and asynchronous: memory extraction is scheduled immediately after the agent request is sent, and failures are logged rather than blocking the response. The extraction appears to operate on the messages passed into the request rather than on the assistant response that is still streaming, so it is better characterized as learning from conversation state up to the current user turn, not from the just-produced answer.

**Curation and deletion.** The LLM can propose `supersedes_id`; the persistence layer inserts new rows and marks superseded rows with `supersededBy`. The frontend exposes memory enablement, edit, and delete controls for users, while project settings expose an admin-level memory toggle ([frontend memories](https://github.com/getnao/nao/blob/f996d94a0063d3313015fa6bf08205f24c97c7ac/apps/frontend/src/components/settings/memories.tsx), [project memory](https://github.com/getnao/nao/blob/f996d94a0063d3313015fa6bf08205f24c97c7ac/apps/frontend/src/components/settings/project-memory.tsx)).

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), Nao belongs in the chat-to-personal-memory family. It strengthens the survey split between raw traces and distilled behavior-shaping artifacts: chat transcripts are evidence, extracted user memories are durable retained artifacts, and only the subset categorized as global rules becomes instruction-like prompt material.

## Curiosity Pass

**The most important "memory" is often `RULES.md`, not the memories table.** Nao's product framing emphasizes an agent context folder. For analytics quality, the always-loaded `RULES.md` and navigable database files likely shape behavior more than personal profile facts.

**`agent/tools` is scaffolded but the inspected runtime uses built-in and MCP tools.** The CLI creates `agent/tools`, but the backend code I read loads project skills from `agent/skills` and MCP servers from `agent/mcps/mcp.json`; I did not find a comparable runtime loader for arbitrary project-local tool files.

**Repository sync intentionally strips git history.** Cloned repos under `repos/` become ordinary copied context. That is good for prompt/file inspection and packaging, but weaker for source lineage than keeping commit metadata or snapshots.

**Compaction is more implemented than deployed.** The compaction service and tests are substantial, but the active agent `prepareStep` has the automatic compaction call commented out. Existing compaction markers can still be rehydrated if present.

**The MCP endpoint turns Nao into a memory/context service for other agents.** This is broader than a chat UI: an outside agent can call `ask_nao`, inspect context files, run SQL, and create stories. That makes Nao's context folder a cross-agent substrate, not just internal prompt material.

## What to Watch

- Whether automatic compaction is re-enabled in `AgentManager._prepareStep`; that would add an active context-efficiency and conversation-memory path.
- Whether memory extraction starts incorporating the just-streamed assistant answer or tool outcomes; that would change the trace source and likely the quality of extracted preferences.
- Whether user memories gain source-span lineage, extraction model/prompt version, or review status before global rules enter future prompts.
- Whether project-local `agent/tools` becomes a loaded runtime surface; that would add a new system-definition artifact family beyond skills and MCP.
- Whether deploy and git-context refresh add explicit version metadata to project rows so deployed context can be audited against git commits.
- Whether `nao test` results become a promotion gate for `RULES.md`, semantic-layer, or context changes rather than a separate eval report.

## Bottom Line

Nao is a file-first analytics context system with a separate trace-derived personal memory loop. Its durable analytics behavior comes mostly from `RULES.md`, generated database context, synced repos/docs, semantic files, skills, MCP config, and tests; its chat-derived memory is a per-user DB store of global rules and profile facts pushed into the prompt when enabled. Commonplace should borrow Nao's deployable context-folder model, visible memory controls, MCP split, and result-based context evals, while keeping stronger git-native lineage and review before generated or trace-derived rules gain durable methodology authority.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Nao extracts persistent user memories from chat traces, then pushes selected categories into future prompts.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Nao requires separating project files, table context, skills, MCP config, chat traces, memories, stories, compaction summaries, and tests by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: database context files, chat traces, story reports, query caches, and profile facts mostly serve as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: `RULES.md`, skills, memory extraction prompts, MCP settings, deploy rules, semantic files, and global-rule memories instruct or configure behavior.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: Nao stores large project context but activates most of it only through tool-mediated search/read, while a small subset is pushed into the prompt.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: Nao derives personal facts and global user rules from chat traces using an LLM extractor and supersession model.
