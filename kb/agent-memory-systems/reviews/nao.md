---
description: "nao review: analytics-agent context builder with file-backed project context, SQL guardrails, stories, and pushed trace-derived user memory"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-04"
tags: [trace-derived]
---

# nao

nao, from `getnao/nao`, is an open-source framework for building and deploying analytics agents. At the reviewed commit it combines a Python `nao-core` CLI for creating a file-backed analytics context, a TypeScript chat backend/frontend, database and file tools, persisted stories, messaging-provider integrations, and a user-memory feature that extracts durable preferences or profile facts from recent conversations and injects active memories into future agent prompts.

**Repository:** https://github.com/getnao/nao

**Reviewed commit:** [b109f5f7318c92ec0ec4341c53bbd5e0214c5432](https://github.com/getnao/nao/commit/b109f5f7318c92ec0ec4341c53bbd5e0214c5432)

**Source directory:** `related-systems/getnao--nao`

## Core Ideas

**The main memory surface is a project context folder, not a vector store.** `nao init` scaffolds a project with `databases/`, `queries/`, `docs/`, `semantics/`, `repos/`, `agent/tools`, `agent/mcps`, `agent/skills`, `tests/`, `RULES.md`, and `.naoignore`; `nao sync` then populates provider-specific context files and renders templates ([cli/nao_core/commands/init.py](https://github.com/getnao/nao/blob/b109f5f7318c92ec0ec4341c53bbd5e0214c5432/cli/nao_core/commands/init.py), [cli/nao_core/commands/sync/__init__.py](https://github.com/getnao/nao/blob/b109f5f7318c92ec0ec4341c53bbd5e0214c5432/cli/nao_core/commands/sync/__init__.py)). The agent is told that database content is represented as files, and it gets `list`, `search`, and `read` tools over the configured project folder ([apps/backend/src/components/ai/system-prompt.tsx](https://github.com/getnao/nao/blob/b109f5f7318c92ec0ec4341c53bbd5e0214c5432/apps/backend/src/components/ai/system-prompt.tsx), [apps/backend/src/agents/tools/list.ts](https://github.com/getnao/nao/blob/b109f5f7318c92ec0ec4341c53bbd5e0214c5432/apps/backend/src/agents/tools/list.ts), [apps/backend/src/agents/tools/search.ts](https://github.com/getnao/nao/blob/b109f5f7318c92ec0ec4341c53bbd5e0214c5432/apps/backend/src/agents/tools/search.ts), [apps/backend/src/agents/tools/read.ts](https://github.com/getnao/nao/blob/b109f5f7318c92ec0ec4341c53bbd5e0214c5432/apps/backend/src/agents/tools/read.ts)).

**Context efficiency is filesystem navigation plus selective prompt injection.** Project context is not loaded wholesale: the system prompt describes the folder conventions, while the agent must search/list/read files as needed. Runtime user memory is bounded separately by category priority and a 1000-token limit before prompt insertion ([apps/backend/src/components/ai/system-prompt.tsx](https://github.com/getnao/nao/blob/b109f5f7318c92ec0ec4341c53bbd5e0214c5432/apps/backend/src/components/ai/system-prompt.tsx)). Tool results and stories can still make context large inside a chat, but story outputs are de-duplicated so only the latest occurrence of each story carries full code ([apps/backend/src/services/agent.ts](https://github.com/getnao/nao/blob/b109f5f7318c92ec0ec4341c53bbd5e0214c5432/apps/backend/src/services/agent.ts)).

**User memory is extracted from recent conversation traces and then always offered back.** After an agent request is sent, the backend schedules memory extraction from recent UI messages. The extractor reads recent user/assistant messages plus existing memories, produces `user_instructions` and `user_profile` objects with optional `supersedes_id`, and persists active rows in a `memories` table ([apps/backend/src/services/agent.ts](https://github.com/getnao/nao/blob/b109f5f7318c92ec0ec4341c53bbd5e0214c5432/apps/backend/src/services/agent.ts), [apps/backend/src/services/memory.ts](https://github.com/getnao/nao/blob/b109f5f7318c92ec0ec4341c53bbd5e0214c5432/apps/backend/src/services/memory.ts), [apps/backend/src/agents/memory/memory-extractor-llm.ts](https://github.com/getnao/nao/blob/b109f5f7318c92ec0ec4341c53bbd5e0214c5432/apps/backend/src/agents/memory/memory-extractor-llm.ts), [apps/backend/src/components/ai/memory-system-prompt.tsx](https://github.com/getnao/nao/blob/b109f5f7318c92ec0ec4341c53bbd5e0214c5432/apps/backend/src/components/ai/memory-system-prompt.tsx), [apps/backend/src/db/sqlite-schema.ts](https://github.com/getnao/nao/blob/b109f5f7318c92ec0ec4341c53bbd5e0214c5432/apps/backend/src/db/sqlite-schema.ts)).

**Analytics artifacts are persisted as versioned stories.** The `story` tool creates, updates, or replaces interactive documents containing markdown, charts, tables, and grids; every change creates a `story_version`, and the agent sees the latest version when the story appears in chat context ([apps/backend/src/agents/tools/story.ts](https://github.com/getnao/nao/blob/b109f5f7318c92ec0ec4341c53bbd5e0214c5432/apps/backend/src/agents/tools/story.ts), [apps/backend/src/queries/story.queries.ts](https://github.com/getnao/nao/blob/b109f5f7318c92ec0ec4341c53bbd5e0214c5432/apps/backend/src/queries/story.queries.ts)). Recent changes add foldering, favorites, sharing, access controls, archive behavior, and live refresh scheduling around these story artifacts ([apps/backend/src/queries/story-folder.queries.ts](https://github.com/getnao/nao/blob/b109f5f7318c92ec0ec4341c53bbd5e0214c5432/apps/backend/src/queries/story-folder.queries.ts), [apps/backend/src/queries/favorite.queries.ts](https://github.com/getnao/nao/blob/b109f5f7318c92ec0ec4341c53bbd5e0214c5432/apps/backend/src/queries/favorite.queries.ts), [apps/backend/src/queries/shared-story.queries.ts](https://github.com/getnao/nao/blob/b109f5f7318c92ec0ec4341c53bbd5e0214c5432/apps/backend/src/queries/shared-story.queries.ts), [apps/backend/src/trpc/story.routes.ts](https://github.com/getnao/nao/blob/b109f5f7318c92ec0ec4341c53bbd5e0214c5432/apps/backend/src/trpc/story.routes.ts)).

**Reliability controls are operational guardrails around the agent, not just memory retrieval.** The SQL tool blocks writes unless an admin enables dangerous write permissions, detects top-level row limits for result warnings, and stores query results for later chart/story references ([apps/backend/src/agents/tools/execute-sql.ts](https://github.com/getnao/nao/blob/b109f5f7318c92ec0ec4341c53bbd5e0214c5432/apps/backend/src/agents/tools/execute-sql.ts), [apps/backend/src/utils/sql-filter.ts](https://github.com/getnao/nao/blob/b109f5f7318c92ec0ec4341c53bbd5e0214c5432/apps/backend/src/utils/sql-filter.ts), [apps/backend/tests/sql-filter.test.ts](https://github.com/getnao/nao/blob/b109f5f7318c92ec0ec4341c53bbd5e0214c5432/apps/backend/tests/sql-filter.test.ts)). Slack thread policy is similarly explicit: mention mode does not reply to ordinary thread messages, and thread mode ignores self/bot messages ([apps/backend/src/utils/slack-reply-policy.ts](https://github.com/getnao/nao/blob/b109f5f7318c92ec0ec4341c53bbd5e0214c5432/apps/backend/src/utils/slack-reply-policy.ts), [apps/backend/tests/slack-reply-policy.test.ts](https://github.com/getnao/nao/blob/b109f5f7318c92ec0ec4341c53bbd5e0214c5432/apps/backend/tests/slack-reply-policy.test.ts)).

## Artifact analysis

- **Storage substrate:** `files` `sqlite` `rdbms` `service-object` — Project context, rules, tests, templates, synced database docs, repo docs, tools, MCP manifests, and skills live as files; chat, messages, memories, stories, versions, folders, favorites, shares, activities, and provider settings live in Drizzle-managed SQLite or Postgres tables; external databases, Slack, Teams, WhatsApp, Telegram, Notion, GitHub, LLM providers, and MCP servers are consumed as service objects.
- **Representational form:** `prose` `symbolic` `parametric` — RULES, docs, table descriptions, story markdown, memories, prompts, and skills are prose; YAML config, schema/type metadata, folder/share/favorite rows, SQL filters, tool schemas, story tags, query ids, cron schedules, permissions, and migration tables are symbolic; LLM-generated memory extraction and AI summaries use parametric model judgments, though nao does not retain embeddings as a visible memory index.
- **Lineage:** `authored` `imported` `trace-extracted` — Humans and agents author RULES, stories, tests, settings, skills, and memory edits; sync imports database metadata, query-history-derived table guidance, repos, Notion docs, and provider config into project context; runtime memory extraction derives user instructions and profile facts from chat traces.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — Project context files, stories, query caches, and memories serve as knowledge artifacts; system prompts, RULES, skills, memory instructions, and messaging prompts instruct the agent; SQL write blocking, role checks, folder/share permissions, Slack reply policy, and budget checks enforce behavior; project paths, mentions, skills, MCP settings, story ids, folders, shares, and database ids route work; test cases, type schemas, schedule validation, and SQL read-only checks validate; folder/favorite/shared-story ordering and memory category priority rank recall; trace-derived extraction and supersession provide the learning path.

**Project context folder.** The most reusable retained surface is the project directory produced by `nao init` and `nao sync`: `nao_config.yaml` defines sources, the default folder tree makes database/docs/repo/semantic/test material navigable, and `.naoignore` plus safe path conversion constrain what the agent can list or read. Its promotion path is file-first: source systems produce markdown/YAML context, templates add derived views, and the agent consumes those files through tools rather than a hidden retriever.

**User memories.** The `memories` table stores normalized prose content, category, user id, optional source chat id, timestamps, and `supersededBy`. The operative split is important: `personal_fact` memories are advisory knowledge, while `global_rule` memories become instruction-like because the system prompt labels them as "Global User Rules" and inserts them into the model call. Supersession is retained as a pointer from old row to new row rather than hard overwriting every old fact.

**Stories and story organization.** Stories are durable analytic artifacts with version rows, optional live refresh state, query-data caches, sharing rows, folder memberships, favorites, and activity records. They are strong user-facing knowledge artifacts, but not a general long-term agent memory by themselves: current code feeds story content back to the agent when the story tool output is in the chat history or when a route returns a requested story, not by automatically searching all prior stories for every future task.

**Guardrails and channel policies.** SQL read-only filtering, row-limit detection, role checks, project/user memory toggles, story sharing, and Slack reply mode are system-definition artifacts. They do not add knowledge, but they determine what the agent can do, when it may respond, and whether retained memory is available for a given user/project.

## Comparison with Our System

nao and Commonplace both treat filesystem context as a practical agent substrate: files are inspectable, versionable, and directly searchable. nao is product-oriented and runtime-oriented: it turns project context into a deployed analytics chat system with tools, stories, messaging providers, and background user-memory extraction. Commonplace is methodology-oriented: it uses collection contracts, type specs, validation, review gates, and curated links to keep retained artifacts semantically governed.

The largest divergence is authority. nao favors automatic continuity and convenience: active memories are inserted into future system prompts, stories can be edited and shared through the UI, and project context is available through broad file tools. Commonplace favors explicit promotion: artifacts gain authority through type contracts, validation, source grounding, and review. nao's design is therefore useful evidence for agent adoption, but weaker evidence for long-term epistemic hygiene.

nao's analytics context builder is closer to Commonplace than its user-memory table is. The project folder is inspectable, can be deployed, and can include tests. The memory table is easier to adopt but less reviewable: its LLM-extracted rows have no quote-level source spans, prompt version, or acceptance review before they influence future prompts.

### Borrowable Ideas

**Project-folder scaffold for a specific domain.** Commonplace could keep using collection contracts while offering domain scaffolds that create the expected folders, starter type specs, and validation targets. Ready when a consuming project has a repeated domain shape.

**Token-bounded always-load memory section.** nao's `MEMORY_TOKEN_LIMIT` is a simple hard bound for pushed memory. Useful as a design reference, but Commonplace should combine it with explicit provenance and authority labels before adopting it.

**Versioned analytic artifacts.** Stories show how an agent-created report can retain versions, user edits, refresh schedules, and query-data references. This is borrowable for workshop/report artifacts once there is a concrete recurring report workflow.

**SQL row-limit warning as context-quality feedback.** Detecting whether the agent's own query truncated the result is a small but valuable reliability hook. Ready for any Commonplace-adjacent analytics workflow that executes SQL.

**Do not borrow unreviewed extracted instructions as high-authority rules.** nao's global-rule memories can shape the next system prompt without a review step. Commonplace should keep automatic extraction in a workshop or candidate layer until promoted.

## Write side

**Write agency:** `manual` `automatic` — Humans and agents write project files, settings, stories, folders, favorites, shares, tests, and memory edits manually through CLI, UI, tools, or config; automatic paths sync provider context, render templates, generate titles, cache story query data, schedule live refresh jobs, extract user memories from conversations, supersede old memories, and log LLM inference/activity records.

**Curation operations:** `evolve` `invalidate` — The memory extractor can return a replacement with `supersedes_id`; persistence inserts the new memory and marks the old row's `supersededBy`, so existing remembered behavior is evolved through replacement while stale rows are invalidated from active read-back. Story edits produce new versions, but those are authored create/update/replace operations rather than automatic memory curation.

### Trace-derived learning

**Trace source:** `session-logs` — The qualifying trace is the chat message history passed to `safeScheduleMemoryExtraction`: recent user and assistant messages, with the last user message receiving a larger character budget, plus the current list of existing memories.

**Extraction.** The extraction oracle is an LLM call constrained by `ExtractorOutputSchema` and a prompt that defaults to no extraction, requires permanence signals for instructions, extracts profile facts such as name/role/company, and can attach `supersedes_id` when a new memory replaces or contradicts an old one ([apps/backend/src/agents/memory/memory-extractor-llm.ts](https://github.com/getnao/nao/blob/b109f5f7318c92ec0ec4341c53bbd5e0214c5432/apps/backend/src/agents/memory/memory-extractor-llm.ts), [apps/backend/src/components/ai/memory-system-prompt.tsx](https://github.com/getnao/nao/blob/b109f5f7318c92ec0ec4341c53bbd5e0214c5432/apps/backend/src/components/ai/memory-system-prompt.tsx), [apps/backend/src/types/memory.ts](https://github.com/getnao/nao/blob/b109f5f7318c92ec0ec4341c53bbd5e0214c5432/apps/backend/src/types/memory.ts)).

**Learning scope:** `cross-task` — Memories are scoped to the user, gated by user and project settings, and active rows can affect later chats in any project where memory is enabled. The source chat id is retained and excluded from the current chat's immediate injection, which avoids feeding a memory back into the same conversation that produced it.

**Learning timing:** `online` — Extraction is scheduled immediately after the agent request is sent, runs asynchronously, and records both memory counts and a `memory_extraction` inference row.

**Distilled form:** `prose` `symbolic` — The durable output is prose memory content plus symbolic category, user id, source chat id, timestamps, and supersession links.

Relative to the trace-derived survey, nao is a trace-to-user-profile and trace-to-user-instruction system. It learns compact prompt material from conversation traces, not validators, route tables, skills, embeddings, or fine-tuned weights. The notable design choice is conservative extraction prompting plus active prompt injection, which makes the write side cautious but the read-back authority comparatively strong.

## Read-back

**Read-back:** `both` — Project context files are pull-served through list/search/read tools, while active extracted user memories are pushed into the system prompt before a model call whenever user and project memory settings allow it.

**Read-back signal:** `coarse` — Memory push uses a lifecycle-wide prompt section for active memories selected by user/project enablement, category priority, current-chat exclusion, and token budget. It is not keyed to the current task by identifier, lexical search, embedding similarity, or judgment relevance.

**Faithfulness tested:** `no` — The inspected tests cover prompt rendering, SQL filtering, Slack reply policy, and other mechanics, but I did not find a with/without-memory ablation or post-answer audit proving that injected memories improve or faithfully constrain downstream agent behavior.

The injection point is pre-invocation. `AgentManager._buildModelMessages` gathers active memories, renders `SystemPrompt`, and then converts it into the model messages before streaming. Extraction after the request is write-side maintenance for later calls, not read-back for the current action.

Selection and complexity are deliberately simple for memory: `getUserMemories` returns non-superseded rows by user, optionally excluding the current chat, and the prompt renderer keeps memories by category priority until the token estimate reaches 1000 tokens. This bounds volume but can dilute relevance because all retained active memories are eligible for every future task.

Authority at consumption is mixed. `personal_fact` rows are advisory user profile context; `global_rule` rows are stronger because the prompt groups them under global user rules. The code does not distinguish reviewed from unreviewed extracted memories at injection time.

Project context has the opposite shape: it is not pushed in bulk, but the agent is instructed to use files and can pull context with path/glob tools. SQL results, stories, and chart/query ids then become chat-local context that can be reused inside the same conversation.

## Curiosity Pass

The repository has two memory systems sharing one product: a project context builder for analytics work and a personal-memory extractor for user preferences/facts. The former is inspectable and tool-pulled; the latter is compact, trace-derived, and prompt-pushed.

The story system looks memory-like because it persists reports, versions, folders, favorites, shares, and refresh schedules. For read-back classification, though, it is not currently a general recall layer: it is loaded through specific UI/routes or current chat/tool context rather than by a global story retriever.

The SQL filter is deliberately heuristic but valuable. It blocks obvious write statements and detects top-level row limits; it is not a full SQL parser, but it gives the agent a concrete safety and interpretation boundary.

The Slack reply policy is intentionally conservative in mention mode. That matters for memory-system comparison because it prevents an external event stream from automatically waking the agent on every thread message.

## What to Watch

- Whether user memories gain source-span provenance, extraction prompt/version metadata, or a review state; that would change their trust model and promotion path.
- Whether story folders, favorites, or shared stories become agent-searchable memory rather than UI organization; that would change story read-back from requested/chat-local to broader pull or push recall.
- Whether memory injection becomes relevance-filtered by the current task; that would change the read-back signal from coarse to inferred or identifier-based targeting.
- Whether SQL filtering moves from regex heuristics to dialect-aware parsing; that would strengthen enforcement authority for analytics agents.
- Whether Slack thread mode starts summarizing or extracting memories from external conversations; that would broaden trace-derived learning beyond in-app chat traces.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes nao's stored context files, active prompt-injected memories, and story persistence.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - supports separating project files, memories, stories, SQL guardrails, and messaging policies by substrate, form, lineage, and authority.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - frames nao's conversation-to-memory extraction loop.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies prompts, SQL filters, role checks, Slack policy, story sharing, and memory toggles as behavior-shaping controls.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies project context files, stories, query caches, and personal facts as advisory remembered context.
- [Symbolic context engineering is bounded by symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - explains why nao's file paths, database ids, story ids, folders, and categories are useful routing symbols.
